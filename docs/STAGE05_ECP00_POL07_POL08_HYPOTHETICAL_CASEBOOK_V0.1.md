# POL-07 / POL-08 — Hypothetical Evidence-Review Casebook V0.1

**Status:** PAPER SCENARIOS ONLY / NOT A RUN / NO VERIFIED APP CLAIM. Cases illustrate how reviewers **might** apply pending P07/P08 rule text if and only if D05-POL-009=A is later signed and test execution separately authorized. Do not report any of these as observed. Use actual `NOT RUN` for all FM today.

| Case | Linked EV/FM | Hypothetical set of records | Potential future review finding (conditional) | Invalid inference |
|---|---|---|---|---|
| HC-01 | EV-05/FM-07 | Two screenshots both show `Đã lưu`; neither links to durable persistence. | Provenance insufficient; no durable-ACK PASS. | Two matching images imply two independent durable writes. |
| HC-02 | EV-06/FM-08 | Hypothetical durable commit recorded, response lost; UI shows pending/unknown. | Preserve uncertainty until authenticated recovery evidence; no automatic FAILED or SAVED label without proof. | Response loss always means failed transaction. |
| HC-03 | EV-01/03/FM-03 | Device reboot; before/after apparent elapsed-time values disagree with another observation. | Timing continuity INCONCLUSIVE unless separately approved authority/tolerance and bounded proof resolve it. | Most recent timestamp necessarily correct; clean Mock PASS. |
| HC-04 | EV-04/FM-05 | Media player says clip completed; audio-focus history suggests interruption. | Conflicting evidence of Listening continuity; do not certify clean Mock solely from player progress. | Player progress proves learner heard audio uninterrupted. |
| HC-05 | EV-07/FM-09 | Save response returns after family learner switched; attempt ownership not proven. | Identity provenance unresolved; learner-isolation PASS blocked, potential incident handled only after authorized evidence review. | Screen currently showing learner B determines ownership of old save. |
| HC-06 | EV-08/FM-10/11 | One data copy has a verified delete receipt; other copies not accounted for. | Evidence incomplete for project deletion obligation; no privacy PASS. | One receipt proves every in-scope copy removed. |
| HC-07 | EV-10/FM-12/17 | A scoring record is presented after an answer-key revision, with no version proof. | Score-history claim unverified; may not infer an ETS-equivalent score or silently replace old meaning. | Agreement of repeated score views demonstrates correct version. |
| HC-08 | EV-02/FM-02 | Android activity restores Reading question and timer label after process reclaim. | Restored UI is presentation evidence only; clean attempt/ACK require other admissible proof. | Screen restoration establishes persistence and uninterrupted timing. |
| HC-09 | EV-11/FM-13 | Two catalog exports both derive from the same unreviewed content list. | No independent proof of mock/practice bank separation; QA remains required. | Duplicate exports prove non-overlap. |
| HC-10 | EV-12/FM-15/18 | Screenshot at default text size looks legible; no large-text Android run exists. | No device/accessibility PASS; future approved device contexts still needed. | Attractive mockup demonstrates usability on real Android. |

## Taxonomy guardrails

All FM-01..18 remain **NOT RUN** now. A hypothetical future authorized run with contradictory artifacts might be **INCONCLUSIVE**; one blocked by absent policy is **BLOCKED**; a validated negative test might produce a **bounded FAIL**; none of those labels is being assigned to a real execution by this casebook. None of the case rows selects source independence or a runtime outcome algorithm.
