# Requirements Breakdown: EC Manage Hiring

## Source and scope

- Source: `data/raw/BRD - EC Manage Hiring.md`
- Processes: Request to Employ (RTE), Salary Build Up (SBU), input of new employee data, and probation evaluation.
- Roles: Department Head User, OD TM/OD Section, HR Recruitment, approval chain, LM Requester, Senior Manager HCM, HR-CompBen, IT & System, and Finance.

## Functional Requirements

### Request to Employ

1. Let Department Head User submit RTE and Position Description documents in PDF after checking approved manning budget.
2. Route RTE through OD TM/OD Section budget validation, HR Recruitment review, and the stated sequential approval chain: Senior Manager HCM, Senior Manager Business Unit, GMO/GM PD/Chief Geo, Director in Charge, and Director of HC.
3. Provide approver views and approve/send-back actions. A returned request supports submit again or withdraw.
4. Support HR Recruitment position search and selection. If no position is available, let OD review a new-position request against manning budget and return the decision to HR Recruitment.

### Salary Build Up

1. Let HR Recruitment create an SBU proposal with hiring demographic information, staff/non-staff gender, staff religion/manpower, grade, multiple internal comparisons, tabular previous employment, previous salary/components, manual salary components, and PTAR Offer employment status/work roster selections.
2. Route SBU through Senior Manager HCM, Director of HC, Senior Manager Business Unit, GMO/GM PD/Chief Geo, and Director in Charge. Each stage approves or sends back; HR Recruitment can resubmit or withdraw.
3. Make Offering Letter generation available to HR Recruitment only after required SBU approvals finish.

### New employee data

1. Enable HR Recruitment to create new employee data after a valid position is selected or created.
2. Capture employment status, organisation data, personal/family/address/education/telephone/national-ID data, HRIS user ID, and email.
3. Support downstream responsibility: HR-CompBen input of compensation and benefits, IT & System activation in Mata Air, and Finance payroll-data input.

### Probation evaluation

1. Trigger reminders 30 and 14 days before probation end.
2. Let Department Head User complete and submit the evaluation; HR Recruitment reviews and configures reviewers; LM Requester and Senior Manager HCM provide review and feedback.
3. Allow approve, send back, correction, resubmission, compilation of feedback, and notification-letter generation by HR Recruitment. The BRD assigns the final distribution responsibility to Department Head User.

**Shared behavioral rules and preconditions**

- RTE must include RTE form and Position Description and depends on approved manning budget.
- SBU cannot advance until the current approver approves. Send back returns the proposal for submit or withdraw.
- New employee data must use an available position or one created through approved manning-budget review.
- Required attachments for RTE and new-hire data are validated; the BRD allows PDF or JPG generally, while RTE and PD are specifically described as PDF.
- Withdrawal sets `Withdrawn`, informs HR Recruitment, and logs the action.
- Notification recipients, triggers, and message details beyond the stated probation reminders are explicitly marked as needing confirmation in the source.

**Cross-module interactions and dependencies**

- Position Management and Organisation Structure supply available-position and organisational data.
- Compensation/benefits, IT activation, and Finance payroll processing are downstream responsibilities, not fully defined integration contracts in this BRD.

**Access, audit, and additional functional behavior**

- The new-hire sequence continues after HR Recruitment entry: HR Compensation & Benefit enters compensation/benefits; IT & System creates the HRIS account/email and activates the employee in Mata Air; Finance enters payroll data; the current process also records face and fingerprint enrolment.
- RTE and SBU notifications are concrete source requirements: submission notifies OD TM/OD Section or Senior Manager HCM; send back notifies the requestor; a prior approval notifies the next approver. Probation reminders at 30 and 14 days go to HR Recruitment; probation submission and final review completion also notify HR Recruitment.
- Sensitive data includes personal and employment information, RTE/PD, SBU salary/proposal information, manning budget, probation evaluations/feedback, and approval comments. Apply RBAC; unauthorised users cannot view, download, or alter the related data or documents.
- Audit submit, approve, send back, resubmit, data changes, workflow actions, new-employee data entry, and position creation, with user ID, role, activity, time, request/reference ID, and relevant changed data. The operational audit trail is read-only.
- Preserve the 2021-to-latest historical-data migration requirement. Recruitment sourcing, organisation maintenance, manning-budget maintenance, payroll payment, employment agreements, and the employment decision/policy remain outside this module.

**Use-case scenarios**

1. An RTE with no approved manning budget cannot advance until the budget path is resolved.
2. An SBU sent back at any approval level can be corrected and resubmitted, then yields an Offering Letter only after final approval.
3. HR Recruitment cannot create a new employee against an unavailable position without OD approval to create one.
4. Probation reminders occur at both stated intervals and the completed review reaches the notification-letter step.

## Source ambiguities outside the executable requirement set

- Define the complete RTE/SBU field catalogue and exact workflow configuration.
- The source specifies notification recipients and triggers, but does not specify transport, template governance, delivery failure behaviour, or an unambiguous final owner for distributing the probation letter.
- The source includes an unrelated section named `Benefits Submission Field Details`; it should not be treated as Manage Hiring scope without business confirmation.
