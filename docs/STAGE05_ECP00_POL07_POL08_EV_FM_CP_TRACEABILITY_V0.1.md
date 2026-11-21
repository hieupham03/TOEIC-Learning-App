# POL-07 / POL-08 — Cross-Candidate EV/FM/Carry-Forward Traceability V0.1

**Purpose:** Ensure future PO consideration of the narrow POL-07/POL-08 documentary policy is connected to the existing **12/12 EV and 18/18 FM**, without claiming new coverage or tests. This is a *risk-filter overlay*, not a replacement for the signed `STAGE05_EVIDENCE_CHECKPOINT_EV_FM_TRACEABILITY_V0.1.md`.

| EV claim | Challenge FM | Relevant proposed P07/P08 controls | Still-open policy families | Evidence status |
|---|---|---|---|---|
| EV-01 time vs wall-clock | FM-03/04 | Source provenance, conflict classification; no plurality voting | POL-01/02/03/07/08 | M2 DOCUMENT ONLY |
| EV-02 restored UI vs true attempt | FM-01/02 | Distinguish presentation record vs event/durability proof | POL-03/05/07/08 | M2 DOCUMENT ONLY |
| EV-03 reboot timing | FM-03/04 | Dependency-aware comparison, no implicit time authority | POL-01/02/07/08 | M2 DOCUMENT ONLY |
| EV-04 audio continuity | FM-01/05/18 | Correlate but do not assume same producer is independent | POL-03/04/07/08/13 | M2 DOCUMENT ONLY |
| EV-05 durable ACK | FM-07/02 | Validate exact claim/provenance before acceptance | POL-05/07/08 | M2 DOCUMENT ONLY |
| EV-06 late/lost ACK | FM-08/14 | Keep unknown until authenticated contrary/confirming proof | POL-05/06/07/08 | M2 DOCUMENT ONLY |
| EV-07 learner isolation | FM-09 | Require consistent scoped learner/attempt provenance | POL-07/08/09/14 | M2 DOCUMENT ONLY |
| EV-08 deletion across copies | FM-10/11 | Count copies by scope, not repeated receipts | POL-07/08/10 | M2 DOCUMENT ONLY |
| EV-09 content readiness | FM-06/16 | Distinguish repeated catalog export from item QA | POL-07/08/11 | M2 DOCUMENT ONLY |
| EV-10 score correction history | FM-12/14/17 | Trace provenance/version and contradiction | POL-07/08/12 | M2 DOCUMENT ONLY |
| EV-11 separate mock/practice | FM-13 | Independent review of source lists, not copies | POL-07/08/11 | M2 DOCUMENT ONLY |
| EV-12 Reading/accessibility | FM-15/18 | Screenshots are not device-testing proof | POL-07/08/13/14 | M2 DOCUMENT ONLY |

**FM accounting:** full FM-01..FM-18 are inherited in the unchanged approved ECP plan's traceability matrix. This overlay references the linked falsifiers for each EV and does **not** change the FM count, assigned checkpoint or actual status (**18/18 NOT RUN**).

**CP/QA interaction:** Stage02 CP-01..05; Stage03 G03-CP01..07; Stage04 G04-CP01..08 **ACTIVE** and unaffected. QA-01..08 approved framework; **zero actual PASS**. Family learner isolation, deletion/retention timelines, B1 two 200-question forms, raw-score-only communication and UI truthful state labels remain binding. No policy review can waive any of these.

**Candidate fairness:** Apply identical P07/P08 evidence burden to ARCH03-A/B/C and to each of 16 T/L/S/P/C/R technical model hypotheses. The approved research direction Evidence Reconciliation First does **not** rank or select an architecture.
