# Stage05 — Technical Evidence Checkpoint Proposal V0.1

**Nature:** A decision-ready **PROPOSAL**, prepared under `D05-ARCH-006=D`. **PENDING PO** for separate `D05-EVIDCP-007`.  
**Not authorized:** conducting any checkpoint, device/learner trial, POC/code, architecture development or selection, ARCH-04, Stage05 Gate, buying products/services or spending.  
**Input:** ARCH03-A/B/C documentary comparison, EV-01..12, FM-01..18, GAP-E01..12, EG01..16, UX04-I01..08/UIA-01..08, signed baselines and CPs.

## I. Goal and decision question

Determine **what later evidence would meaningfully distinguish or falsify ARCH03-A, B, C** on the *same* signed product duties, **without presupposing an answer**. The PO must be able to say (1) what claims are currently document-supported; (2) which app behavior is UNKNOWN; (3) what later evidence and prior policy authorization is needed; and (4) which checkpoint can veto a candidate. Evidence planning ≠ evidence collection ≠ feasibility PASS ≠ selecting an architecture.

## II. Evidence maturity and admissibility

| Level | Claim allowed | Examples of admissible material | Cannot infer |
|---|---|---|---|
| **M0 — Signed rule** | Business duty or approved design rule exists | PO decision, immutable PRD/SRS/AT/Design spec | It is implemented or tested |
| **M1 — External constraint** | Android/ETS/Play/OWASP may impose a condition | Official dated document, version applicability, quote/link and scope | Target app satisfies it |
| **M2 — Method / synthetic case** | A scenario is defined and could falsify a claim | FM negative-case, planned observations and pass/fail criteria | Scenario executed or architecture feasible |
| **M3 — Observed result** | A bounded actual tested behavior was observed | Later PO-authorized test logs, device/version info, inputs, timelines, expected vs observed, replayable artifacts | Other devices/users/forms necessarily pass |
| **M4 — Controlled QA verdict** | Approved QA performed and exception disposition recorded | Owner-signed QA-01..08 result, asset/version provenance, regression and defects | Official ETS equivalence, generalizable learning gains |

**CURRENT LIMIT:** M0–M2 ONLY. M3=M4=0 for product behavior; no test operation is proposed as already performed. Prohibit self-assigning positive verdict to missing/conflicting observations. Record `DOCUMENT_SUPPORTED`, `HYPOTHESIS`, `NEEDS_POLICY`, `NO_APP_EVIDENCE`, `CONFLICTED`, `NOT_APPLICABLE_WITH_REASON` separately.

## III. Proposed checkpoints — separated by authority, NOT a project schedule

| ID | Scope and output required IF later authorized | EV / FM covered | Future preconditions | Gate/owner/status |
|---|---|---|---|---|
| **ECP-00** | **Policy and evidence-contract decision**: measurable time/interrupt tolerances, claim-state vocabulary, what counts as an independent observation, admissible output fields | EV01..08; FM01..05/07..11/14 | PO explicitly approves any numeric and authority policy; never invent grace, skew or clock source | PO policy sign-off; **PROPOSED ONLY** |
| **ECP-01** | **Mock time and Listening integrity**: future process-loss/reboot/clock changes/audio focus, interruptions, no arbitrary replay; preserve `clean / non-comparable / unknown` distinction | EV01..04; FM01..05/18 | ECP-00 signed; target Android/device scope separately authorized; executable test permission | Later Android/audio QA03/08; **PROPOSED ONLY** |
| **ECP-02** | **Durable answer, late ACK and duplicate prevention**: distinguish selection, pending, durable-confirmed, unknown; recovery, correct learner/form/attempt/item binding | EV05..06; FM02/07/08/14 | Approved persistence evidence contract; no stack presupposed; later actual test permission | Later persistence QA08; **PROPOSED ONLY** |
| **ECP-03** | **Data isolation, deletion and retention**: shared-device account switch, all in-scope copies incl backups, lawful exceptions, auditable requests and expiry | EV07..08; FM09..11 | Identity/privacy SOP and any technical authority separately approved; user data never tested now | Later privacy QA08, data rights; **PROPOSED ONLY** |
| **ECP-04** | **B1 content and scores**: 2 × 200 QA, media/key/passages, mock/practice non-leakage, provenance, corrections, raw results without ETS-scale claim | EV09..11; FM06/12..14/16/17 | QA01..07 run by later authorized curator; PO inventory NOT reopened; content use remains controlled | Content-release and scoring QA; **PROPOSED ONLY** |
| **ECP-05** | **Android Reading/accessibility and UX understanding**: context return, text scaling, focus/state labels, 2+ *actual* device contexts and short user tasks if later approved | EV04/12; FM01/15/18 | Target/version review + separate device/participant consent/test permission | Later UX/Android QA08; **PROPOSED ONLY** |
| **ECP-06** | **Cross-option evidence adjudication**: apply identical falsifiers A/B/C, show source dependence, disconfirmations, uncertainty and reversible choice; submit PO choice | EV01..12; FM01..18 | Evidence from prior approved checkpoints is available OR gaps explicitly carried as blockers; no invented scores | Future PO architecture-choice decision; **PROPOSED ONLY** |

**Checkpoint order:** ECP-00 is a **policy precondition** before tests that depend on it. ECP-01..05 are workstreams, **not** permission to execute or a mandated chronology. ECP-06 compares only material actually collected. Some content QA may proceed independently at its separately authorized later gate; this package sets no dates, spending, staff allocation or technical architecture.

## IV. Mandatory evidence record schema (agnostic of architecture)

A later evidence report should include `claim_id (EV)`, `negative_case_id (FM)`, `relevant requirement/QA`, `candidate A/B/C`, `observed environment/version and provenance`, `actor/learner/attempt binding`, `input/event order`, `expected and observed result`, `time evidence & its uncertainty`, `artifact reference/hash`, `test owner`, `deviation and retest`, `status {PASS/FAIL/INCONCLUSIVE/BLOCKED/NOT_RUN}` and `PO decision ID` for thresholds/permissions. **This is a documentation contract**, not a schema, API, protocol or database design.

Disallow `PASS` from screenshots alone, a restored UI, cached selection, a log without trustworthy attempt linkage, two correlated sources, content inventory alone, or unreviewed media/keys. A meaningful counterexample (`FAIL`) vetoes a claim until resolved under approved change control. Conflicting evidence yields **INCONCLUSIVE**, not majority vote.

## V. Architecture-neutral challenge and reversibility

- **ARCH03-A:** strongest challenge is local reboot/clock trust, storage durability, identity switch and deletion coverage. Observing offline continuity would not prove trusted elapsed time or security.
- **ARCH03-B:** strongest challenge is outage/late response, association with correct attempt, privacy/deletion copies and whether outside observation establishes audible Listening progress.
- **ARCH03-C:** strongest challenge is dependency/correlation between signals, source disagreement, arbitration rules and unnecessary additional complexity/copies. More signals ≠ stronger proof automatically.
- A future scorecard must separate **supported/unsupported/inconclusive** by claim, disclose missing conditions and retain all candidates until PO signs an independent architecture selection. No weighted winner, budget/risk number or efficiency claim without evidence.

## VI. Proposed PO decision now — D05-EVIDCP-007

**Recommended A:** approve the **checkpoint PLAN and evidence-admissibility review obligations only**, with ECP-00 prior to any future execution. No tests are authorized by this approval.  
**B:** request modifications to checkpoint priorities, evidence format or stop rules in one batch.  
**C:** HOLD, preserve the desk research with all A/B/C unselected.

To authorize any particular real test/device/POC in the future would require a **separate scope-and-permission decision**, including approved relevant policies, QA owner, legal/privacy consent, target scope, handling of personal data and any required spending authority. Until then, **ALL ECP-00..06 remain proposed and no test is executed**.
