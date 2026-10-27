# Requirements Breakdown: EC Foundation

## Source and scope

- Source: `data/raw/BRD - EC Foundation.md`
- Foundation is a shared-services module. It does not directly manage Human Capital transactions; consuming BRDs specify their own fields and process details.

## Functional Requirements

1. Support multiple companies in one platform. HR administrators create, update, activate, and deactivate companies without deleting history, assign users to one or more companies, and expose company configuration to EC modules.
2. Provide Proxy Access. A requestor selects a target user, validity in days, and reason; reviews request details; and submits into `Pending Approval`.
3. Notify the target user and allow approve or reject. Activate an approved proxy only when its effective period starts.
4. List active proxies, including requestor, target user, start date, and end date. Allow the requestor to switch user only while the proxy is active.
5. Allow the requestor to return access and the target user to revoke access. Automatically expire access when validity ends and prevent further switching.
6. Distinguish activities executed through proxy from direct activities, preserving requestor and target-user identities in audit data.
7. Provide reusable, configurable approval workflows with one or more sequential levels, approver types based on specific user, position, line manager, manager level, role, and optionally organisational unit. Support submit, approve, delegate, send back, and withdraw.
8. Provide shared RBAC, authentication, audit trail, integration support, and migration import/validation/reconciliation logs for EC modules.

**Behavioral rules and access controls**

- Proxy requires target user, reason, day-based validity, eligible user status, and target-user approval.
- Proxy activity has the target user's authorised data scope only. It does not grant the requestor additional permissions.
- A rejected, returned, revoked, or expired proxy cannot be used for switch user.
- Delegated workflow activity must identify the delegate in audit logs. Workflow configurations are reusable across modules.
- Access is constrained by role, authority, company, and organisational scope. Sensitive personal data requires application-layer encryption before database persistence.
- Audit trails for master data include actor, timestamp, action, and before/after values, and are immutable to application users.
- Integration failures must be logged. SAP SuccessFactors migration data must be validated and reconciled before go-live, while PTAR is responsible for providing the exported source data.

**Sensitive-data protection behavior**

The BRD marks national identity, financial, health, biometric, genetic, legal, child, and location-history information as requiring encryption. Field-level processing, masking, search, migration, and integration rules remain the responsibility of each consuming module BRD.

**Additional functional behavior**

- Workflow configurations must be creatable, editable, activatable, and deactivatable by an administrator. Delegation is time-bounded and available only to active users with the required authority.
- Proxy notifications are required for request submission (Target User), approval and rejection (Requestor), activation (Requestor and Target User), early return (Target User), revocation (Requestor), and expiry (both parties).
- Audit trails must cover Create, Update, and Delete with user, time, activity, and before/after values when applicable; application users cannot alter the trail.
- Migration support includes import, pre-import validation, validation/reconciliation output, and migration logs. SAP SuccessFactors is the identified source system and PTAR supplies the exported data.
- Foundation is responsible for shared company, workflow, proxy, security, audit, integration, migration, and data-protection capabilities. Consuming modules remain responsible for their own business fields and transactions.

**Use-case scenarios**

1. A target user approves a valid proxy, the requestor switches user during the approved period, and the log retains both identities.
2. Return, revoke, and automatic expiry immediately prevent switch user and create audit records.
3. A configured multi-level workflow routes sequentially, delegates only to an eligible active user, and logs the delegation actor.
4. A company is deactivated without loss of prior records and cannot be used as an active operating scope.

**Cross-module interaction boundary**

Foundation capabilities are consumed by Organization Structure, Position Management, Hiring, ESC, Benefit, Termination, and all other EC modules for security, audit, integration, and proxy behaviour.
