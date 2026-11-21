# ECP-00 — Policy & Evidence Contract Review Brief V0.1

**Status:** DOCUMENT-ONLY POLICY REVIEW CANDIDATE; separate `D05-ECP00-008` Product Owner decision **PENDING**.  
**Authority to prepare:** D05-EVIDCP-007=A (plan-only). **No policy signoff or tests are authorized.**  
**Inputs:** exact approved ECP plan V0.1, ARCH03-A/B/C V5.9 still unselected, EV01..12, FM01..18, active CP and signed Requirements/Design Baselines.

## I. What ECP-00 must decide, and what it must never pre-decide

The purpose of ECP-00 is to make *future evidence judgments reproducible*, not to prescribe architecture. This document **separates inherited binding product rules from still-undecided test policies** so no invented clock source or numeric threshold becomes a silent release criterion. ECP-00 is an approval checkpoint for **policy wording and evidence authority**; it is not a device test, QA run, architecture design or implementation protocol.

| Class | What is already fixed | What remains unresolved |
|---|---|---|
| P0 mock | Two B1 forms of 200 items, strict clean/comparable Full Mock, no arbitrary pause/replay, time fidelity | Time authority, reboot/skew/interrupt tolerances, what bounded proof would establish a clean attempt |
| P0 saving | Display `Đã lưu` **only with credible durable ACK** linked to learner/form/attempt/item; missing ACK remains `chưa thể xác nhận` | What later observation/provenance qualifies as durable, source precedence, retry semantics to test |
| P0 privacy | Family learner separation, verified deletion within 7 calendar days, routine retention ≤30 days after pilot absent valid exception | Which in-scope copies/backups are present in the future application, audit evidence and exception handling |
| Content & raw score | B1 inventory and source-rights already affirmed; item-by-item QA still required, no ETS-equivalent score claim | Future QA owners, actual content release artifacts, score-history correction evidence |
| UX/Android | Controlled UI V0.3, UI-G01..16, Reading return and truthful state labels | Target device/version accessibility evidence and test authorizations |
| Decision maturity | EV01..12 DOCUMENT REVIEWED; FM01..18 NOT RUN; same falsifiers for A/B/C | M3/M4 actual evidence must be separately authorized and collected |

## II. Approved plan-level outcome language — NOT runtime implementation

| Review outcome | Allowed only when | Exclusion |
|---|---|---|
| **NOT RUN** | No actual authorized observation performed | Never report as PASS |
| **BLOCKED** | Missing approved policy, permissions, privacy controls, test assets or owner | Never bypass with implied defaults |
| **INCONCLUSIVE** | Future real evidence is conflicting, insufficient or cannot distinguish alternatives | Never convert to clean/comparable or durable-confirmed |
| **FAIL** | Bounded test yields credible signed counterexample under pre-approved criteria | Preserve raw artifact and exceptions |
| **PASS (bounded)** | Actual pre-authorized test within an explicit environment, policy, requirement and QA scope passes | Never generalize across other devices, forms or learners |
| **NOT APPLICABLE (reasoned)** | PO/QA supplies controlled applicability rationale | Never silently remove a required FM or B1 obligation |

**Current state:** EV01..12 `DOCUMENT REVIEWED / NO APP PROOF`; FM01..18 `NOT RUN`; QA-01..08 actual PASS = 0. The table is a **review taxonomy**, not app state machine, data schema or policy signoff.

## III. Proposed future evidence-record contract (neutral of solution)

For each eventual *authorized* observation, the reviewer would need: source ID and provenance, EV/FM linkage, signed requirement and QA checkpoint, actual environment/version, event order, learner/form/attempt/item linkage where appropriate, expected-versus-observed result, timestamp uncertainty (without assuming a clock authority), original artifact reference/hash, independent/correlated-source caveat, owner and PO permissions, verdict + exception/retest, and constraints on generalization.

**No fields above designate implementation schema/API/database.** An architecture A/B/C candidate has the same burden of proof. Multiple copied logs or two mutually dependent indicators do not constitute independent confirmation. A UI screenshot and process-recreated state alone are not durable-write or continuity proof.

## IV. ECP-00 unresolved decision groups and dependencies

See `STAGE05_ECP00_PENDING_POLICY_REGISTER_V0.1.md` for the complete 16-item issue register. The essential policy domains are: authority of elapsed time across reboot and clock manipulation; quantitative tolerances and interruptions; trustworthy durable ACK; treatment of conflicting/late observations; learner/data-copy boundaries and deletion; target Android and accessibility; test approvals and privacy/participant safeguards.

No numeric timeout, grace period, skew, audio tolerance, evaluation weighting, clock precedence, technology, target SDK or service placement is set in this brief. These values must be **PO-approved when justified and before any bounded PASS claim depending on them**. Do not invent figures just to mark a planning row complete.

## V. Mandatory future stop/hold rules (review-level)

1. If timing/audio continuity is not adequately proven, do not certify a clean/comparable Full Mock; do not imply an automatic pause/replay permission.
2. Missing/lost or contradictory durable ACK is `chưa thể xác nhận`, not successful and not necessarily failed; avoid double-submission claims without evidence.
3. Any learner-isolation or deletion-copy uncertainty blocks a privacy PASS; retain the already signed deadlines unchanged.
4. Unverified keys/media/explanations or wrong bank/form association block related content; B1 inventory alone is not item QA.
5. Refuted, inconsistent or missing evidence is never resolved by a weighted total or research preference. ECP-06 comparisons must preserve all candidate-specific blockers.
6. No real device/learner/media test, code/POC, architecture design, spending or ARCH-04 without a **separate explicit PO authorization**.

## VI. Deliverables and decision sequencing

- **Current output (prepared):** this brief + pending-policy register + authorization-boundary matrix + `D05-ECP00-008` owner packet.
- **Next possible PO decision:** sign **ECP-00 evidence-review protocol ONLY**, amend the documents, or HOLD. Signing a process protocol leaves numeric and technical policy choices OPEN.
- **Later separate PO decision(s):** approve exact numeric/source precedence/consent policies as applicable, then approve a specific bounded execution plan if execution is desired. Neither action is triggered automatically by this brief.
- **Architecture decision:** only after evidence is gathered and assessed, in its own PO decision; no candidate choice now.

**Not a gate report.** Stage05 IN PROGRESS; Stage05 Gate NOT HELD; ARCH-04 NOT OPENED.
