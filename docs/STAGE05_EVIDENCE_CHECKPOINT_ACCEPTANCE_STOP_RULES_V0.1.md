# Stage05 — Proposed Evidence Admissibility, Outcome & Stop Rules V0.1

**Document-only proposal under D05-ARCH-006=D; PENDING PO as part of D05-EVIDCP-007. No execution authorization.** These are *meta-rules for a future review*, not selected product runtime behavior or changes to signed acceptance thresholds.

## A. Proposed review outcomes (avoid optimistic verdicts)

| Outcome | Meaning and minimum required evidence | Forbidden shortcut |
|---|---|---|
| **NOT RUN** | Test was not authorized or has not been executed | Labeling a prepared FM as PASS |
| **BLOCKED** | Missing PO policy, device authorization, candidate/test boundary, required material or privacy controls | Using an assumed numeric tolerance |
| **INCONCLUSIVE** | A test was authorized/run but evidence missing, inconsistent, late, untraceable or cannot distinguish hypotheses | Treating unknown as success OR definitive failure |
| **FAIL** | A valid authorized falsifier shows expected integrity/ACK/privacy/content/reading behavior not met | Excluding inconvenient failures without owner signoff |
| **PASS (bounded)** | Future signed run meets pre-approved criteria within stated versions, scopes, artifacts and exception list | Claiming other devices/learners/versions also pass |
| **NOT APPLICABLE (reasoned)** | PO/QA confirms a scenario is inapplicable to signed scope, with traceable explanation | Silently skipping an FM or reducing B1 requirements |

**Current statuses:** EV01..12 `DOCUMENT REVIEWED / NO APP PROOF`; FM01..18 `NOT RUN`; 0 bounded PASS, 0 real-device tests; QA01..08 no actual PASS. No architecture selection.

## B. Minimum record to distinguish claims

1. Immutable linkage: baseline item, EV/FM ID, observed learner/form/attempt/item/version (when applicable), candidate tested, PO permission and approved expectation.
2. Actual observation: test environment and version, ordered events with provenance, raw supporting artifact and tamper/independence limitations. Avoid selecting a clock authority in this planning document.
3. Decision trail: owner, date, deviations, known gaps, disposition and retest; never replace previously signed history silently.
4. Negative tests must be capable of **falsifying** a success claim; screenshots or UI-only transitions are not enough for durable ACK, clock continuity, privacy deletion or content integrity.

## C. Proposed fail-closed and pause triggers for future checkpoint owners

- **P0 integrity:** Without credible evidence of time/audio continuity, do not certify `clean/comparable Full Mock`. Reboot and wall-clock changes require PO-controlled quantitative tolerance and authority **before a future test can claim PASS**.
- **P0 saved-answer truth:** Missing ACK or contradictory copies ⇒ `chưa thể xác nhận`, not `đã lưu`, not automatic failure; later retry must be consistent with one logical attempt/answer under approved rules.
- **P0 data trust:** Any learner isolation breach or inability to account for in-scope copies during deletion ⇒ report blocker; do not certify privacy success. Existing verified-request deletion deadline is 7 calendar days, and ordinary retention after pilot is ≤30 days, with signed exceptions.
- **P0 content release:** Wrong audio/key, unverified explanation or mock/practice overlap must block the affected content until QA evidence is signed. Inventory and rights affirmation are already recorded; no new content audit claims made now.
- **P0 history integrity:** Corrected keys must not silently rewrite historical raw result meaning or imply official ETS scores.
- **Reading/accessibility:** Any case preventing answerability at required Android contexts stays open even if desk layout looks good.
- **Administrative stop:** No paid service, POC/code, learner/device test, architecture choice, target version or real data may begin without separate, applicable PO approval. Stop the activity before changing a baseline or controlled UX rule.

## D. Fair comparative scoring — no invented ranking

For A/B/C, a future report should show **per-EV**, not one opaque total: `supported` with artifact, `refuted` with counterexample, `inconclusive`, `not run`, operational complexity *described not priced*, reversible change risk and remaining blockers. Don't give C extra credit solely because prior research was called Evidence Reconciliation First; don't give A or B automatic benefits without empirical proof. A single hard blocker cannot be averaged away by other successes.

## E. PO approvals needed before any executable checkpoint

- Distinct authority for **checkpoint execution**, exact test/QA scope and boundary, plus policy decisions for time/skew/interruption and source-of-truth criteria where necessary.
- Later technical/test planning may require separately approved target Android contexts, participant recruitment/consent, privacy SOP, content QA owner and traceable defect handling; **none** is granted by D05-ARCH-006 or proposal approval.
- Budget **DEFERRED** throughout; if future authorized execution would require spending, separate PO reopening is mandatory **before commitment**, not a reason to ask for budget today.
