# Stage05 — Technical Evaluation Brief: Evidence Reconciliation First V0.1

**Project:** TOEIC Learning App — Stage05  
**Authority:** `D05-TECH-003=A` (research emphasis + preparation of this brief ONLY)  
**Status:** **BRIEF READY FOR PRODUCT OWNER REVIEW — NOT AN EXECUTED EVALUATION**  
**Date:** 2026-11-21  
**Decision boundary:** No ARCH-03, technical architecture, clock authority, backend/API/database/framework, code/POC, device testing or spending.

## 1. What question this evaluation must eventually answer

**Decision question (future, NOT decided):** What minimum **evidence obligations**, contradiction/unknown handling, and later falsifiable tests would allow a technical candidate to truthfully satisfy the *already-signed* Full Mock integrity and durable answer/learner-data requirements **without inventing a successful confirmation, clock continuity or privacy proof**?

Evidence Reconciliation First is the **review ordering**: evaluate how proposals would deal with contradictory, absent or delayed evidence before optimizing convenience. **It is not a selection of a multi-source technology topology.** If a simpler model later proves compliance, it remains eligible. Retain device-contained and independent corroboration as **equal eligibility challengers**, though investigated after the primary contradictions.

## 2. Inputs — provenance, not implementation

| Input classification | Inputs | Permitted inference |
|---|---|---|
| Signed requirements | PRD V0.6, SRS V0.6, Acceptance V0.4, D03-SCOPE-009 | Binding business behavior and acceptance intent |
| Signed UX policy | Design Specification V0.3, UI-G01..16; saved-answer, interrupted-mock copy | UI cannot claim proof that is not actually available |
| PO attestation | Two B1 Full Mock forms inventoried; permitted content sources | Inventory/rights reported, **not per-item QA PASS** |
| Desk evidence | ARCH01 AD01..16, EG01..16, CW01..10; ARCH02 E02-01..12, models, FM01..18 | Risk and evidence hypotheses; not tested system behavior |
| Not yet collected | Android real-device, crash/reboot/audio, storage/retry, identity/deletion, pilot QA | No feasibility, usability or security outcome may be claimed |

**Nonnegotiable signed constraints:** two distinct Full Mock A/B, each 200 questions (100 Listening ~45m + 100 Reading 75m); no arbitrary voluntary pause/replay for a comparable clean attempt; truthful saved-state messages; preserve acknowledged answers; explicit noncomparable/unknown handling; learner privacy and deletion within 7 calendar days after verified request, routine retention at most 30 days after pilot absent approved exception; versioned content and raw-score integrity.

## 3. Hypotheses to be evaluated later — not selected designs

| Domain | Primary evidence question | Candidates to compare (all UNCHOSEN) | Failure that defeats an unqualified clean/saved claim |
|---|---|---|---|
| Time continuity | Can a reviewer reconcile elapsed duration, stage changes and process/reboot interruptions without silently extending allowed time? | T-C reconciliation emphasis, challenge by T-A device-contained and T-B independent corroboration | Missing reboot continuity; wall clock disagreement; overwritten event history |
| Listening | Can ordered play/no discretionary replay be supported when audio focus or app state changes? | L-A foreground-bounded; L-B documented recovery | Lost audio segment, replay advantage, unproven focus recovery |
| Answer acknowledgement | Is a confirmed answer demonstrably durable and user/form-bound even if an ACK is delayed, lost or duplicated? | Compare S-C tiered states against S-A device-contained and S-B independently retrievable claims | UI says saved after only transient selection, duplicate counted result |
| Data isolation/deletion | Can each learner's evidence be separated, queried and deleted without unauthorized disclosure? | P-A, P-B, P-C as competing identity responsibility hypotheses | Shared-device account mix-up, unverifiable deletion completion |
| Content release/history | Can two Full Mock forms, separate practice pool, audited corrections and historic raw results remain unambiguous? | C-A, C-B, C-C; R-A, R-B | Wrong-key revision retroactively changes old record silently, practice exposes mock items |
| Device UX | Can screen-return context and state language remain truthful after interruptions? | Signed UX states only; later Android applicability | Reading anchor lost or save state mismatched; accessibility failure |

All rows refer to **information needed from a later evaluation**, not an architectural or storage topology. No weights, benchmark figures, SLAs or quantitative technology claims are invented here.

## 4. Evidence-reconciliation review procedure — future desk evaluation only

When the PO separately authorizes the next evaluation, reviewers should assess each *candidate explanation* using the same five questions (no software build required to write this procedure):

1. **Claim:** Exactly what business statement is being asserted (e.g., saved/clean/comparable/deleted)? Which signed FR/NFR/AT allows it?
2. **Required evidence:** What observations must exist to support this claim across the relevant failure mode? Describe provenance and expected observability abstractly — **not a schema, endpoint or component**.
3. **Conflict/absence:** What if observations disagree, arrive out of order, are missing, stale or inconsistent with identity/form/version?
4. **Conservative outcome:** What is the **truthful user-facing state** while proof is absent? Do not promote unknown to success. Whether an attempt becomes noncomparable or remains pending review must follow already-approved policy and later signed test thresholds.
5. **Falsifier:** Which FM01..18 negative case would show the claim is false? Who owns collecting evidence at the correct later checkpoint?

**Qualitative review outcomes (not test results):**
- `EVIDENCE OBLIGATION DEFINED`: reviewer can specify a falsifiable claim/evidence pattern; does **not** mean any evidence was captured.
- `EVIDENCE INSUFFICIENT`: claim remains unsubstantiated; retain unknown/noncomparable semantics as applicable.
- `EVIDENCE CONTRADICTORY`: apparent support conflicts with other relevant observations; no clean/saved claim until resolved by authorized policy.
- `EVIDENCE NOT EVALUATED`: not examined; never mark verified.

Do **not** call these classifications API response fields, database enums or a selected runtime state machine.

## 5. Cross-model decision matrix (qualitative, non-numeric)

| Review dimension | Evidence reconciliation priority | Device-contained challenger | Independent corroboration challenger | What later evidence is required |
|---|---|---|---|---|
| Clock conflict/reboot | Explicitly flag contradiction / unknown | Show own continuity protection across reboot/tampering | Show handling when corroboration unreachable | FM01..04; target-version/device context |
| Offline / response loss | Do not assume absent confirmation is proof of failure or success | Prove persistence without current connectivity | Prove truthful pending/unknown during outage | FM07..08 and life-cycle tests |
| Audio interruption | Separate attempted resumption from integrity proof | Demonstrate bounded clean continuity or invalidate | Demonstrate independent event evidence if used | FM01,05,18 |
| Cross-user privacy | Compare evidence of identity/isolation and deletion | Prove shared-device protection and lost-device deletion | Prove access protections and deletion coverage | FM09..11 |
| Version / historical score | Reconcile correction history with original meaning | Prove tamper-resistant original-form history | Prove retrievable version and correction evidence | FM06,12..14,17 |
| Complexity and availability | Highlight additional coordination burden | Highlight local failure/single-device risks | Highlight network and identity dependence | Later architecture evaluation, **NOT NOW** |

**Decision rule for next review:** Do not rank a candidate as feasible/selected merely because its diagram seems elegant. Unknown facts remain unknown. The goal is an actionable *evidence requirement list*, not a winning architecture.

## 6. Falsification inventory and ordering

Priority A — **time/audio integrity:** FM01 app switch, FM02 process loss, FM03 reboot, FM04 wall-clock change, FM05 audio focus, FM18 Android target restrictions.  
Priority B — **durable answer/identity:** FM07 disconnected selection, FM08 lost ACK/duplicate, FM09 learner switch, FM10 verified deletion, FM11 retention.  
Priority C — **release/scoring:** FM06 wrong media, FM12 corrected answer key, FM13 mock/practice overlap, FM14 duplicate submission, FM16 missing vetted explanation, FM17 raw result comparison.  
Priority D — **Reading context:** FM15 long Reading + large text + background.

These are **test designs** already defined in ARCH02. A future approver must explicitly authorize any experiments, code, simulators or Android/learner testing before anyone conducts them. Before pilot, QA-01..08 remain mandatory; no simulated evidence passes them.

## 7. Missing inputs, exact owner and checkpoint

| Unresolved issue | Why it matters | Checkpoint / authority |
|---|---|---|
| Recovery/clock skew/audio-loss tolerances | Changes which interruptions may be called comparable | Later test-plan business-policy review; PO signs numeric thresholds before execution |
| Target Android versions/device classes | Platform restrictions differ by target and OEM | Later Android applicability review, not chosen now |
| Evidence authority for timing and ACK | Would imply a system boundary/architecture choice | **Separate future architecture-option decision**; not in this brief |
| Learner identity and deletions across copies | Must satisfy signed privacy policy | Privacy/access review before pilot and future system design approval |
| Content QA & provenance release | Inventory is not tested correctness | QA-01..06 before content release |
| Real runtime and usability proof | Documented UI and platform facts do not establish implementation correctness | Actual QA-07..08 and Android/learner checks before pilot |
| Costs and service dependencies | Cannot assume free resources or spend | **DEFERRED BY PO; do not reopen here** |

## 8. Proposed outputs of a *future* separately authorized evaluation

- One **claim-to-evidence coverage matrix** across T/L/S/P/C/R alternatives with FM01..18 negative cases.
- One **contradiction and unknown handling register** showing unresolved evidence and truthful user-facing status.
- One **reversible candidate comparison** identifying prerequisites for later architectural choice, with *no selected winner* unless a different explicit PO authority is granted.
- One **technical choice readiness memo**: `READY FOR PO ARCHITECTURE DECISION` or `NOT READY — missing proof`, not `APPROVED ARCHITECTURE`.

These are **proposed deliverables**, not work already run or authorized by D05-TECH-003. This brief itself is the sole newly authorized work.

## 9. Boundaries and next authorization

**Completed now:** Approved-direction record and this evaluation brief; only desk preparation.  
**NOT completed:** evaluating or selecting architecture candidates, conducting real tests, picking clock authority, designing system/API/database, POC or code.  
**Next:** PO review of `STAGE05_D05_EVAL_004_OWNER_REVIEW_DECISION_PACK_V0.1.md`. Approving its optional future evidence-only desk evaluation would **still not authorize ARCH-03**. ARCH-03 requires a wholly separate explicit PO decision.

**Source cross-references:** `STAGE05_ARCH02_RESEARCH_METHOD_AND_SOURCE_LEDGER_V0.1.md` E02-01..12 (official sources), `STAGE05_ARCH02_FAILURE_MODE_AND_EVIDENCE_MATRIX_V0.1.md`, `STAGE05_ARCH02_OPTION_SCORECARD_AND_RESEARCH_FINDINGS_V0.1.md`, `STAGE05_ARCH02_TRACEABILITY_AND_CONTROL_V0.1.md`.
