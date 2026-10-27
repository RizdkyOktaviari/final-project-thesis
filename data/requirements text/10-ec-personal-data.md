# Requirements Breakdown: EC Personal Data

## Source and scope

- Source: `data/raw/BRD - EC Personal Data.md`
- Roles: Employee/Requestor and HR Compensation & Benefit.
- Model: requested personal-data changes follow a request, review, approval, history, and integration lifecycle rather than direct employee mutation.

## Functional Requirements

1. Enable employees to request updates across the listed Personal Data sections, including personal/biographical data, address, contact, National ID, emergency contact, dependents, payment, position/organisation, job/employment/time data, documents, compensation, education, career background, and memberships/volunteering.
2. Use a section-specific Personal Data form, validate mandatory fields and supporting evidence, and allow only one `In Progress` request for the same Personal Data section and employee.
3. Let HR Compensation & Benefit review all requested changes and evidence, approve with optional comment, or send back with mandatory comment. Employees may edit sent-back requests, resubmit, or withdraw a sent-back request.
4. On approval, apply the change, complete workflow, record change history, and trigger downstream update only after final approval.
5. Support attachments tied to the request and subject to company policy, with examples such as marriage-book/family-card evidence for marital-status change and family-card evidence for child-data change.
6. Provide request status, employee history, HR history, and activity log covering submit, approve, edit, send back, resubmit, withdraw, data change, and review comments.
7. Send HR submission, resubmission, withdrawal, and reminder notifications; send employees send-back and completed notifications.

**Functional input, output, and field constraints**

- Personal Information has effective date, names, auto-filled full name, salutation, religion, gender, marital status, nationality/locale, and optional family-card evidence.
- Address is home address with geographic values, postal code, and primary flag. Contact supports personal/work phone and email types.
- National ID supports KTP and Passport, country, ID number, attachment, and primary flag.
- Emergency Contacts allow multiple entries up to two. Dependents require effective date, name, relationship, date of birth, and may have attachments; only HR can set dependent eligibility during review.
- Payment Information contains effective start/end dates and Payroll/Insurance bank/account information. The BRD says bank-account change may be submitted only once per year.
- Job, organisation, time, and job-relationship information are listed as non-editable in the field catalogue despite appearing in the wider requestable-section list. Treat the field-level editability table as the more specific rule unless business confirms otherwise.

**Additional functional behavior**

- National ID is repeatable; KTP is mandatory, and Passport is also supported. A record includes country, ID number, optional attachment, and primary flag. The source notes that an expatriate may enter a passport number in the KTP section, which requires a business decision before implementation.
- Dependents are limited to three, while Emergency Contacts are limited to two. Dependents support person relationship, personal/biographical, National ID, address, and multiple attachments; a dependent's eligibility remains HR-only. A dependent attachment is not the same as an employee attachment.
- Payment Information permits more than one account. Insurance defaults to the Payroll account; its field set includes insurance type/classification in addition to bank/payment data. The effective end date is system-disabled.
- Editable employee-maintained field groups include personal/biographical data, home address, phone, National ID, emergency contact, dependent, personal document, and the specified compensation amount. Contact email, position, organisation, job details, time information, job relationships, and Pay Targets are marked read-only in the detailed catalogue.
- Personal-document fields include country/region, type, title, number, issue date/place/authority, expiry date, and attachment. Education, honours/awards, internal work experience, previous employment, courses, certifications, professional memberships, and volunteer involvement are source-listed request sections; their detailed field catalogues are retained in the BRD.

**Behavioral rules and preconditions**

- Mandatory fields must be complete before submit. File size cannot exceed the configured limit.
- Send back requires a comment. Withdraw is permitted only for `Sent Back`; a withdrawn request cannot be processed again.
- A bank-account change may be submitted once per year.
- HR can mark a dependent `Eligible` or `Not Eligible` during review/approval.
- A request only updates official data after approval and the stated Effective Date. HR administrators with authority may also submit permitted changes; this does not override the employee-owned request rule for normal self-service.
- After approval, integration can update Organisation Structure, Position Management, Payroll & Compensation, and Benefit Reimbursement, depending on the change type.

**Access, audit, and confidentiality behavior**

- National ID, date of birth, address, personal contact, emergency contact, payment, dependent, grading, and basic salary are confidential. Apply RBAC and deny unauthorised reading or change.
- Employee sees only own personal data, requests, and history. HR Compensation & Benefit sees the requests/evidence within its responsibility.
- Supporting documents remain confidential and request-bound. Employees cannot change or delete stored evidence after the request enters approval except through the supplied change mechanism.
- Audit trail is read-only and includes user, role, activity, time, and request ID. Change history includes section, changed field, prior value, new value, actor, time, and request ID.
- Personal Data history migration covers 2021 through the latest available records. Employee termination, payroll execution, recruitment, performance evaluation, organisation/position management, and ESC are outside this module even where approved data is consumed by them.

**Use-case scenarios**

1. An employee submits a valid address change. A second in-progress address request is blocked, while a different eligible section may be requested.
2. HR sends back without comment and is blocked; after comment, the employee corrects and resubmits.
3. A sent-back request can be withdrawn and becomes non-processable.
4. An unauthorised user cannot view National ID, payment data, or the attached evidence.
5. An approved relevant change updates the appropriate downstream module only after workflow completion.

## Source ambiguities outside the executable requirement set

- Confirm which listed sections employees may genuinely edit where the detailed field table marks the fields read-only.
- Confirm allowed file formats and configured size limits.
- Confirm whether the one-per-year payment rule applies to all account changes or a specified payment subtype.
