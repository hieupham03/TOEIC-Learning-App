# Stage 03 B1 — Authorized Web Source Audit Plan V0.1

**Date:** 2026-11-21. **Status:** PLANNED / NO DATA IMPORT, NO QA CLAIM. **Content approach:** web-first for PO-authorized sources, original content only for gaps if later approved.

## Source shortlist and working order (analyst proposal, not MVP lock)

| Priority | Source / candidates | Public evidence | What remains |
|---|---|---|---|
| Primary candidate | STUDY4 `TOEIC LR Collection 1 Test 1`, `Test 2` | Both pages explicitly list 120 minutes, 7 parts, 200 questions; count per Part 6/25/39/30/30/16/54 | Full item and answer/audio/image manifest, valid delivery route, independence and all-item QA |
| Parallel fallback | Zenlish 2026 `Test 1`, `Test 2` | Both test pages public, guest mode; actual questions and part counts loaded dynamically | Confirm 200 per test and Part structure, full answers and media, asset source, rights and QA |
| Additional candidate | The TOEIC Lab | App site returned login-check page in public research | Authorized catalog/metadata; do not request passwords or bypass controls |
| Future inventory | Other PO-licensed websites and question banks | PO reports more sources | URLs/canonical source IDs not yet specified, so no counts assigned |

**Verified public references, last checked 2026-11-21:**
- STUDY4: https://study4.com/tests/6852/toeic-lr-collection-1-test-1/ ; https://study4.com/tests/6853/toeic-lr-collection-1-test-2/ .
- Zenlish: https://zenlishtoeic.vn/stm-quizzes/test-1-2026/ ; https://zenlishtoeic.vn/stm-quizzes/test-2-2026/ .
- The TOEIC Lab: https://test.thetoeiclab.vn/ .

## Minimal mock manifest for source audit (metadata, not copied question content)

Required fields per form: source URL, form title, authorized collection/delivery method, content owner/right-holder reference, reuse basis and coverage, count of items per Part, unique item IDs, item-group IDs, audio IDs, image IDs, passage IDs, answer-key IDs, explanation availability, revision/version, provenance, last-verified timestamp, QA reviewer/status, costs and restrictions.

Quality checks before B1 lock:
1. Each form exactly **200 items** and Part counts **6,25,39,30,30,16,54**; total **400 distinct items**.
2. 100% of Listening questions are linked to matching playable audio; Part 1 and visual items map to authorized images; Part 6/7 passage–question group mapping intact; full answer keys are verified.
3. Cross-form deduplication, including common book-mirrors across different websites; avoid using the two mock forms as a practice bank.
4. Independent content QA, correction log and provenance; no known severe ambiguity/answer mismatch/audio mismatch before pilot.
5. Record rights evidence at the content and media granularity before copying/distributing, without re-requesting the general assertion.
6. Distinguish raw/mock progress from officially equated ETS scores. Only claim comparability if appropriate quality/calibration evidence exists.
7. Estimate time and cash cost for authorized export, mapping, QA, audio hosting, and 4-week pilot before asking PO to approve a budget cap.

## Evidence-first next action

Public metadata for two STUDY4 full-test candidates has been verified. **Do not treat public HTML as an authorized export interface.** Determine if PO has a legitimate provider export / owned archive / documented reuse-delivery method. Only when authorized access or content is available, perform a batched item-level audit and report one readiness matrix to PO.

**No bulk download, scraping, login bypass, app development or publication is part of this document.**
