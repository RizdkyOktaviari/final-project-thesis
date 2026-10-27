# Requirements Breakdown: EC Benefit Reimbursement

## Source and scope

- Source: `data/raw/BRD - EC Benefit Reimbursement.md`
- Focus: Benefit Assistance, specifically Education Assistance.
- Primary roles: Employee, HR Compensation & Benefit, and Super Admin for permitted backdate submission or approved-claim cancellation.

## Functional Requirements

1. Provide an employee Benefit Assistance submission form with claim date, benefit selection, currency, and system-calculated entitlement amount.
2. Provide Education Assistance detail rows for eligible dependents. The employee may add up to three dependents and complete student identity, school, grade, education year, and supporting information.
3. Source eligible dependent data, date of hire, and related validation data from Employee Central. Auto-fill available dependent data after selection.
4. Calculate entitlement by benefit category, school level, eligible dependent count, applicable ceiling, and prorata rule for new or contract employees. The calculated amount is not editable by the employee.
5. Validate eligibility, dependent age, dependent-to-claim relationship, claim frequency, duplicate claims, submission period, and remaining ceiling before submission.
6. Support Super Admin submission on behalf of an employee with a distinct submitted date for authorised backdate cases. Retain both the creator and request owner for audit.
7. Accept required supporting documents only in PDF or JPG format and retain them with the claim. Provide a downloadable Education Assistance form for HR Compensation & Benefit.
8. Route submitted claims to HR Compensation & Benefit for review. Reviewers can approve or send back; send back requires a comment and enables employee correction and resubmission.
9. Allow Super Admin to cancel an approved claim and record the cancellation actor and status.
10. Provide employee and HR claim history, current status, status dates, activity actors, reporting export in Excel, and an approved-claim dataset for payment administration.
11. Notify HR on submission; notify the employee on approve, send back, or cancellation; notify the reviewer for pending approval reminders.

**Behavioral rules and preconditions**

- Only the employee may submit normally. Super Admin is an exception for authorised backdate processing.
- A benefit type must be eligible for the employee and have complete required information before it can proceed.
- Education Assistance only uses Employee Central dependents, permits at most three dependents, and excludes dependents older than 23 years.
- The same dependent cannot be claimed by more than one employee in the same period. A permanent employee cannot make a duplicate claim for the same dependent and period; contract employees may claim again only while ceiling remains.
- Frequency limits are one PAUD claim and two TK claims per dependent. SD through university may be claimed while entitlement remains.
- The benefit period runs from 1 July through 15 June of the following year. Normal employee submission is rejected from 16 through 30 June. The system warns at or after cut-off; the source names 15 June as the annual academic-year lock date.
- Required documents block processing when missing. The BRD refers to PDF or JPG generally, while the Education Claim Form table specifically notes PDF for its attachment field.
- A request in progress for the same employee and dependent blocks a new equivalent request, except the document also describes contract employees with remaining ceiling. Implementation needs a precise status and eligibility rule to reconcile these statements.
- Withdraw changes the request to `Withdrawn`, notifies HR Compensation & Benefit, and records the action. One earlier rule limits withdraw to `Sent Back`, while the exception section describes withdrawal more generally; this needs confirmation before implementation.

**Functional interactions, access, and integration**

- Employee Central is the source for employee, dependent, and date-of-hire information used in eligibility and prorata calculations.
- Approved claims become input for HR Compensation & Benefit payment administration. The BRD does not require direct payroll payment execution.
- Employee sees own claims; HR Compensation & Benefit sees claims within its authority; Super Admin has only the stated exceptional capabilities.
- History must record request status, dates, actors, and change activity. Submission data must align with attached evidence and be verified by HR.

**Additional functional behavior**

- Limit each supporting document to 10 MB. The source accepts PDF or JPG at the general upload rule, but the Education Claim Form specifically labels its mandatory attachment as PDF; retain this as an unresolved format conflict.
- Preserve the field behaviour of the Education Claim Form: Currency, entitlement, selected dependent data, student name, age, date of birth, gender, and education year are system-derived/read-only where indicated; the employee supplies the student identity number, school, optional grade, school name/address, attachment, and optional remarks.
- Retain the rule that benefit already received is not returned merely because the employee later resigns.
- Preserve the future policy configuration requirement for Education Assistance category by job level, while leaving benefit-policy maintenance itself outside this module.
- Migrate Benefit Reimbursement history from 2021 through the latest available source data. Do not include Condolence Assistance, employee/dependent maintenance, policy maintenance, direct payroll payment, or offline post-cut-off processing in this module.
- Send-back and cancellation notifications include the reviewer comment. The pending-approval reminder is sent to HR Compensation & Benefit.
- The audit trail must record at least submit, edit, approve, send back, resubmit, and withdraw with user, role, activity time, and request ID.

**Use-case scenarios**

1. An eligible employee submits Education Assistance for an eligible dependent with mandatory evidence and receives a status trail.
2. A dependent over 23, an over-limit PAUD/TK claim, a duplicate permanent-employee claim, or a submission in the 16-30 June closed window is rejected before submission.
3. HR sends back with a required comment; the employee corrects and resubmits.
4. A contract employee with available ceiling follows the intended repeat-claim rule once the ambiguity above is resolved.
5. Super Admin backdates a claim and the audit trail distinguishes the admin creator from the employee owner.

## Source ambiguities outside the executable requirement set

- Confirm the complete allowed attachment formats for the Education Claim Form.
- Confirm whether withdrawal is valid only after `Sent Back` or at all unfinished stages.
- Define the exact statuses that constitute an active duplicate claim and the contract-employee exception.
