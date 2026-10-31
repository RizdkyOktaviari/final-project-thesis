import asyncio
import json

import pytest

from conftest import FR, LINEAR, ROOT, bundle
from thesis_agents.config import Settings, load_settings
from thesis_agents.logging_utils import EventLog
from thesis_agents.models import Explanation, Narrative
from thesis_agents.pipeline import Pipeline, PipelineFailure
from thesis_agents.storage import restore, write_json


class FixtureBackend:
    """Test fixture only; never used as a production fallback."""
    def __init__(self, fail_report=False):
        self.calls = []
        self.fail_report = fail_report
        spec, _, alignment, verified, _, _ = bundle()
        self.responses = {"agent1": spec, "agent2": alignment, "agent3": verified}

    async def generate(self, stage, payload, schema):
        self.calls.append((stage, payload))
        if stage == "agent4":
            if self.fail_report:
                raise RuntimeError("Fixture report failure")
            return Narrative(explanations=[Explanation(finding_id=f.id, explanation="Fixture prose",
                                                       recommendation="Fixture recommendation")
                                           for f in payload["report"].findings])
        return self.responses[stage].model_copy(deep=True)


def workspace(tmp_path):
    (tmp_path / "examples").mkdir()
    (tmp_path / "examples/requirements.md").write_text(FR, encoding="utf-8")
    (tmp_path / "examples/sequence.mmd").write_text(LINEAR, encoding="utf-8")
    path = tmp_path / "case.json"
    write_json(path, bundle()[-1].case)
    return path


def quiet(**kwargs):
    return Settings(logging={"enabled": False}, **kwargs)


def test_full_pipeline_isolated_agents_canonical_report_and_artifacts(tmp_path):
    case = workspace(tmp_path)
    backend = FixtureBackend()
    directory = asyncio.run(Pipeline(tmp_path, quiet(), backend).run(case))
    assert [name for name, _ in backend.calls] == ["agent1", "agent2", "agent3", "agent4"]
    first = json.dumps(backend.calls[0][1])
    assert "sequence.mmd" not in first and "ground_truth" not in first
    report = json.loads((directory / "report.json").read_text())
    assert "Fixture prose" not in json.dumps(report)
    assert (directory / "narrative.json").is_file()
    trace = json.loads((directory / "traceability.json").read_text())
    assert trace["requirements_to_messages"]["APPROVE"]
    for stage in ("parse", "agent1", "validate", "agent2", "agent3", "check", "aggregate", "agent4"):
        assert (directory / f"{stage}.json").is_file()
    metadata = json.loads((directory / "run.json").read_text())
    assert metadata["backend"] == "FixtureBackend" and metadata["status"] == "completed"
    assert metadata["code_sha256"]


def test_report_failure_keeps_canonical_findings(tmp_path):
    directory = asyncio.run(Pipeline(tmp_path, quiet(), FixtureBackend(True)).run(workspace(tmp_path)))
    assert (directory / "report.json").is_file()
    assert "Narasi LLM tidak digunakan" in (directory / "report.md").read_text()
    assert json.loads((directory / "run.json").read_text())["status"] == "completed_with_report_fallback"


def test_disable_report_without_checkpoint(tmp_path):
    backend = FixtureBackend()
    settings = quiet(stages={"agent4": {"enabled": False}})
    directory = asyncio.run(Pipeline(tmp_path, settings, backend).run(workspace(tmp_path)))
    assert len(backend.calls) == 3 and (directory / "report.md").is_file()


def test_disabled_dependency_fails_closed(tmp_path):
    case = workspace(tmp_path)
    pipeline = Pipeline(tmp_path, quiet(stages={"agent1": {"enabled": False}}), FixtureBackend())
    with pytest.raises(PipelineFailure, match="agent1"):
        asyncio.run(pipeline.run(case))
    assert not (pipeline.directory / "report.json").exists()
    assert json.loads((pipeline.directory / "run.json").read_text())["status"] == "failed"


def test_checkpoint_reuse_skips_call(tmp_path):
    case = workspace(tmp_path)
    first = asyncio.run(Pipeline(tmp_path, quiet(), FixtureBackend()).run(case))
    backend = FixtureBackend()
    settings = quiet(stages={"agent1": {"enabled": False}})
    second = asyncio.run(Pipeline(tmp_path, settings, backend).run(case, first))
    assert "agent1" not in [name for name, _ in backend.calls]
    assert (first / "report.json").read_text() == (second / "report.json").read_text()


def test_stale_checkpoint_rejected(tmp_path):
    case = workspace(tmp_path)
    first = asyncio.run(Pipeline(tmp_path, quiet(), FixtureBackend()).run(case))
    with (tmp_path / "examples/requirements.md").open("a") as stream:
        stream.write("\nChanged source.\n")
    pipeline = Pipeline(tmp_path, quiet(stages={"agent1": {"enabled": False}}), FixtureBackend())
    with pytest.raises(PipelineFailure):
        asyncio.run(pipeline.run(case, first))


def test_checkpoint_output_integrity(tmp_path):
    directory = asyncio.run(Pipeline(tmp_path, quiet(), FixtureBackend()).run(workspace(tmp_path)))
    path = directory / "agent4.json"
    data = json.loads(path.read_text())
    data["output"]["explanations"][0]["explanation"] = "Tampered"
    write_json(path, data)
    with pytest.raises(ValueError, match="Corrupt"):
        restore(path, data["signature"], Narrative)


def test_parse_only_makes_no_llm_calls(tmp_path):
    backend = FixtureBackend()
    directory = asyncio.run(Pipeline(tmp_path, quiet(), backend).run(workspace(tmp_path), until="parse"))
    assert backend.calls == [] and not (directory / "report.json").exists()


def test_narrative_schema_cannot_replace_status():
    from pydantic import ValidationError
    with pytest.raises(ValidationError):
        Narrative.model_validate({"explanations": [], "status": "no_violation_found"})


def test_logging_switches_levels_and_secrets(tmp_path):
    settings = Settings(logging={"console": False, "level": "DEBUG"},
                        stages={"agent1": {"log_enabled": False}})
    log = EventLog(tmp_path, "test", settings)
    log.emit("agent1", "hidden")
    log.emit("agent2", "visible", key="sk-test-secret-123", authorization="Bearer secret")
    log.emit("check", "detail", "DEBUG", rule="R1")
    output = log.path.read_text()
    assert "hidden" not in output and "detail" in output
    assert "sk-test-secret-123" not in output and "Bearer secret" not in output
    assert output.count("[REDACTED]") == 2


def test_unknown_config_name_fails(tmp_path):
    path = tmp_path / "bad.toml"
    path.write_text('[stages.agnet1]\nenabled=false\n')
    with pytest.raises(ValueError, match="Unknown"):
        load_settings(path)


def test_environment_model_override(monkeypatch):
    monkeypatch.setenv("OPENAI_MODEL", "test-model")
    assert load_settings(ROOT / "config/pipeline.toml").llm.model == "test-model"


def test_gateway_base_url_selects_chat_completions(monkeypatch):
    monkeypatch.delenv("OPENAI_API_MODE", raising=False)
    monkeypatch.setenv("OPENAI_BASE_URL", "https://co.agentrouter.org/v1")
    assert load_settings(ROOT / "config/pipeline.toml").llm.api_mode == "chat_completions"


def test_explicit_responses_mode_overrides_gateway_default(monkeypatch):
    monkeypatch.setenv("OPENAI_BASE_URL", "https://co.agentrouter.org/v1")
    monkeypatch.setenv("OPENAI_API_MODE", "responses")
    assert load_settings(ROOT / "config/pipeline.toml").llm.api_mode == "responses"


def test_invalid_gateway_mode_fails_fast(monkeypatch):
    monkeypatch.setenv("OPENAI_API_MODE", "unknown")
    with pytest.raises(ValueError):
        load_settings(ROOT / "config/pipeline.toml")


def test_sdk_contracts_when_installed():
    agents = pytest.importorskip("agents", reason="Agents SDK not installed in offline test environment")
    from agents.agent_output import AgentOutputSchema
    from thesis_agents.models import Alignment, Narrative, Specification, Verification
    for schema in (Specification, Alignment, Verification, Narrative):
        output = AgentOutputSchema(schema)
        assert output.is_strict_json_schema()
        assert output.json_schema()["additionalProperties"] is False
    agents.ModelSettings(max_tokens=10000, store=False, temperature=None)
    agents.RunConfig(tracing_disabled=True, trace_include_sensitive_data=False)
