# Stage05 ARCH-01 — External Platform Evidence Ledger V0.1

**Checked:** 2026-11-21. **Use:** factual constraints for later verification planning; neither product requirement changes nor an architecture/stack recommendation.

| Evidence | Official URL | Relevant non-implementation inference | Stage05 follow-up |
|---|---|---|---|
| Android process and app lifecycle | https://developer.android.com/guide/components/activities/process-lifecycle | Android controls process lifetime; app process may be reclaimed. Continuous UI process availability must not be assumed for a 120-minute evaluation session. | CW-01, AD-01/04 require interrupted-activity cases later |
| Android activity lifecycle | https://developer.android.com/guide/components/activities/activity-lifecycle | App moving through background/resume/destroy states is a platform condition to model in user-observable requirements. | AT-05/11/19 future test design |
| Save UI states | https://developer.android.com/topic/libraries/architecture/saving-states | Transient UI-state restoration and durable business-answer acknowledgement are **different obligations**. Public docs support studying lifecycle, not assuming a particular persistent store. | AD-03/04 and future feasible persistence proofs |
| Accessibility testing | https://developer.android.com/guide/topics/ui/accessibility/testing | Automated and manual checks are complementary; static raster examples alone are not real-device accessibility proof. | G04-CP03/04, UIA-08, two Android contexts |
| ETS TOEIC Listening & Reading format | https://www.ets.org/toeic/about/listening-reading.html | Format reference for 100 Listening and 100 Reading questions; our particular two forms need content-level QA. | B1 form QA evidence QA-01..06 before pilot |
| Google Play User Data | https://support.google.com/googleplay/android-developer/answer/10144311?hl=en | Distribution requirements must be checked against actual implementation and data practices at the appropriate checkpoint. Not a reason to select an account system now. | AD-05/06/16 before external release |

**Evidence labels:** Android and ETS external documentation is **public reference**. Signed app policies come from **PO decisions**. Source websites and the PO-affirmed rights/inventory are handled by previously signed Stage03 governance documents. No external content was copied or a business/vendor consulted during ARCH-01.
