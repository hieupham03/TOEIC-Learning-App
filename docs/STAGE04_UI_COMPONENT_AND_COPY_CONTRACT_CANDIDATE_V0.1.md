# Stage04 — UI Components & Copy Contract CANDIDATE V0.1

**Status:** Proposed annex for D04-UI-007, not an implemented UI toolkit and not a modification to PRD/SRS. No software architecture or application code.

## A. Visual hierarchy and tokens

| Role | Candidate value | Rule |
|---|---|---|
| Typeface | A single Vietnamese-safe sans-serif, e.g. Noto Sans/Roboto; final platform font requires review | Do not mix decorative families or inconsistent weights |
| Hero / title / section / body / metadata | 28 / 22 / 18 / 16 / 14 sp | Resize and test with large-text Android setting |
| Brand / CTA | `#0B736A` + white text | ~5.71:1 declared pair |
| Main text | `#0F172A` on white | ~17.85:1 |
| Secondary | `#475569` on white | ~7.58:1 |
| Canvas / muted surface | `#F8FAF9` / `#EDF4F1` | Main content on white; muted used sparingly |
| Decorative line | `#D9E1DE` | ~1.33:1 white, **not** a required control boundary |
| Meaningful outline | `#64748B` | Essential input boundary; verify against exact adjacent backgrounds |
| System warnings | amber/red + semantic text | Not color-only; distinguish pending, unknown, invalid |
| Spacing | 8dp grid, 4dp micro-offset | Empty space before new card/fill |
| Clickable | target >=48×48dp | Target only until real Android device checked |
| CTA | one primary/action per screen, except equal Home learning route pair | No competing CTA stack; stable labels |

## B. Contract for reusable components

| Component | Required states | Truthful text or behavior |
|---|---|---|
| LearningRouteTile | available / blocked | `Luyện theo Part` and `Full Mock` equally discoverable; no unready content launch |
| QuestionChoice | default / selected / pending / confirmed / unknown | Answer choice is not saved automatically by appearance |
| SaveIndicator | pending / confirmed / unknown/failure | `Đang xác nhận lưu` → `Đã xác nhận lưu` only after durable ACK; else `Chưa thể xác nhận lưu` and retry |
| ReadingContextSwitcher | passage / question / anchor unknown | `Đoạn văn` and `Câu hỏi`; attempt P7-177 anchor return; do not falsely claim position saved |
| MockTimerStatus | Listening / Reading / interruption / expiry | Distinguish ~45min audio-based Listening and 75min Reading; no arbitrary pause/replay in comparable mock |
| AttemptIntegrityLabel | valid / incomplete / noncomparable | State in plain language; invalid cannot inherit valid badge |
| RawResultSummary | raw correct / attempted / unanswered / part / L-R | `Kết quả luyện tập — không phải điểm TOEIC chính thức` |
| VettedExplanation | verified / unavailable | Only `Giải thích đã kiểm duyệt` when proof exists; otherwise `Chưa có lời giải được kiểm duyệt` |
| ContentReadiness | QA-ready / unready / withdrawn | Unready blocks start; show reason and return action |
| LearnerContext | active / switching / access denied | No other learner's scores/history exposed |

## C. Copy consistency examples

| NEVER imply | Use only under condition |
|---|---|
| `Đã lưu` while request pending | `Đang xác nhận lưu` while awaiting actual ACK |
| `Đã xác nhận lưu` from local visual change only | `Đã xác nhận lưu` on durable evidence; otherwise `Chưa thể xác nhận lưu` |
| `Thi thử hợp lệ` after invalidating interruption | `Lượt thi không đủ điều kiện so sánh` |
| `Tăng 100 điểm TOEIC` from two raw forms | `Số câu đúng (đề A/B), mức khó có thể khác nhau` |
| `Giải thích đã kiểm duyệt` on draft AI sample | `Lời giải mẫu (chưa kiểm duyệt)` in static design, or omit until QA |
| `Vị trí đã lưu` when scroll state not captured | `Quay lại đoạn liên quan` until implemented and verified |

## D. Flow and business boundaries

- Mock A/B remain two mandatory Full Mocks (2 × 200, Listening ~45m, Reading 75m), separate from Part practice bank.
- No revealing correct answer in active clean mock. No custom replay/pause and no auto timer reset.
- Short practice recommendations are optional rule-based suggestions, not runtime AI.
- Personal data controls respect approved 7-calendar-day verified-deletion policy and routine ≤30 days after pilot, subject to approved exceptions; this is requirements text, not implementation proof.
- For every visual state, require a trace to corresponding FR/NFR and AT; preserve `UI-G01..16` anti-pattern guardrails.
