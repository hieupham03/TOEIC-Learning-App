# QA-01..08 — Approved Framework → Verification & Evidence Matrix V0.2

**Approval:** Product Owner APPROVED D03-QA-006 on 2026-11-21 **as a framework**.  
**Execution:** **NONE VERIFIED** by analyst; do not mark PASS based solely on existing inventory.  
**Mock inventory:** both sets PO-CONFIRMED DONE. No repeated inventory request.  
**Budget:** DEFERRED BY PO; not in this QA check list.

| QA ID | Review question | Proposed evidence (one batch, later if available) | Proposed hold condition | Timing |
|---|---|---|---|---|
| QA-01 | Each form has correct total and allocation by Part? | Form ID, Part distribution, completeness summary | Missing/misallocated item | Content pre-pilot |
| QA-02 | Every question has exactly one correct, validated answer? | Key coverage, resolution log for ambiguous items | Wrong/unknown key | Content pre-pilot |
| QA-03 | Are audio clips complete and correctly mapped to groups/items? | Audio/group mapping coverage plus representative listening QA | Wrong clip, ordering or missing media | Content pre-pilot; playback later |
| QA-04 | Are image, tables, reading passages and question groups complete? | Passage/group/asset relation and exception list | Missing context required to answer | Content pre-pilot; rendering later |
| QA-05 | Are A/B independent and isolated from Part practice before assessment? | Cross-form and practice bank duplicate/leakage report | Duplicate/leaked scored item affecting score comparison | Content pre-pilot |
| QA-06 | Is each released item/media traceable to source and authorization? | Source-ID, use-rights attestation, item-version, asset link | Untraceable item/media | Content pre-pilot |
| QA-07 | Are scores computed and communicated without misleading ETS equivalence? | Result rules, known-answer examples, copy review | Wrong count/Part or official-score assertion | Requirements; later test |
| QA-08 | Does the user retain responses and know what happened after interruption; can they read long Part 7 on Android? | Edge-case requirements now; actual device tests and incident log later | Silent answer loss, unclear timer, clipped reading content | Requirements and later Android testing |

## Proposed batch checklist — NOT an upload request now

When actual content and/or prototype become available, review by **one** consolidated signed evidence packet: Form A/B summaries, Part counts, key/media/passages, duplicates and any exceptions, plus eventual test reports. No requirement to send entire copyrighted corpus into chat. Do not claim a full 400-question audit was done.

## Acceptance thresholds pending future PO approval

- Proposed zero **known blocking** defects in released mock content; all mismatches in keys/audio/passages block affected form until fixed.
- Proposed all active item-to-asset/key relationships resolvable; numeric source-data coverage verified in audit artifact.
- Timer behavior, long-form accessibility and reliability must be testable; actual target devices and quantitative performance bounds are TBD.
- Any cross-form accuracy improvement is descriptive unless validated for form difficulty; no official score equivalent.

**Explicitly outside current review:** app screens, architecture, testing runnable software, procurement and budget questions.
