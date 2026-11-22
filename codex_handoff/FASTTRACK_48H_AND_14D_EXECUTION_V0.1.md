# Codex handoff — FAST-01..04 accelerated execution

The PO wants an **installable two-person internal trial by 2026-11-24** and **Google Play-ready testing bundle by 2026-12-06**. Treat these as hard prioritization/timeboxes, NOT permission to misrepresent QA or bypass any signed control. Branch: development/fasttrack-48h-preview; parent commit a0253b5e899b643ecc261323b603db3cca1073fc. READ AGENTS.md and docs/STAGE05_FASTTRACK_48H_PREVIEW_14D_PLAY_PLAN_V0.1.md FIRST.

## First working session — FAST-01, P0

Build a useful coherent **offline internal demo**. On an existing Compose project:
- keep Listening Part1–4 DEMO and Reading Part5–7, and keep actual bank+Full Mock locked;
- improve onboarding/start practice/single question/choose/review/back/resume UX, large font and 48dp controls;
- show accurate only-illustrative answer state. If adding app-private persistence, test write/read, clear data, separate-device/no-account isolation and label it **on-device only**, never authoritative saved ACK;
- validate source mapping against local ingestion manifests using synthetic-only fixtures. Existing 4 real Zenlish groups have no verified keys and must not be silently shipped as scored, QA-ready content or checked into public Git;
- run full build and unit tests and create a debug APK locally. No services, cost, paid libraries, backend, official Full Mock, content promotion or signed baseline edits.

Deliver safe source/test diffs + text-only engineering log with actual exits. Commit and push this branch. Fix reversible P0/P1 issues autonomously.

## Second working session — FAST-02, P0

Review the previous commit as a separate phase. Rebuild, run guards, 36 ingestion tests, core Kotlin smoke, Gradle assembleDebug/testDebugUnitTest, emulator 360dp+large font and 800dp, main flow, playback errors, Reading passage return, back/restart/clear, privacy posture. Run one/two consenting real-device preview checks ONLY IF the PO has recorded explicit authorization for this bounded nonformal observation and phones are actually available; else NOT RUN. Write docs/STAGE05_FASTTRACK_48H_ENGINEERING_REPORT_V0.1.md; include exact APK SHA, test outcomes, build instructions and GO/NO-GO. **Do not call it formal learner pilot.**

## Third working session — FAST-03, P1

Check current Google Play policy from official primary documentation if web tools available. New mobile Play app targetSdk must be API36+. Upgrade targetSdk, test Android16 compatibility and app lifecycle/edge-to-edge. Produce safe AAB **locally**, with signing and secrets local only; no Play Console upload without the PO's account-specific authorization. Prepare accurate store text/screenshots/privacy-policy and Data safety checklist as *drafts* based on audited functionality and SDKs; don't claim no data collected unless actually audited. Explicitly check developer account class, 12 continuous testers for 14d if newly created personal account, and unresolved Play production eligibility. Deliver docs/STAGE05_FASTTRACK_PLAY_PACKAGE_V0.1.md; do not publish.

## Fourth working session — FAST-04, P1

Independent preflight all guards, unit/build tests, AAB targetSdk/permissions, content rights and QA, privacy/security, test-track readiness. Produce docs/STAGE05_FASTTRACK_PLAY_SUBMISSION_READINESS_REPORT_V0.1.md with GO/NO-GO and production blockers, without false CI/Play verification. Do not start new features past FAST-04 or announce Production submitted.

## Continuous rules

- Timebox each session and prefer finishing a functional vertical slice with tests over scaffolding unsupported functionality.
- Can autonomously choose reversible implementation details and fix compiler issues inside scope. Do not wait for microapproval.
- Stop for material rights/QA, real-content integration, B1 mock, external two-user testing without explicit scoped approval, cloud/backend, official durable ACK/timer, paid service, signing/upload/account or release authorization. Record exact blocker instead.
- Keep raw scraped third-party audio/HTML/questions/keys and original user media in gitignored local tooling; public repo receives only safe original code, synthetic fixtures, metadata schema and text reports.
- Do not run indefinitely or claim tomorrow's deliverable is guaranteed. STOP at the agreed engineering evidence boundary.
