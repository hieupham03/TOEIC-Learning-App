# Development Alpha CX-00..03 — Execution Report V0.2

**Authority:** PO `D05-DEV-GATE-012=A`, Stage05 conditional development transition only. This report records local engineering evidence for CX-00..03. It is not an ECP, formal QA, device test, learner test, content-QA result, pilot result, or a release approval.

## Scope delivered

| Slice | Delivered source behavior | FR / AT trace | Boundary retained |
|---|---|---|---|
| CX-00 | Kotlin + Jetpack Compose three-tab shell (`Bắt đầu`, `Tiến độ`, `Cá nhân`) and restrained V0.3 token set | FR-002/FR-009; AT-02/AT-09 | No real account, storage, network, API, backend or durable ACK |
| CX-01 | Synthetic Part 5–7 picker; Part 1–4 and Full Mock A/B visibly blocked | FR-002/FR-010/FR-017; AT-02/AT-10/AT-17 | No B1 item, media, key or Full Mock launch |
| CX-02 | In-memory Part 5 choice and sample feedback with explicit `chưa lưu bền vững` copy | FR-009; AT-09 | This does not implement FR-005 durable answer acknowledgement |
| CX-03 | Synthetic Part 6–7 passage/question view with in-session passage anchor retained on return | FR-004; AT-04 | No process-death, device readability or accessibility acceptance claim |

## Changes made during local engineering validation

- `android-app/scripts/check_alpha_scope.py`: explicitly reads UTF-8 Kotlin/XML source so the scope guard works on Windows with Vietnamese copy.
- `android-app/app/build.gradle.kts`: pins Compose BOM `2025.06.00`. The prior `2026.09.00` resolved Compose 1.12.1, which required API 37 and AGP 9.1 while this approved Alpha toolchain is API 36 / AGP 8.13.
- `android-app/gradle.properties`: limits local Gradle workers and heap, and uses in-process Kotlin compilation after the first build consumed excessive memory/GC resources.
- Standard Gradle 8.13 wrapper files were generated under `android-app/gradle/wrapper/`, `android-app/gradlew`, and `android-app/gradlew.bat`.

## Engineering evidence

| Check | Actual result | Evidence / limit |
|---|---|---|
| `python scripts/check_alpha_scope.py` | **PASS** | 10/10 static scope safeguards: no INTERNET permission, synthetic-only fixtures, B1 blocked, Part 1–4 blocked, truthful volatile-answer copy, Full Mock block, passage return, three tabs, no remote package, no media assets. Documentary source guard only. |
| `scripts/run_pure_kotlin_core_checks.sh` | **FAIL / BLOCKED in this environment** | Host Bash returned `Bash/Service/CreateInstance/E_ACCESSDENIED`; `kotlinc` was absent from PATH. The previous V0.1 log's 22 assertion result is historical authoring evidence, not repeated here. |
| `:app:assembleDebug` | **PASS — artifact observed** | Local JDK 17, Gradle 8.13, Android SDK 36. APK created at `android-app/app/build/outputs/apk/debug/app-debug.apk` (10,196,418 bytes at 2026-11-21 18:38 ICT). |
| `:app:testDebugUnitTest` | **PASS — 3/3** | `AlphaRulesTest`: 3 tests, 0 failures, 0 errors, 0 skipped; report at `android-app/app/build/test-results/testDebugUnitTest/TEST-vn.toeiclearning.alpha.domain.AlphaRulesTest.xml`. |
| Device/emulator/learner/accessibility, ECP, FM, QA01..08 and B1 content QA | **NOT RUN** | Outside authorization or requires separate future evidence; no PASS claim. |

## Risks and remaining work

- The wrapper and local toolchain only establish Alpha engineering build evidence. They do not establish real-device layout, 48dp targets, TalkBack, font scaling, contrast, two-phone Reading legibility, recovery after process death, or learner usability.
- G05-CP01..08 and all prior active conditions remain active. POL01..16 remain open; no ARCH03 choice, clock/ACK authority, backend/API/DB, B1 release, CX-04+ or spending was introduced.
- The next material PO decision is required only before a new scope beyond CX-03 or any formal QA/ECP/device/learner/B1 activity.
