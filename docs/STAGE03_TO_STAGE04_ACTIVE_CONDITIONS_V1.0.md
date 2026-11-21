# Stage 03 → Future Stages — Activated Condition Register V1.0

**Status:** **ACTIVE**, via **D03-GATE-011 = CONDITIONAL PASS** approved 2026-11-21.  
**Scope:** seven new `G03-CP` conditions **plus** five continuing `Stage02 CP` obligations.  
**Budget:** DEFERRED BY PO — no budget tasks reopened by this register.  
**Evidence level:** controls and planned checks only; actual downstream test results are NOT yet available.

## A. Seven Stage 03 Gate conditions (approved in exact terms)

| ID | Binding obligation | Due / enforcement checkpoint | Evidence status now | Role / proposed owner |
|---|---|---|---|---|
| **G03-CP01** | **Separate PO approval before opening Stage04**; Gate does not allow design, architecture or code | Before any Stage04 UX activity | Stage04 kickoff PENDING | PO / project lead |
| **G03-CP02** | B1 Mock A/B each 200 items; distinct practice bank; QA-01..06 covering source/rights, assets/keys/audio/passage accuracy, duplicates, versions; 100% critical assets and no known critical defects | Before pilot content release | Two inventories PO-confirmed; QA execution NOT VERIFIED | Content QA owner + PO |
| **G03-CP03** | QA-07..08 + AT for scoring, timer, integrity, answer persistence/recovery, learner privacy and long Reading on ≥2 Android contexts; no known critical failures | Before pilot app release | NOT RUN | Future test lead + PO |
| **G03-CP04** | Define numeric performance/recovery tolerances before test-plan baseline; verified identity/deletion/exception SOP and content-key correction workflow before relevant use; preserve S2 policies | Before test-plan baseline / relevant pilot operations | TBD with future checkpoint; 7d deletion & 30d retention business policies already approved | Future test/data owners + PO |
| **G03-CP05** | Honor PO budget deferral; require **separate permission** before spending or budget-dependent commitment/release | Before expense/financial authorization | **DEFERRED BY PO**, not waived | PO |
| **G03-CP06** | Change-control PRD/SRS/Acceptance and business MVP; no silent AI, automatic PDF import, advanced notifications, ETS-equivalent score claims or removal of B1 | Any material proposed change | **ACTIVE now** | PO / requirements owner |
| **G03-CP07** | Evaluate four-week pilot 2–5 learners; target ≥2 learners with valid both-Mock A/B and ≥2 giving Part-practice feedback; report limits of form comparison and no official score-gain claims | Pilot review | NOT RUN | Future pilot evaluator + PO |

These are actively binding *requirements for future work*, not evidence that downstream steps have already passed. Stage 04 may clarify experience-level failure states **without overriding** approved mock/data policies.

## B. Existing Stage 02 conditions continue unchanged

| ID | Continued meaning | Relevant downstream control |
|---|---|---|
| **CP-01** | Requirements analysis alone never implicitly authorized MVP/PRD/SRS/UI/architecture/code; explicit approvals needed | Existing D03 scope and baseline signed; Stage04 still needs separate kickoff |
| **CP-02** | AI, auto PDF/audio ingestion, 990-equivalence, advanced notification and full-mode commitments only by explicit evidence/PO approval | Current MVP OUT and baseline change-control |
| **CP-03** | Content provenance/license for each used source and asset; rights-appropriate storage/distribution | Content QA and release rights audit; PO rights attestation recorded |
| **CP-04** | Quantified future quality gates for audio-key mapping, content, scoring, AI if later enabled, mobile Reading and OPEX | QA/test-plan gates; budget-related planning DEFERRED by PO |
| **CP-05** | Old manual validation baselines remain optional; deferred files/competitor price checks not fabricated completed | No new mandatory personal experiments or stale blockers |

## C. Conditions specifically relevant to *future* Stage04 UX/UI

The Stage04 proposal must capture user journeys and failure-state UX for: 200-question Full Mock ordered Listening/Reading and no voluntary pause/replay for clean attempts; explicit non-comparable attempts; separate Part practice and one-item microlearning; answer-save pending vs confirmed state; network/audio failure, resume/recovery, result/score caveats, privacy/data deletion requests, and long Reading legibility. It must **not** claim these flows/wireframes exist now.

**Stage04 design approval would NOT** close `G03-CP02..04` or `G03-CP07`. Actual content/device QA and pilot evidence remain due at their separate checkpoints. No technical architecture selection is part of this handoff.
