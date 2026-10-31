"""Reference/evidence validation; never presented as semantic completeness proof."""
import re

from .dataset import REQUIREMENT
from .mermaid import parse
from .models import Alignment, Diagram, Evidence, Inputs, Narrative, Report, Specification
from .models import Validation, Verification


def unique(values: list[str], label: str) -> set[str]:
    if len(set(values)) != len(values):
        raise ValueError(f"Duplicate IDs: {label}")
    return set(values)


def check_evidence(items: list[Evidence], inputs: Inputs, both: bool = False,
                   fr_only: bool = False) -> None:
    sources = {s.id: s for s in [*inputs.requirements, inputs.diagram]}
    seen = set()
    for item in items:
        if item.source_id not in sources or (fr_only and item.source_id == inputs.diagram.id):
            raise ValueError("Evidence points to an unauthorized source")
        lines = sources[item.source_id].text.splitlines()
        if not 1 <= item.line_start <= item.line_end <= len(lines):
            raise ValueError("Evidence line span is out of bounds")
        if item.quote not in "\n".join(lines[item.line_start - 1:item.line_end]):
            raise ValueError("Evidence quote does not exist in the declared source span")
        seen.add(item.source_id)
    if both and (inputs.diagram.id not in seen or not seen.intersection(s.id for s in inputs.requirements)):
        raise ValueError("Mapping evidence must cover both FR and SD")


def validate_ir(spec: Specification, diagram: Diagram, inputs: Inputs) -> Validation:
    roles = unique([r.id for r in spec.roles], "roles")
    predicates = unique([p.id for p in spec.predicates], "predicates")
    atoms = unique([a.id for a in spec.atoms], "atoms")
    for item in [*spec.roles, *spec.predicates, *spec.atoms, *spec.orders]:
        check_evidence(item.evidence, inputs, fr_only=True)
    sections = {}
    for source in inputs.requirements:
        for heading in REQUIREMENT.finditer(source.text):
            start = source.text[:heading.start()].count("\n") + 1
            next_heading = re.search(r"^#{1,3}\s+", source.text[heading.end():], re.MULTILINE)
            end_pos = heading.end() + next_heading.start() if next_heading else len(source.text)
            end = source.text[:end_pos].count("\n") + (2 if end_pos == len(source.text) else 1)
            sections[heading.group(1)] = (source.id, start, end)
    for atom in spec.atoms:
        if atom.requirement_id not in inputs.case.requirement_ids:
            raise ValueError("Agent 1 extracted an atom outside the selected scope")
        if atom.actor_role_id not in roles or (atom.receiver_role_id and atom.receiver_role_id not in roles):
            raise ValueError("Unknown role in specification atom")
        facts = [*atom.activation, *atom.preconditions, *atom.effects]
        if any(f.predicate_id not in predicates for f in facts):
            raise ValueError("Unknown predicate in specification atom")
        for group in (atom.activation, atom.preconditions, atom.effects):
            unique([f.predicate_id for f in group], "atom facts")
        source_id, start, end = sections[atom.requirement_id]
        if not any(e.source_id == source_id and start <= e.line_start <= e.line_end < end
                   for e in atom.evidence):
            raise ValueError("Atom has no evidence inside its own requirement section")
    for order in spec.orders:
        if order.before_atom_id not in atoms or order.after_atom_id not in atoms:
            raise ValueError("Order references an unknown atom")
        if order.before_atom_id == order.after_atom_id:
            raise ValueError("Self-referential order constraint")
    if diagram != parse(inputs.diagram):
        raise ValueError("Diagram IR does not match the source parser output")
    warnings = [*spec.uncertainties, *diagram.uncertainties]
    for req in inputs.case.requirement_ids:
        if not any(a.requirement_id == req for a in spec.atoms):
            warnings.append(f"No extracted atom for {req}; semantic coverage not established")
    return Validation(valid=True, uncertainties=list(dict.fromkeys(warnings)))


def validate_alignment(alignment: Alignment, spec: Specification, diagram: Diagram,
                       inputs: Inputs) -> None:
    mappings = [*alignment.roles, *alignment.behaviors, *alignment.guards]
    unique([m.id for m in mappings], "mappings")
    roles, atoms = {r.id for r in spec.roles}, {a.id for a in spec.atoms}
    predicates = {p.id for p in spec.predicates}
    participants = {p.id for p in diagram.participants}
    messages = {m.id for m in diagram.messages}
    branches = {b.id for f in diagram.fragments for b in f.branches}
    for mapping in mappings:
        check_evidence(mapping.evidence, inputs, both=True)
    for link in alignment.roles:
        if link.role_id not in roles or link.participant_id not in participants:
            raise ValueError("Role mapping references unknown elements")
    for link in alignment.behaviors:
        if not set(link.atom_ids) <= atoms or not set(link.message_ids) <= messages:
            raise ValueError("Behavior mapping references unknown elements")
        unique(link.atom_ids, "mapping atoms")
        unique(link.message_ids, "mapping messages")
        if link.anchor_message_id not in link.message_ids:
            raise ValueError("Anchor must belong to the mapped message group")
        if not link.atom_ids and link.relation != "refinement":
            raise ValueError("Only implementation refinements may have no requirement atom")
    for link in alignment.guards:
        if link.branch_id not in branches or any(f.predicate_id not in predicates for f in link.facts):
            raise ValueError("Guard mapping references unknown elements")
        unique([f.predicate_id for f in link.facts], "guard facts")


def validate_verification(result: Verification, alignment: Alignment, spec: Specification,
                          diagram: Diagram, inputs: Inputs) -> None:
    expected = {m.id for m in [*alignment.roles, *alignment.behaviors, *alignment.guards]}
    actual = unique([d.mapping_id for d in result.decisions], "decisions")
    if actual != expected:
        raise ValueError("Agent 3 must decide every candidate once, without inventing mappings")
    if not set(result.searched_atom_ids) <= {a.id for a in spec.atoms}:
        raise ValueError("Unknown searched atom")
    if not set(result.searched_message_ids) <= {m.id for m in diagram.messages}:
        raise ValueError("Unknown searched message")
    unique(result.searched_atom_ids, "searched atoms")
    unique(result.searched_message_ids, "searched messages")
    for decision in result.decisions:
        check_evidence(decision.evidence, inputs, both=True)
    accepted = {d.mapping_id for d in result.decisions if d.status == "accepted"}
    facts = {}
    for guard in alignment.guards:
        if guard.id in accepted:
            for fact in guard.facts:
                key = (guard.branch_id, fact.predicate_id)
                if key in facts and facts[key] != fact.value:
                    raise ValueError("Conflicting accepted facts for a diagram guard")
                facts[key] = fact.value
    roles = {}
    for link in alignment.roles:
        if link.id in accepted:
            key = (link.role_id, link.participant_id)
            compatible = link.relation != "incompatible"
            if key in roles and roles[key] != compatible:
                raise ValueError("Conflicting accepted role interpretations")
            roles[key] = compatible


def validate_narrative(result: Narrative, report: Report) -> None:
    ids = unique([x.finding_id for x in result.explanations], "report explanations")
    if ids != {f.id for f in report.findings}:
        raise ValueError("Agent 4 must explain exactly the canonical finding IDs")
