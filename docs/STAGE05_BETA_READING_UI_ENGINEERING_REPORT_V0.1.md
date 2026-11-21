# Development Beta BUI-01..BUI-03 — Engineering Report V0.1

**Authority:** `docs/STAGE05_DEVELOPMENT_BETA_READING_UI_PO_AUTHORIZATION_V0.1.md`, on branch `development/beta-reading-ui` after Alpha closure `199bc0dae751e33b2f7e1306f877f461207d2cb8`.

**Claim boundary:** This is bounded internal engineering evidence only. It is not a formal ECP/QA result, UI acceptance, accessibility certification, device/emulator result, learner test, content-QA result, release approval, or authorization for CX-04..CX-09.

## Implemented BUI scope

| ID | Delivered source behavior | Reference / boundary |
|---|---|---|
| BUI-01 | Added an in-memory `ReadingSession`/`ReadingPane` model. Before opening questions, the current passage list anchor is captured; returning to passage restores that anchor in the same open composition. The passage list has stable paragraph keys and the question picker scrolls horizontally. | Existing CX-03, FR-004 / AT-04, W-02A. No process-death or durable recovery claim. |
| BUI-02 | Applied a 16dp/20dp responsive Reading gutter, 720dp maximum readable measure, existing 16sp body typography, source-targeted 48dp controls, and Compose semantics for question selection and radio choices. Teal V0.3 token use remains unchanged. | Design V0.3 / UI-G01..16. Source intent only; no device/accessibility PASS claim. |
| BUI-03 | Added a Beta static guard and one deterministic JVM state test for capture/select/return Reading navigation. Expanded the pure Kotlin smoke assertion count. | Internal engineering safeguard only. |

## Files changed

| Path | Purpose |
|---|---|
| `android-app/app/src/main/java/vn/toeiclearning/alpha/domain/AlphaModels.kt` | In-memory `ReadingSession` state transitions. |
| `android-app/app/src/main/java/vn/toeiclearning/alpha/ui/AlphaApp.kt` | Bounded Reading layout, navigation, touch-target and semantic source changes. |
| `android-app/app/src/test/java/vn/toeiclearning/alpha/domain/AlphaRulesTest.kt` | Deterministic BUI Reading-session test. |
| `android-app/tests/pure-kotlin/AlphaCoreSmokeTest.kt` | Deterministic BUI Reading-session smoke assertions. |
| `android-app/scripts/check_beta_reading_ui_scope.py` | BUI source boundary guard. |
| `docs/STAGE05_BETA_READING_UI_ENGINEERING_REPORT_V0.1.md` | This report. |

## Executed engineering evidence

| Command / artifact | Actual result |
|---|---|
| `python .\\scripts\\check_alpha_scope.py` | **PASS**, exit code `0`; 10/10 Alpha documentary checks remain intact. |
| `python .\\scripts\\check_beta_reading_ui_scope.py` | **PASS**, exit code `0`; 11/11 BUI documentary checks, including synthetic-only fixtures, in-memory Reading state, responsive source layout, 48dp targets and no remote/media addition. |
| `.\\scripts\\run_pure_kotlin_core_checks.ps1 -KotlinHome .tooling\\kotlin-compiler-2.2.21\\kotlinc -JavaHome .tooling\\jdk17` | **PASS**, exit code `0`; 25 assertions. This is a pure local JVM CLI check, not an Android build or device test. |
| `.\\gradlew.bat --offline --no-daemon --console=plain :app:assembleDebug :app:testDebugUnitTest` | **PASS**, Gradle exit code `0`; `BUILD SUCCESSFUL in 13s`. Local JDK 17, Android SDK 36 and Gradle 8.13 wrapper. |
| `app/build/test-results/testDebugUnitTest/TEST-vn.toeiclearning.alpha.domain.AlphaRulesTest.xml` | **PASS** — 4 tests, 0 failures, 0 errors, 0 skipped, `0.045` seconds. Generated XML is ignored and not committed. |

## Controls, limits and NOT RUN evidence

- Signed baseline bytes were not edited. The implementation retains the Design V0.3 token set and content-first Reading direction, while the authorization itself remains the governing scope for BUI-01..03.
- Existing disabled Part 1..4, disabled B1 Full Mock A/B, synthetic Part 5–7 fixtures, no `INTERNET` permission, no account/backend/API/remote DB, no media, no timer/clock authority and no durable answer acknowledgement remain unchanged.
- Compose Preview, Android emulator, Android real-device execution, screenshot review, font-scale/rotation/process-death verification, TalkBack, contrast measurement, learner usability, ECP, formal QA and content QA are **NOT RUN**. Source targets such as 48dp and semantics are not evidence of physical-device accessibility acceptance.
- G05-CP01..08 and all retained Stage02/03/04 conditions remain ACTIVE. QA remains not PASS, POL01..16 remain open, ARCH03 A/B/C remains unselected and the budget remains DEFERRED.

## Technical/usability risks and next material decision

Long-passage return is verified only as deterministic in-memory state and local Compose source; its readability and behavior across real Android widths, system font scales, rotation, process death and assistive technology remain unverified. The next material decision is PO authorization only if it wants a further Beta slice or separately bounded device/QA evidence; this report authorizes neither.
