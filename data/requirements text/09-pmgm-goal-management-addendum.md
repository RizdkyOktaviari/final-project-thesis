# Requirements Breakdown: PMGM Goal Management Addendum

## Source and scope

- Source: `data/raw/BRD20Goal20-%20Adendum.md`
- This is an addendum to Goal Management. It contains three active business rules and should be read together with `08-pmgm-goal-management.md`.

## Functional Requirements

1. A manager may cascade KPI to a subordinate only after submitting the manager's own KPI.
2. For Non-Staff, only a Supervisor may cascade KPI to employees.
3. Staff and Non-Staff employees may create and save KPI drafts even before receiving a manager cascade.

**Behavioral specification implication**

Separate draft capability from submit capability. Draft creation must not require cascade. Submission must still apply the confirmed cascade and total-weight validations from the main Goal Management BRD.

## Source ambiguities outside the executable requirement set

The addendum reaffirms the main BRD's cascade order and draft rule. It does not resolve the 40% versus 50% minimum cascade-weight conflict in the main BRD.
