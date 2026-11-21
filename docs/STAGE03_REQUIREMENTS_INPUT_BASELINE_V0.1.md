# TOEIC Learning App — WP-01 Requirements Input Baseline V0.1

**Date:** 2026-11-21  
**State:** WP-01 **COMPLETED AS ANALYST INPUT DRAFT**. Not approved PRD, SRS or MVP.  
**Authority:** Product Vision V1.0 approved; Stage 02 Gate CONDITIONAL PASS with CP-01..05.  
**Process:** Evidence-First; no compulsory stepwise experiments unless a decision-critical fact cannot be determined otherwise.

## 1. Product charter that is already binding

- **Target:** Vietnamese TOEIC learners; Android smartphone, online-first, Listening & Reading in initial product direction. iOS, offline, Speaking/Writing deferred as vision horizon, not presumed MVP.
- **Pilot:** 2–5 family learners, 4 weeks. Pilot is for feasibility, usability, habit and directional progress signals; it is **not** a guarantee to raise a TOEIC score by 100–200 points within 4 weeks.
- **Known learner 01:** self-reported full mock ~550, target 650–750. **Known learner 02:** officially tested ~650, target 750–850. The bases are not directly equivalent. Learner 02 difficulties are secondhand.
- **Core objective:** help each learner choose appropriate activities, understand errors, study with irregular free time, and follow progress. Comparative full mock results are a preferred progress indicator **only if forms are defensibly comparable**.
- **Operating constraints:** near-zero recurring cost for 2–5-person pilot desired, not yet cost-proved; user can acquire modest legitimately licensed content; build-time flexible; PO approves scope; later Codex coding only with explicit authorization.
- **Product boundary:** nothing in this baseline authorizes technologies, interfaces, data pipelines, AI features, a specific MVP, or publishing third-party content.

## 2. Stakeholders and actors

| Actor | Role, needs | Evidence |
|---|---|---|
| L01 — learner/PO | Practice L&R, microlearning, irregular schedule, owned materials, goal 650–750 | Direct PO reports VAL-001/004/013/016–024 |
| L02 — second pilot learner | Goal 750–850; perceived similar difficulties; specific workflow not independently verified | PO secondhand VAL-011; do not assume identical materials |
| Pilot content curator (could be PO) | Make available licensed/original content, check audio-answer match and corrections, control rights | Process requirement from CP-03/04, NOT proof capacity exists |
| Future public learner | Affordable self-guided TOEIC preparation | Product Vision aspiration, broad-market evidence insufficient |

## 3. Jobs-to-be-done and problem statements

| JTBD | Evidence type / state | Desired outcome / candidate requirement |
|---|---|---|
| J-01: I want to practice a TOEIC question with matching audio, answers and explanation without multiple tabs | PO direct report; problem confirmed | One coherent L&R practice workflow; support audio/answer synchronization and error review |
| J-02: I want to study in whatever time I have, from one question to a short Part session | PO direct report; outcome requested | Learner chooses duration or content; recommend appropriately sized activity, no forced fixed schedule |
| J-03: I want to assess current level and track areas to improve | Approved Vision + PO tests | Baseline, Part-level error analytics and credible assessment labels; no fabricated official-equivalent 990 scale |
| J-04: I want to use books/PDF/audio I own in a convenient study workflow | PO direct report; source readiness self-reported | Rights-aware personal content journey; ingestion automation NOT validated; manual/controlled source fallback |
| J-05: I want learning to continue after mistakes, with understandable explanations | Approved Vision; learning research supports principles | Error logging, feedback, active recall / spaced review as candidates; no guarantee of score gain |
| J-06: I want a quick word on my phone and direct control of reminders | PO VAL-005–009 | Optional interactive notification concept; permission, silence/vibrate/sound, hide-word/disable-all/postpone; 4 desired actions vs max 3 direct buttons; not default MVP |
| J-07: I want full L&R mock tests on Android and flexible practice across 7 Parts | PO VAL-017–020; one successful phone mock is retrospective self-report | Explore Part practice + Full Mock options; Reading-long-form eye strain/scrolling are actual reported pains |

## 4. Evidence-grade mapping

| Grade | Definition | Examples | Scope of confidence |
|---|---|---|---|
| O — official | ETS/Android/Google Play authoritative standards/policies | ETS 200 items and 45m+75m, Play IP rules | High for published rule, not for our implementation |
| P — product-public | Provider's own capability claims | STUDY4 Part/full test and review; Migii roadmap | Proves capability is advertised, not independently audited effectiveness |
| D — direct user | Firsthand PO report and aspirations | fragmented desktop flow, smartphone 120m mock completed, Reading eyestrain | Strong for this learner's needs, weak for whole market |
| I — indirect | PO report about another learner | Learner 02 'same difficulties' | Hypothesis only; ask during future pilot naturally |
| U — unknown | Not yet tested/source missing | rights, PDF/audio automation accuracy, comparable 2 test forms, AI cost/quality | No assertion permitted |

## 5. Business outcomes and preliminary metrics (proposals, not targets approved)

| Outcome | Candidate observable signal | Caveat |
|---|---|---|
| Lower study friction | Start a session without context switching; number of completed short sessions | No actual speed reduction has been measured |
| Build sustainable usage | Sessions per active pilot user / weekly continuation / self-selected return | Small pilot descriptive only |
| Close skill gaps | Error patterns per Part, answered-with-explanation records, revisit performance | Do not infer causality or TOEIC score gains automatically |
| Credible progress | Correct answers and comparable diagnostic/full mock test results where valid | Official TOEIC-equivalent score only with validated methodology/licensing |
| Control content risk | Every used item has rights/provenance and answer-audio QA; rights gaps blocked | Ownership of a personal PDF does not prove right to share/cloud-process |
| Near-zero ongoing cost | Pilot monthly recurring expense tracked and capped before execution | Numerical cap is PO decision later |

## 6. Requirements input catalog (not approved feature inventory)

- **CAP-01 Content supply:** legal question/audio/answer/explanation source, provenance and controlled fallback; explicit rights for local/private/cloud/shared/public uses.
- **CAP-02 Practice:** Listening and Reading sessions; audio, content, answer, review, question error correction; Part completeness to be decided.
- **CAP-03 Assessment:** baseline and mock with transparent score semantics and no unwarranted ETS-equivalent claims.
- **CAP-04 Learning history:** errors, attempts, per-Part weaknesses, opportunity to review.
- **CAP-05 Recommendation:** activity choices by time availability/goal/weakness; start with rules if AI not justified.
- **CAP-06 Quick learning:** one question/word; richer notifications optional, requires opt-in and user controls.
- **CAP-07 Content ingestion:** manual curation is candidate; automatic PDF/audio importer is deferred until representative file/quality/rights feasibility.
- **CAP-08 Safety/quality/operations:** user data safeguards, app resilience, interruption handling, Android long-reading usability, content corrections, OPEX ceiling.

## 7. Mandatory dependency gates carried from CP-01..CP-05

| Gate | What must be specified in Requirements | When evidence must exist |
|---|---|---|
| Rights | Intended personal/cloud/family/public uses; fallback original/licensed | Before acting on or distributing content beyond rights |
| Content supply | Minimum QA-ed items per Part/test, audio/answer references | Before PO commits specific scope and before pilot |
| Ingestion | Supported input/quality, human review, error handling, or out-of-scope | Before import automation is promised |
| Score semantics | %correct vs internal diagnostics vs validated comparable full mocks | Before progress claims or calibrated 990 labels |
| AI | Eval set, human oversight, hallucination controls, fallback, spend cap | Before AI is used with learners |
| Android long-form | Long Reading comprehension usability, fatigue, continuity, interruptions | Prior to UX acceptance / pilot |
| Privacy + OPEX | User consent, retention/deletion approach, cost measurement and limits | Prior to pilot or user data processing as applicable |

## 8. Deliberate non-goals at this point

No MVP approval, no feature timeline, no PRD/SRS baseline, no mock implementation, no UX wireframe, no tech stack, no backend/data schema, no code. Do not ask user to re-run Listening/Reading desktop baselines merely to proceed. No invented pricing estimates or raw materials permissions.

## 9. Handoff

WP-01 is complete as an **analyst-prepared input baseline**. WP-02 options ready for PO decision; scope selection must precede WP-03 PRD/SRS drafting. Reference `STAGE03_BUSINESS_USER_JOURNEYS_V0.1.md`, `STAGE03_MVP_OPTIONS_AND_TRADEOFFS_V0.1.md` and `STAGE03_REQUIREMENTS_EVIDENCE_TRACEABILITY_V0.1.md`.

### Source ledger

- ETS Listening & Reading official: https://www.ets.org/toeic/about/listening-reading.html
- STUDY4 official feature description (2026): https://study4.com/posts/4447/
- Migii TOEIC product: https://migii.net/vi/toeic
- Google Play Intellectual Property: https://support.google.com/googleplay/android-developer/answer/18265346?hl=en
- Academic spacing/feedback/retrieval article: https://pmc.ncbi.nlm.nih.gov/articles/PMC8638698/
- Approved internal evidence: `PRODUCT_VISION_V1.0.md`, `STAGE02_EVIDENCE_SOURCE_LEDGER_V1.0.md`, `STAGE02_GATE_DECISION_RECORD_V1.0.md`.
