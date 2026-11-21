# Development Alpha CX-00..03 — Actual Verification Log V0.1

**Environment:** 2026-11-21 authoring container; JDK 21 available, Kotlin CLI 1.9.0 available. **Gradle executable absent; Android SDK / android.jar absent. No dedicated Codex agent tool attached.**

| Check | Command / evidence | Actual result | Classification |
|---|---|---|---|
| Pure Kotlin core compile + deterministic assertions | `cd android-app && ./scripts/run_pure_kotlin_core_checks.sh` | **PASS: 22 assertions**; standalone `kotlinc` compiled and Java ran | Internal *non-Android* engineering check only |
| Static scope/no-real-data safeguard | `cd android-app && python scripts/check_alpha_scope.py` | **PASS: 10 static conditions** incl XML parse and blocked B1 | Static documentary code check, not Android QA |
| `:app:assembleDebug` | Gradle / Android SDK not installed | **NOT RUN**, no APK produced | Not build PASS |
| `:app:testDebugUnitTest` | Gradle / Android SDK not installed | **NOT RUN**, JUnit source supplied | Not Android unit test PASS |
| Real device / emulator, fonts/TalkBack, 2 phone contexts | Outside this Alpha authorization and no SDK | **NOT RUN** | No UX04/UIA/QA PASS |
| ECP-00..06, FM-01..18, QA01..08, B1 item/media QA | Not authorized in Alpha | **NOT RUN** | Never call PASS |

**Interpretation:** Alpha source coverage CX00..03 implemented in repository. **Overall Alpha verification remains PARTIAL** until actual Android build and local JVM test task run in properly equipped Codex/Android Studio environment; those engineering commands remain inside the *already signed Alpha scope* and do not need a new PO micro-approval. Do not expand scope while running them.
