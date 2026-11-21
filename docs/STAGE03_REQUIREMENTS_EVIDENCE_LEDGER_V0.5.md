# Official Research Source Ledger — Stage03 Draft V0.5

**Checked:** 2026-11-21. Public reference supports general requirements **only**, not content QA or implementation results.

| Reference | Official source | Grounded use | What it DOES NOT prove |
|---|---|---|---|
| E-ETS-01 | https://www.ets.org/toeic/about/listening-reading.html | TOEIC L&R uses 100 Listening +100 Reading, about 45+75 min | Our two forms have been QA-verified or calibrated |
| E-ETS-02 | https://www.ets.org/toeic/about/faq/product-specific-faq/toeic-listening-reading.html | ETS reports scale by section and comparability across official forms | Our raw scores convert validly to ETS official scores |
| E-AND-01 | https://developer.android.com/guide/components/activities/process-lifecycle | Android may kill cached/background processes; requirement must anticipate lost transient state | Any app currently preserves answers |
| E-AND-02 | https://developer.android.com/guide/components/activities/activity-lifecycle | Activity callbacks and return/exit cases need robust user-state behavior | Choice of architecture or exact persistence implementation |
| E-AND-03 | https://developer.android.com/guide/topics/ui/accessibility/testing | Device and accessibility tests matter for readable/operable app | Part 7 passed tests on pilot phones |
| E-PLAY-01 | https://support.google.com/googleplay/android-developer/answer/10144311?hl=en | User-data policy and privacy disclosure requirements | A privacy program for our not-yet-developed app is compliant |
| E-PLAY-02 | https://support.google.com/googleplay/android-developer/answer/13327111?hl=en | Account creation, if implemented, entails account deletion request obligations under Google Play rules | The app will necessarily use accounts or has passed deletion test |

## Internal controlling evidence

- Product Vision V1.0 APPROVED; CP-01..05 APPROVED, Stage02 CONDITIONAL PASS.
- D03-LOCK-001=B1 APPROVED (two full mocks); D03-SOURCE-004 two mock inventories PO-REPORTED complete; D03-WEB-SOURCE-003 PO affirmed source rights.
- D03-QA-006 APPROVED QA-01..08 **as a framework**, no execution PASS.
- D03-REQ-007 APPROVED R1–R4 as drafting principles, NOT detailed subpolicies or PRD/SRS.
- D03-BUDGET-005 budget DEFERRED BY PO.

**Source policy:** cite verified public references only for framework claims, PO for governance; do not treat website contents as app product/data evidence.
