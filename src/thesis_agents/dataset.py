"""Inference never reads mutation labels. prepare_cases is a separate projection."""
import hashlib
import json
import re
from pathlib import Path

from .logging_utils import EventLog
from .models import Case, Inputs, Source
from .storage import write_json

REQUIREMENT = re.compile(r"^###\s+(REQ-[A-Z0-9]+-\d+):", re.MULTILINE)


def inside(root: Path, path: str) -> Path:
    result = (root / path).resolve()
    if not result.is_relative_to(root.resolve()):
        raise ValueError("Input path leaves the repository")
    return result


def read_source(root: Path, path: str, kind: str, limit: int, log: EventLog) -> Source:
    file = inside(root, path)
    relative = file.relative_to(root.resolve()).as_posix()
    prefixes = ("data/requirements text/", "data/raw/", "examples/") if kind == "fr" else (
        "data/sequence-diagrams/diagrams/", "examples/",
    )
    suffix = ".md" if kind == "fr" else ".mmd"
    if not relative.startswith(prefixes) or file.suffix != suffix:
        raise ValueError(f"Source is outside the {kind} input allowlist")
    if file.stat().st_size > limit * 4:
        raise ValueError("Source exceeds configured character budget")
    text = file.read_text(encoding="utf-8-sig")
    if len(text) > limit:
        raise ValueError("Source exceeds configured character budget")
    source = Source(id=relative, text=text, sha256=hashlib.sha256(text.encode()).hexdigest())
    log.emit("load", "source_loaded", source_id=source.id, chars=len(text), sha256=source.sha256)
    return source


def load_inputs(root: Path, case_file: Path, limit: int, log: EventLog) -> Inputs:
    case = Case.model_validate_json(case_file.read_text(encoding="utf-8"))
    if len(set(case.requirement_ids)) != len(case.requirement_ids):
        raise ValueError("Duplicate requirement IDs in case")
    if len(set(case.requirement_files)) != len(case.requirement_files):
        raise ValueError("Duplicate requirement files in case")
    sources = [read_source(root, p, "fr", limit, log) for p in case.requirement_files]
    diagram = read_source(root, case.diagram_file, "sd", limit, log)
    if sum(len(s.text) for s in sources) + len(diagram.text) > limit:
        raise ValueError("Combined inputs exceed configured character budget")
    ids = [req for source in sources for req in REQUIREMENT.findall(source.text)]
    for requirement in case.requirement_ids:
        if ids.count(requirement) != 1:
            raise ValueError(f"Requirement must exist exactly once: {requirement}")
    return Inputs(case=case, requirements=sources, diagram=diagram)


def numbered(source: Source) -> dict:
    """Preserve original line numbers; supporting context is not extraction scope."""
    return {"source_id": source.id, "lines": [
        {"line": i, "text": text} for i, text in enumerate(source.text.splitlines(), 1)
    ]}


def prepare_cases(root: Path, output: Path) -> int:
    """Offline allowlist projection; never serialize labels or explanations."""
    index: dict[str, str] = {}
    for path in sorted((root / "data/requirements text").glob("*.md")):
        for req in REQUIREMENT.findall(path.read_text(encoding="utf-8")):
            if req in index:
                raise ValueError(f"Duplicate requirement: {req}")
            index[req] = path.relative_to(root).as_posix()
    rows = json.loads((root / "data/sequence-diagrams/manifest.json").read_text(encoding="utf-8"))
    cases = []
    for row in rows:
        ids = row["requirement_ids"]
        case = Case(id=row["diagram_id"], requirement_ids=ids,
                    requirement_files=sorted({index[r] for r in ids}),
                    diagram_file="data/sequence-diagrams/" + row["diagram_file"])
        inside(root, case.diagram_file)
        cases.append(case)
    if len({c.id for c in cases}) != len(cases):
        raise ValueError("Duplicate case IDs")
    for case in cases:
        if (output / f"{case.id}.json").exists():
            raise ValueError(f"Will not overwrite curated contract: {case.id}")
    for case in cases:
        write_json(output / f"{case.id}.json", case)
    return len(cases)
