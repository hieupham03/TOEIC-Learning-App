# D03-SCOPE-009 — Product Owner Approval Record V1.0

**Date:** 2026-11-21  
**Authority:** Product Owner (explicit user decision in this conversation)  
**Disposition:** **APPROVED — combined S1-A + S2-A + S3-A**, per Stage03 Formal Scope Decision Package V4.0  
**Project:** TOEIC Learning App · Stage03 Requirements IN PROGRESS

## Signed decision statement

> Tôi, Product Owner, PHÊ DUYỆT D03-SCOPE-009 = A: chấp thuận tổ hợp S1-A + S2-A + S3-A của hồ sơ Stage03 V4.0 để khóa phạm vi nghiệp vụ MVP, các chính sách nghiệp vụ và tiêu chí nghiệm thu đã nêu. Hãy ghi quyết định, đối chiếu và cập nhật PRD/SRS thành bản đề xuất baseline mới, rồi trình D03-BASELINE-010 để tôi duyệt riêng. Không tự phê duyệt PRD/SRS baseline, Stage03 Gate, UX/UI, kiến trúc hay code. Giữ B1 hai Full Mock, QA-01..08, CP-01..05 và ngân sách DEFERRED.

**Effect of approval:** Formal **business MVP scope lock**, approved **P01–P09** policy defaults in S2-A, and approved **AC-01..08 + PM-01..06** criteria in S3-A, subject to the explicit verification-stage boundaries of V4.0. Not a signoff that QA passed, no implementation, no PRD/SRS baseline, no Gate pass.

## 1. Approved S1-A MVP business boundary

- **IN (M01–M07, M09):** Android smartphone/online-first/2–5 family learners/4 weeks; separate Part1–7 practice; two mandatory independent full L&R mock forms (B1), each 200 items; vetted answers, raw scores, history/errors; one-item quick practice; optional basic deterministic next-practice suggestion that users can override; content source/version/review/withdraw controls; acknowledged-answer preservation, family-data separation and long-Reading usability requirements.
- **CONDITIONAL (M08):** show curator-verified explanations if actually available; disclose absence otherwise. A practice item bank distinct from both mocks must satisfy quality and non-exposure checks before release; these content dependencies are not feature approvals by themselves.
- **OUT/DEFERRED (X01–X05):** automatic PDF/audio extraction and answer mapping, runtime AI tutor/generation, interactive vocabulary notification actions, iOS/offline-first/S&W, payment/ads, any official ETS-equivalent score claim.
- **Content:** Two Full Mock inventories are **PO-REPORTED COMPLETE**. PO affirmed reuse rights for nominated sites and further owned/authorized sources; specific item/audio/image/key QA evidence **NOT REVIEWED**. Release gate **OPEN**, no changes to B1.

## 2. Approved S2-A business rules

- Strict evaluative full-mock mode with ordered Listening audio (~45m) and a Reading 75-minute limit; practice sessions are flexible. Do not cut a valid audio clip merely to force a rigid 45:00 boundary.
- No voluntary pause or discretionary replay in an attempt presented as clean/comparable. Interrupted or assisted attempts with unproven timing/audio integrity are explicitly **non-comparable**, not silently valid. Exact technical tolerances may be determined for test planning without weakening this rule.
- Acknowledged answers must not disappear silently. Unacknowledged network operations may be pending; do not falsely indicate saved. Single finalized result; raw/Part scores and honest attempt/version labels, no ETS 10–990 equivalent. Record affected versions on content corrections.
- Minimal pilot learner data, separated participants, ability to request data deletion, **within 7 calendar days after a valid verified request** subject to lawful retention exceptions, and routine retention **no longer than 30 days after the four-week pilot** unless explicitly otherwise agreed. Identity/auth and legal exception details require application before pilot; no technology choice made here.

## 3. Approved S3-A QA, acceptance and pilot metrics

- At documentation signoff, **100% critical MVP FR/NFR** mapped to preconditions, observable expected results, AT ID and verification phase (AC-01).
- **Before pilot content use:** both 200-question forms and seven-Part counts, 100% essential key/audio/image/passage/source/version review, no known critical content issue and no exposed/duplicate evaluative items (AC-02..04; QA-01..06). Tests **NOT RUN** to date.
- **Before pilot:** zero known critical scoring/answer-loss/duplicate-result/data leakage/false-score claims; Reading usable on **at least two Android device sizes/contexts** (AC-05..06); QA evidence logged PASS/FAIL/NOT RUN/BLOCKED/EXCEPTION (AC-07).
- Performance/device/time numeric SLA values not grounded yet: **TBD BEFORE SOFTWARE TEST PLAN BASELINE** (AC-08), not silently approved.
- **Four-week family pilot:** 2–5 invited participants; at least **2 people** each complete **both** full mocks in valid attempts and report usability; at least **2 people** use Part practice and give useful feedback; otherwise label comparative pilot evidence inconclusive. Log attempts and incidents, do not promise TOEIC score gains (PM-01..06).
- **Budget-related steps:** **DEFERRED BY PO, NOT WAIVED**; CP-04 tracked at relevant future authorization. Do not request budget, prepare estimates or authorize spend at this stage.

## 4. Explicitly unapproved

- `D03-BASELINE-010` **PENDING PO**: revised PRD/SRS V0.6 are **candidate baseline documents only**.
- Stage03 Gate Review/closure **NOT APPROVED**; no Stage04.
- No UI/UX design, architecture, database/API/provider selection, app code/Codex, scraping/extraction, supplier contact, money, or release approved.
- QA-01..08 **approved framework only**; item-by-item and actual Android/software verification **NOT PASSED**.

## 5. Trace and non-reopening

This record supersedes `D03-SCOPE-009 PENDING` labels in historical V4.0 proposals **without modifying historical documents**. Preserve approved Product Vision V1.0 unchanged and previous decisions D03-QA-006, D03-REQ-007, D03-READY-008, B1 and CP-01..05. Do not re-request mock inventory, site rights or budget. See `STAGE03_MVP_SCOPE_LOCK_MATRIX_V1.0.md`, `STAGE03_MOCK_AND_DATA_POLICIES_APPROVED_V1.0.md` and the D03-BASELINE-010 packet.
