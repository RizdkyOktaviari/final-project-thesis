"""Canonical decisions are Python-owned. LLM prose is a separate advisory layer."""
from .config import RULES
from .models import Alignment, Checks, Diagram, Narrative, Report, Specification, Verification


def aggregate(case_id: str, checks: Checks, rules: dict[str, bool]) -> Report:
    unique = {}
    for finding in checks.findings:
        key = (finding.rule, tuple(sorted(finding.element_ids)), finding.status,
               finding.expected, finding.observed)
        unique.setdefault(key, finding)
    findings = list(unique.values())
    abstained = sum(f.status == "needs_review" for f in findings)
    assessed = len(findings) - abstained
    disabled = [r for r in RULES if not rules.get(r, True)]
    uncertainties = list(dict.fromkeys(checks.uncertainties))
    if any(f.status == "violation" for f in findings):
        status = "violation"
    elif not findings or abstained or uncertainties or disabled:
        status = "needs_review"
    else:
        status = "no_violation_found"
    return Report(case_id=case_id, status=status, findings=findings, uncertainties=uncertainties,
                  assessed=assessed, abstained=abstained,
                  coverage=assessed / len(findings) if findings else 0.0,
                  disabled_rules=disabled)


def render(report: Report, narrative: Narrative | None) -> str:
    prose = {p.finding_id: p for p in narrative.explanations} if narrative else {}
    lines = [f"# Laporan konsistensi: {report.case_id}", "", f"Status: `{report.status}`", "",
             f"Pemeriksaan terputuskan: {report.assessed}; abstention: {report.abstained}.",
             f"Coverage pemeriksaan yang dihasilkan: {report.coverage:.1%}.", "",
             "Coverage bukan jaminan seluruh makna sumber telah diekstraksi. Jumlah hasil",
             "pemeriksaan bukan jumlah akar masalah unik. needs_review adalah abstention",
             "otomatis, bukan tahap persetujuan manusia.", ""]
    if not narrative:
        lines += ["Narasi LLM tidak digunakan; laporan dirender deterministik.", ""]
    for finding in report.findings:
        lines += [f"## {finding.id} - {finding.rule}", f"Status: `{finding.status}`", "",
                  f"Elemen: {', '.join(finding.element_ids) or '-'}",
                  f"Expected: {finding.expected}", f"Observed: {finding.observed}", ""]
        for evidence in finding.evidence:
            lines += [f"Sumber: `{evidence.source_id}` baris {evidence.line_start}-{evidence.line_end}",
                      "", *(f"> {line}" for line in evidence.quote.splitlines()), ""]
        if finding.id in prose:
            item = prose[finding.id]
            lines += ["**Narasi LLM (advisory; status di atas tetap otoritatif):**",
                      item.explanation, "", "**Usulan, belum diterapkan:**", item.recommendation, ""]
    if report.uncertainties:
        lines += ["## Ketidakpastian", *[f"- {x}" for x in report.uncertainties], ""]
    return "\n".join(lines)


def traceability(spec: Specification, diagram: Diagram, alignment: Alignment,
                 verified: Verification) -> dict:
    """Bidirectional indices of accepted REALIZATIONS, not mere candidates."""
    accepted = {d.mapping_id for d in verified.decisions if d.status == "accepted"}
    forward = {a.id: set() for a in spec.atoms}
    reverse = {m.id: set() for m in diagram.messages}
    refinements = set()
    for link in alignment.behaviors:
        if link.id not in accepted:
            continue
        if link.relation == "refinement":
            refinements.update(link.message_ids)
        if link.relation == "realizes":
            for atom in link.atom_ids:
                forward[atom].update(link.message_ids)
            for message in link.message_ids:
                reverse[message].update(link.atom_ids)
    return {
        "requirements_to_messages": {k: sorted(v) for k, v in forward.items()},
        "messages_to_requirements": {k: sorted(v) for k, v in reverse.items()},
        "atoms_without_accepted_realization": [k for k, v in forward.items() if not v],
        "messages_without_requirement_realization": [k for k, v in reverse.items() if not v],
        "verified_refinement_message_ids": sorted(refinements),
        "note": "Unmatched does not itself mean violation; inspect scope and rule results.",
    }
