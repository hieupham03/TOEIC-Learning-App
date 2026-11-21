# Stage05 Development Alpha CX-00..03 — Consolidated Review V0.1

**Status:** BOUNDED SOURCE IMPLEMENTATION DELIVERED; **ALPHA VERIFICATION PARTIAL** (Android build NOT RUN). **Authority:** D05-DEV-GATE-012=A, development-transition conditional Gate.

## Completed code deliverables

- **CX-00:** Native Compose Android module, minimal teal typography/spacing and 3 tabs `Bắt đầu | Tiến độ | Cá nhân`; pure synthetic application shell.
- **CX-01:** Part 1..7 selection with QA gate. Parts1–4 disabled without audio/QA; Part5–7 synthetic-only UI. Two mandatory B1 Full Mock forms informational and entirely blocked.
- **CX-02:** Part 5 deterministic synthetic question selection; explicit *temporary/not saved* status; explanation only after a user chooses and explicitly requests demo feedback; no fake QA-ready content.
- **CX-03:** Part 6/7 authored long synthetic reading text; passage-question switching preserves in-session passage lazy-scroll object and selected question ID. No promise of persistence across process kill, no actual device test.

## Actual observed verification

- Kotlin 1.9 CLI compilation and local JVM **22 checks PASS**; static permission/scope guard **10 checks PASS**.
- **NOT RUN:** Gradle Android assembly, Gradle JUnit, UI instrumentation, device or emulator, accessibility on-device, full system QA; no APK. See `STAGE05_ALPHA_CX00_CX03_VERIFICATION_LOG_V0.1.md`.

## Deviations and boundaries

- The tool environment lacks Android SDK/Gradle and no Codex external execution connector is available. Source was authored locally for follow-up by Codex/Android Studio, not an autonomous external Codex run. No build/screenshot was invented.
- Android plugin/dependency version pins are **reversible Alpha toolchain choices**, not architecture/vendor/production authority. Use official release notes to revalidate dependencies during first real Gradle sync.
- `remember`/`rememberSaveable` used for UI-only in-screen state; no ACK, clock, remote database, real account, data deletion, audio playback or Full Mock implementation.
- `PracticeFeedback` is explicitly synthetic, not validated TOEIC correctness; no official ETS score conversion.

## Next action without new material scope

Open `android-app/` in Codex or Android Studio with Android SDK 36, Gradle 8.13 and JDK 17+, generate standard wrapper with the included script if needed, run `:app:assembleDebug :app:testDebugUnitTest`, capture honest build/test evidence and fix **only CX00..03 engineering issues**. Since this is part of the already signed Alpha, there is no need to request PO per build failure.

## Material boundary requiring future PO decision

Stop before CX04 media, CX05 durable ACK, CX06 live Full Mock, accounts/privacy/pilot, ECP formal verification, new backend or architecture-selection. Request a single later scoped authorization only when needed, after the above Alpha proof is available.
