# Stage05 Fast Track — 48h Internal Preview / 14-day Google Play Readiness V0.1

**STATUS:** PO schedule-acceleration directive, 2026-11-22. Reversible engineering work toward a limited 2-person internal preview is in scope. NOT a blanket QA, pilot, content-release or public Play authorization.

**Target 1:** 2026-11-24, installable offline Android APK for two consenting internal evaluators. **Target 2:** 2026-12-06, Play Internal/Closed Testing upload-ready AAB and compliance package. These are engineering targets and NOT guaranteed outcomes or approval to publish Production.

**Branch:** development/fasttrack-48h-preview. Base: ingestion/listening-overnight-bounded commit a0253b5e899b643ecc261323b603db3cca1073fc.

## Facts and blocking gates

The current Kotlin/Compose app has synthetic Reading Part5–7 and DEMO Listening Part1–4 with generated tone WAVs, not a production media bank. Full Mock A/B is blocked; no backend/production durable ACK/authoritative clock. The isolated Zenlish ingestion obtained four groups, eight questions, four real MP3s and one PNG stored privately under ignored android-app/.tooling/listening-overnight/. The answer key for ALL eight remains unverified, compressed decoding and semantic listening review NOT RUN, two group data structures PARTIAL. Do not promote those files to verified app content or check them into public GitHub. PO has affirmed source rights, but individual clip chain-of-rights and content QA evidence remain separate from that declaration.

Stage05 conditional Development transition, G05-CP01..08 ACTIVE, POL01..16 OPEN, 2 independent 200-question B1 mock forms mandatory before real Full Mock pilot availability, budget DEFERRED. Nothing here changes the signed Vision/PRD/SRS/Acceptance/Design/guardrails or formal QA.

**Google Play as of 2026-11-22:** new mobile apps must target API36+ (https://support.google.com/googleplay/android-developer/answer/11926878). Current Gradle app targets API35 although it compiles API36. New personal developer accounts created after Nov13 2023 require 12 opted-in closed testers continuously for 14 days before applying for Production access (https://support.google.com/googleplay/android-developer/answer/14151465). Internal testing track is different and can serve a small group. Review times are external. Do not promise a December 6 public production launch.

## Priority order and four large Codex batches

### FAST-01 — 48h engineering vertical slice (large prompt #1)

- Create a coherent, offline-first Android INTERNAL PREVIEW while preserving all existing source guards, synthetic notices and media locks.
- Improve Task Hub and rapid practice flow: Part navigation, safe Listening DEMO audio/playback/errors, usable Reading Part5–7, one short practice session, review of in-memory selections and transparent results where verified synthetic answer keys exist. No official TOEIC/ETS score or Full Mock comparable claim.
- Prefer two separate Android installations over accounts/backend. Local sample selection persistence is optional only if implemented safely in app-private storage, tested with clear on-device-only wording and a clear-data path; never represent local state as durable remote ACK or as production synchronization. If not safe, keep ephemeral-only state and clear messaging.
- Existing four real MP3s/questions are *local candidates*, not preapproved for APK inclusion. Use only original synthetic bundled WAV and safe synthetic questions by default. A separately documented per-asset QA + rights review is required before any real audio is bundled or shown as vetted. Work may prepare a local-only candidate import dry-run but may NOT relax official bank/Full Mock locks, publish real media, or introduce scored answers absent attributable keys.
- Improve layout (360dp, 800dp, 1.5 font), accessibility labels/touch >=48dp, safe back navigation and lifecycle. Add tests. Report Gradle build and demo APK SHA, keep APK local. Stop if safety gates prevent non-synthetic progress.

### FAST-02 — 48h stabilization + bounded technical observation (large prompt #2)

- Independently re-run Alpha/Beta/CX04 guards, ingestion 36 synthetic tests, Kotlin smoke, Android Gradle assembleDebug/testDebugUnitTest and any added tests. Keep reports honest.
- Emulator test navigation, Reading scroll context, Listening errors and completion, any locally stored demo state/clear action, battery/network-off UX if available. One or two real-device checks only with the actual consenting testers and an explicitly recorded bounded nonformal preview authorization; otherwise NOT RUN. Do NOT claim official four-week pilot, ECP/QA or universal compatibility.
- Fix P0/P1 regressions only, complete text-only docs/STAGE05_FASTTRACK_48H_ENGINEERING_REPORT_V0.1.md with PASS/FAIL/BLOCKED/NOT RUN and GO/NO-GO. APK stays local; no private logs/screenshots/media/keystore in Git.

### FAST-03 — 14d Google Play packaging (large prompt #3)

- Change targetSdk to 36 for a new mobile Play app. Test Android16 runtime and edge-to-edge and upgrade compatibility, media lifecycle, navigation, privacy, permissions and inaccessible content behaviour. Preserve old Android support according to supported baseline.
- Prepare safe bundle task (.aab) and signing instructions (no signing secrets or private keys committed), package/application naming and release versionCode. Do not upload to Play Console or spend without PO account-specific approval.
- Draft accurate Play description, Data safety answers based on actual data flows/SDKs, privacy policy text, app content/rating, screenshot checklist and other store metadata. Use only authorized source material and real app screenshots; no ETS affiliation or official score claims. A public privacy-policy URL must exist before actual store submission, not just in docs.
- Distinguish Internal Testing, Closed Testing and public Production; verify account eligibility and 12/14 rule if applicable. Generate text-only docs/STAGE05_FASTTRACK_PLAY_PACKAGE_V0.1.md. No automatic Play publication, baseline policy change, paid SDK or service.

### FAST-04 — submission-readiness audit (large prompt #4)

- Rebuild with production settings and validate AAB, targetSdk 36, manifest, startup, account/data-safety claims, secrets, provenance and release assets, crash checks and all test regressions.
- Document docs/STAGE05_FASTTRACK_PLAY_SUBMISSION_READINESS_REPORT_V0.1.md with evidence and a PO go/no-go. Mark Production BLOCKED if Play account tester obligations, content QA, actual app review, privacy or B1 scope gates remain open.
- Stop at readiness: no invented approvals or pilot results.

## Three levels of readiness — must not confuse

1. **TECHNICAL PREVIEW:** 2-person small offline non-formal use; synthetic/illustrative parts labelled; must have actual consent, safe install and no known blocker.
2. **PLAY INTERNAL/CLOSED TESTING PACKAGE:** signed AAB with policy/privacy and target API readiness; account owner must control upload, tester list and applicable approvals.
3. **PLAY PRODUCTION + full business MVP:** requires actual Play approval and all applicable signed content/QA/release gates, including B1 A/B 2x200 if representing evaluative Full Mock. No waiver implied.

Completion means engineering evidence, not formal QA/Pilot/Store approval. Codex may make reversible technical choices without microapproval, but stop before any material scope, cost, content or release authority decision.
