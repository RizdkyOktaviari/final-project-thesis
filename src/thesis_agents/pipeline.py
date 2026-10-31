"""Explicit orchestration. No agent chooses the next agent or bypasses validation."""
import inspect
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, TypeVar

from pydantic import BaseModel, ValidationError

from .config import Settings
from .dataset import load_inputs, numbered
from .llm import Backend, OpenAIBackend
from .logging_utils import EventLog
from .mermaid import parse
from .models import Alignment, Checks, Diagram, Narrative, Report, Specification, Validation, Verification
from .reporting import aggregate, render, traceability
from .rules import RuleChecker
from .storage import checkpoint, digest, git_revision, implementation_digest, restore
from .storage import runtime_versions, write_json
from .validation import validate_alignment, validate_ir, validate_narrative, validate_verification

T = TypeVar("T", bound=BaseModel)


class PipelineFailure(RuntimeError):
    """Safe error without chained API request payloads."""


class Pipeline:
    def __init__(self, root: Path, settings: Settings, backend: Backend | None = None):
        self.root, self.settings = root.resolve(), settings
        self.run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ-") + uuid.uuid4().hex[:8]
        self.directory = self.root / settings.output_dir / self.run_id
        self.directory.mkdir(parents=True, exist_ok=False)
        self.log = EventLog(self.directory, self.run_id, settings)
        self.backend = backend or OpenAIBackend(settings.llm, self.log)
        self.code_digest = implementation_digest()
        self.current_stage = "load"
        self.metadata = {
            "run_id": self.run_id, "status": "running", "stages": [],
            "backend": type(self.backend).__name__, "code_sha256": self.code_digest,
            "git": git_revision(self.root), "dependencies": runtime_versions(),
            "config": settings.model_dump(mode="json"),
        }
        write_json(self.directory / "run.json", self.metadata)

    async def step(self, name: str, payload: object, schema: type[T], action: Callable,
                   resume: Path | None) -> T:
        self.current_stage = name
        started = time.monotonic()
        llm_config = None
        if name.startswith("agent"):
            llm_config = self.settings.llm.model_dump(mode="json", exclude={"models"})
            llm_config["model"] = self.settings.llm.models.get(name, self.settings.llm.model)
        signature = digest({"stage": name, "payload": payload, "code": self.code_digest,
                            "schema": schema.model_json_schema(), "llm": llm_config,
                            "backend": type(self.backend).__name__,
                            "dependencies": self.metadata["dependencies"]})
        path = self.directory / f"{name}.json"
        if not self.settings.stage(name).enabled:
            if resume is None:
                raise ValueError(f"Stage {name} disabled: supply --resume with a compatible checkpoint")
            output = restore(resume / f"{name}.json", signature, schema)
            state = "reused"
            self.log.emit(name, "checkpoint_reused")
        else:
            self.log.emit(name, "step_started")
            value = action()
            output = await value if inspect.isawaitable(value) else value
            output = schema.model_validate(output)
            state = "completed"
        checkpoint(path, signature, output)
        self.log.emit(name, "checkpoint_saved", "DEBUG", artifact=path.name, signature=signature)
        elapsed = round(time.monotonic() - started, 3)
        self.metadata["stages"].append({"step": name, "state": state, "seconds": elapsed})
        write_json(self.directory / "run.json", self.metadata)
        self.log.emit(name, "step_finished", state=state, duration_seconds=elapsed)
        return output

    def finish(self, status: str) -> Path:
        self.metadata["status"] = status
        self.metadata["finished_at"] = datetime.now(timezone.utc).isoformat()
        self.metadata["llm_calls"] = getattr(self.backend, "usage", [])
        write_json(self.directory / "run.json", self.metadata)
        self.log.emit("pipeline", "run_finished", status=status)
        return self.directory

    async def run(self, case_file: Path, resume: Path | None = None,
                  until: str | None = None) -> Path:
        try:
            return await self._run(case_file, resume, until)
        except Exception as error:
            self.metadata.update(status="failed", failed_stage=self.current_stage,
                                 error_type=type(error).__name__)
            details = {}
            if isinstance(error, ValidationError):
                details["validation_errors"] = [{"loc": e["loc"], "type": e["type"]}
                                                 for e in error.errors(include_input=False)]
            elif type(error) is ValueError:
                details["detail"] = str(error)
            self.log.emit(self.current_stage, "step_failed", "ERROR",
                          error_type=type(error).__name__, **details)
            self.finish("failed")
            raise PipelineFailure(
                f"Stage {self.current_stage} failed ({type(error).__name__}). Artifacts: {self.directory}"
            ) from None

    async def _run(self, case_file: Path, resume: Path | None, until: str | None) -> Path:
        inputs = load_inputs(self.root, case_file, self.settings.max_source_chars, self.log)
        self.metadata["inputs"] = {
            "case": inputs.case.model_dump(mode="json"),
            "source_hashes": {s.id: s.sha256 for s in [*inputs.requirements, inputs.diagram]},
        }
        write_json(self.directory / "run.json", self.metadata)
        # Parsing first finds malformed input before paying for an API call.
        diagram = await self.step("parse", inputs.diagram, Diagram,
                                  lambda: parse(inputs.diagram, self.log), resume)
        if until == "parse":
            return self.finish("stopped_after_parse")
        extraction = {"requirement_ids": inputs.case.requirement_ids,
                      "requirements": [numbered(s) for s in inputs.requirements],
                      "assumptions": inputs.case.contract.assumptions}
        spec = await self.step("agent1", extraction, Specification,
                               lambda: self.backend.generate("agent1", extraction, Specification), resume)
        if until == "agent1":
            return self.finish("stopped_after_agent1")
        ir_payload = {"spec": spec, "diagram": diagram, "inputs": inputs}
        validation = await self.step("validate", ir_payload, Validation,
                                     lambda: validate_ir(spec, diagram, inputs), resume)
        if until == "validate":
            return self.finish("stopped_after_validate")
        shared = {"specification": spec, "diagram": diagram, "contract": inputs.case.contract,
                  "sources": [numbered(s) for s in [*inputs.requirements, inputs.diagram]],
                  "ir_validation": validation}
        alignment = await self.step("agent2", shared, Alignment,
                                    lambda: self.backend.generate("agent2", shared, Alignment), resume)
        validate_alignment(alignment, spec, diagram, inputs)
        self.log.emit("agent2", "mappings_validated", roles=len(alignment.roles),
                      behaviors=len(alignment.behaviors), guards=len(alignment.guards))
        if until == "agent2":
            return self.finish("stopped_after_agent2")
        verification_input = {**shared, "candidates": alignment}
        verified = await self.step("agent3", verification_input, Verification,
                                   lambda: self.backend.generate("agent3", verification_input, Verification), resume)
        validate_verification(verified, alignment, spec, diagram, inputs)
        self.log.emit("agent3", "decisions_validated", count=len(verified.decisions))
        write_json(self.directory / "traceability.json", traceability(spec, diagram, alignment, verified))
        if until == "agent3":
            return self.finish("stopped_after_agent3")
        checker_payload = {**ir_payload, "alignment": alignment, "verified": verified,
                           "validation": validation, "rules": self.settings.rules,
                           "max_paths": self.settings.max_paths}
        checks = await self.step("check", checker_payload, Checks, lambda: RuleChecker(
            spec, diagram, alignment, verified, validation, inputs, self.settings.rules,
            self.settings.max_paths, self.log).run(), resume)
        if until == "check":
            return self.finish("stopped_after_check")
        report = await self.step("aggregate", {"case_id": inputs.case.id, "checks": checks,
                                                "rules": self.settings.rules}, Report,
                                 lambda: aggregate(inputs.case.id, checks, self.settings.rules), resume)
        write_json(self.directory / "report.json", report)
        (self.directory / "report.md").write_text(render(report, None), encoding="utf-8")
        if until == "aggregate":
            return self.finish("stopped_after_aggregate")
        narrative = None
        fallback = False
        if self.settings.stage("agent4").enabled:
            try:
                narrative = await self.step("agent4", report, Narrative,
                                            lambda: self.backend.generate("agent4", {"report": report}, Narrative), resume)
                validate_narrative(narrative, report)
                write_json(self.directory / "narrative.json", narrative)
            except Exception as error:
                narrative, fallback = None, True
                self.log.emit("agent4", "report_fallback", "WARNING", error_type=type(error).__name__)
                self.metadata["stages"].append({"step": "agent4", "state": "fallback"})
        else:
            self.log.emit("agent4", "step_skipped", reason="Deterministic report available")
            self.metadata["stages"].append({"step": "agent4", "state": "disabled"})
        (self.directory / "report.md").write_text(render(report, narrative), encoding="utf-8")
        return self.finish("completed_with_report_fallback" if fallback else "completed")
