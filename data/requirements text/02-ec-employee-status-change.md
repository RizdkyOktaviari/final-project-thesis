# Requirements Breakdown: EC Employee Status Change

## Source and scope

- Source: `data/raw/BRD - EC Employee Status Change.md`
- Supported change types: re-classification, transfer, working-hours or work-schedule change, contract renewal, promotion, and demotion.
- Main roles: Requestor, Organization Development, HR Admin, approvers, delegate approvers, and the affected employee.

## Functional Requirements

1. Enable a requestor to create one Employee Status Change (ESC) request per employee at a time, complete mandatory fields and evidence, submit, revise after send back, or withdraw before approval completes.
2. Use one role-aware ESC form. Requestor edits employee status, position title, department, report-to, and work schedule or hours. OD reviews position title, report-to, Position Description, and CAM. HR Admin reviews all data, may set Annual Bonus and Vehicle Allowance, and may override the next approver.
3. Present old employee status from current data and collect new employment status, position, department, report-to, pay grade, wage classification, work schedule, work hours, effective date, HR-only salary data, percentage increase, and reference number.
4. Require Position Description in PDF for every ESC. Require CAM in PDF for Non-Staff, but not Staff.
5. Support sequential approval, approve with optional comment, send back with mandatory comment, resubmission, delegate approval, and HR Admin override of the next approver. Record every workflow or data change in the activity log.
6. Generate a digitally signed Individual ESC Report in PDF, an XLSX monitoring report by selected period, and an HR Admin memorandum in PDF and DOC after the relevant approval state.
7. Provide status monitoring, pending-approver visibility, history, activity log, and search/filter by employee, organisation, ESC type/status, request date, and effective date.
8. Notify the next approver on submit or approval, requestor and prior approvers on send back, HR Admin on withdraw, and requestor, employee, and HR Admin after final completion. Send reminder email and in-app notification every two days until action, with the interval described as configurable.
9. After final approval and the effective date, update the relevant organisation, position, job, reporting-line, payroll and compensation, time management, and PMGM data.

**Behavioral rules and preconditions**

- One `In Progress` ESC per employee blocks a new ESC until the preceding request is approved or withdrawn.
- All ESC fields are mandatory except CAM, which is mandatory only for Non-Staff. Annual Bonus and Vehicle Allowance are HR Admin-only and visible only for Senior Manager and above.
- Send back requires a comment; approve does not. Only the requestor can revise a sent-back request.
- Delegate access applies only to the approver's own approval task. HR Admin may change the next approver while approval is running.
- Promotion and transfer require OD review before the main approval workflow. Other ESC types proceed directly through their configured workflow.
- Changes apply only after final approval and the effective date. The source permits backdate and future date according to company policy, but gives no detailed boundary rule.
- The affected employee can see only their latest ESC. An ESC submitted by a Department Head cannot be accessed by that employee.
- Demotion can be voluntary or involuntary and may be discipline, ethics, or performance based. It may change grade, job responsibilities, and compensation/benefits.

**Access, audit, and confidentiality behavior**

- Individual ESC reports are accessible only to HR Admin and the affected employee.
- Digital signatures used in generated documents must be stored encrypted.
- Approval history and comments cannot be deleted. The audit log covers submit, approval, send back, withdrawal, approver override, data changes, and comments.

**Additional functional behavior**

- The common ESC form also requires reason, Position Description, justification, and, when applicable, CAM. It displays employee name, ID, and date of hire as source data; old status is read from current data rather than edited in place.
- The requested new-status fields are employment status, position title, department, report-to, pay grade, wage classification, work schedule, work hours, effective date, Base Salary, Percentage Increase, and Reference Number. Base Salary, Percentage Increase, and Reference Number are HR-only; Annual Bonus and Vehicle Allowance are HR-only and appear only for Senior Manager and above.
- Only HR Admin and the affected employee may access the individual report. Department Heads may view full subordinate ESC history; the employee sees only the latest own ESC summary and report, subject to the stated Department-Head exception.
- A delegate must be an active user; only one active delegate may exist for an approval task; delegation neither changes the approval sequence nor removes attribution to the original approver. Delegate decisions must record both the delegate and the delegated approver.
- Migrate ESC history from 2021 through the latest source data. ESC supplies approved changes to organisation, job/position, reporting line, payroll/compensation, roster/shift/time management, and PMGM transfer/promotion flags; it does not own termination, payroll calculation, recruitment, performance evaluation, organisation/position creation, or self-service outside ESC.
- Base salary, annual bonus, vehicle allowance, percentage increase, approval information, supporting documents, and digital signatures require role-scoped confidential handling. Digital signatures remain encrypted at rest.

**Use-case scenarios**

1. A promotion request cannot skip OD review and cannot submit without Position Description.
2. A Non-Staff request without CAM is rejected; a Staff request does not require CAM.
3. An approver sends back with a comment, the requestor revises, and the request returns to the configured first/next approver.
4. A request is approved before its effective date and changes master data only when the effective date is reached.
5. HR Admin overrides the next approver and the activity is auditable.

## Source ambiguities outside the executable requirement set

- Define the full configured workflow per ESC type and escalation ownership.
- Clarify how `Withdraw` differs from `Withdrawn` and which unfinished statuses permit it.
- Define approval-report access for delegates and override actors.
- Reconcile the withdrawal conflict: the functional section permits withdrawal while approval is unfinished, while the validation table limits it to the requester stage.
