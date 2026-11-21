# Development Beta Reading UI — Engineering Report V0.2

This update records the BUI-02 correction for [GitHub Issue #1](https://github.com/hieupham03/TOEIC-Learning-App/issues/1) on `development/beta-reading-ui`. The [Beta Reading UI authorization](STAGE05_DEVELOPMENT_BETA_READING_UI_PO_AUTHORIZATION_V0.1.md) defines the development scope. [V0.1](STAGE05_BETA_READING_UI_ENGINEERING_REPORT_V0.1.md) documents the preceding BUI-01..BUI-03 implementation.

## Finding and correction

In commit `14f8f38`, the Reading column applied `fillMaxSize()` before `widthIn(max = 720.dp)`. The fill set a tight width constraint, so the downstream width cap could not narrow the column on a wide layout. The column now applies the cap first, fills the resulting width and available height, and uses `Alignment.TopCenter`. The cap covers the shared column for both passage and questions, including their existing gutters. [Android Developers — Constraints and modifier order](https://developer.android.com/develop/ui/compose/layouts/constraints-modifiers)

Traceability is BUI-02, Design V0.3 and UI-G07/UI-G11, with FR-004 / AT-04 as the existing Reading references. Source review covers modifier ordering and placement.

| Changed path | Purpose |
|---|---|
| `android-app/app/src/main/java/vn/toeiclearning/alpha/ui/AlphaApp.kt` | Apply the width cap before filling the available space. |
| `android-app/scripts/check_beta_reading_ui_scope.py` | Check the Reading column's modifier chain in order, with whitespace normalized. The previous guard checked only for the presence of `widthIn`. |
| `docs/STAGE05_BETA_READING_UI_ENGINEERING_REPORT_V0.2.md` | Record the fix and observed engineering evidence. |

## Local engineering checks

Commands ran from `android-app` with JDK 17, Android SDK 36, Gradle 8.13 and Kotlin CLI 2.2.21.

| Command | Result | Exit |
|---|---|---:|
| `python .\scripts\check_alpha_scope.py` | PASS, 10/10 checks | 0 |
| `python .\scripts\check_beta_reading_ui_scope.py` | PASS, 11/11 checks, including modifier order | 0 |
| `.\scripts\run_pure_kotlin_core_checks.ps1 -KotlinHome .tooling\kotlin-compiler-2.2.21\kotlinc -JavaHome .tooling\jdk17` | PASS, 25 assertions | 0 |
| `.\gradlew.bat --offline --no-daemon --console=plain :app:assembleDebug :app:testDebugUnitTest --rerun` | PASS, both tasks executed. Gradle reported `BUILD SUCCESSFUL in 28s`. | 0 |

The new regression check rejected the original modifier order with exit `1` and accepted the corrected order with exit `0`. An intermediate run also rejected a comment placed before the modifier argument. Moving the comment above the column restored the guard match.

- JUnit XML at `app/build/test-results/testDebugUnitTest/TEST-vn.toeiclearning.alpha.domain.AlphaRulesTest.xml` records 4 tests, 0 failures, 0 errors and 0 skipped.
- Debug APK at `app/build/outputs/apk/debug/app-debug.apk` has SHA-256 `e6e644c85495572238a8f0724a7c1c8a01588b7cec4aa9e36fc4594fb76f1db4`. The APK and generated XML are ignored by Git.
- The six baseline and guardrail SHA-256 values match the [controlled manifest](STAGE05_ALPHA_CX00_CX03_SOURCE_AND_CONTROL_MANIFEST_V0.1.md).

## Evidence limits

Rendered width, text wrapping at different font scales, Compose Preview, device/emulator execution, learner testing, ECP and formal QA are **NOT RUN**. The regression check covers source order. G05-CP01..08 are ACTIVE and the budget is DEFERRED.
