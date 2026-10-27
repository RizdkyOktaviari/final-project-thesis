# Requirements Corpus Readiness

## Scope

This note records the repository-level readiness of the requirements corpus for
thesis work on requirement analysis, consistency checking, and text-to-model
experiments. It is an inventory and validation record, not a claim that the
underlying business requirements are internally consistent.

## Verified inventory

| Item | Status | Evidence |
| --- | --- | --- |
| Source BRDs | Complete | 10 Markdown BRDs under `data/raw/` |
| Derived requirement texts | Complete | 10 numbered files under `data/requirements text/` |
| Source-to-derived traceability | Complete | Each derived file contains one `Source:` path to its BRD |
| Local visual assets | Complete | 63 PNG/JPG/JPEG files retained beside the relevant source material |
| Local image-link integrity | Passed | Every Markdown image reference resolves after URL decoding |
| Image decodability | Passed | All local PNG/JPG/JPEG assets expose readable image dimensions |

The detailed mapping and reuse rules are maintained in
[`data/README.md`](../../data/README.md).

## Research-use limitations

- The BRDs are source evidence. They include drafts, revisions, diagrams,
  signatures, and business-language inconsistencies; these are not silently
  corrected in `raw/`.
- The requirement texts are derived analysis artefacts. They retain open
  conflicts as explicit source gaps rather than treating an analyst's
  interpretation as ground truth.
- Visual assets are complete as locally available source material. This check
  cannot establish whether a historical Word/PDF source contained an image that
  was never supplied to this repository.
- The current corpus is ready for text-centred thesis experiments. A study that
  evaluates diagram extraction should define a separate visual ground-truth
  annotation set before measuring accuracy.

## Conclusion

The repository is complete and traceable for its current supplied corpus:
every requirement breakdown has a BRD source, and every local Markdown image
reference resolves. The remaining work is research design—defining the
experiment, labels, and evaluation protocol—not recovery of missing repository
assets.
