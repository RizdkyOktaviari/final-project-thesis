"""Shared typed contracts. Evidence lines are 1-based and inclusive.

These schemas validate representation, not the semantic truth of an LLM response.
Unknown information must stay explicit instead of being silently treated as false.
"""
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

Status = Literal["violation", "no_violation_found", "needs_review"]
DecisionStatus = Literal["accepted", "rejected", "needs_review"]


class Model(BaseModel):
    model_config = ConfigDict(extra="forbid", validate_assignment=True)


class Evidence(Model):
    source_id: str
    line_start: int = Field(ge=1)
    line_end: int = Field(ge=1)
    quote: str = Field(min_length=1)


class Source(Model):
    id: str
    text: str
    sha256: str


class Contract(Model):
    """Dataset policy, never the expected answer for a particular diagram."""
    scope_complete: bool = False
    allow_technical_refinement: bool = True
    closed_world: bool = False
    ordering: Literal["shared_lifeline", "explicit_message_order"] = "shared_lifeline"
    assumptions: list[str] = Field(default_factory=list)


class Case(Model):
    id: str = Field(pattern=r"^[A-Za-z0-9_-]+$")
    requirement_ids: list[str] = Field(min_length=1)
    requirement_files: list[str] = Field(min_length=1)
    diagram_file: str
    contract: Contract = Field(default_factory=Contract)


class Inputs(Model):
    case: Case
    requirements: list[Source]
    diagram: Source


class Role(Model):
    id: str
    name: str
    evidence: list[Evidence] = Field(min_length=1)


class Predicate(Model):
    id: str
    meaning: str
    evidence: list[Evidence] = Field(min_length=1)


class Fact(Model):
    predicate_id: str
    value: bool


class Atom(Model):
    id: str
    requirement_id: str
    actor_role_id: str
    receiver_role_id: str | None = None
    action: str
    object: str
    modality: Literal["required", "optional", "prohibited"]
    flow: Literal["main", "alternative", "exception"] = "main"
    activation: list[Fact] = Field(default_factory=list)
    preconditions: list[Fact] = Field(default_factory=list)
    effects: list[Fact] = Field(default_factory=list)
    evidence: list[Evidence] = Field(min_length=1)


class Order(Model):
    before_atom_id: str
    after_atom_id: str
    evidence: list[Evidence] = Field(min_length=1)


class Specification(Model):
    roles: list[Role]
    predicates: list[Predicate]
    atoms: list[Atom]
    orders: list[Order]
    uncertainties: list[str]


class Participant(Model):
    id: str
    label: str
    kind: Literal["actor", "participant"]
    implicit: bool = False
    evidence: Evidence


class Message(Model):
    id: str
    sender: str
    receiver: str
    arrow: str
    text: str
    branch_ids: list[str]
    evidence: Evidence


class Branch(Model):
    id: str
    guard: str
    nodes: list[str] = Field(default_factory=list)
    evidence: Evidence


class Fragment(Model):
    id: str
    kind: Literal["alt", "opt", "loop"]
    branches: list[Branch]
    evidence: Evidence


class Diagram(Model):
    participants: list[Participant]
    messages: list[Message]
    fragments: list[Fragment]
    nodes: list[str]
    uncertainties: list[str]


class Validation(Model):
    valid: bool
    uncertainties: list[str]


class RoleLink(Model):
    id: str
    role_id: str
    participant_id: str
    relation: Literal["equivalent", "component_of", "incompatible"]
    evidence: list[Evidence] = Field(min_length=2)


class BehaviorLink(Model):
    id: str
    atom_ids: list[str]
    message_ids: list[str] = Field(min_length=1)
    anchor_message_id: str
    relation: Literal["realizes", "contradicts", "partial", "refinement"]
    evidence: list[Evidence] = Field(min_length=2)


class GuardLink(Model):
    """Facts must be ENTAILED by the whole guard, not merely mentioned."""
    id: str
    branch_id: str
    facts: list[Fact] = Field(min_length=1)
    evidence: list[Evidence] = Field(min_length=2)


class Alignment(Model):
    roles: list[RoleLink]
    behaviors: list[BehaviorLink]
    guards: list[GuardLink]
    uncertainties: list[str]


class Decision(Model):
    mapping_id: str
    status: DecisionStatus
    reason: str
    evidence: list[Evidence] = Field(min_length=2)


class Verification(Model):
    decisions: list[Decision]
    searched_atom_ids: list[str]
    searched_message_ids: list[str]
    uncertainties: list[str]


class Finding(Model):
    id: str
    rule: Literal["R1", "R2", "R3", "R4", "R5", "R6", "R7"]
    status: Status
    element_ids: list[str]
    expected: str
    observed: str
    evidence: list[Evidence]


class Checks(Model):
    findings: list[Finding]
    uncertainties: list[str]


class Report(Model):
    case_id: str
    status: Status
    findings: list[Finding]
    uncertainties: list[str]
    assessed: int
    abstained: int
    coverage: float
    disabled_rules: list[str]


class Explanation(Model):
    finding_id: str
    explanation: str
    recommendation: str


class Narrative(Model):
    """No status/evidence fields: LLM prose cannot replace canonical decisions."""
    explanations: list[Explanation]
