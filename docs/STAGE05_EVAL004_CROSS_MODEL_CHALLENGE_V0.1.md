# Stage05 — D05-EVAL-004 Cross-Model Challenge and Reversibility V0.1

**Authority:** DOCUMENT-ONLY evaluation; alternative families remain **UNCHOSEN**. Qualitative desk comparisons do not establish performance, cost, feasibility, or a preferred system architecture. No numeric weights are invented.

## 1. Model-by-model challenge

| Model | Domain | Hypothesized evidence responsibility | Potential conceptual benefit | Weakest falsifier/evidence gap | Negative cases | Desk result |
|---|---|---|---|---|---|---|
| T-A | Time | Device-contained elapsed evidence | Less need for live network during local activity | Reboot and clock manipulation evidence remain unproven | FM01..04 | Keep as challenger; no selection |
| T-B | Time | Independently corroborated elapsed evidence | Potential independent continuity observation | Outage/late reports and learner privacy may create unknowns | FM01..04 | Keep as challenger; no selection |
| T-C | Time | Reconciling multiple signals | Can expose contradictions and ambiguous intervals | Conflicting sources need future adjudication rule/authority | FM01..04 | Research emphasis only; no selection |
| L-A | Audio | Foreground-bounded clean attempt | Conservative about interruptions | Could yield more noncomparable attempts | FM01/05/18 | Conditional |
| L-B | Audio | Evidence-based interrupted playback recovery | Potential learner continuity | May risk advantage via partial replay/resumption | FM01/05/18 | Conditional |
| S-A | Answer | Device-contained acknowledgment | May work under partial connectivity | Durability/identity after loss/reboot uncertain | FM07/08/09/14 | Conditional |
| S-B | Answer | Independently retrievable acknowledgment | Potential cross-restart confirmation | Network/identity and delayed response unknown | FM07/08/09/14 | Conditional |
| S-C | Answer | Explicit pending/confirmed/uncertain tiers | Can communicate absence of proof honestly | Must still show real durable ACK and reconcile duplicate writes | FM07/08/14 | Language emphasis only; no selection |
| P-A | Privacy | Device-scoped learners | Potentially simple family pilot | Shared-device leaks, lost-device access/deletion | FM09/10/11 | Conditional |
| P-B | Privacy | Individually authenticated learner | Accountability and access segmentation potential | User friction, identity verification/deletion and availability | FM09/10/11 | Conditional |
| P-C | Privacy | Combined evidence checks | Potential corroborated isolation/deletion | Coordination/consent and copy-coverage uncertainty | FM09/10/11 | Conditional |
| C-A | Content | Frozen reviewed form release | Historic exam content stable | Corrections and out-of-date keys need process | FM06/12/13/16 | Conditional |
| C-B | Content | Audited revisions | May correct faulty released items | Historical score reinterpretation risk | FM06/12/13/16 | Conditional |
| C-C | Content | Release + amendment record | Potential traceable review/correction history | Additional QA/governance proof needed | FM06/12/13/16 | Conditional |
| R-A | Raw results | Original version record | Preserves provenance of historical result | Separate correction explanation may be necessary | FM12/14/17 | Conditional |
| R-B | Raw results | Versioned correction view | Can disclose revised interpretation | Must avoid overwriting and misleading improvement claims | FM12/14/17 | Conditional |

## 2. Identical tests for preferred research priority and challengers

| Challenge | Evidence Reconciliation First | Device-contained challenger | Independently corroborated challenger | Fair adjudication |
|---|---|---|---|---|
| Reboot destroys one elapsed reference | Must state how contradictory/missing signals are recognized; cannot declare resolved by adding sources | Must demonstrate locally defensible reboot continuity | Must demonstrate availability and integrity of independent observation | All conditional until FM03/04 evidence |
| Offline answer write has no ACK | Must show how uncertainty is represented without assuming response loss means failure | Must show proof of durable local confirmed answer | Must show behavior when external evidence unreachable | All conditional until FM07/08 evidence |
| Shared learner device | Must identify which learner each observation belongs to | Must prevent one device profile from exposing another | Must prove authorization independent of connectivity assumptions | All conditional until FM09/10 |
| Changing answer key | Must preserve versioned interpretation | Must show historical records stable even with local changes | Must show version/correction retrieval without retroactive replacement | All conditional until FM12/17 |
| Audio focus interruption | Must not elevate disagreement to clean playback | Must support conservative invalidation/recovery claims | Must show proof persists under connection interruptions | All conditional until FM05/18 |

## 3. Evaluation verdict — no winner

- **Evidence Reconciliation First** is the **approved analysis order**, *not proof* that a multiple-source system is needed or best.
- **Device-contained** remains eligible, provided its future evidence can satisfy every signed condition including reboot, identity and deletion.
- **Independently corroborated** remains eligible, provided its future evidence can satisfy connectivity, response-delay and privacy conditions.
- A model cannot be called feasible based on a plausible diagram, and no hidden scoring/ranking is introduced. Later tests, defined acceptance thresholds, device contexts, identity policy and resource constraints may alter qualitative tradeoffs.
- **Qualitative readiness:** all 16 conceptual options are **CONDITIONAL / NOT VERIFIED**. No engineering selection authorized.
