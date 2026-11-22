# D05-CONTENT05-PO-11 — PO review acceptance of 11 publisher-keyed Reading items

**Date:** 2026-11-22 (Asia/Ho_Chi_Minh).  
**Decision:** **PO REVIEW PASS / APPROVED FOR CONTROLLED IMPORT of exactly 11 already source-matched Reading items**, not formal independent QA or an assertion of already built/working graded APK.  
**Authority:** Direct, new Product Owner instruction in ongoing chat, following instructions for opening `review.html`:

> "tôi đẫ kiểm tra ua và đều ổn r. hãy cho pass luôn bước này"

English: PO states that they have checked the review and it all looks fine, and explicitly asks to PASS this step. **Evidence class:** PO self-attestation of actual review, not a separately attached item-by-item JSON export, external examiner report or machine-import log. The Product Owner is the human approving reviewer for this limited step. Do not falsely claim the PO clicked the JSON export button or that Codex independently performed the human review.

## Exact scope of authorized decision

Review approval applies **only to the 11 source-key-matched questions already in the CONTENT-04/05 private source pack** as recorded in `docs/STAGE05_TWO_USER_MULTI_SOURCE_GRADED_REPORT_V0.1.md` and `docs/STAGE05_TWO_USER_FIRST_GRADED_PRACTICE_REPORT_V0.1.md`:

- **Faust Academy Reading 01 / Part 5:** five source-key-matched items **101–105** (`faust-r01`).
- **EnglishClub / Part 5:** four publisher examples (`englishclub-p5`).
- **EnglishClub memo / Part 7:** two questions (`englishclub-p7:memo`).

**Counts:** Part 5 **9**, Part 7 **2**, total **11**. These 11 all have already documented publisher answer evidence and item/source/version/ordered-choice fingerprints. No other Zenlish 198 items or ETS/IIG sample items are included, because no PO item-review decision is claimed for those.

## Controlled implementation authorization

1. **The PO's direct chat approval is a real owner approval instruction; no need to demand that the PO click 11 times or supply a JSON file to re-express it.** Codex may transcribe that **one explicit PO approval** into the precise local `reviews.json` / `review-decisions.json` rows for these 11 items, with truthful provenance:
   - `reviewer`: an unambiguous role annotation such as `Product Owner — explicit chat attestation 2026-11-22`, **not an invented person's name**.
   - `reviewedAt`: `2026-11-22` (date of the attested review).
   - `status`: `APPROVED` only if its existing genuine publisher source-key record validates.
   - `label`, source URL/version, item/group ID, ordered choices, media/passage fingerprint, evidence SHA256 and page/line locator: **copy verbatim from the already sourced matching 11 key-evidence rows**, never infer new values or invent source documents.
   - Store the PO attestation document ID `D05-CONTENT05-PO-11` in a non-sensitive private review audit/metadata field if existing schema allows it, otherwise the document and issue #13 comment are sufficient provenance.
2. Validate each row using the existing `review_study_content.py --workspace content-04 --import-review ...` workflow and exact local PDF/HTML file SHA256 checks. **Fail closed** and leave that particular item unscored if any matching source file, hash, locator or content mapping is missing, stale or inconsistent. Report counts less than 11 if appropriate; **do not mark all 11 activated without actual technical proof**.
3. Rebuild a new **versionCode >9** private Study APK from the now-reviewed content pack, keeping Android package and signing compatibility, preserving SQLite attempt/history and revoked-key rules. Verify that on a real source item there is true correct/incorrect result, a wrong-answer history entry, and no explanation if source explanation is missing.
4. Unit/ingestion/guard/Android emulator and upgrade tests must pass. Report actual source-key-matched vs reviewer-approved vs APK-scorable totals, SHA256 and test outcome.
5. Prepare APK for the user's two actual phones; their physical-device results remain **NOT RUN** until PO actually tries the NEW build. Do not inherit earlier 0.2.1 phone test.
6. **No formal Stage05 ECP/QA PASS, pilot approval, official TOEIC score, Google Play release or Full Mock unlock** is conferred by this limited PO review. Full Mock A/B still require their separate 200+200 independent reviewed item/asset gates and approved baseline. Keep Google Play ON HOLD.

**Disposition:** User's requested **review step is approved now**. **Engineering activation and two-device acceptance are separate, pending steps.** This doc is recorded in public Git as a *decision only*, never containing original proprietary question/answer/key data, reviewer PII, PDF or source media.
