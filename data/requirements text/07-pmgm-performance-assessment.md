# Requirements Breakdown: PMGM Performance Assessment

## Source and scope

- Source: `data/raw/BRD PMGM - Performance Assessment.md`
- Roles: OD Admin, Employee, Direct Supervisor, and One-Up Supervisor.
- Lifecycle: template configuration and launch, self rating, supervisor reviews, external normalisation with system import, finalisation, reporting, and audit.

## Functional Requirements

1. Allow OD to create, edit, duplicate, preview, launch, close, and configure separate Staff and Non-Staff Performance Assessment templates. Configuration includes general settings, rating scale, route map/workflow, period, notifications, participants, language, sections, and fields.
2. Let employees use their category/language-specific form, see route-map stage, rate and comment on goals, upload optional attachments, enter aspiration, save draft, and submit after mandatory validation.
3. Lock employee editing after submission, except when the assessment is sent back.
4. Let Direct Supervisor review self rating, adjust rating, comment, record strengths and improvement areas, and submit to One-Up Supervisor. Let One-Up Supervisor see self and Direct Supervisor assessments, adjust rating/comments, and complete its stage.
5. Support one or two review layers for Non-Staff. Use organisation structure for Staff; OD configures Non-Staff route maps per department at launch.
6. Provide configurable notifications and reminders based on action, outstanding task, due date, recipients, subject, timing, and frequency.
7. Let OD export PA data for selected departments as one XLSX or CSV file per department; create normalisation batches; import/re-import department results with mandatory remarks and optional attachment; retain prior import history; and individually adjust final rating with mandatory remarks.
8. Let OD finalise after department normalisation. The system changes PA to `Completed`, locks final rating, and makes only final rating visible to the employee.
9. Provide PA reporting with filters for period, Staff/Non-Staff, job level, department, employee, and status, with XLSX or CSV export.
10. Support employee transfer/promotion, employee resignation/termination, and supervisor resignation handling, including OD reviewer replacement or bypass when a supervisor resigns before review.

**Behavioral rules, calculations, and preconditions**

- Rating scale is 1 to 6, with a configured name and description. Goal comments are mandatory; attachments optional. Aspiration is employee input, strengths/improvement areas are supervisor input.
- Save Draft does not advance stage. Submission requires every mandatory field. Template cannot be changed after launch.
- Direct Supervisor cannot see One-Up Supervisor scoring; One-Up Supervisor sees employee and Direct Supervisor scores. Rating history is OD-only.
- OD has no approval action in the PA workflow. OD may bulk-move assessments to Normalization and performs normalisation administrative actions only.
- Overall Form Rating is calculated as `sum(section rating x section weight) / sum(section weight)`. Before completion, employee sees a dash rather than the overall rating.
- Normalisation discussion occurs outside the system. The most recently successful import is active; all prior files remain in history and audit log.
- Goal Management activity does not affect PA rating/calculation. Auto-rating for unfinished self-rating, GAP display, signature section, and acknowledge section are out of scope.

**Access and audit behavior**

- OD sees all assessments, statuses, rating/comment histories, and audit trail; may override reviewer mapping with mandatory remarks.
- Employees see their assessment and final rating at the allowed stage, not One-Up Supervisor detail or rating history.
- All rating, comment, approval/send-back, reviewer change, import, re-import, and finalisation events are auditable.

**Additional functional behavior**

- Direct Supervisor and One-Up Supervisor can save draft and send back before submitting their respective review. Summary Section is available according to stage; Direct Supervisor can set a manual section rating, while the Overall Form Rating remains system-calculated.
- A configured administrator path uses one Manager review layer; a Director may be the final reviewer when OD configures it. This supplements—not replaces—the Staff hierarchy and Non-Staff route-map rules.
- A normalisation batch needs only a name and inherits the active PA period; it has no separate open/close period. The source also requires review of import validation results.
- Employee transfer/promotion retains the submitted goal and adds an `Is Transferred` flag; resignation/termination removes the employee from active participants.

**Use-case scenarios**

1. A Staff employee submits a valid self-assessment, triggering Direct Supervisor review and form lock.
2. A Non-Staff participant receives an OD-configured route map with no more than two review layers.
3. OD exports two departments and receives two separate files, then re-imports a corrected result while history remains available.
4. Finalisation locks final rating and exposes it, but not detailed review data, to the employee.
