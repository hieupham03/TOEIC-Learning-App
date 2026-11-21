# S3 — Acceptance Thresholds, QA Milestones and Pilot Signoff V0.1

**Status:** PROPOSAL; not actual QA evidence or PO-approved metrics.  **Stage03 ≠ software verification stage.**

## 1. Quality acceptance proposed

| Gate ID | Threshold / target **PROPOSED** | Verification when | Gate effect |
|---|---|---|---|
| AC-01 | All MVP critical FR/NFR have mapped AT ID, preconditions, expected result, and future test phase (coverage target **100%**) | Before Stage03 Gate documentation signoff | Requirements completeness, NOT test PASS |
| AC-02 | Both mocks A/B each 200 questions and exact seven-Part distribution; **400 total items** identified | Item manifest QA before pilot | No affected mock released if wrong count |
| AC-03 | **100%** of published Full Mock items have answer-key linkage and required audio/images/passages, version and rights/source trace | Content audit QA-01..06 pre-pilot | Reject incomplete or wrong content |
| AC-04 | **Zero known critical defects** in answer keys, audio mapping, indispensable reading passages and cross-form duplicate/exposed items for evaluative Full Mock | Content signoff QA-01..06 pre-pilot | Release-blocker until fixed/re-audited |
| AC-05 | **Zero known critical** wrong scores, silent confirmed-answer loss, duplicate result, cross-user exposure, or misleading official-score claim in tested build | QA-07/08 on software before pilot | Release-blocker until fixed/regressed |
| AC-06 | On at least **two Android phone sizes/device contexts** supplied for pilot, Part 7 long/multiple passages must be complete, legible and answerable; accessibility/resize checks | After implementation, before pilot | Adjust if long-form Reading unusable |
| AC-07 | QA-01..08 test evidence log distinguishes PASS, FAIL, NOT RUN, BLOCKED, EXCEPTION; no auto-pass based on approved framework | At appropriate QA checkpoints | Auditability |
| AC-08 | Performance SLAs (latency, app stability under varying network, recovery time), device versions and quantitative accessibility thresholds = **TBD BEFORE TEST PLAN BASELINE**; must be explicitly signed later | At test-plan/device selection gate, not as invented Stage03 values | No false precision now |

**Important:** Source-inventory completion **PO-REPORTED**, no item/media/key audit performed here. If mock Part practice would expose test items, the exposure condition in AC-04 is evaluated separately before pilot. Budget work **DEFERRED**, not eliminated from CP-04.

## 2. Four-week 2–5 person pilot measures — proposal

| Indicator | Proposed observation/target | Meaning |
|---|---|---|
| PM-01 | At least **2 participants** complete **both Mock A and Mock B** under declared comparable conditions within 4 weeks | Minimum practical evaluability, **not** a statistical efficacy claim |
| PM-02 | At least **2 participants** use Part practice and independently share a short post-pilot usefulness/usability assessment | Confirms pilot exercises both learning and evaluation use cases |
| PM-03 | For every evaluable attempt, record form/version/date, raw score counts per Part and L/R, answered/unanswered and validity labels | Provides transparent exploratory outcome |
| PM-04 | Track reported critical crashes, confirmed-answer loss, audio/mapping errors and long-Reading readability issues | Quality signal; zero known blocking defects **prior to pilot launch**, issues logged during pilot |
| PM-05 | Compare raw outcomes within caveats, never claim official TOEIC score gain or equated test improvement | Prevents misleading conclusions from forms of uncalibrated difficulty |
| PM-06 | If fewer than two participants complete paired mocks, label the four-week effectiveness comparison **INCONCLUSIVE**, not PASS; document why | Protects interpretation with N=2–5 |

**Why small N:** This is a family usability/feasibility pilot, not a statistical market validation or ETS certification study. Do not require a fixed +100/+200 score change.

## 3. Deferral ledger — what is allowed to remain open at Stage03 Gate?

| Evidence item | Can Stage03 Gate decide with it open? | Must be due by |
|---|---|---|
| Actual mock item-by-item answer/audio/asset QA (QA-01..06) | **Yes, only if PO expressly accepts future evidence gate** | Before pilot content marked ready |
| Real Android lifecycle/scoring/privacy test execution (QA-07..08) | **Yes** (not feasible before build) | Before pilot release |
| Concrete latency SLA and device/version matrix | **Yes if PO approves verification-phase TBD and due date** | Before software test plan signoff |
| Business rules determining comparable attempt, timer, replay, deletion | **No: PO should decide before requirements baseline** | Stage03 business-policy signoff |
| MVP IN/OUT boundaries | **No** | D03-SCOPE-009 formal PO choice |
| Budget estimates and ceilings | **PO explicitly DEFERRED**; carry CP-04, cannot mark budget PASS | Before PO authorizes any spending/operational commitment or release-related gate, as applicable |

## 4. Recommended decision

`S3-A`: approve these *proposed* documentation-coverage and pre-pilot QA controls, and exploratory pilot thresholds. Actual PASS evidence must be produced later. Approving S3 does not approve test execution, budget, MVP lock, PRD/SRS baseline or Gate.

`S3-B`: approve same quality gates but amend minimum paired-completion count, phone coverage, data-deletion timing or acceptance numbers in one set. `S3-HOLD`: do not establish thresholds yet.
