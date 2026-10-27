# Requirements Corpus

This directory contains the requirements corpus used as evidence for the
thesis. The corpus is deliberately split into source material and derived
analysis so that a result can be traced back to the BRD that supplied it.

## Directory roles

| Path | Role | Editing rule |
| --- | --- | --- |
| `raw/` | Source BRDs converted to Markdown and the visual assets referenced by them. | Preserve source wording and structure; only repair broken local asset links or add a source-asset reference. |
| `requirements text/` | Ten derived, normalised module breakdowns plus a corpus coverage audit used for analysis. | Record interpretations, explicit business rules, acceptance scenarios, and unresolved source conflicts. |

## Traceability manifest

| ID | Derived requirements file | Source BRD | Referenced visual assets |
| --- | --- | --- | --- |
| 01 | `requirements text/01-ec-benefit-reimbursement.md` | `raw/BRD - EC Benefit Reimbursement.md` | 10 |
| 02 | `requirements text/02-ec-employee-status-change.md` | `raw/BRD - EC Employee Status Change.md` | 18 |
| 03 | `requirements text/03-ec-foundation.md` | `raw/BRD - EC Foundation.md` | 3 |
| 04 | `requirements text/04-ec-manage-hiring.md` | `raw/BRD - EC Manage Hiring.md` | 8 |
| 05 | `requirements text/05-ec-organization-structure.md` | `raw/BRD - EC Organization Structure.md` | 3 |
| 06 | `requirements text/06-ec-position-management.md` | `raw/BRD - EC Position Management.md` | 5 |
| 07 | `requirements text/07-pmgm-performance-assessment.md` | `raw/BRD PMGM - Performance Assessment.md` | 3 |
| 08 | `requirements text/08-pmgm-goal-management.md` | `raw/BRD_PMGM_Goal_Management.md` | 1 |
| 09 | `requirements text/09-pmgm-goal-management-addendum.md` | `raw/BRD20Goal20-%20Adendum.md` | 0 |
| 10 | `requirements text/10-ec-personal-data.md` | `raw/BRD - EC Personal Data.md` | 14 |

The count is the number of Markdown image occurrences, not necessarily the
number of distinct files; a source image may be deliberately shown more than
once in a BRD. The corpus currently contains 10 source BRDs, 10 derived module
requirement breakdowns, one coverage audit, and 63 distinct local image assets.
All source-image references resolve locally.

## Interpretation boundary

The files in `requirements text/` are not replacements for the BRDs. They are
analysis artefacts: implementation implications and ambiguities remain clearly
labelled as such. When an experiment needs a ground-truth requirement, cite the
corresponding `raw/` BRD; when it needs a compact analysis input, cite both the
breakdown and its source BRD from the table above.

## Reproducibility checks

Before using the corpus in an experiment or committing new source material:

1. Ensure every file in `requirements text/` has one `Source:` entry pointing
   to an existing file in `raw/`.
2. Resolve every local Markdown image reference from its BRD directory,
   including percent-encoded paths.
3. Keep unresolved business conflicts in the derived breakdown rather than
   silently selecting a value. Current examples include the Goal Management
   cascade threshold and several module-specific rules marked as source gaps.
4. Do not use signatures, logos, or diagrams as labelled ground truth unless
   the relevant experiment explicitly evaluates visual content.
