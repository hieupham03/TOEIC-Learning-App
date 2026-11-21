# Stage05 ARCH-02 — Full Mock Time, Audio & Integrity: Comparative Models V0.1

**Authority:** D05-ARCH-002=A. **Type:** document-only *conceptual evidence models*. NOT technical architecture, algorithm, technology, server/API design or implementation approval.

## A. Locked Full Mock rules — not options

- **Two independently inventoried Full Mock A/B**, 200 questions each (100 Listening ~45 minutes in ordered Parts 1–4 and 100 Reading 75 minutes in Parts 5–7); practice content must remain separate.
- Under signed S2-A/P01..P09, a comparable Mock provides no user-discretionary pause/replay; time cannot silently reset or be extended on reconnect; attempts affected by integrity violations are labeled **non-comparable**, not secretly classed valid.
- Answer acknowledgement and attempt integrity are separate claims. Scoring is raw and descriptive; no automatic ETS-equivalent official scaled score.
- Technical thresholds/tolerance/grace, real clock and media reliability still **TBD at software test-plan signoff**, not chosen here.

## B. Compare time-integrity evidence models (not selection)

| Model | Basic evidence hypothesis | Strength in a mock | Main failure / trade-off | Falsifiable later tests | Finding |
|---|---|---|---|---|---|
| **T-A Device-contained elapsed evidence** | App relies on measured elapsed intervals and continuity information available on the device; declares unknown/invalid when continuity is unprovable | Minimizes dependency on continuous connectivity, suits online-first but intermittent network | App termination, device reboot, clock changes/tampering, cross-session continuity uncertain; must not imply tamper-proof validity | sleep/wake; background/reclaim; reboot; wall-clock edit; connectivity loss; compare displayed and stored elapsed duration | **Plausible conditional concept; integrity proof not established** |
| **T-B Independently corroborated chronology** | Some independent observation corroborates elapsed progress and final status; app does not mark clean without sufficient evidence | May strengthen detection of altered/missing device evidence | Network outage, timing latency, privacy/external dependence, unknown continuity gap; may make attempts noncomparable often | no connection mid-Listening; delayed/duplicated observations; interrupted return; contradictory time evidence | **Plausible conditional concept; availability and access unknown** |
| **T-C Reconciled evidence from multiple sources** | Two or more independently reasoned signals are reconciled, with explicit uncertainty precedence; cannot create bonus time or replay rights | Can preserve auditability while detecting inconsistencies | More failure states, complexity, conflict resolution needs explicit policy; no guarantee of continuity | conflicting clocks; device reboot during Reading; message order changes; deterministic noncomparable classification | **Candidate for deeper study, NOT recommended as selected architecture** |

**Source:** E02-01, E02-02, E02-03. Android `elapsedRealtime` counts time since boot incl. sleep; this fact does **not** establish a trustworthy anti-cheat time source or persistence after reboot.

## C. Compare Listening interruption evidence models

| Model | Concept | Pros | Failure/risk | Required proof before pilot |
|---|---|---|---|---|
| **L-A Foreground-bounded evaluative audio** | A clean Mock is evidenced only in an interaction state whose audio continuity is demonstrable; interrupted conditions get clear classification | Conservative and simpler integrity rule | More failed/noncomparable attempts from calls/background; UX must explain, not imply resume as clean | incoming call, loss of audio focus, Bluetooth switch, app switch, media load error |
| **L-B Recovery-with-explicit-validity evidence** | Resume flow can preserve acknowledged answers while separately deciding whether evaluation integrity is provable | Can improve learner continuity without silently waiving validity | Danger of replay/time advantage if state proof is inadequate; no voluntary pause/replay | stop/resume after network loss, process death, speaker disconnect, missing audio |

**Important:** Either model must obey signed no-voluntary-pause/replay rules. No authorization to add a replay control in clean Full Mock. E02-04/05/06 show platform audio focus and background restrictions; target/API/OS applicability must be checked later, NOT a technology commitment.

## D. Attempt state distinction — shared invariants

1. `NOT STARTED`: not a timed attempt.
2. `IN PROGRESS`: running with only known evidence; not an assertion of final comparability.
3. `COMPLETED, INTEGRITY SUPPORTED`: all required sections and evidence pass later agreed tests.
4. `INCOMPLETE`: explicit termination/timeout; raw answer history may be retained according to policy, no clean performance comparison.
5. `NONCOMPARABLE`: continuity/replay/clock/media evidence missing or violated; clear user-facing reason.
6. `UNKNOWN / NEEDS REVIEW`: do **not** silently normalize to a comparable attempt; later retention/recovery details require signed test policy.

**Source of truth caveat:** These are conceptual semantic states to compare with FR/AT, not a database enumeration, API contract or new user policy. Existing signed wording prevails.

## E. Red-team scenarios and guards

| Scenario | Baseline guard | Still unknown |
|---|---|---|
| App backgrounded while Listening audio playing | No automatic clean classification without ordered-audio evidence | Feasibility under target Android restrictions |
| Process killed and restored during Reading | Never reset time; preserve previously confirmed answers | Authoritative elapsed proof across process loss |
| Phone rebooted at minute 90 | Do not silently grant time or treat uncertain continuation as clean | Clock continuity, signed retry/grace tolerance |
| Audio lost for 20 seconds | No automatic replay of evaluated audio; explicitly report integrity impact | Exact audio-loss tolerance before QA |
| User changes wall clock | No silent change to allowed duration | Anti-tamper evidence and noncomparable classification |
| Same form restarted / result duplicated | Distinct attempt identity and truthful status; historical raw results not overwritten | Later deduplication mechanism and test evidence |

## F. Interim feasibility judgement

- **Document-level feasibility:** all three time-evidence model families can *describe* the locked behavior; NONE has demonstrated ability to meet all exceptional cases.
- **Blockers to a final technical choice:** agreed numeric time/audio thresholds, Android target environments, fault-injection test evidence and a PO-controlled choice of evidence responsibility.
- **Next decision:** `D05-TECH-003` chooses a *research candidate priority* only. Any definitive clock authority/architecture requires subsequent explicit PO approval.
