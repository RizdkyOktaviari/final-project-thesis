# BRD-to-Functional-and-Behavioral-Requirements Coverage Audit

## Purpose and method

This audit tests whether each supplied BRD has a corresponding, substantive
functional and behavioral requirements breakdown. It treats the following as
**requirements evidence**: scope, roles/access, business rules, functional
requirements, validation, security, audit, integration, migration, reporting,
and notification triggers.
It does not copy document-control metadata, source-image pixels, signatures,
literal email prose, sample error-message prose, or current-state narrative
word-for-word; those remain preserved and citable in `data/raw/`.

## Result

| ID | BRD | Requirement breakdown | Coverage after this audit | Material source areas represented |
| --- | --- | --- | --- | --- |
| 01 | EC Benefit Reimbursement | `01-ec-benefit-reimbursement.md` | Complete | Scope/exclusions, form, eligibility/calculation, approval, period/cut-off, notifications, history/export, access, audit, migration, integration |
| 02 | EC Employee Status Change | `02-ec-employee-status-change.md` | Complete, with source conflicts retained | Scope/exclusions, role form, workflow/delegation, attachments, reports, monitoring, validation, security, migration, integration |
| 03 | EC Foundation | `03-ec-foundation.md` | Complete | Multi-company, proxy lifecycle/notifications, workflow, RBAC, encryption, audit, integration, migration, dependencies |
| 04 | EC Manage Hiring | `04-ec-manage-hiring.md` | Complete | RTE, SBU, new hire, probation, workflow, notification triggers, validation, security, audit, migration, dependencies |
| 05 | EC Organization Structure | `05-ec-organization-structure.md` | Complete | Scope/exclusions, manual approval boundary, internal update/import, policy, role access, effective dating, ESC dependency |
| 06 | EC Position Management | `06-ec-position-management.md` | Complete | Scope/exclusions, create/add-below/edit flows, hierarchy/effective dating, role access, import/export, audit, policy |
| 07 | PMGM Performance Assessment | `07-pmgm-performance-assessment.md` | Complete | Template/launch, assessment workflow, normalisation, finalisation/reporting, reassignment, calculation, visibility, audit |
| 08 | PMGM Goal Management | `08-pmgm-goal-management.md` | Complete, with source conflict retained | Period/template, KPI validation, cascade, workflow, notification, visibility, export, Mid-Year revision, audit, exclusions |
| 09 | PMGM Goal Management Addendum | `09-pmgm-goal-management-addendum.md` | Complete | Three addendum business rules and their relationship to the main Goal Management BRD |
| 10 | EC Personal Data | `10-ec-personal-data.md` | Complete, with source conflict retained | Request/review lifecycle, section and field constraints, evidence, history, security, audit, migration, integration, exclusions |

## Explicitly retained source conflicts and gaps

- Benefit Reimbursement: attachment format, withdrawal state, and active-duplicate/contract-employee interpretation.
- Employee Status Change: withdrawal eligibility is inconsistent between the functional and validation sections; the exact configured workflow is not specified.
- Goal Management: the cascade-weight default is 40% in a diagram and 50% in the text.
- Personal Data: the requestable-section list conflicts with the detailed field catalogue's read-only entries; allowed attachment formats/size and payment-change subtype remain unspecified.

These are captured as source gaps in the respective breakdowns, not resolved by this audit.
