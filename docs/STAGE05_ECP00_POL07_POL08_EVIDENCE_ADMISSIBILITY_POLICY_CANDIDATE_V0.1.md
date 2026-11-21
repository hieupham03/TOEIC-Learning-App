# POL-07 / POL-08 — Concrete Documentary Evidence Admissibility and Conflict Policy Candidate V0.1

**Status:** PENDING `D05-POL-009`; **NOT SIGNED**. This is a proposed **review policy only**, not an application algorithm, schema or system design.  
**Existing authority:** D05-EVIDCP-007=A approved the ECP plan; D05-ECP00-008=A approved ECP-00 REVIEW METHOD ONLY. **No evidence authority or values signed.**

## Scope of the proposed decision

**POL-07:** Reviewers need to distinguish genuine corroboration from reprints, mirrors or unknown dependencies.  
**POL-08:** Reviewers need to report conflicting, incomplete and late evidence without selecting a winning authority by assumption.  
**Inherited nonnegotiables:** `Đã lưu` requires credible durable confirmation, unknown ACK is not success or default failure; clean/comparable Full Mock requires demonstrated integrity; privacy/content/scoring claims require their own QA/proof. This proposal does not add or waive those signed obligations.

## Proposed adjudication rules for a future authorized review

| ID | Proposed concrete review rule | Required explanation | What this MUST NOT decide |
|---|---|---|---|
| **P07-R1** | Every evidence claim identifies the **exact proposition** and signed requirement/EV/FM, affected learner/form/attempt/item/version **where applicable**, observable provenance, and the original artifact reference. | A review note explains what the artifact actually establishes and which conditions were not observed. | No database fields, API schema, event format, key structure or technology choice. |
| **P07-R2** | Evidence is labeled **INDEPENDENCE DEMONSTRATED**, **CORRELATED/DERIVED**, or **DEPENDENCY UNKNOWN**. Missing provenance means independence **NOT DEMONSTRATED**. | Explicitly record known common inputs, producers, failure paths and limitations of the independence claim. | No required number of sources, weighting or local/remote preference. |
| **P07-R3** | Multiple copies or transformations of the same event **may document consistency but cannot be counted as independent corroboration**. | Cite the shared origin or state that it is not established. | No forced multi-source architecture, quorum or majority vote. |
| **P08-R1** | Positive and negative artifacts are assessed **against the same bounded claim and environment**, not collapsed into one overall candidate score. | Identify applicability, actual run/scope, evidence maturity and the exact disagreement. | No preferred candidate A/B/C, no automatic PASS/FAIL by tallied votes. |
| **P08-R2** | If a future authorized run has material unresolved conflicting, late or missing proof, mark its affected claim **INCONCLUSIVE** or **BLOCKED** under the already approved verdict taxonomy; otherwise unexecuted FM remains **NOT RUN**. | Identify which additional observation or separately approved source/threshold would be needed. | No assumed clock/ACK authority; no conversion of missing ACK into saved or failed. |
| **P08-R3** | A credible **falsifying counterexample** cannot be averaged away by unrelated positives. Under a signed test protocol it may support a **bounded FAIL**; where admissibility/scope is unresolved, record **INCONCLUSIVE** instead of a fabricated verdict. | Keep original counterexample, competing evidence, owner/review decision and any unresolved challenge. | No broad product FAIL or PASS beyond tested claim; no test execution authority. |
| **P08-R4** | Disagreements require **documented escalation and a new separately admissible observation or explicit PO policy resolution** before they can support a positive outcome. | Preserve historical revisions, reason and decision authorization without erasing prior observations. | No preselected adjudicator, precedence hierarchy, backend or clock authority. |

### Categories are review labels, not runtime UI states

`INDEPENDENCE DEMONSTRATED` is a claim about evidence provenance only, **not** proof the application is correct. `DEPENDENCY UNKNOWN` is not `INDEPENDENCE DEMONSTRATED`. `INCONCLUSIVE/BLOCKED/NOT RUN/FAIL/PASS (bounded)` retain the definitions and conditions in the already approved `STAGE05_EVIDENCE_CHECKPOINT_ACCEPTANCE_STOP_RULES_V0.1.md` and `STAGE05_ECP00_POLICY_AND_EVIDENCE_CONTRACT_REVIEW_BRIEF_V0.1.md`.

### Illustrative boundary cases (not observations)

- Two screenshots of a green `Đã lưu` label are correlated presentation evidence, not durable ACK proof.
- An acknowledged request and its copied audit line can share one source; two records alone do not establish independent durability proof.
- Two contradictory durations after a device reboot stay unresolved until time authority and acceptable tolerance are separately authorized; do not prefer a wall clock, elapsed timer or network receipt.
- Verified deletion on one visible copy does not certify deletion across other in-scope copies without separate evidence and approved scope.

## Scope exclusions and exact statuses after *possible* PO option A

If D05-POL-009=A were separately signed: **POL-07 and POL-08 review-admissibility wording APPROVED (DOCUMENTARY ONLY)**, while their source authority, conflict arbitration privileges, measured proof and related test decisions **remain OPEN**. POL-01..06 and POL-09..16 remain OPEN without change. No FM/QA execution, no ARCH-04, no system architecture selection, no money. Until that separate approval, **this entire document remains PROPOSED**.
