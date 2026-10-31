from conftest import LINEAR, bundle
from thesis_agents.models import Decision, GuardLink, RoleLink
from thesis_agents.reporting import aggregate


def results(checker, rule):
    return [f for f in checker.run().findings if f.rule == rule]


def test_r1_absence_requires_complete_scope(make_checker):
    text = LINEAR.replace("HR->>S: Setujui permohonan\n", "")
    assert any(f.status == "violation" for f in results(make_checker(bundle(text)), "R1"))
    assert not any(f.status == "violation" for f in results(make_checker(bundle(text, False)), "R1"))


def test_r1_conditional_obligation_abstains(make_checker):
    parts = bundle()
    parts[0].atoms[0].activation = [{"predicate_id": "effective", "value": True}]
    assert results(make_checker(parts), "R1")[0].status == "needs_review"


def test_r2_unmatched_detail_not_automatically_wrong(make_checker):
    parts = bundle(LINEAR + "S->>DB: Audit\n")
    assert results(make_checker(parts), "R2")[-1].status == "needs_review"
    parts[5].case.contract.closed_world = True
    assert results(make_checker(parts), "R2")[-1].status == "violation"


def test_r3_alias_accepted(make_checker):
    parts = bundle(LINEAR.replace("actor HR as HR", "actor HR as Line Manager"))
    assert all(f.status == "no_violation_found" for f in results(make_checker(parts), "R3"))


def test_r3_unknown_actor_not_automatically_incompatible(make_checker):
    parts = bundle(LINEAR.replace("HR->>S: Setujui", "DB->>S: Setujui"))
    assert results(make_checker(parts), "R3")[0].status == "needs_review"


def test_r3_explicit_verified_incompatibility(make_checker):
    parts = bundle(LINEAR.replace("HR->>S: Setujui", "DB->>S: Setujui"))
    link = RoleLink(id="ROLE-CONFLICT", role_id="HR", participant_id="DB", relation="incompatible",
                    evidence=[parts[0].roles[0].evidence[0], parts[1].participants[-1].evidence])
    parts[2].roles.append(link)
    parts[3].decisions.append(Decision(mapping_id=link.id, status="accepted", reason="Fixture",
                                      evidence=link.evidence))
    assert results(make_checker(parts), "R3")[0].status == "violation"


def test_r4_verified_conflicting_action(make_checker):
    parts = bundle()
    parts[2].behaviors[0].relation = "contradicts"
    assert results(make_checker(parts), "R4")[0].status == "violation"


def test_r5_reversed_direction(make_checker):
    parts = bundle(LINEAR.replace("HR->>S: Setujui", "S->>HR: Setujui"))
    assert results(make_checker(parts), "R5")[0].status == "violation"


def test_r6_linear_order_and_inversion(make_checker):
    assert results(make_checker(), "R6")[0].status == "no_violation_found"
    lines = LINEAR.splitlines()
    lines[-2], lines[-1] = lines[-1], lines[-2]
    assert results(make_checker(bundle("\n".join(lines))), "R6")[0].status == "violation"


def test_r6_separate_branches_not_globally_ordered(make_checker):
    text = LINEAR[:LINEAR.index("HR->>")] + "alt approved\nHR->>S: Setujui permohonan\nelse other\nS->>DB: Terapkan data\nend"
    assert results(make_checker(bundle(text, False)), "R6")[0].status == "needs_review"


def test_r6_unrelated_lifelines_abstain(make_checker):
    parts = bundle(LINEAR.replace("S->>DB: Terapkan", "X->>DB: Terapkan"))
    assert results(make_checker(parts), "R6")[0].status == "needs_review"


def test_r7_unknown_condition_abstains(make_checker):
    assert results(make_checker(), "R7")[0].status == "needs_review"


def guarded_parts(value):
    text = LINEAR.replace("S->>DB: Terapkan data", "alt Effective\nS->>DB: Terapkan data\nend")
    parts = bundle(text)
    spec, diagram, mapping, verified, _, _ = parts
    branch = diagram.fragments[0].branches[0]
    link = GuardLink(id="GUARD-1", branch_id=branch.id,
                     facts=[{"predicate_id": "effective", "value": value}],
                     evidence=[spec.atoms[-1].evidence[0], branch.evidence])
    mapping.guards.append(link)
    verified.decisions.append(Decision(mapping_id=link.id, status="accepted", reason="Fixture", evidence=link.evidence))
    return parts


def test_r7_guard_and_previous_effects(make_checker):
    assert results(make_checker(guarded_parts(True)), "R7")[0].status == "no_violation_found"


def test_r7_negative_required_condition(make_checker):
    assert results(make_checker(guarded_parts(False)), "R7")[0].status == "violation"


def test_future_guard_cannot_justify_earlier_action(make_checker):
    parts = guarded_parts(True)
    checker = make_checker(parts)
    assert "effective" not in checker.facts_before(parts[1].messages[0].id, checker.paths[0])


def test_rejected_mapping_not_realization(make_checker):
    parts = bundle()
    for decision in parts[3].decisions:
        if decision.mapping_id.startswith("MAP-APPROVE"):
            decision.status = "rejected"
    assert results(make_checker(parts), "R1")[0].status == "violation"


def test_disabled_rule_is_not_pass(make_checker):
    checks = make_checker(enabled={"R6": False}).run()
    assert all(f.status == "needs_review" for f in checks.findings if f.rule == "R6")
    report = aggregate("DEMO", checks, {"R6": False})
    assert report.abstained > 0 and report.coverage < 1 and "R6" in report.disabled_rules


def test_parser_uncertainty_prevents_definite_findings(make_checker):
    checks = make_checker(bundle(LINEAR + "unsupported command\n")).run()
    assert {f.status for f in checks.findings} == {"needs_review"}


def test_loop_order_not_claimed_fully_verified(make_checker):
    text = LINEAR[:LINEAR.index("HR->>")] + "loop Retry\nHR->>S: Setujui permohonan\nS->>DB: Terapkan data\nend"
    assert results(make_checker(bundle(text)), "R6")[0].status == "needs_review"


def test_unrelated_effect_cannot_satisfy_precondition(make_checker):
    parts = bundle(LINEAR.replace("S->>DB: Terapkan", "X->>DB: Terapkan"))
    checker = make_checker(parts)
    assert "approved" not in checker.facts_before(parts[1].messages[-1].id, checker.paths[0])


def test_many_to_many_group_requires_all_messages_on_path(make_checker):
    parts = bundle()
    first = parts[2].behaviors[0]
    first.atom_ids = ["APPROVE", "APPLY"]
    first.message_ids = [m.id for m in parts[1].messages]
    parts[2].behaviors = [first]
    assert all(f.status == "no_violation_found" for f in results(make_checker(parts), "R1"))
