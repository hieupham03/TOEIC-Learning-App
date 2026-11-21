# Stage05 ARCH-03 — Official Source Pointers and Applicability Limits V0.1

**Rechecked:** 2026-11-21. These are official Android Developers, OWASP and Google Play references for architectural *constraints*. They do not evaluate the future app, and they are not endorsement of any candidate A/B/C. Existing ETS references are inherited from ARCH02.

| Source URL | Supports | Does NOT support |
|---|---|---|
| https://developer.android.com/reference/android/os/SystemClock | `elapsedRealtime` since boot incl. sleep, wall-clock distinction | A standalone reboot-proof or externally authoritative exam clock |
| https://developer.android.com/guide/components/activities/process-lifecycle | Cached process may be reclaimed, execution constraints depend on lifecycle | A clean Full Mock automatically survives termination |
| https://developer.android.com/topic/libraries/architecture/saving-states | UI state vs persistent storage distinction | Durable answer ACK from restored UI |
| https://developer.android.com/media/optimize/audio-focus | Audio focus can change; target-sensitive conditions | Uninterrupted Listening or safe arbitrary replay in target app |
| https://developer.android.com/about/versions/17/changes/bg-audio | Some Android17 background audio hardening and applicability | All target devices behave identically; a target version has been chosen |
| https://mas.owasp.org/MASVS/05-MASVS-STORAGE/ | Secure storage obligations for sensitive mobile data | One selected storage solution or verified deletion |
| https://mas.owasp.org/MASVS/07-MASVS-AUTH/ | Auth and authorization security controls | Device/remote/hybrid identity boundary selected |
| https://support.google.com/googleplay/android-developer/answer/13327111?hl=en | Applicable account deletion requirements depending on account features | Project-specific ≤7d / ≤30d targets originate in Google policy |
| https://www.ets.org/toeic/about/listening-reading.html | L&R official structure and timing | The two inventoried forms are QA-ready or ETS-equated |

**Provenance:** Signed scope/requirements remain stronger for *product commitments* than this ledger; public documentation supplies only supporting platform constraints. No API, DB, framework or clock authority is selected here. See `STAGE05_ARCH02_RESEARCH_METHOD_AND_SOURCE_LEDGER_V0.1.md` and `STAGE05_EVAL004_OFFICIAL_EVIDENCE_REVALIDATION_LEDGER_V0.1.md` for prior evidence classifications.
