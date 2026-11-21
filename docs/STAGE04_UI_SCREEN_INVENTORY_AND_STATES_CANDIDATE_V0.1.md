# Stage04 — Screen / Component / States Inventory CANDIDATE V0.1

**Status:** Proposed visual UX/UI design inventory for D04-UI-007; does not imply screens are implemented, visually complete pixel by pixel, or usability-tested. **Referenced illustrations = four representative screens**; prior UX04 PDF V0.2 covers 31 linked low/mid states.

| Screen/state | Candidate UI elements, truthful copy | Requirements / AT | Visual evidence |
|---|---|---|---|
| UI-01 Task Hub | Equal Luyện tập / Full Mock, optional rule suggestion, bottom destinations | FR-001/002/009/010/014, AT-01/02/09/14 | Illustrated |
| UI-02 Part Selector | Part 1–7, short study, bank readiness, no mock leakage | FR-002/009/015, AT-02/09/15 | Earlier clickable PDF |
| UI-03 Listening Practice | Group/audio label/availability, answer; replay obeys practice mode | FR-003/005, AT-03/05 | Spec, not illustrated |
| UI-04 Reading Passage | Semantic group/anchor, scroll context, complete images/tables | FR-004, AT-04 | Illustrated (W-02A) |
| UI-05 Reading Question | Switch to question and return to same passage anchor | FR-004/005, AT-04/05 | Earlier clickable PDF |
| UI-06 Answer Pending | "Đang xác nhận lưu" without success claim | FR-005/019, AT-05/19 | State specified |
| UI-07 Answer ACK Confirmed | "Đã xác nhận lưu" only upon ACK, backed by test in actual app | FR-005/019, AT-05/19 | Illustrated W-03A concept |
| UI-08 Answer ACK Unknown | "Chưa thể xác nhận" + idempotent retry/leave guidance | FR-005/019, AT-05/19 | Earlier clickable PDF |
| UI-09 Mock A/B | Two form choices, readiness indicator, never launch invalid source | FR-010/017, AT-10/17 | Earlier clickable PDF |
| UI-10 Mock Rules | 200 questions, 45+75, restrictions and integrity notice | FR-010/011/013, AT-10/11/13 | Earlier clickable PDF |
| UI-11 Clean Mock Listening | Ordered audio, timer as defined; no replay/pause UI | FR-003/011, AT-03/11 | Concept illustration only |
| UI-12 Clean Mock Reading | Passage/question context; no mid-exam key | FR-004/011, AT-04/11 | Earlier clickable PDF |
| UI-13 Mock Interrupted | Warning and next action, no automatic reset | FR-011/019, AT-11/19 | Earlier clickable PDF |
| UI-14 Mock Noncomparable | Badge text, no progression claim, preserve acknowledged answers | FR-011/012/013, AT-11/12/13 | Earlier clickable PDF |
| UI-15 Mock Raw Results | Raw correct/attempted/unanswered, Part/L/R and form/version | FR-006/012/013, AT-06/12/13 | Earlier clickable PDF |
| UI-16 Mistake Detail | Reviewed key; curator-approved explanation only if available | FR-007/008, AT-07/08 | Illustrated W-04A |
| UI-17 Next Practice | User override rule suggestions, no forced path | FR-009/014, AT-09/14 | Illustrated W-04A |
| UI-18 Personal / Data | Active family profile, privacy, access/delete request status | FR-018, AT-18 | Earlier clickable PDF |
| UI-19 Unready Content / Updated Result | Safety block, source version/revision note, no fabricated key | FR-015/016/017, AT-15/16/17 | Earlier clickable PDF |

## Mandatory state models

- **Save:** `idle → pending → durable-ACK` OR `pending → unknown/failure → retry/reconcile`; UI text may never skip from pending to acknowledged without evidence. Actual technical semantics reserved to authorized architecture/testing phase.
- **Mock:** `not-started → rules acknowledged → active Listening → active Reading → submitted/timeout → raw result` OR `interrupted → potentially noncomparable`; do not render a compromised attempt as a valid comparable result.
- **Content:** `candidate → source/asset/key QA → ready` OR `blocked/withdrawn/revision`; candidate/unready content cannot be falsely launched.
- **Feedback:** `active clean mock → no key disclosure`; `ended/eligible review → verified key` and optional vetted explanation; missing explanation disclosed.
- **Family privacy:** active learner context must be clear; switching cannot expose other learner's result.

## Coverage and handoff

- **19/19 MVP FR** have at least one candidate UX touchpoint or explicit non-UI QA dependency; NFR-001..013, including budget NFR-013 as *DEFERRED non-UI*, retain owner/test checkpoints. Acceptance Catalogue AT-01..19 mapped in prior UX-01 matrix and carried forward.
- Color/typography/touch tokens are **proposal**; accessible contrast, large text, English + Vietnamese wrapping, focus order, talkback, real viewport safe areas and physical device checks **NOT validated**.
- IA-B and W-02B remain references; choosing the visual candidate cannot delete either comparator's research notes or break approved baseline.
