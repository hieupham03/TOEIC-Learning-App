# Stage05 — D05-EVAL-004 Claim-to-Evidence Desk Adjudication V0.1

**Authority:** PO-approved `D05-EVAL-004=A` · **Date:** 2026-11-21 · **Mode:** DOCUMENT ONLY.  
**Scope:** EV-01..EV-12 against signed requirements, ARCH-02 FM01..18 and public official reference E02-01..12; compare competitors without choosing architecture, clock authority, API/backend/DB/framework or running tests.

## Evaluation method and outcome legend

For each EV: (1) isolate exact claim; (2) cite what official docs or signed requirements actually support; (3) explicitly identify missing proof; (4) challenge all materially distinct model families; (5) state conservative business interpretation and later falsifier/owner. **No numeric scoring or technology winner.**

- **`DOCUMENT CLAIM SUPPORTED`** means the *risk/platform/requirement statement* has documentary support, not the app behavior.
- **`RUNTIME CLAIM NOT VERIFIED`** means no actual implementation has been tested or observational proof collected. Applies to all 12 cases.
- **`CONFLICT NOT OBSERVED IN APP`** means the ambiguity is a documented hypothetical, not a defect found by testing.
- **`EVIDENCE OBLIGATION SPECIFIED`** means the future evidence needed is described, not captured. Applies to all 12 claims.

**Decision result:** **12/12 documentary claim reviews completed**; **0/12 actual app-level claims validated**, **0 tests executed**, **0 architectures or technologies selected**. This is **not 12 PASS results**.

## Individual adjudication
### EV-01 — Full Mock duration survives clock change

| Field | Desk finding |
|---|---|
| Signed acceptance guard | FR-011/019; NFR-004; AT-11/19; S2-A |
| Supporting document/source | E02-03 Android SystemClock; signed Full Mock time policy |
| **Evidence gap** | A wall clock may change; elapsedRealtime since boot does not prove reboot continuity. No observed production timeline. |
| Alternative challenge | T-A device-contained must show tamper/reboot continuity; T-B independent needs outage proof; T-C reconciliation must resolve contradictory evidence without silently granting time. |
| Truthful treatment while unresolved | If elapsed cannot be demonstrated, do NOT label attempt clean/comparable; decide invalid/unknown only per approved policy and later thresholds. |
| Falsification cases | FM-04; FM-03 |
| Evidence owner/checkpoint | Future implementation/Android QA; PO later signs numeric tolerance |
| Evaluation status | **EVIDENCE OBLIGATION SPECIFIED; RUNTIME CLAIM NOT VERIFIED** |

### EV-02 — App restoration proves continuous clean mock

| Field | Desk finding |
|---|---|
| Signed acceptance guard | FR-011/019; AT-11/19; QA-08 |
| Supporting document/source | E02-01 Android lifecycle; E02-02 saved UI state |
| **Evidence gap** | UI appearance may be restored after process death but critical elapsed/audio/ack evidence may not survive. No app test. |
| Alternative challenge | T-A must independently justify survival; T-B must reconcile downtime when disconnected; T-C must not assume restored screen validates attempt. |
| Truthful treatment while unresolved | Restored UI does not automatically mean clean mock. Status remains explicit until required evidence exists. |
| Falsification cases | FM-01,02 |
| Evidence owner/checkpoint | Future real Android process-death QA before pilot |
| Evaluation status | **EVIDENCE OBLIGATION SPECIFIED; RUNTIME CLAIM NOT VERIFIED** |

### EV-03 — Rebooted mock retained trustworthy time

| Field | Desk finding |
|---|---|
| Signed acceptance guard | FR-011/019; NFR-004; AT-11 |
| Supporting document/source | E02-03 SystemClock since boot |
| **Evidence gap** | Clock measured since boot reinitializes across boot; no verified chain covering reboot or elapsed downtime. |
| Alternative challenge | T-A/T-B/T-C each need a rebuttable explanation of missing interval; external corroboration alone may be unavailable. |
| Truthful treatment while unresolved | No automatic time reset or clean flag on reboot; preserve unknown/noncomparable handling per signed rules. |
| Falsification cases | FM-03 |
| Evidence owner/checkpoint | Future Android QA + PO numeric policy checkpoint |
| Evaluation status | **EVIDENCE OBLIGATION SPECIFIED; RUNTIME CLAIM NOT VERIFIED** |

### EV-04 — Listening audio was delivered without improper replay

| Field | Desk finding |
|---|---|
| Signed acceptance guard | FR-003/010/011; QA-03/08; P04 |
| Supporting document/source | E02-04 Android audio focus; E02-05 background playback; E02-06 Android17 conditional rules |
| **Evidence gap** | OS version/target-dependent focus changes; playback position and interruption duration have not been observed. |
| Alternative challenge | L-A foreground-bounded may mark more attempts noncomparable; L-B evidence-driven recovery can introduce replay advantage. Both are untested. |
| Truthful treatment while unresolved | Do not claim audio intact, clean, or automatically resumable without evidence; never permit arbitrary clean-mock replay. |
| Falsification cases | FM-01,05,18 |
| Evidence owner/checkpoint | Later target-version review + Android audio QA |
| Evaluation status | **EVIDENCE OBLIGATION SPECIFIED; RUNTIME CLAIM NOT VERIFIED** |

### EV-05 — Selected answer already durably saved

| Field | Desk finding |
|---|---|
| Signed acceptance guard | FR-005/019; AT-05/19; W-03A |
| Supporting document/source | E02-02 UI state vs persistent state; signed truthful-ACK policy |
| **Evidence gap** | A UI selection or restored selection proves neither durable persistence nor identity/form association. |
| Alternative challenge | S-A local, S-B independent, S-C explicit tiers each must demonstrate their own durable event, not a presumed topology. |
| Truthful treatment while unresolved | Display pending or unconfirmed until the required evidence is available; do not show saved. |
| Falsification cases | FM-07 |
| Evidence owner/checkpoint | Later durable-answer implementation QA |
| Evaluation status | **EVIDENCE OBLIGATION SPECIFIED; RUNTIME CLAIM NOT VERIFIED** |

### EV-06 — Lost ACK establishes failed write or safe retry

| Field | Desk finding |
|---|---|
| Signed acceptance guard | FR-005/019; AT-05/19; QA-08 |
| Supporting document/source | Signed policy, E02-02 lifecycle; no public source proves this app write result |
| **Evidence gap** | Acknowledgement may be lost after success; absence of ACK is ambiguous, not proven success or failure. Duplicate attempts untested. |
| Alternative challenge | S-A/B/C each must show how it distinguishes deduplication, late acknowledgement and user/form attribution. |
| Truthful treatment while unresolved | Use cannot-confirm/pending until reconciled; do not double count submission; do not falsely claim definite failure. |
| Falsification cases | FM-08,14 |
| Evidence owner/checkpoint | Future persistence/integrity QA before pilot |
| Evaluation status | **EVIDENCE OBLIGATION SPECIFIED; RUNTIME CLAIM NOT VERIFIED** |

### EV-07 — Shared-phone learner data is isolated

| Field | Desk finding |
|---|---|
| Signed acceptance guard | FR-018; NFR-006; AT-18 |
| Supporting document/source | E02-07/08 OWASP security controls; signed privacy policy |
| **Evidence gap** | No defined or tested identity boundary, no access-control negative test, no user switching evidence. |
| Alternative challenge | P-A device-scoped shared-phone assumptions challenged; P-B learner authorization challenged by availability; P-C by coordination and consent. |
| Truthful treatment while unresolved | Treat isolation as an acceptance obligation, not a verified security property; never show another learner data. |
| Falsification cases | FM-09 |
| Evidence owner/checkpoint | Future privacy/security QA before pilot |
| Evaluation status | **EVIDENCE OBLIGATION SPECIFIED; RUNTIME CLAIM NOT VERIFIED** |

### EV-08 — Verified deletion completed across all copies

| Field | Desk finding |
|---|---|
| Signed acceptance guard | FR-018; NFR-006; BR-08 |
| Supporting document/source | Signed ≤7-calendar-day request requirement; E02-09/10 Google Play policy conditional on account/distribution |
| **Evidence gap** | Actual learner identity/account lifecycle, copies, backups, exception mapping and deletion audit unavailable. |
| Alternative challenge | P-A/P-B/P-C must all account for every in-scope copy and justified exception; no authorization of a data topology. |
| Truthful treatment while unresolved | Do not mark a request completed without supported completion evidence; respect signed 7-day bound and 30-day post-pilot retention. |
| Falsification cases | FM-10,11 |
| Evidence owner/checkpoint | Later privacy SOP / before-pilot and post-pilot verification |
| Evaluation status | **EVIDENCE OBLIGATION SPECIFIED; RUNTIME CLAIM NOT VERIFIED** |

### EV-09 — Released mock content meets QA

| Field | Desk finding |
|---|---|
| Signed acceptance guard | FR-003/010/015..017; B1; QA-01..06 |
| Supporting document/source | PO reported two forms inventoried; official ETS format E02-11/12 |
| **Evidence gap** | 400-item inventory is attested, but key/audio/asset/rights per-item release audit has not been executed. |
| Alternative challenge | C-A frozen release, C-B revisions and C-C release/amendment must all demonstrate media/key QA before use. |
| Truthful treatment while unresolved | Not QA ready = cannot release to pilot; inventory is not QA PASS. |
| Falsification cases | FM-06,12,16 |
| Evidence owner/checkpoint | Content curator and QA01..06 before pilot release |
| Evaluation status | **EVIDENCE OBLIGATION SPECIFIED; RUNTIME CLAIM NOT VERIFIED** |

### EV-10 — Historic raw score remains truthful after correction

| Field | Desk finding |
|---|---|
| Signed acceptance guard | FR-008/012/013/017; QA-07; R2 |
| Supporting document/source | Signed raw-score rule, ETS E02-11/12 format/score caution |
| **Evidence gap** | No actual score history, correction process or duplicate submission behavior evaluated. |
| Alternative challenge | R-A original attempt version vs R-B amended interpretation must preserve old meaning, context and no implicit ETS equating. |
| Truthful treatment while unresolved | Never silently overwrite historical attempt or present raw delta as proven proficiency gain. |
| Falsification cases | FM-12,14,17 |
| Evidence owner/checkpoint | Future scoring and content-change QA |
| Evaluation status | **EVIDENCE OBLIGATION SPECIFIED; RUNTIME CLAIM NOT VERIFIED** |

### EV-11 — Part practice independent from both Full Mocks

| Field | Desk finding |
|---|---|
| Signed acceptance guard | B1; FR-002/010/015; QA-05 |
| Supporting document/source | PO-confirmed two mock inventories; approved distinct practice-bank obligation |
| **Evidence gap** | No item-to-item or media overlap check conducted for two forms and practice pool. |
| Alternative challenge | C-A/B/C require reproducible comparison and release provenance; neither model has real content verification. |
| Truthful treatment while unresolved | Keep separate pool only as a requirement; block content release if leakage cannot be excluded by QA. |
| Falsification cases | FM-13 |
| Evidence owner/checkpoint | Content curator QA-05 before pilot release |
| Evaluation status | **EVIDENCE OBLIGATION SPECIFIED; RUNTIME CLAIM NOT VERIFIED** |

### EV-12 — Reading anchor preserved after background/text-size changes

| Field | Desk finding |
|---|---|
| Signed acceptance guard | FR-004/019; NFR-005/010; Design-Spec V0.3; QA-08 |
| Supporting document/source | Signed UX W-02A priority; E02-01/02 process and state restrictions |
| **Evidence gap** | Static prototype context-return is not Android measured persistence, rendering or accessibility behavior. |
| Alternative challenge | All models must satisfy device/user test of long passage and text size; does not choose toolkit. |
| Truthful treatment while unresolved | Maintain open usability/device verification; do not claim successful restoration. |
| Falsification cases | FM-15 |
| Evidence owner/checkpoint | Later >=2 Android contexts and accessibility QA before pilot |
| Evaluation status | **EVIDENCE OBLIGATION SPECIFIED; RUNTIME CLAIM NOT VERIFIED** |


## What was and was not learned

- Direct official Android references support platform lifecycle, time-since-boot and audio focus *constraints*; they never certify this app's continuity, user experience or saved state.
- Signed business policy is strong **normative evidence**, not empirical feasibility proof.
- Every EV can be falsified by named later FM cases; coverage of an FM label does not mean the test was run.
- A late or lost ACK is **genuine uncertainty** about a write outcome, not evidence that the write definitely failed. Equally, a restored UI is not evidence of a clean timed attempt.
- Any later architectural option must be reviewed against this ledger without silently downgrading alternatives, privacy, content QA or budget controls.
