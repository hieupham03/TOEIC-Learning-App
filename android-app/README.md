# TOEIC Learning App — Bounded Development Alpha CX-00..CX-03

**Authority:** Product Owner `D05-DEV-GATE-012=A`, CONDITIONAL Stage05 Gate **FOR DEVELOPMENT TRANSITION ONLY**. This is not a verified production architecture, a pilot-ready TOEIC app, or proof of any ECP/QA result.

## What the Alpha provides

- **CX-00:** Android Native Kotlin + Jetpack Compose, three text-labelled tabs (`Bắt đầu`, `Tiến độ`, `Cá nhân`), minimal teal theme honoring signed Design Baseline V0.3 and UI-G01..16.
- **CX-01:** Part 1–7 picker; Parts 1–4 are blocked due to missing QA/audio. Parts 5–7 use original **synthetic fixture** text only. Full Mock A/B blocked; PO-inventoried B1 content is *not* copied into app.
- **CX-02:** Part 5 demo practice: temporary choice, explicit reveal of sample explanation, clear **chưa lưu bền vững**. No production ACK or real scoring.
- **CX-03:** Part 6 and 7 long synthetic passages, switch to linked questions and return to passage without resetting the in-session scroll state; large-font/device QA pending.

No `INTERNET` permission or real user accounts; no storage, backend, timer, audio player, durable acknowledgment, ETS conversion, real item keys or Live Full Mock.

## Reproduce the checks

Local pure Kotlin core test without Android SDK:

```bash
./scripts/run_pure_kotlin_core_checks.sh
```

Build Android app on a **properly configured** Android Studio / Gradle machine (Android SDK 36, JDK 17+, Gradle 8.13, Android Gradle Plugin 8.13.2, Kotlin 2.2.21). **The build was not run in the authoring environment**, where Android SDK and Gradle are unavailable.

```bash
# After Gradle 8.13 and Android SDK are available:
./scripts/prepare_android_gradle_wrapper.sh  # creates standard gradlew + wrapper JAR
./gradlew :app:assembleDebug :app:testDebugUnitTest
```

The generated wrapper JAR is deliberately not faked or silently downloaded. If the versions fail Gradle sync, log the exact incompatibility and adjust only reversible Alpha toolchain details (with no change to trusted architecture or signed product baseline).

## Security, legal and correctness boundaries

- **Synthetic data are not QA-approved learning content**, and preview explanation is never described as vetted production answer.
- ``PracticeState`` is in-memory and is *not a durable ACK*. Do not label a choice as confirmed/saved.
- Reading passage state is restored when switching to/from questions **within the same open screen**; no claim of recovery after a process kill or reboot.
- B1 two separate 200-question Full Mock forms remain mandatory but intentionally inaccessible. The inventory was affirmed by PO; per-item QA has not been run.
- Real-device, learner usability, accessibility, security and content QA = **NOT RUN**. All conditional Gate controls and policy gaps remain active.
- Dev can choose cosmetic/typing and build-environment details in CX-00..03; may **not** start CX-04+, choose trust architecture ARCH03-A/B/C, clock/ACK authority, backend/API/database, or spend.

## Reference

Read `../docs/PROJECT_STATE.md` top current block, `../docs/STAGE05_D05_DEV_GATE_012_A_APPROVAL_RECORD_V1.0.md`, the unchanged signed PRD/SRS/Acceptance and UI baseline, and `../codex_handoff/README_START_HERE.md` before further work.
