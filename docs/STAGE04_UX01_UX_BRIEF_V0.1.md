# Stage 04 — UX-01 Brief V0.1

**Status:** ANALYST DRAFT — UX-01 EXECUTED after PO approval `D04-KICKOFF-001`. **Not a PO-approved user experience or screen design.**  
**Authority:** Approved Product Vision V1.0; exact controlled PRD/SRS V0.6; Acceptance V0.4; Stage04 Kickoff Plan V0.1. **Do not add MVP capabilities.**

## 1. Product outcome, audience and context

Android smartphone TOEIC Listening & Reading learning app for **2–5 family learners** over a **four-week pilot**, online-first; the experience consolidates Part practice, audio, reading passages, answer checking, two long Full Mock A/B assessments, an error-learning loop and small practice sessions. Target learners have **irregular time**, so quick practice and full evaluation need to coexist without confusing their rules. Pilot success is usage evidence, valid A/B paired mock results for >=2 learners and feedback, **not** a promised official score increase. Android long Reading/Part7 scrolling and eye strain are material user-reported pain points; no invented usability test data.

## 2. Signed UX principles (constraints, not a screen)

| Principle | Expected UX behavior | Normative trace |
|---|---|---|
| EXAM vs PRACTICE | Visually/semantically distinguish strict mock from flexible Part/one-item training; users understand rules **before** mock starts | BR-01/02/04; FR-002/009/010/011; AT-02/09/10/11 |
| TWO FORMS B1 | A and B each 200 items, 7 Parts; no one-form release fallback without PO change | FR-010; AT-10 |
| TIMING & INTEGRITY | ~45min ordered Listening (not cut simply at 45:00); 75min Reading. Clean comparable mock permits neither voluntary pause nor discretionary replay; interrupted/uncertain attempts honestly marked | BR-04; FR-011/013/019; AT-11/13/19 |
| TRUTHFUL SAVE | ‘Đã lưu’ only after durable confirmed answer; pending/unsaved conditions and recovery must be understandable | BR-05; FR-005/019; AT-05/19 |
| UNIFIED CONTENT | Correct audio/question group and fully legible Reading passage/figures, errors don't become silently available | FR-003/004/015/017; AT-03/04/15/17 |
| HONEST RESULT | Raw correct/attempted/blank, by Part and L/R, with form/version and comparability caveat; no official 990 or proven gain assertion | FR-006/012/013; AT-06/12/13 |
| REVIEW AND CHOICE | Wrong-answer review/verified explanations when available, concise rule-based suggestions optional and overridable; no AI tutor | FR-007/008/014; AT-07/08/14 |
| FAMILY PRIVACY | Minimal private participant context, no cross-learner disclosure, explain verified deletion within 7 calendar days and routine retention <=30 days post-pilot with lawful exceptions | BR-08; FR-001/018; AT-01/18 |
| ACCESSIBLE PHONE READING | Complete long multi-passage Reading, scalable legibility, touch affordances, no loss of answer context on return | FR-004/005; NFR-005/010; AT-04/05 |

## 3. UX actors and jobs

- **Learner:** invited family member (pilot), has own goals, time budget, response/history, not privileged to see others' history.
- **Content reviewer/operator:** governed responsibility for QA and content/version status. A full user-facing admin console is **NOT** approved by requirements; only define learner-visible effects of unavailable, corrected or withdrawn questions.
- **Product Owner/pilot evaluator:** reads aggregate feedback and valid/incomplete pilot evidence under a separate, permitted governance context; no new unapproved analytics dashboard.

## 4. User-journey inventory (what to solve, not a completed flow map)

| J | Job-to-be-done | Observable finish / bad outcome to prevent | Current scope |
|---|---|---|---|
| J01 | Establish goals, approximate level and available duration | Preference linked to correct learner; no compulsory quiz | M01 IN |
| J02 | Launch practice quickly by Part or one-question session | Can self-choose without accepting suggestion; avoid mock confusion | M02/M05 IN |
| J03 | Answer L/R content with audio/passage and navigation | Correct content context, answers preserved, missing assets blocked | M02/M07 IN |
| J04 | Start/complete mock A or B under strict rules | Understand form, 7 Parts, time and no replay/pause; receive honest finish/integrity label | M03 IN B1 |
| J05 | Background/network/process interruption | Understand last confirmed answer and whether attempt is still comparable | M07 IN |
| J06 | See results and learn from mistakes | Raw totals, form/version, explanation when vetted, action to return to practice | M04 IN; vetted explanation conditional |
| J07 | Get next practice suggestion or ignore it | Reasonable default if no data, user may choose another Part | M05 IN non-AI |
| J08 | View own history, understand retention and request deletion | No family crossover; verified deletion rules conveyed accurately | M07 IN |
| J09 | Encounter unavailable/corrected content | Cannot begin false-ready mock; impacted historical record isn't silently rewritten | M06 IN; backoffice design not committed |

## 5. Critical exceptional conditions to represent eventually

`E01` no verified content; `E02` wrong/missing Listening audio; `E03` missing Reading table/image; `E04` no/slow network; `E05` answer pending/not acknowledged; `E06` background/OS termination during mock; `E07` audio interrupted/timing integrity unknown; `E08` explicit timeout/submit/quit; `E09` repeated submit/duplicate result; `E10` no QA-approved explanation; `E11` invalid/comparability-excluded mock; `E12` content revised after an attempt; `E13` unauthorized cross-user view; `E14` verified delete request/exception; `E15` font-size adjustment or small-screen long Reading; `E16` empty first-use recommendation. Detailed state/action variants are proposed in UX-02, not approved UX assets.

## 6. UX-01 acceptance and future evidence

1. Every **IN** FR-001..019 and NFR-001..013 must be mapped to a UX touchpoint or deliberately identified **NON-UI** responsibility. `STAGE04_UX01_REQUIREMENTS_COVERAGE_V0.1.md` provides this map; **coverage as an inventory is not UX testing PASS**.
2. Each primary journey has a success condition, at least one failure/exception, and associated AT reference.
3. Decision candidates for UX-02 are limited to four **consequential interaction tradeoffs**, grouped as one PO decision; no screen count, wireframe, visual layout, visual identity or backend architecture yet.
4. No extra mandatory feature, especially auto PDF import, AI runtime, advanced vocabulary notifications, offline-first or ETS-certified score, may be introduced without change control.

## 7. Design-informed external evidence (not implementation mandate)

- Android recommends preserving user-visible state across lifecycle/process changes; a promise that an answer was saved must reflect a truthful persistent result, independently of whatever future architecture is chosen. Official: https://developer.android.com/topic/libraries/architecture/saving-states
- Android accessibility recommends minimum **48dp × 48dp** interactive touch targets; treat as a later prototype accessibility check, **not** an already-approved formal KPI. Official: https://developer.android.com/guide/topics/ui/accessibility/apps
- Android recommends considering system text scaling and adaptive layout. Small-screen phone is first priority; tablet/iOS scope is not added by this observation. Official: https://developer.android.com/develop/ui/compose/accessibility/scalable-content ; https://developer.android.com/design/ui/mobile/guides/layout-and-content/adapt-layout

**Boundary:** UX-01 is an evidence-organized brief, **not** the actual UX design, a prototype, and certainly not a running Android app. Actual tests QA-01..08 remain due before pilot under signed G03 conditions.
