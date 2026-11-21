# TOEIC Learning App — Codex handoff (Alpha AUTHORIZED)

**Latest decision:** PO `D05-DEV-GATE-012=A` approved CONDITIONAL Stage05 Gate for bounded development and implementation of **CX-00..CX-03** only. This replaces the old `PENDING` banner in the V6.7 handoff but does not approve CX-04+. See formal record in `docs/STAGE05_D05_DEV_GATE_012_A_APPROVAL_RECORD_V1.0.md`.

## Read in order

1. `docs/PROJECT_STATE.md` TOP authoritative block (history below is archived).
2. `docs/STAGE05_D05_DEV_GATE_012_A_APPROVAL_RECORD_V1.0.md` + `docs/STAGE05_G05_ACTIVE_CONDITIONS_V1.0.md`.
3. Exact signed PRD/SRS/Acceptance V0.6/V0.4, Design-Spec V0.3 and UI-G01..16 (do not modify).
4. `android-app/README.md`, `codex_handoff/ALPHA_CX00_CX03_AUTHORIZED_CONTINUATION_V0.1.md`.
5. `docs/STAGE05_ALPHA_CX00_CX03_VERIFICATION_LOG_V0.1.md` (truthful validation state).

## Approved execution focus

All UI content is synthetic. First verify pure Kotlin and static checks, then build and Gradle local unit test on an Android SDK/Gradle machine. Don't claim real Android/device/learner QA PASS. Use Kotlin + Jetpack Compose only for this client Alpha; don't select remote trust architecture/clock/ACK authority, backend/API/DB, execute ECP or spend. Stop before CX04+.
