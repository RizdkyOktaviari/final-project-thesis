# Requirements Breakdown: EC Position Management

## Source and scope

- Source: `data/raw/BRD - EC Position Management.md`
- Purpose: manage the position lifecycle, position hierarchy, organisational-unit attributes, history, charting, migration, import/export, and shared reference data.
- Roles: OD Admin has position lifecycle and chart/import/export permissions; Comben manages cost code; employees view their own position-chart data.

## Functional Requirements

1. Create, read, update, activate, and deactivate positions, with general creation and `Add Position Below` creation from a selected Position Chart node.
2. Maintain Position Code, Position Title, organisational-unit association, Higher-Level Position, and subordinate relationships.
3. Display Position Chart and support search by Position Code, Position Title, incumbent employee name, and employee ID.
4. Apply effective dating to changes and retain historical organisation/position views for a chosen effective date.
5. Manage Company, Directorate, Division, Department, Section, and cost code/cost centre data within the allocated role boundaries.
6. Bulk import SAP SuccessFactors position data, export Position Chart as PDF and PNG, and expose positions as a single reference source for related EC modules.
7. Record all changes in audit trail, including actor, time, and changed data.

**Behavioral rules and preconditions**

- Position Code is unique. Position Title must fit the active organisation structure and business need.
- Only OD manages position lifecycle and hierarchy. General users have authorised read-only views.
- Each position has at most one active Higher-Level Position for the same effective period. The hierarchy must be valid and must not be circular.
- `Create Position` requires manual completion of the data. `Add Position Below` inherits/auto-fills hierarchy from the selected parent chart node.
- Changes preserve prior data through effective dating. A position with employee, organisational, or transaction history cannot be deleted.
- Deactivation is permitted only when there is no active incumbent, active candidate, or active subordinate position.
- Reporting-line changes update both Position Chart and Organisation Chart according to effective date.
- Position must reference valid Directorate, Division, Department, and Section data.

**Additional functional behavior**

- Creation and edit validation must cover mandatory data, data format, Position Code uniqueness, organisational consistency, valid higher-level relationship, and the applicable Position Management business rules before storage.
- An edit may cover Position Title, Job Code, Cost Center, Location, Position Level, or Reporting Line within the user's authority. A successful edit updates related position and organisation structure information and writes effective-dated audit history.
- `Add Position Below` must at least auto-fill Higher-Level Position, Division, and Department from the selected chart node before the user completes the new position data.
- OD Admin may import/export position data and charts; Comben manages Cost Code/Cost Center; employees have authorised read-only Position Chart access. Source migration is SAP SuccessFactors position data.

**Scope exclusions**

Job Code Framework auto-generation, recruitment, RTE, ESC transactions, personal/employment data, manning budget, payroll/compensation, approval-workflow management, contract processes, talent pools, and drag-and-drop reporting-line changes are not included.

**Use-case scenarios**

1. OD creates a general position with a unique code and valid organisational references.
2. OD adds a subordinate position from the chart and receives the expected inherited hierarchy.
3. A position with active incumbent or subordinate cannot be deactivated; a historical position cannot be deleted.
4. A selected historical date displays the correct chart and prior position state.

## Source ambiguities outside the executable requirement set

The BRD does not contain a dedicated detailed functional-requirements chapter or position field catalogue. The breakdown is based on in-scope items, expected process flows, roles, and policy rules.
