# Stage 04 — UX-04 Usability Scenario Protocol PROPOSAL V0.1

**State:** PLANNED ONLY. NO usability sessions executed; NO actual participant results; NO prototype exists. UX-04 starts only if PO approves `D04-PROTO-004`.

## 1. Scope and participants

The authorized pilot persona is 2–5 family learners, Android phone, TOEIC L&R, uneven available study time. Prefer desk heuristics first, and target 2–5 *voluntary* learners for focused walkthrough only if a material UX uncertainty remains. Record actual participants and devices later; no assumption that the group represents the public market. **Do not require the Product Owner to sit a second 120-minute Full Mock.** Test comprehension by simulated partial scenarios, not a live complete test.

## 2. Proposed scenario cases (short mock-state simulations, not full 120m)

| Case | Learner's task / prompt | Observe, do not instruct | Requirement / QA bridge |
|---|---|---|---|
| UT-01 | 'Bạn có 5 phút, tìm một câu để luyện' | Locate short practice without entering full mock; skip suggestion | U1-A, FR-001/002/014, AT-01/02/14 |
| UT-02 | 'Bạn muốn bắt đầu một đề 200 câu' | Choose one of Mock A/B, identify timing/replay/no-pause rules *before* starting | B1, S2-A, AT-10/11 |
| UT-03 | 'Đang đọc Part 7, mở câu hỏi rồi quay lại bằng chứng' | Re-find relevant passage/table and earlier reading position; compare W-02A/W-02B if selected | U2-A, AT-04, QA-08 |
| UT-04 | 'Chọn đáp án, mạng chậm, chỉ thấy Đang lưu' | Distinguish selected/pending/confirmed/failed; avoid assuming persistence | U3-A, AT-05/19, QA-08 |
| UT-05 | 'Lượt Full Mock bị gián đoạn trong Listening' | Interpret whether comparable, what happened to acknowledged answers and time; not assume voluntary pause/replay | W-03A, AT-11/13/19 |
| UT-06 | 'Bài luyện đã kết thúc và có câu sai' | Access vetted answer and optional practice; missing explanation disclosed, no answer mid-mock | W-04A, AT-06..09 |
| UT-07 | 'Kết quả hai đề khác nhau' | Learner understands raw score and that it does not prove official scaled TOEIC improvement | R2, AT-12/13, QA-07 |
| UT-08 | 'Thành viên khác sử dụng điện thoại' | No accidental cross-user history; understand deletion request status if shown | R4, AT-18, approved retention policies |
| UT-09 | 'Không có audio hoặc câu bị rút khỏi đề' | Notice not-ready/error state; no false success or fabricated explanation | AT-15..17, QA-01..06 |

## 3. Proposed observation sheet (unfilled template)

For each scenario record: `candidate`, `context`, `participant (anonymous ID if any)`, `moderation`, `task outcome (completed / completed with assist / not completed / not run)`, `confusion`, `time only if actually measured`, `user quote only if captured with consent`, `severity P0..P3`, `requirements link`, `next decision`.

`P0`: Misleading exam integrity/official score, exposed other learner data, false saved state resulting in data-loss expectation, hidden/missing mandatory Reading/media, early exam answers. `P1`: Cannot complete core task without assistance. `P2`: Recoverable confusion/friction. `P3`: Cosmetic/copy preference. Definitions are **candidate heuristics**, not approved quantified acceptance thresholds.

## 4. Procedural safeguards

- If user testing is approved later: ask permission, avoid collecting official scores or unnecessary identifiable/personal data, do not record media automatically, accept refusal without consequences.
- Prototype cases **simulate** interruptions, timeouts, content errors and account separation; never assert the prototype has the reliability of an app.
- Run context checks in two different Android phone viewport/text size conditions; device names and measurements are TBD until actually tested.
- Summarize qualitative findings + uncertainty; for 2–5 learners no population-level claims or proof of TOEIC score improvement.
- Separate 'reviewed screen/path' from 'test run PASS' and later release QA.

## 5. Proposed output for a later review

An issue register prioritized by risk, concise interaction alternatives, evidence snapshots with consent, recommendation to KEEP/AMEND/HOLD selected UX patterns, and an explicit decision for PO. This document contains **no actual evidence** yet.
