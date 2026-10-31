import json

import pytest

from conftest import FR
from thesis_agents.config import Settings
from thesis_agents.dataset import inside, prepare_cases, read_source
from thesis_agents.logging_utils import EventLog
from thesis_agents.models import Case


def test_path_traversal_rejected(tmp_path):
    with pytest.raises(ValueError):
        inside(tmp_path, "../secrets.env")


def test_gold_not_an_inference_source(tmp_path):
    (tmp_path / "ground_truth.csv").write_text("confidential label")
    log = EventLog(tmp_path, "test", Settings(logging={"enabled": False}))
    with pytest.raises(ValueError, match="allowlist"):
        read_source(tmp_path, "ground_truth.csv", "fr", 1000, log)


def test_prepare_projects_safe_fields_preserves_curated_cases(tmp_path):
    frdir = tmp_path / "data/requirements text"
    frdir.mkdir(parents=True)
    (frdir / "test.md").write_text(FR, encoding="utf-8")
    directory = tmp_path / "data/sequence-diagrams"
    directory.mkdir()
    manifest = [{"diagram_id": "SD-DEMO", "requirement_ids": ["REQ-DEMO-001"],
                 "diagram_file": "diagrams/a.mmd", "has_injected_inconsistency": True,
                 "inconsistency": "SECRET_GOLD_ANSWER"}]
    (directory / "manifest.json").write_text(json.dumps(manifest))
    output = tmp_path / "cases"
    assert prepare_cases(tmp_path, output) == 1
    text = (output / "SD-DEMO.json").read_text()
    assert "SECRET_GOLD_ANSWER" not in text and "inconsistency" not in text
    assert not Case.model_validate_json(text).contract.scope_complete
    with pytest.raises(ValueError, match="overwrite"):
        prepare_cases(tmp_path, output)
