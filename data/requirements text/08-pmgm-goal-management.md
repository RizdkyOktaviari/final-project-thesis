# Requirements Breakdown: PMGM Goal Management

## Source and scope

- Source: `data/raw/BRD_PMGM_Goal_Management.md`
- Roles: OD Section, employee, Direct Supervisor, upper managers/One-Up Supervisor, and Department Head/leadership for reminder escalation.

## Functional Requirements

1. Let OD create KPI periods with start and due dates, choose exempt employees, open/reopen the period, and configure notifications.
2. Provide two automatically selected KPI forms, one for Staff and one for Non-Staff. While the period is open, employees create, edit, delete, save, and submit their KPIs; after closure they may only create or amend linked activities.
3. Validate a maximum of 10 KPI items, 100% total weight, Staff per-item weights of 5-25%, Non-Staff per-item weights of 5-30%, and Learning & Growth total no greater than 15%.
4. Support KPI cascade by eligible managers to direct subordinates. Validate required cascade weight before submit, then send submitted KPI to Direct Supervisor review.
5. Let Direct Supervisor approve or request revision with mandatory notes. Let OD perform final approval or revision. A revision returns the KPI to the employee, then through Direct Supervisor again before OD.
6. Lock completed KPI even if the period remains open. Provide appropriate in-app and email notifications, reminder escalation, and configurable format/duration/recipients/content.
7. Enforce visibility: employees manage their own KPIs; supervisors/managers see authorised subordinate KPIs based on organisation hierarchy; OD sees all employees, statuses, review history, and revision history.
8. Store KPI changes, approval, revisions, and review notes in audit trail. Export own/subordinate KPI in PDF and department KPI data in Excel for OD.
9. Support Mid-Year revision, including OD status override and reopening. For a position/department change during a KPI period, reset the KPI to draft so it can be reauthored for the new role.
10. Allow OD to configure KPI business rules, participant inclusion/exclusion, notification settings, and whether a cascaded KPI is mandatory. A mandatory cascaded KPI cannot be edited or deleted by the subordinate.

**Behavioral rules and preconditions**

- Staff use Finance, Stakeholder, Internal Process, and Learning & Growth perspectives. Not all perspectives must be used if they do not fit the work.
- The lowest role permitted to cascade is Supervisor. Staff Direct Supervisor cannot skip levels in cascade; non-staff cascade is performed by Supervisor.
- A manager must complete and submit their own KPI before cascading to subordinates. Employees may create and save draft without receiving cascade, but cannot submit before required cascade validation passes.
- The document says the default minimum received cascade weight is 50% and configurable by OD. Its embedded diagram states 40%. This is a source conflict; do not select either value without a business decision.
- When a manager's position changes, OD adjusts the workflow so the role can continue review and authorised KPI changes.
- Employees excluded by OD do not receive KPI-period notifications and need not submit KPI.
- Goal Management excludes automatic forwarding to OD at the due date, a drag-and-drop Activity/Kanban board, in-system KPI creation for Board members, and a launch/open/close approval request.

**Notification behavior**

- Submission sends in-app notification to requestor and Direct Supervisor and email to Direct Supervisor.
- Approval sends in-app notification to requestor and approver and email to requestor.
- Revision/send-back sends in-app notification to requestor and approver and email to requestor.
- Default reminder stages are three weeks to Department Head, two weeks to Senior Manager/Director, and one week to GMO/Director, subject to OD configuration.

**Use-case scenarios**

1. A Staff employee with 11 KPIs, incorrect total weight, invalid individual weight, or excessive Learning & Growth weight cannot save or submit.
2. An employee can save draft without cascade but cannot submit until the confirmed cascade-weight threshold is met.
3. Supervisor revision with notes produces `Revise Required`, permits correction, and returns to the correct review path.
4. A completed KPI cannot be edited; a Mid-Year period enables the documented revision process.

## Source ambiguities outside the executable requirement set

Confirm whether the production default minimum cascade weight is 40% or 50%, and whether it is configurable per period, form, or organisation.
