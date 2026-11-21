# Synthetic Android Emulator UI Engineering Report V0.1

- **Run date** 2026-11-21 (Asia/Saigon)
- **Branch** `validation/android-ui-synthetic`
- **Start HEAD** `323607986d436bc795fe605c58f6a32ef802f61a` after `git pull --ff-only` reported up to date. The app matched Beta `cd2fc2e97bcf6f5a1e7cd1e30098c62de0f83024` before the UI fix.
- **Scope** Observations use synthetic fixtures and the Debug build. [EUI-01..03 authorization](STAGE05_SYNTHETIC_ANDROID_EMULATOR_UI_CHECK_AUTHORIZATION_V0.1.md) and [GitHub Issue #2](https://github.com/hieupham03/TOEIC-Learning-App/issues/2).

## EUI-01 — Local engineering checks

Windows with Temurin JDK 17.0.21.1, Kotlin CLI 2.2.21, Gradle wrapper 8.13 and Android SDK 36. The following commands ran from `android-app`. Initial and post-fix runs returned exit `0`.

| Command | Result after fix |
|---|---|
| `python .\scripts\check_alpha_scope.py` | PASS, 10/10 |
| `python .\scripts\check_beta_reading_ui_scope.py` | PASS, 11/11 |
| `.\scripts\run_pure_kotlin_core_checks.ps1 -KotlinHome .tooling\kotlin-compiler-2.2.21\kotlinc -JavaHome .tooling\jdk17` | PASS, 25 assertions |
| `.\gradlew.bat --offline --no-daemon --console=plain :app:assembleDebug :app:testDebugUnitTest --rerun` | PASS, both tasks executed. `BUILD SUCCESSFUL in 30s`. |
| `aapt dump permissions app/build/outputs/apk/debug/app-debug.apk` | PASS, exit `0`. The only requested permission is the app's signature-protected dynamic-receiver permission. No Android INTERNET permission. |

JUnit XML under `app/build/test-results/testDebugUnitTest/` recorded 4 tests, 0 failures, 0 errors and 0 skipped. All six baseline/guardrail hashes match the [controlled manifest](STAGE05_ALPHA_CX00_CX03_SOURCE_AND_CONTROL_MANIFEST_V0.1.md).

## EUI-02 — Local emulator observations

Android Emulator 37.2.13.0 with WHPX and a separate `TOEIC_EUI_API34` AVD using the already installed Android 14 / API 34 Google APIs x86_64 image. The AVD booted locally. The command used `emulator -avd TOEIC_EUI_API34 -port 5560 -no-window -no-snapshot -no-audio -gpu swiftshader -memory 3072 -cores 2`. Both APK installs returned success. ADB commands targeted this AVD by serial.

One AVD ran two measured display configurations with `adb shell wm size` and `wm density`. Font scale was set via `adb shell settings put system font_scale`. Display widths in dp use `px × 160 / dpi`. The physical AVD setting was 1080 × 1920 px at 420 dpi.

| Context | Effective display | Font scale |
|---|---|---:|
| Compact default | 1080 × 2160 px at 480 dpi, 360dp wide | 1.0 |
| Wide default | 1200 × 1000 px at 240 dpi, 800dp wide | 1.0 |
| Compact enlarged | 1080 × 2160 px at 480 dpi, 360dp wide | 1.5 |

### Finding and source fix

**FAIL on the initial enlarged Part 7 screen.** At 360dp and 1.5, open Part 7, then tap “Sang câu hỏi”. The long notice in the fixed header wrapped to five lines. The question viewport was only 331 px high (approximately 110dp), and the question selector was below the initial viewport. The local check exited `1` when it attempted to select question 2 directly.

The fix shortens the fixed Reading notice to “Vị trí đọc chỉ được giữ trong màn hình này.” The existing header still labels the data synthetic and the note still limits the promise to the current screen. The change is confined to BUI-02, Design V0.3, UI-G07/UI-G11/UI-G16, and the existing Reading trace FR-004 / AT-04.

**OBSERVED after the fix at 360dp / 1.5.** The notice wraps to two lines. The passage viewport grew to 628 px (about 209dp), and question 2 was visible and selectable when both question screens opened. Part 6 returned via “Về đoạn văn”, and Part 7 via Android Back. In both cases, visible passage text and bounds matched the scrolled snapshot captured before opening questions. The recheck exited `0`.

The initial APK also showed these flows in all three configurations: the three tabs navigated to their expected screens, Part 1–4 buttons were disabled, Part 5 showed the synthetic explanation only after the explicit reveal action, and Full Mock A/B showed “CHƯA THỂ BẮT ĐẦU” and the unmet QA conditions. These code paths sit outside the changed Reading notice.

**OBSERVED after the fix at 800dp / 1.0.** Both Reading passages moved when swiped inside the list and returned to the captured anchor. At 240 dpi, the UI hierarchy bounds for both lists ran from x=60 to x=1140 on the 1200 px display. That is a centered 1080 px / 720dp passage viewport in this configuration. The screenshot shows the centered text column. The recheck exited `0`.

**OBSERVED after the fix at 360dp / 1.0.** Both Parts scrolled, opened questions, selected question 2 and returned to the captured passage positions. The recheck exited `0`.

The inspected Reading labels used multiple lines at 1.5 where needed. In the final Part 7 samples, “Sang câu hỏi” and the selected question button measured 144 px high at 480 dpi and 72 px at 240 dpi, both equivalent to 48dp high. The sampled text and controls were visually distinguishable. At 360dp / 1.5, a follow-up reached answer C by scrolling and returned to the passage using the lower “Đọc lại đoạn văn” action (exit `0`). The logcat crash buffer was empty. The inspected main/system log recorded no app crash or ANR event.

## EUI-03 — Evidence and publication

- Changed paths are `android-app/app/src/main/java/vn/toeiclearning/alpha/ui/AlphaApp.kt` and this report.
- Initial APK SHA-256 is `e6e644c85495572238a8f0724a7c1c8a01588b7cec4aa9e36fc4594fb76f1db4`. Rebuilt APK SHA-256 is `99a6dc6109e5ce736535287fd6fcb417aa39904b232a89ceed2716874d686b05`.
- Local evidence is under the ignored `android-app/.tooling/eui-validation/` directory. Original screenshots and UI XML are in `compact-1.0-recheck/`, `wide-1.0/` and `compact-1.5/`. Post-fix screenshots and XML are in `final-compact-1.0/`, `final-compact-1.5/` and `final-wide-1.0/`. Startup and command logs, `emulator-logcat.log` and `emulator-crash.log` are in the same local evidence directory. The final build outputs are in ignored `android-app/app/build/`. The public commit contains source and this text report.
- **NOT RUN** applies to real Android hardware, learners, formal ECP/QA, TalkBack, quantitative contrast, process-death recovery, and configurations outside the sampled widths and font scales. G05-CP01..08 are ACTIVE and the budget is DEFERRED.
