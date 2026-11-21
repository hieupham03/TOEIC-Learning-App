# Stage 04 — UX-04 Focused Click-through Prototype Candidate Specification V0.1

**Status:** **ANALYST RESEARCH CANDIDATE — NOT FINAL UI OR IA**  
**Medium:** **26-page PDF with internal clickable navigation links**, grayscale phone-like wireframe. No executable app code, no backend, no true state, timer, audio or persistence. Generated text/question placeholders only.

**Open:** `../prototypes/STAGE04_UX04_FOCUSED_CLICKTHROUGH_PROTOTYPE_CANDIDATE_V0.1.pdf`. In a PDF reader that supports internal links, activate the rectangular action labels; in static preview, follow page labels manually.

## Route inventory and purpose

| Prototype page/state | Purpose | Baseline mapping |
|---|---|---|
| START / HOME / PARTSELECT | IA-A: equal visible practice/full-mock entry; quick/Part choice | FR-001,002,009,010,014; AT-01,02,10,14 |
| PRACTICE / PENDING / SAVED / SAVEERR | Part practice; honest unsaved/pending/ack/error semantics | FR-002,005,018,019; AT-02,05,19 |
| FEEDBACK | Vetted explanation when available, no invented explanation, user choice of next study | FR-006..009,014; AT-06..09,14 |
| MOCKLIST / RULES / LISTENING | B1 A/B selection, exam no-pause/no-arbitrary-replay, audible phase explicitly simulated | FR-010,011,019; AT-10,11,13 |
| INTERRUPTED / INVALID | Distinguish interruption and non-comparability, protect acknowledged answers | FR-005,013,018,019; AT-05,11,13,19 |
| PASSAGE / READQUESTION / ANCHOR / READINGPENDING / READINGSAVED | W-02A Reading passage-question switching and back-to-context, truthful save status, no answer reveal before completion | FR-003,004,005,011,019; AT-04,05,11,19 |
| RESULTS / PROGRESS | Example raw 130/200; show ETS non-equivalence, only compare eligible mock attempts | FR-008,012,013; AT-08,12,13 |
| PRIVACY | Own learner data and request/deletion policy display (7-day verified delete; ≤30 days post-pilot routine retention as approved) | FR-008,018; AT-08,18 |
| UNAVAILABLE | Incomplete/unreviewed content must not masquerade as clean exam | FR-015..017; AT-15..17 |
| ALTIA / ALTREAD | **Only IA-B / W-02B comparator** | U1-A/U2-A; UX-03 challengers |
| LARGEPASS / LARGEQ | Second **illustrative** Android viewport context with larger fonts, not device test | QA-08 future, AT-04 |

## Interaction design truths

- Every page explicitly says **UX simulation / no application code**. Internal links only move among static scenario states. No actual save confirmation, scroll anchor restoration, timers, audio, authentication, deletion, backend or live content.
- Any numeric mock scores are demonstrative fiction, not pilot results; no official ETS scaled score.
- Original sample English passages and sentences were composed for this prototype; no third-party TOEIC test items copied.
- PDF click targets are designed for review, not measured against physical touchscreen/Android accessibility requirements.
- Two layout contexts simulate **compact ≈360×780dp** and **larger ≈412×915dp with larger text**; page-coordinate dimensions are illustrative, not real dp device measurements.
- IA-A, W-02A, W-03A and W-04A remain **priority candidates**, not signed final IA, wireframes or visual system.

## Reviewer pathway

**Route A:** HOME → PARTSELECT → PRACTICE → PENDING → SAVED or SAVEERR → FEEDBACK.  
**Route B:** HOME → MOCKLIST → RULES → LISTENING → INTERRUPTED → INVALID.  
**Route C:** LISTENING → PASSAGE → READQUESTION → ANCHOR → READQUESTION; then compare ALTREAD.  
**Route D:** LISTENING → RESULTS → PROGRESS → PRIVACY.  
**Route E:** MOCKLIST → UNAVAILABLE.  
**Route F:** START → ALTIA; START → LARGEPASS → LARGEQ.

**Design review limit:** Task coverage/readability can be inspected in a PDF; real touch hit behavior, Android process restoration, screen-reader semantics, dynamic font reflow, audio sequencing and timing remain unverified until the appropriate product/UX test checkpoint.
