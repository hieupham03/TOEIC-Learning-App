# Stage05 ARCH-02 — Failure Modes, Required Evidence and Gate Owners V0.1

**Scope:** falsifiable test *definitions only*; NOT executed cases, no QA PASS. Maintains ARCH01 EG-01..16 and CW-01..10 without closing them.

| Case | Failure injection / question | Non-negotiable invariant | Proof to collect later | Relevant refs | Due |
|---|---|---|---|---|---|
| FM-01 | Switch app during clean Listening | No arbitrary replay/pause or silently clean pass | Logged timeline + actual audio state, attempt validity | AD01/02, CW01, AT11, QA08 | Before pilot |
| FM-02 | Process reclaimed at minute ~80 | Time not reset, ACKed answers not lost | Restart state, elapsed evidence, answer comparisons | AD01/03/04, EG02/04 | Before pilot |
| FM-03 | Reboot mid-Reading | Uncertain time is not labeled clean | Startup / contradiction reason evidence | AD01/04, EG02 | Before pilot |
| FM-04 | Change system clock during attempt | No advantage or hidden duration extension | Independent clock-change negative case | AD01, CW01 | Before pilot |
| FM-05 | Audio focus lost to phone call | No unacknowledged Listening replay | Media state + attempt integrity reason | AD02, EG03, QA03/08 | Before pilot |
| FM-06 | Media missing / wrong question clip | Form not incorrectly released or scored | Asset version and QA exception, blocked release | AD07, EG01/03 | Before content release |
| FM-07 | Select choice while disconnected | Do not claim confirmed save without durable proof | Pending / unknown / ACK state logs, saved answer audit | AD03, CW02/07, AT05 | Before pilot |
| FM-08 | Lose confirmation response after successful write | Retry must not double-count or falsely deny durable state | Duplicate retry + out-of-order outcome traces | AD03/04, EG04 | Before pilot |
| FM-09 | Switch family learner on shared phone | No cross-learner access including pending answers | Negative isolation tests with 2+ learner contexts | AD05, EG05, AT18 | Before pilot |
| FM-10 | Delete verified learner data | Request completed ≤7 calendar days with proof, exceptions logged | Request and completion times, copy inventory | AD06, EG05, AT18 | Before pilot use |
| FM-11 | Revisit data after pilot +30 days | Ordinary expired data not retained without authorized exception | Retention/deletion verification | AD06, EG05 | After pilot |
| FM-12 | Wrong key found on a released item | Prior result not silently overwritten | Old/new key and form versions; correction audit | AD09, CW09, QA02/07 | Before pilot and on corrections |
| FM-13 | Part practice reveals A/B mock item | Separate bank and no unintended exposure | Duplicate/overlap checks and release manifest | AD08, EG06, QA05 | Before pilot content release |
| FM-14 | Same submission repeated twice | One logical result per intended attempt | Deduplication behavior + result audit | AD09, EG07, QA07 | Before pilot |
| FM-15 | Long Reading + large text + app background | Context anchor stable, passages untruncated | Actual ≥2 Android contexts, accessibility results | AD10/13, EG08/09 | Before pilot |
| FM-16 | Explanations not QA-ready | Do not display “verified explanation” or unavailable content as if released | Release gate / negative case | AD07/11, EG12 | Before pilot |
| FM-17 | Two mock scores have differing raw totals | Do not imply ETS scaling/equating or proven proficiency gain | Comparison text and noncomparable-attempt test | AD09/12, CW06 | Before pilot |
| FM-18 | Selected target Android changes background media rules | Platform applicability rechecked, no untested clean playback claim | Target-level docs and real-device evidence | AD02/04, EG03 | Target/platform review |

## Evidence owner boundary

- **ARCH-02 analyst:** descriptions, official platform fact citations, alternatives and recommended verification order ONLY.
- **Future content curator + QA-01..06:** item/key/media/provenance/duplicate QA and release manifest.
- **Future implementation/QA owner:** runtime timing, persistence, privacy, scoring, Android/device and performance tests; cannot backdate evidence.
- **PO:** policy exceptions, thresholds at checkpoint, budget reopening (if ever), architectural selection and Gate decisions.

**Severity:** P0 means pilot-blocking **if unmet**, not a currently proven defect. No test can be marked PASSED because this case matrix exists.
