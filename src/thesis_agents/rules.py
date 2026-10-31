"""Deterministic R1-R7 over verified IR; no LLM calls or executable input expressions.

Verdicts are relative to extracted semantics and accepted mappings, not formal proofs
of the source language. Absence requires complete scope and explicit bounded search.
Unsupported or uncertain semantics abstain rather than pretending to pass.
"""
from .config import RULES
from .logging_utils import EventLog
from .mermaid import traces
from .models import Alignment, Atom, BehaviorLink, Checks, Diagram, Evidence, Finding
from .models import Inputs, Specification, Validation, Verification


class RuleChecker:
    def __init__(self, spec: Specification, diagram: Diagram, alignment: Alignment,
                 verified: Verification, validation: Validation, inputs: Inputs,
                 enabled: dict[str, bool], max_paths: int, log: EventLog):
        self.spec, self.diagram = spec, diagram
        self.alignment, self.verified = alignment, verified
        self.validation, self.contract = validation, inputs.case.contract
        self.enabled, self.log = enabled, log
        self.atoms = {a.id: a for a in spec.atoms}
        self.messages = {m.id: m for m in diagram.messages}
        accepted = {d.mapping_id for d in verified.decisions if d.status == "accepted"}
        self.behaviors = [m for m in alignment.behaviors if m.id in accepted]
        self.roles = [m for m in alignment.roles if m.id in accepted]
        self.guards = [m for m in alignment.guards if m.id in accepted]
        self.paths, self.paths_complete = traces(diagram, max_paths)
        self.findings: list[Finding] = []
        self.warnings = list(dict.fromkeys([
            *validation.uncertainties, *alignment.uncertainties, *verified.uncertainties,
        ]))
        if not self.paths_complete:
            self.warnings.append("Path analysis incomplete: loop, unsupported syntax or path limit")
        if any(d.status == "needs_review" for d in verified.decisions):
            self.warnings.append("Some semantic mappings remain uncertain")

    def emit(self, rule: str, status: str, ids: list[str], expected: str, observed: str,
             evidence: list[Evidence]) -> None:
        if self.validation.uncertainties and status != "needs_review":
            status = "needs_review"
            observed = "IR uncertainty prevents a definite verdict. " + observed
        number = 1 + sum(f.rule == rule for f in self.findings)
        unique = {e.model_dump_json(): e for e in evidence}
        finding = Finding(id=f"{rule}-{number:04d}", rule=rule, status=status,
                          element_ids=ids, expected=expected, observed=observed,
                          evidence=list(unique.values()))
        self.findings.append(finding)
        self.log.emit("check", "rule_result", "DEBUG", rule=rule,
                      finding_id=finding.id, status=status, element_ids=ids)

    def links(self, atom: Atom, relation: str | None = None) -> list[BehaviorLink]:
        return [m for m in self.behaviors if atom.id in m.atom_ids
                and (relation is None or m.relation == relation)]

    def absence_ready(self, atom_id: str | None = None, message_id: str | None = None) -> bool:
        return (self.contract.scope_complete and self.paths_complete and not self.warnings
                and (atom_id is None or atom_id in self.verified.searched_atom_ids)
                and (message_id is None or message_id in self.verified.searched_message_ids))

    def role_targets(self, role_id: str | None) -> set[str]:
        return {r.participant_id for r in self.roles
                if r.role_id == role_id and r.relation != "incompatible"}

    def incompatible(self, role_id: str | None, participant_id: str) -> bool:
        return any(r.role_id == role_id and r.participant_id == participant_id
                   and r.relation == "incompatible" for r in self.roles)

    def evidence(self, atom: Atom, link: BehaviorLink) -> list[Evidence]:
        return [*atom.evidence, *link.evidence,
                *(self.messages[m].evidence for m in link.message_ids)]

    def run(self) -> Checks:
        self.log.emit("check", "paths_built", count=len(self.paths), complete=self.paths_complete)
        for rule in RULES:
            self.log.emit("check", "rule_start", rule=rule)
            previous = len(self.findings)
            if self.enabled.get(rule, True):
                getattr(self, f"check_{rule.lower()}")()
            else:
                self.emit(rule, "needs_review", [], "Rule enabled", "Rule disabled by config", [])
            if len(self.findings) == previous:
                self.emit(rule, "needs_review", [], "Applicable verified constraints",
                          "No applicable constraints/mappings; no consistency claim", [])
            self.log.emit("check", "rule_end", rule=rule, results=len(self.findings) - previous)
        return Checks(findings=self.findings, uncertainties=self.warnings)

    def check_r1(self) -> None:
        for atom in self.spec.atoms:
            if atom.modality != "required":
                continue
            links = self.links(atom, "realizes")
            covered = [any(set(m.message_ids) <= set(path) for m in links) for path in self.paths]
            if atom.activation or not self.paths_complete:
                status, detail = "needs_review", "Conditional obligation or incomplete path semantics"
            elif covered and all(covered):
                status, detail = "no_violation_found", "Realization group exists on every modeled path"
            elif self.absence_ready(atom_id=atom.id):
                status, detail = "violation", "A complete modeled path lacks the mandatory realization"
            else:
                status, detail = "needs_review", "No proven realization; scope/search may be incomplete"
            evidence = [*atom.evidence, *(e for link in links for e in link.evidence)]
            self.emit("R1", status, [atom.id], atom.action, detail, evidence)

    def check_r2(self) -> None:
        for atom in self.spec.atoms:
            if atom.modality != "prohibited":
                continue
            for link in self.links(atom, "realizes"):
                status = "needs_review" if atom.activation or not self.paths_complete else "violation"
                self.emit("R2", status, [atom.id, *link.message_ids], "Prohibited action absent",
                          "Verified realization of a prohibited action", self.evidence(atom, link))
        for message in self.diagram.messages:
            links = [m for m in self.behaviors if message.id in m.message_ids]
            supported = any(m.relation == "realizes" and all(
                self.atoms[a].modality != "prohibited" for a in m.atom_ids
            ) for m in links)
            refinement = any(m.relation == "refinement" for m in links)
            if supported or (refinement and self.contract.allow_technical_refinement):
                status, text = "no_violation_found", "Supported behavior or allowed technical refinement"
            elif self.contract.closed_world and self.absence_ready(message_id=message.id) and not links:
                status, text = "violation", "Unmatched message violates explicit closed-world contract"
            else:
                status, text = "needs_review", "Additional/unmatched behavior is not automatically forbidden"
            self.emit("R2", status, [message.id], "Supported or explicitly permitted behavior",
                      text, [message.evidence, *(e for link in links for e in link.evidence)])

    def endpoints(self, rule: str) -> None:
        for atom in self.spec.atoms:
            for link in self.links(atom):
                if link.relation not in {"realizes", "contradicts"}:
                    continue
                message = self.messages[link.anchor_message_id]
                senders = self.role_targets(atom.actor_role_id)
                receivers = self.role_targets(atom.receiver_role_id)
                reverse = message.sender in receivers and message.receiver in senders
                correct = message.sender in senders and (
                    not atom.receiver_role_id or message.receiver in receivers)
                conflict = self.incompatible(atom.actor_role_id, message.sender) or (
                    bool(atom.receiver_role_id) and self.incompatible(atom.receiver_role_id, message.receiver))
                if len(link.atom_ids) > 1:
                    status, text = "needs_review", "Multi-atom anchor has ambiguous endpoint responsibility"
                elif rule == "R5":
                    if not atom.receiver_role_id:
                        status, text = "needs_review", "Required receiver is unspecified"
                    elif reverse and not correct:
                        status, text = "violation", "Verified endpoints reverse the required interaction"
                    elif correct:
                        status, text = "no_violation_found", "Endpoints follow the required direction"
                    else:
                        status, text = "needs_review", "Endpoint correspondence not established"
                elif correct or reverse:
                    status, text = "no_violation_found", "Roles present; reversal is handled separately by R5"
                elif conflict:
                    status, text = "violation", "Verified incompatible participant responsibility"
                else:
                    status, text = "needs_review", "Missing alias does not prove incompatible responsibility"
                evidence = self.evidence(atom, link)
                evidence.extend(e for role in self.roles for e in role.evidence
                                if role.role_id in {atom.actor_role_id, atom.receiver_role_id})
                self.emit(rule, status, [atom.id, message.id], "Endpoints match verified responsibilities",
                          text, evidence)

    def check_r3(self) -> None:
        self.endpoints("R3")

    def check_r4(self) -> None:
        for atom in self.spec.atoms:
            for link in self.links(atom):
                status = {"realizes": "no_violation_found", "contradicts": "violation"}.get(
                    link.relation, "needs_review")
                self.emit("R4", status, [atom.id, *link.message_ids], atom.action,
                          f"Verified semantic relation: {link.relation}", self.evidence(atom, link))

    def check_r5(self) -> None:
        self.endpoints("R5")

    def precedes(self, before: str, after: str, path: list[str]) -> bool:
        """Conservative message precedence; unrelated lifelines are not serialized."""
        if path.index(before) >= path.index(after):
            return False
        if self.contract.ordering == "explicit_message_order":
            return True
        reached = {before}
        for node in path[path.index(before) + 1:path.index(after) + 1]:
            current = self.messages[node]
            if current.arrow.endswith(")"):
                continue
            current_roles = {current.sender, current.receiver}
            if any(not self.messages[r].arrow.endswith(")") and current_roles.intersection(
                {self.messages[r].sender, self.messages[r].receiver}) for r in reached):
                reached.add(node)
        return after in reached

    def check_r6(self) -> None:
        for order in self.spec.orders:
            before, after = self.atoms[order.before_atom_id], self.atoms[order.after_atom_id]
            evidence = list(order.evidence)
            outcomes = []
            for path in self.paths:
                first = [m for m in self.links(before, "realizes") if set(m.message_ids) <= set(path)]
                second = [m for m in self.links(after, "realizes") if set(m.message_ids) <= set(path)]
                for tail in second:
                    evidence.extend(tail.evidence)
                    if not self.paths_complete or before.activation or after.activation:
                        outcomes.append("needs_review")
                        continue
                    end = min(tail.message_ids, key=path.index)
                    if any(self.precedes(max(head.message_ids, key=path.index), end, path) for head in first):
                        outcomes.append("no_violation_found")
                    elif any(self.precedes(end, min(head.message_ids, key=path.index), path) for head in first):
                        outcomes.append("violation")
                    elif not first and self.absence_ready(atom_id=before.id):
                        outcomes.append("violation")
                    else:
                        outcomes.append("needs_review")
                    evidence.extend(e for head in first for e in head.evidence)
            self.emit("R6", self.combine(outcomes), [before.id, after.id],
                      "First behavior must precede second",
                      f"Path-relative precedence outcomes: {outcomes or ['not established']}", evidence)

    @staticmethod
    def combine(outcomes: list[str]) -> str:
        if "violation" in outcomes:
            return "violation"
        if not outcomes or "needs_review" in outcomes:
            return "needs_review"
        return "no_violation_found"

    def facts_before(self, target: str, path: list[str]) -> dict[str, bool | None]:
        """Accepted guard entailments and completed effects, never future/own effects."""
        facts: dict[str, bool | None] = {}
        previous_branches: set[str] = set()
        for node in path:
            message = self.messages[node]
            entered = set(message.branch_ids) - previous_branches
            new_facts: dict[str, set[bool]] = {}
            for guard in self.guards:
                if guard.branch_id in entered:
                    for fact in guard.facts:
                        new_facts.setdefault(fact.predicate_id, set()).add(fact.value)
            for predicate, values in new_facts.items():
                facts[predicate] = next(iter(values)) if len(values) == 1 else None
            if node == target:
                return facts
            effects: dict[str, set[bool]] = {}
            for link in self.behaviors:
                if link.relation != "realizes" or not set(link.message_ids) <= set(path):
                    continue
                if node != max(link.message_ids, key=path.index) or not self.precedes(node, target, path):
                    continue
                for aid in link.atom_ids:
                    for fact in self.atoms[aid].effects:
                        effects.setdefault(fact.predicate_id, set()).add(fact.value)
            for predicate, values in effects.items():
                facts[predicate] = next(iter(values)) if len(values) == 1 else None
            previous_branches = set(message.branch_ids)
        return facts

    def check_r7(self) -> None:
        for atom in self.spec.atoms:
            if not atom.preconditions:
                continue
            outcomes = []
            evidence = list(atom.evidence)
            for path in self.paths:
                for link in self.links(atom, "realizes"):
                    if not set(link.message_ids) <= set(path):
                        continue
                    facts = self.facts_before(link.anchor_message_id, path)
                    values = [facts.get(f.predicate_id) for f in atom.preconditions]
                    if not self.paths_complete:
                        outcomes.append("needs_review")
                    elif any(v is not None and v != f.value for v, f in zip(values, atom.preconditions)):
                        outcomes.append("violation")
                    elif all(v is not None and v == f.value for v, f in zip(values, atom.preconditions)):
                        outcomes.append("no_violation_found")
                    else:
                        outcomes.append("needs_review")
                    evidence.extend(link.evidence)
            evidence.extend(e for guard in self.guards for e in guard.evidence)
            evidence.extend(e for other in self.spec.atoms for e in other.evidence if other.effects)
            self.emit("R7", self.combine(outcomes), [atom.id],
                      "All preconditions hold before the mapped action",
                      f"Forward condition outcomes: {outcomes or ['not established']}", evidence)
