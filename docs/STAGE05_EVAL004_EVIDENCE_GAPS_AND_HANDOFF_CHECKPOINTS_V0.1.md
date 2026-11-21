# Stage05 — Evidence Gap Handoff and Ownership V0.1

**Nature:** evidence requirements and future checkpoints **only**. Not approved tests, no new milestones with spending/implementation permission. Existing EG01..16 and UX04-I/UIA remain open; do not close them by documentation.

| Gap | What cannot be claimed yet | Supporting review IDs | Later proof that would be needed | Accountable checkpoint | Priority / blocking meaning |
|---|---|---|---|---|---|
| GAP-E01 | Clean mock after process loss/reboot and clock change | EV01..03, FM01..04 | Actual elapsed reconciliation, attempt history, negative reboot/tamper outcomes | Later authorized implementation + QA08 before pilot; PO thresholds first | P0 pilot validation |
| GAP-E02 | Uninterrupted/no-advantage Listening | EV04, FM05/18 | Target-Android applicability, audio focus traces, interrupted playback and replay negative tests | Future target choice, Android/audio QA03/08 | P0 pilot validation |
| GAP-E03 | Confirmed answer durability and safe retries | EV05/06, FM07/08/14 | Evidence of user/form binding, confirmed write, lost/reordered ACK and duplicate attempt behavior | Future app persistence QA08 | P0 pilot validation |
| GAP-E04 | Cross-user isolation on a shared phone | EV07, FM09 | Two-learner cross-access negative tests and late-pending activity | Future identity/privacy design approval + QA08 | P0 pilot validation |
| GAP-E05 | Complete deletion and retention | EV08, FM10/11 | Verified request timestamps, in-scope data/copy inventory, lawful exception and post-pilot deletion checks | Future privacy SOP; <=7 calendar days; retention <=30 days after pilot | P0 pilot and post-pilot obligations |
| GAP-E06 | Correct B1 and practice content release | EV09/11, FM06/13/16 | QA01..06 per form/item/key/audio/asset/provenance, independent pool overlap test | Content curator before pilot release | P0 content release blocker |
| GAP-E07 | Historic scores survive correction | EV10, FM12/14/17 | Versioned original attempt, corrected key transparency, no misleading score equivalence | Scoring QA07 before pilot + future corrections | P0 score integrity |
| GAP-E08 | Reading and accessible state copy on Android | EV12, FM15 | Actual tests at >=2 Android contexts; text-size/anchor/accessibility scenarios | Later authorized UX/Android QA08 before pilot | P1 usability; P0 if blocking answerability |
| GAP-E09 | Numeric tolerance for interruption/skew/audio loss | EV01..04 | PO-approved quantitative acceptance thresholds; cannot infer here | Future test-plan business policy decision before execution | Policy decision, not desk-passable |
| GAP-E10 | Technical evidence authority and systems boundary | EV01..08 | Explicit architecture decision after option evaluation | **Separate ARCH-03 authorization and architecture selection later** | No solution choice now |
| GAP-E11 | Android target/version applicability | EV04/12 | Target Android scope and device evidence; Android15/17 constraints conditional | Later target/version decision + QA | Deferred applicability |
| GAP-E12 | Permission to run any test, POC or spend | all | Separate PO authorization, future planned checkpoints | PO only | Not authorized; budget DEFERRED |

## Evidence handoff rules

- **Proof exists** only when a later owner produces an actual artifact: device run, test results, signed content QA, approved policy threshold or validated privacy/deletion audit. A list of expected artifacts is not proof.
- Content source inventory and rights attestation were already supplied by PO; do **not** reopen inventory requests or imply a new attestation is necessary. Content QA01..06 is a distinct future control.
- Full Mock valid/comparable decisions must follow existing signed policy; do not invent auto-invalid conditions or arbitrary grace thresholds. Raw score comparison cannot be described as a scientifically confirmed TOEIC improvement.
- CP01..05, G03-CP01..07, G04-CP01..08 remain active across stages. Defer every budget task until expressly reopened by PO.
