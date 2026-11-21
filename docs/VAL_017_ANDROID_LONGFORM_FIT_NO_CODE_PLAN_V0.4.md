# VAL-017 — Android Dual-Mode Fit, No-code Validation V0.4

- **Date:** 2026-11-21
- **Status:** APPROVED INTENT / PRIOR FULL MOCK COMPLETION SELF-REPORTED VAL-020 / STRUCTURED STUDY NOT RUN
- **Replaces active plan:** V0.3 (retained for traceability)
- **Owner:** Product Owner; solo; no facilitator, no coding, no UI mockup required, no PDF/audio upload
- **Sources:** VAL-016 baseline PC, VAL-017 wish Android replace PC, VAL-018 wants both Part Practice and continuous Full Mock Test, VAL-019 confirms prior >=30-min Android TOEIC experience felt fairly convenient; VAL-020 confirms the user reports completing at least one full 200q/~120m mock on Android (both retrospective self-reports)

## 1. Question, definitions, and decision boundaries

**Main study question:** Is a smartphone Android acceptable as a practical environment BOTH for flexible practice across Listening Parts 1–4 and Reading Parts 5–7, AND for a continuous 120-minute TOEIC-style Full Mock?

**M1 Part Practice:** Practice independently in one or more Parts, in bite-sized sessions. VAL-018 does **not** yet approve a pause/resume feature or a timer per Part. Learn from mistakes; partial Part results are NOT direct TOEIC total score measurements.

**M2 Full Mock Test:** Full continuous linear TOEIC L&R format (200 questions, Listening 100 in ~45 minutes and Reading 100 in ~75 minutes). Full mock can only be compared across tests with controlled/question-set quality and scoring validity. The user wants the ability, but one Android full mock completion is REPORTED RETROSPECTIVELY in VAL-020, but comfort, interruptions, quality and willingness to repeat remain unknown; the structured M2 trial is NOT RUN.

**Parallel third direction:** Instant Microlearning remains separately on the vision; not an experiment outcome here.

## 2. Necessary constraints

- Android phone in real-use conditions; record model/screen size if known, headphones, network, battery at start/end if observable.
- User does testing SOLO, independently; use a legally accessed third-party TOEIC Android learning service with appropriate questions and audio. If none exists for the task, write `NOT AVAILABLE`; no app building or unauthorized copying.
- PC baseline `VAL_013_LIBRARY_NO_CODE_TEST_PLAN_V0.5.md` remains independent, still `NOT RUN`.
- Neither proposal is approved MVP scope. The study is not a design spec, not an engineering estimate, and not a feasibility test for PDF/audio ingestion.

## 3. M1 — Flexible Part Practice track (NOT RUN)

1. Find an Android TOEIC source allowing modular practice; record product/source and which Parts are actually accessible.
2. **Listening:** try one legitimate Part 3 or Part 4 set, ~10–15 minutes if available; use ordinary headphones and answer as a normal learner.
3. **Reading:** try a Part 6 or Part 7 passage with relatively long/multiple text blocks, ~10–15 minutes if available.
4. Optional: later sample Parts 1/2/5 and remaining Parts to verify coverage; do not mark all seven validated from only two samples.
5. Fill log after each sample: start delay, completion, context switches, legibility, audio/question coordination, fatigue, interruptions, willingness to repeat, any hard blocker.

**Success signal (not signed-off acceptance threshold):** can finish L and R samples without hard blockers; user says suitable for use again; readable long passage and manageable audio/questions. If negative, document where and why, do not force completion.

## 4. M2 — Continuous Full Mock track (NOT RUN)

1. Check whether an appropriately licensed app/test really provides complete linear 200-question, ~120-minute test; record evidence of coverage, audio, time rules and score reliability limits.
2. **Optional readiness walkthrough 20–30 minutes** only if needed to find specific listening, scrolling, screen, or comfort blockers. VAL-019 documents prior >=30-minute Android use and VAL-020 reports prior full 120-minute mock completion: **do not require repeating these solely to establish basic endurance or that a mock can be finished once**. Any new 20–30-min trial is **not a Full Mock, not an exam score**.
3. **Only if a specific evidence gap remains after retrospective review**, and product access, participant time and comfort permit, voluntarily try **another continuous ~120-minute mock** (not staged as several days). Record actual completion and elapsed time, interruption type/count, lost answers, audio failure, device heat/battery, reading comfort, fatigue, and willingness to repeat.
4. If app interruptions invalidate/mock auto-pauses or scoring is unclear, log exact event and do not treat displayed score as equivalent to ETS official TOEIC.
5. If unable or unwilling to sit continuously, record `NOT RUN`, reason and needed next evidence. This must never be reported as failure of a product that was never built.

**Success signal (not accepted KPI):** VAL-020 already supports that this participant completed one full mock historically; seek evidence about quality (legibility, interruptions, battery, fatigue, repeated-use willingness), not another proof of mere completion. A well-documented future session could add these details if needed. Validity of score and comparison across tests requires separate content/scoring review.

## 5. Measurements — do not mix different environments

| Metric | M1 Part Practice | M2 Full Mock |
|---|---|---|
| app/source & coverage | Part and question count, source | Claimed 200q/120m, source |
| startup latency | Seconds to first question | Seconds to starting full mock |
| completion | Questions/attempted, reasons | Full completed? actual duration |
| L audio coordination | Ease 1–5 and mapping errors | Audio failures/errors  |
| R readability | Ease 1–5 of long passage | Long-session text comfort 1–5 |
| switches/navigation | Count and reasons | Count plus timing impact |
| interruptions | Count and effect | Count, timer/audio/save/score consequences |
| fatigue | Eye/hand fatigue 1–5 | Eye/hand fatigue after long session 1–5 |
| intent to reuse | Yes/no and why | Would repeat continuous mock? |
| score | Only per-Part practice context | Mock estimate only, if quality verified |

Use `NOT RUN`, `NOT AVAILABLE`, `N/A`, `ESTIMATED` as appropriate. Count both positive and negative observations; no invented benchmarks, no % benefit from cross-source PC vs phone data. A Likert scale of 1 = poor/uncomfortable and 5 = very good/comfortable should be consistent.

## 6. Gate / next evidence

- **VAL-019 answer received:** YES, previous TOEIC Android >=30-minute continuous learning/test felt fairly convenient (self-report). This does not validate 120 minutes or 7-Part coverage.
- **VAL-020 next one question:** Has learner #1 ever **completed** a continuous full 200-question/~120-minute TOEIC mock test on Android? Options: completed / started but not completed / never tried. Do not request a new 120-minute trial to answer.
- Mobile-fit results and third-party benchmark cannot prove personal PDF ingest, copyright rights, automated audio mapping, or TOEIC score equivalence.
- VAL-003 file sample and VAL-010 price comparisons remain DEFERRED.
- Product Vision V1.0 APPROVED; Stage 02 IN PROGRESS/HOLD. Stage 03 NOT STARTED. No MVP, PRD/SRS, UX/UI, architecture or code authorized.

## 7. Public references
- ETS L&R format: https://www.ets.org/toeic/about/listening-reading.html
- Android app lifecycle interruptions: https://developer.android.com/guide/components/activities/activity-lifecycle.html

## 8. Evidence note for VAL-019 (added in V0.3)

- RETROSPECTIVE EXPERIENCE: prior Android TOEIC session >=30 minutes and subjectively quite convenient. Date/app/part/exact duration unreported; no assistant-run observation.
- `H-PLATFORM-01M`: moderate qualitative signal for tolerating some sessions >30min; insufficient to prove all Listening and Reading Parts on smartphone.
- `H-PLATFORM-01F`: no established completion of continuous ~120-min full mock. Prior 30min is not a proxy for 120min.
- Both structured M1/M2 tests are still NOT RUN; PC separate baseline also NOT RUN.
- Next: VAL-020 to determine if full mock experience already exists and whether there is an actual gap worth testing.


## 9. VAL-020 revision: reported prior full mock completion (current)

- On 2026-11-21 owner selected **A: completed at least one continuous ~200-question/~120-minute TOEIC L&R full mock on an Android phone**. This is **retrospective self-report**. It supersedes the prior assumption of “no confirmed prior full mock” but does NOT constitute a supervised/no-code structured trial run or verify score quality.
- **Do not ask for a new two-hour mock merely to prove it is possible.** Start with retrospective usability/friction assessment. The existing participant's reported successful completion reduces the feasibility concern for finishing once; it does not close the risks of readability, audio coordination, fatigue, mobile interruptions, persistence, repeat use, fairness of scores or importing personal material.
- **VAL-021 one question:** Which single issue was most inconvenient during the previously completed Android mock? A Reading navigation/long passages; B Listening playback/answering; C eye/hand fatigue or battery/heat; D calls/notifications/other interruptions; E nothing significant; F other (optional detail). If the user chooses E, record positive self-report, then proceed to an outstanding question about personal content ingestion/workflow or pilot cross-user evidence, not an unnecessary extra mobile-UX questionnaire.
- Structured M1/M2 logs remain `NOT RUN`; PC baseline remains `NOT RUN`. Do not fill timestamps, scores or friction ratings from assumptions.
- Project gates remain unchanged; no UI, code, architecture, PRD or MVP authorization.
