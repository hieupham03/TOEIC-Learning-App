# Stage05 ARCH-02 — Research Method, Evidence Classes and Source Ledger V0.1

**State:** DESK RESEARCH COMPLETE FOR PO REVIEW; NOT a solution design, performance measurement or QA PASS.  
**Approved research order:** D05-ARCH-002=A, Integrity-first. Date accessed: 2026-11-21.

## Research method

1. Treat approved requirements, business policies, design copy and Gate conditions as **non-negotiable constraints**; no proposals can waive them.
2. Separate **observed public platform facts** (official docs), **product-owner attestations** (content inventory and rights), **approved targets** (acceptance), **analyst hypotheses** (comparative options) and **not yet collected empirical evidence**.
3. Compare at least two materially different conceptual evidence/responsibility models for every P0 driver. Score **coverage, failure transparency, offline/network uncertainty, complexity, privacy implications, falsifiable test cases** qualitatively; no invented benchmarks or prices.
4. Retain the hardest negative case: ambiguity must remain visible; no simulated or static UI claims that audio, clock, persistence or permission checks passed.
5. Do not equate Android platform documentation with validation on a particular handset, OS version, OEM or implementation.

## Public evidence ledger

| Ref | Authority/source | Fact supported / boundaries | Official URL |
|---|---|---|---|
| E02-01 | Android Developers — Activity lifecycle | Activity/process may be destroyed and recreated; lifecycle behavior must be planned; NOT evidence any app persisted answers | https://developer.android.com/guide/components/activities/activity-lifecycle |
| E02-02 | Android Developers — Save UI states | Transient UI restoration differs from durable business persistence; limits and tradeoffs depend on data complexity | https://developer.android.com/topic/libraries/architecture/saving-states |
| E02-03 | Android Developers — SystemClock | `elapsedRealtime()` includes time in deep sleep since boot; standard wall clock differs. Does NOT establish an anti-tampering/independent exam authority or reboot continuity | https://developer.android.com/reference/android/os/SystemClock |
| E02-04 | Android Developers — Audio focus | Audio focus is interruptible; Android 15+ target-related restrictions apply to apps seeking focus unless foreground or eligible service | https://developer.android.com/media/optimize/audio-focus |
| E02-05 | Android Developers — media playback foreground constraints | Specific background playback behavior requires lifecycle/service considerations; NOT a commitment to use Media3/service | https://developer.android.com/media/media3/session/background-playback |
| E02-06 | Android Developers — Android 17 background audio hardening | New/target-dependent restriction area; verify applicability at later target-version decision and real devices | https://developer.android.com/about/versions/17/changes/bg-audio |
| E02-07 | OWASP MASVS-STORAGE | Sensitive data requires secure storage controls. Does NOT prescribe a product-specific identity/storage architecture | https://mas.owasp.org/MASVS/05-MASVS-STORAGE/ |
| E02-08 | OWASP Android storage testing | Consider leaked sensitive data and minimize unnecessary local exposure; future security testing needed | https://mas.owasp.org/MASTG/0x05d-Testing-Data-Storage/ |
| E02-09 | Google Play — account deletion rules | If accounts may be created from within app, corresponding account deletion requests/paths are subject to applicable policy | https://support.google.com/googleplay/android-developer/answer/13327111?hl=en |
| E02-10 | Google Play — User Data policy | Collection/use/deletion/privacy obligations depend on actual app distribution and data behavior | https://support.google.com/googleplay/android-developer/answer/10144311?hl=en |
| E02-11 | ETS official TOEIC L&R | Two timed sections: Listening 100/~45m, Reading 100/75m. Does not authorize equivalence of our raw scores to ETS scaled scores | https://www.ets.org/toeic/about/listening-reading.html |
| E02-12 | ETS TOEIC L&R FAQ | Official format 200 questions across two sections; forms may require calibrated score equating for official scores | https://www.ets.org/toeic/about/faq/product-specific-faq/toeic-listening-reading.html |

## Internal evidence anchors (not independent tests)

| ID | Signed / current internal record | Reliance |
|---|---|---|
| I02-01 | `STAGE03_PRD_BASELINE_CANDIDATE_V0.6.md`, `STAGE03_SRS_BASELINE_CANDIDATE_V0.6.md`, `STAGE03_ACCEPTANCE_CATALOGUE_CANDIDATE_V0.4.md` | Normative MVP, FR/NFR and test acceptance |
| I02-02 | `STAGE04_DESIGN_BASELINE_CONTROLLED_ARTIFACT_MANIFEST_V1.0.md` and `STAGE04_UI_V03_DESIGN_BASELINE_CANDIDATE_V0.3.md` | Approved UI/copy semantics, static illustration only |
| I02-03 | `STAGE05_ARCH01_DRIVER_REGISTER_V0.1.md` / Evidence Gap & Conflict Watchlists | Original AD01..16, EG01..16, CW01..10 |
| I02-04 | `STAGE04_TO_STAGE05_ACTIVE_CONDITIONS_V1.0.md`, `STAGE03_TO_STAGE04_ACTIVE_CONDITIONS_V1.0.md` | Carry-forward Gate conditions |
| I02-05 | D03-SCOPE-009 and D03-BASELINE-010 approval records | Approved Full Mock integrity, deletion ≤7 calendar days and ordinary retention ≤30 days after pilot unless authorized exception |

## Status meanings

- `SOURCE CONFIRMED`: an official statement directly supports a *platform/standards* observation.
- `ANALYST COMPARISON`: a falsifiable model hypothesis; not a selected design.
- `PO-ATTESTED`: inventory/rights and directives; don't demand repeat proof as busywork.
- `QA NOT RUN`: no app, physical devices, actual real-user session or item-level test evidence.
- `D05-TECH-003 PENDING`: no technical model selection, no authority to turn any diagram or model into an implementation.

**Research limitation:** Several platform statements are version/target-dependent; applicability to a future build cannot be affirmed before the later target-Android/version decision and real testing.
