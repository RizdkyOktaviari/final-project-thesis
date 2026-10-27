# Requirements Breakdown: EC Organization Structure

## Source and scope

- Source: `data/raw/BRD - EC Organization Structure.md`
- Purpose: central organisational-unit management and historical organisation visualisation.
- Roles: Organization Development (create/read/update) and Employee (read-only).

## Functional Requirements

1. Maintain master organisational units and a valid hierarchical Organisation Structure.
2. Display an organisation chart, employee profile detail, and organisation state as of a selected date or period.
3. Export Organisation Structure in PDF and PNG.
4. Search by department name, position name, employee name, or ID NH through integration with related modules.
5. Retain historical records with effective dating and audit trail for structural changes.
6. Act as an organisation reference for Employee Central modules; integrate ESC changes that affect employee placement or visualisation.

**Behavioral rules and access controls**

- Every organisation unit requires a unique identity and must belong to a valid hierarchy.
- OD can access all organisational structures. Other users see only the structure permitted by their access and only in read-only mode.
- Directorate, Division, Department, and Section code standards follow HR Organization Development policy.
- A line-reporting adjustment that does not change Organisation Structure may be performed by OD at any time on a Business Unit request from at least Department Head/Manager level.
- Position management, IPS code management, position hierarchy, recruiting, workforce planning, compensation, authorisation administration, drag-and-drop restructuring, and actual ESC transactions are out of scope.

**Functional process boundary**

The external approval of an organisation-change proposal remains manual. OD reviews proposal, documentation, hierarchy, and business justification before successive review by Training and Development, Senior Manager HCM, GMO/Director in Charge, and Board of Director. The in-system scope begins at updating the approved organisation structure and preserving history.

**Additional functional behavior**

- After manual approval, OD must be able to add/change organisation data directly or import an Organisation Structure CSV/XLSX, with the resulting approved structure becoming the active reference for related modules.
- For annual or quarterly changes below Department level, the manual approval path may end at GMO/Director in Charge; Department-and-above changes must reach the Director. A rejected proposal returns to the Requester and OD for revision.
- Organisation Structure does not itself create or manage a Position, IPS code, position hierarchy, employee personal/employment data, manager assignment, recruiting, workforce planning, payroll/benefit, performance, talent, finance-system integration beyond Cost Center reference, security roles, or drag-and-drop restructuring.

**Use-case scenarios**

1. OD creates or changes an organisation unit only when its parent and hierarchy are valid, then the change is historically traceable.
2. A user opens the organisation chart at a prior effective date and sees the structure valid then.
3. An approved ESC transfer is reflected in the relevant organisation display without enabling ESC creation in this module.
4. An employee can view only authorised organisation information and cannot mutate it.

## Source ambiguities outside the executable requirement set

The BRD has no standalone functional-requirements chapter. The requirements above are distilled from its scope, expected flow, and module-policy sections; detailed create/update field definitions and validation messages are not specified.
