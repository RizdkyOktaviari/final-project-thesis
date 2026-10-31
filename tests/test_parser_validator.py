import pytest

from conftest import LINEAR, bundle, source
from thesis_agents.mermaid import parse, traces
from thesis_agents.models import Evidence
from thesis_agents.validation import check_evidence, validate_alignment, validate_ir, validate_verification


def test_nested_fragments_preserve_membership():
    text = "sequenceDiagram\nalt Success\n opt Notify\n  A->>B: Notify\n end\nelse Failure\n A->>C: Error\nend"
    diagram = parse(source("examples/nested.mmd", text))
    paths, complete = traces(diagram, 32)
    assert complete and len(paths) == 3
    assert len(diagram.messages[0].branch_ids) == 2
    assert not any(len(p) == 2 for p in paths)


def test_alt_without_else_has_skip_path():
    diagram = parse(source("examples/a.mmd", "sequenceDiagram\nalt ok\n A->>B: hi\nend"))
    assert [] in traces(diagram, 10)[0]


@pytest.mark.parametrize("text", ["", "graph TD", "sequenceDiagram\nend",
                                  "sequenceDiagram\nalt ok\nA->>B: hi",
                                  "sequenceDiagram\npar task\nA->>B: hi\nend",
                                  "sequenceDiagram\nelse wrong"])
def test_malformed_or_unsupported_structure_fails(text):
    with pytest.raises(ValueError):
        parse(source("examples/bad.mmd", text))


def test_unknown_line_not_silent():
    diagram = parse(source("examples/a.mmd", LINEAR + "mystery data\n"))
    assert diagram.uncertainties and not traces(diagram, 10)[1]


def test_implicit_participants_and_async_arrows():
    diagram = parse(source("examples/a.mmd", "sequenceDiagram\nA-)B: job\nB-->>A: done"))
    assert all(p.implicit for p in diagram.participants)
    assert diagram.messages[0].arrow == "-)"


def test_loop_and_path_limit_incomplete():
    diagram = parse(source("examples/a.mmd", "sequenceDiagram\nloop Retry\nA->>B: job\nend"))
    assert not traces(diagram, 10)[1]
    diagram = parse(source("examples/a.mmd", "sequenceDiagram\nalt ok\nA->>B: x\nelse no\nA->>B: y\nend"))
    assert not traces(diagram, 1)[1]


def test_grounded_ir_and_mappings_pass():
    spec, diagram, mapping, verified, _, inputs = bundle()
    validate_alignment(mapping, spec, diagram, inputs)
    validate_verification(verified, mapping, spec, diagram, inputs)
    assert validate_ir(spec, diagram, inputs).valid


@pytest.mark.parametrize("field,value", [("quote", "A fabricated quote"), ("line_end", 999),
                                          ("source_id", "ground_truth.csv")])
def test_fabricated_evidence_rejected(field, value):
    *_, inputs = bundle()
    ev = Evidence(source_id=inputs.requirements[0].id, line_start=3, line_end=3, quote="HR")
    setattr(ev, field, value)
    with pytest.raises(ValueError):
        check_evidence([ev], inputs)


def test_unknown_role_and_out_of_scope_atom():
    spec, diagram, _, _, _, inputs = bundle()
    spec.atoms[0].actor_role_id = "UNKNOWN"
    with pytest.raises(ValueError):
        validate_ir(spec, diagram, inputs)
    spec.atoms[0].actor_role_id = "HR"
    spec.atoms[0].requirement_id = "REQ-UNSCOPED-999"
    with pytest.raises(ValueError):
        validate_ir(spec, diagram, inputs)


def test_tampered_diagram_rejected():
    spec, diagram, _, _, _, inputs = bundle()
    diagram.messages[0].receiver = "DB"
    with pytest.raises(ValueError):
        validate_ir(spec, diagram, inputs)


def test_verifier_must_cover_every_candidate():
    spec, diagram, mapping, verified, _, inputs = bundle()
    verified.decisions.pop()
    with pytest.raises(ValueError):
        validate_verification(verified, mapping, spec, diagram, inputs)


def test_atom_evidence_cannot_escape_own_section():
    spec, diagram, _, _, _, inputs = bundle()
    inputs.requirements[0].text += "\n## Supporting context\nAn unrelated rule.\n"
    spec.atoms[-1].evidence = [Evidence(source_id=inputs.requirements[0].id,
                                       line_start=8, line_end=8, quote="An unrelated rule.")]
    with pytest.raises(ValueError, match="own requirement"):
        validate_ir(spec, diagram, inputs)
