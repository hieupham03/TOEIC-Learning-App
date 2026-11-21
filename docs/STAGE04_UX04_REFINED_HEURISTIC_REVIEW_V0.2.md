# Stage04 UX04 — Focused Prototype V0.2 Desk Heuristic Review

**Performed:** 2026-11-21 · **Method:** document link graph validation + rendered screen inspection + 9 scripted paper paths.  
**Evidence class:** analyst desk inspection **only**. Not learner validation or Android device QA.

## Design-review rubric

| Heuristic | Candidate V0.2 evidence | Desk outcome | Remaining gap |
|---|---|---|---|
| Task discoverability | IA-A presents Practice + Full Mock as equal task cards | REPRESENTED | Short human discoverability test if necessary |
| Honest save status | Four save states: local selection, pending, ACK-confirmed, unknown/error; retry branch | COPY CLARIFIED | Real save state and accessibility |
| Mock integrity | Rules page, no voluntary pause/replay controls in clean mock candidate, explicit interruption/noncomparable | REPRESENTED | Real timed audio/clock behavior |
| Reading context | W-02A passage/question with P7-177 return and linked question; W-02B comparator | REPRESENTED | Actual scroll/Back/zoom and reading task |
| Score meaning | Fictional 130/200 raw correct only; caveat on ETS scale and nonequated forms | COPY CLARIFIED | Learner interpretation / real scoring |
| Conditional explanations | Practice feedback only where vetted; no early reveal in mock branch | REPRESENTED | Actual content release checks |
| Privacy | Learner isolation and already approved 7-day/30-day policy visible | REPRESENTED | Real auth/data deletion QA |
| Content unavailable | Cannot enter mock as eligible when asset/key unreviewed | REPRESENTED | Actual QA release gating |

## Document integrity checks

- **31 PDF pages, 81 internal link annotations, no unreachable page from intro** (verified by parsing PDF destinations).
- Checked two illustrative viewport cases (compact nominal ~360×780 and larger nominal ~412×915), **not real-device rendering**.
- No dangling links after revision; visible navigation labels remain text, not color-only.
- All mock/example scores are explicitly hypothetical; sample questions self-authored.

## Clear non-findings

No sampled learner walkthrough: **n=0**. No full 120-minute mock. No real audio/timer/persistence/auth. No accessibility compliance test. No proven quantitative usability improvement and no QA-01..08 PASS. This package supports a **design candidate review**, not unconditional final UI or Stage04 Gate PASS.
