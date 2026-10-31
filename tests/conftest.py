"""Hand-authored fixtures test software behavior, not research accuracy."""
import hashlib
from pathlib import Path

import pytest

from thesis_agents.config import Settings
from thesis_agents.logging_utils import EventLog
from thesis_agents.mermaid import parse
from thesis_agents.models import Alignment, Atom, BehaviorLink, Case, Contract, Decision
from thesis_agents.models import Evidence, Fact, Inputs, Order, Predicate, Role, RoleLink
from thesis_agents.models import Source, Specification, Verification
from thesis_agents.validation import validate_ir

ROOT = Path(__file__).resolve().parents[1]
FR = (ROOT / "examples/requirements.md").read_text(encoding="utf-8")
LINEAR = """sequenceDiagram
actor HR as HR
participant S as Sistem
participant DB as Database
HR->>S: Setujui permohonan
S->>DB: Terapkan data
"""


def source(identifier, text):
    return Source(id=identifier, text=text, sha256=hashlib.sha256(text.encode()).hexdigest())


def bundle(text=LINEAR, complete=True):
    fr, sd = source("examples/requirements.md", FR), source("examples/sequence.mmd", text)
    inputs = Inputs(case=Case(id="DEMO", requirement_ids=["REQ-DEMO-001", "REQ-DEMO-002"],
                             requirement_files=[fr.id], diagram_file=sd.id,
                             contract=Contract(scope_complete=complete)), requirements=[fr], diagram=sd)
    ev1 = Evidence(source_id=fr.id, line_start=3, line_end=3, quote=FR.splitlines()[2])
    ev2 = Evidence(source_id=fr.id, line_start=5, line_end=5, quote=FR.splitlines()[4])
    spec = Specification(
        roles=[Role(id="HR", name="HR", evidence=[ev1]),
               Role(id="SYSTEM", name="Sistem", evidence=[ev2])],
        predicates=[Predicate(id="approved", meaning="Approved", evidence=[ev1]),
                    Predicate(id="effective", meaning="Tanggal efektif berlaku", evidence=[ev2])],
        atoms=[Atom(id="APPROVE", requirement_id="REQ-DEMO-001", actor_role_id="HR",
                    receiver_role_id="SYSTEM", action="approve", object="request", modality="required",
                    effects=[Fact(predicate_id="approved", value=True)], evidence=[ev1]),
               Atom(id="APPLY", requirement_id="REQ-DEMO-002", actor_role_id="SYSTEM",
                    action="apply", object="data", modality="required",
                    preconditions=[Fact(predicate_id="approved", value=True),
                                   Fact(predicate_id="effective", value=True)], evidence=[ev2])],
        orders=[Order(before_atom_id="APPROVE", after_atom_id="APPLY", evidence=[ev1])],
        uncertainties=[],
    )
    diagram = parse(sd)
    participants = {p.id: p for p in diagram.participants}
    roles = [RoleLink(id=f"ROLE-{r}", role_id=r, participant_id=p, relation="equivalent",
                      evidence=[e, participants[p].evidence]) for r, p, e in
             [("HR", "HR", ev1), ("SYSTEM", "S", ev2)] if p in participants]
    behaviors = []
    for atom, word, ev in [("APPROVE", "Setujui", ev1), ("APPLY", "Terapkan", ev2)]:
        for message in diagram.messages:
            if word in message.text:
                behaviors.append(BehaviorLink(id=f"MAP-{atom}-{message.id}", atom_ids=[atom],
                                              message_ids=[message.id], anchor_message_id=message.id,
                                              relation="realizes", evidence=[ev, message.evidence]))
    alignment = Alignment(roles=roles, behaviors=behaviors, guards=[], uncertainties=[])
    decisions = [Decision(mapping_id=m.id, status="accepted", reason="Synthetic test fixture",
                          evidence=m.evidence) for m in [*alignment.roles, *alignment.behaviors]]
    verified = Verification(decisions=decisions, searched_atom_ids=[a.id for a in spec.atoms],
                            searched_message_ids=[m.id for m in diagram.messages], uncertainties=[])
    validation = validate_ir(spec, diagram, inputs)
    return spec, diagram, alignment, verified, validation, inputs


@pytest.fixture
def make_checker(tmp_path):
    from thesis_agents.rules import RuleChecker
    def factory(parts=None, **kwargs):
        log = EventLog(tmp_path, "test", Settings(logging={"enabled": False}))
        return RuleChecker(*(parts or bundle()), enabled=kwargs.get("enabled", {}),
                           max_paths=kwargs.get("max_paths", 128), log=log)
    return factory
