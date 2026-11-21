# Development Alpha CX-00..CX-03 — Engineering Closure V0.3

**Authority and boundary:** PO `D05-DEV-GATE-012=A`, Stage05 CONDITIONAL PASS for development transition only. This is a local engineering closure for CX-00..CX-03; it is **not** a formal ECP/QA pass, release approval, device/learner test, accessibility result, B1 content-QA result, or approval for CX-04+.

## Baseline and Alpha source review

The signed baseline bytes were re-hashed on 2026-11-21 and all matched the controlled manifest:

| Controlled item | SHA-256 verification |
|---|---|
| `docs/PRODUCT_VISION_V1.0.md` | PASS — `d296b085543c4646952d1572b570c1659b8b63fbcf1c61a513393a4489cca56c` |
| `docs/STAGE03_PRD_BASELINE_CANDIDATE_V0.6.md` | PASS — `0cf1981c33a7469a10c2db8a2c33e71c8e1ac12bb285fa605f0fc6d49b46ffcc` |
| `docs/STAGE03_SRS_BASELINE_CANDIDATE_V0.6.md` | PASS — `5dedf4493e6ec4f970fa3f9a26267547e1a87c30649629a831b6334118f86f08` |
| `docs/STAGE03_ACCEPTANCE_CATALOGUE_CANDIDATE_V0.4.md` | PASS — `4f07a02edeb95ebfb2cdc3743bf3c0b8e70b256a69f957b4e50d149c3b108e8b` |
| `docs/STAGE04_UI_V03_DESIGN_BASELINE_CANDIDATE_V0.3.md` | PASS — `0e04a707f4341d9ccbdd949bed2c18688fcc70d47476ff32d73114cfdbab17bb` |
| `docs/STAGE04_UI_AI_ANTIPATTERN_GUARDRAILS_V1.0.md` | PASS — `801a526babc74f73dfa01d8314ca9b78092a162d604b163eff63da373a47f57a` |

Initial Alpha source (commit `fa76435`) was reviewed against `AGENTS.md`, `android-app/README.md`, the D05 record, G05 active conditions, Alpha handoff/scope, signed Design V0.3 and Alpha traceability. Static review found no prohibited scope creep: no internet permission, real account/data, persistence/ACK, backend/API/remote DB, media, real B1 content, Full Mock launch, timer/clock authority, or ARCH03 selection. Maintainability observations (route branching and synthetic string IDs) are proportional to the deliberately bounded Alpha and are not changed here.

The historical traceability document's CX-00 reference to FR-001 must not be read as a claim that real goal/level/duration capture was delivered. This closure retains the bounded implementation links: CX-00 FR-002/FR-009 and AT-02/AT-09; CX-01 FR-002/FR-010/FR-017 and AT-02/AT-10/AT-17; CX-02 FR-009/AT-09; CX-03 FR-004/AT-04. No signed baseline or historical traceability bytes were edited.

## Closure changes

| Path | Change | FR / AT link |
|---|---|---|
| `android-app/scripts/run_pure_kotlin_core_checks.ps1` | Added native Windows PowerShell runner for the existing pure Kotlin domain smoke test. It accepts explicit `-KotlinHome` and `-JavaHome`, creates only a temporary JAR, and removes it on exit. | CX-01..03 engineering safeguard; no product FR/AT claim |
| `android-app/tests/pure-kotlin/AlphaCoreSmokeTest.kt` | Corrected terminal wording so the pure-Kotlin result does not make a stale Android-build claim. | CX-01..03 engineering safeguard |
| `android-app/README.md` | Reconciled historical toolchain wording with current bounded closure evidence and documented the PowerShell command. | Handoff clarity only |
| `docs/STAGE05_ALPHA_CX00_CX03_ENGINEERING_CLOSURE_V0.3.md` | Added this closure record, evidence, risks and decision proposal. | Engineering evidence only |
| `docs/STAGE05_DEVELOPMENT_BETA_SCOPE_PROPOSAL_V0.1.md` | Added an explicitly unapproved PO review proposal; no Beta source was created. | No implementation claim |

## Executed evidence

All commands below used local JDK 17, Android SDK 36 and the checked-in Gradle 8.13 wrapper. Generated files remain ignored and were not staged.

| Command / evidence | Actual result |
|---|---|
| `python .\\scripts\\check_alpha_scope.py` | **PASS**, exit code `0`; 10/10 documentary scope checks. It is a static source guard, not compiler/QA evidence. |
| `.\\scripts\\run_pure_kotlin_core_checks.ps1 -KotlinHome .tooling\\kotlin-compiler-2.2.21\\kotlinc -JavaHome .tooling\\jdk17` | **PASS**, exit code `0`; `ALPHA PURE-KOTLIN CORE CHECKS: PASS (22 assertions)`. This is a JVM CLI smoke test, not an Android build or device test. |
| `.\\gradlew.bat --offline --no-daemon --console=plain :app:assembleDebug :app:testDebugUnitTest` | **PASS**, Gradle exit code `0`; `BUILD SUCCESSFUL in 14s`, 43 actionable tasks (up-to-date). |
| JUnit XML: `android-app/app/build/test-results/testDebugUnitTest/TEST-vn.toeiclearning.alpha.domain.AlphaRulesTest.xml` | **PASS** — suite `vn.toeiclearning.alpha.domain.AlphaRulesTest`; tests `3`, failures `0`, errors `0`, skipped `0`, time `0.064`. |
| APK: `android-app/app/build/outputs/apk/debug/app-debug.apk` | Generated locally only; **not committed**. Size `10,196,418` bytes; SHA-256 `946d6c070fba059caa0d85e8573c52857138fa8f8680d418316ce25d287cdffd`; observed 2026-11-21 18:47:57 +07:00. |

## Limits, risks and active controls

- G05-CP01..08, all prior CPs, QA statuses, POL01..16 and the DEFERRED budget remain unchanged and active.
- Device/emulator rendering, 48dp target verification, TalkBack, font scaling, contrast, rotation, process-death recovery, learner usability, content QA, formal ECP/QA and release acceptance are **NOT RUN**. No synthetic screenshot/visual-QA artifact is asserted as acceptance evidence.
- The reading anchor is an in-session Compose state behavior only; it is not recovery, lifecycle, device, or accessibility proof.
- This closure does not approve B1, Full Mock, media, backend/API/remote DB, authentication, real data, durable answer acknowledgement, clock authority, ARCH03 A/B/C, CX-04+, spending, or an external service.

## Next material PO decision

Review and explicitly approve, reject or revise the bounded Development Beta proposal in `docs/STAGE05_DEVELOPMENT_BETA_SCOPE_PROPOSAL_V0.1.md`. No further implementation is authorized by this document.
