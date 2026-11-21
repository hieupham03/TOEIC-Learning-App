# AGENTS.md — TOEIC Learning App / Codex (current branch authority)

## Active PO decision — 2026-11-21

**D05-CX04-013=A is APPROVED BY PRODUCT OWNER**, scoped to **Development CX-04 synthetic Listening foundation only**: `CX04-L01..L03` plus **one local Android Emulator engineering smoke check**. The exact binding approval is `docs/STAGE05_D05_CX04_013_A_APPROVAL_RECORD_V1.0.md`; the detailed scope is `docs/STAGE05_D05_CX04_013_LISTENING_DEVELOPMENT_DECISION_PROPOSAL_V0.1.md`; the executable instructions are `codex_handoff/CX04_SYNTHETIC_LISTENING_AUTHORIZED_EXECUTION_V0.1.md`. **Read these before changing code.**

**Work exclusively on:** `development/cx04-listening-synthetic`. Source baseline: completed EUI engineering commit `52e0af4a051edb5832262a0720f1dd486012a4f5` (no QA PASS). Do not rewrite old branches. Preserve any local user changes safely.

The original `D05-DEV-GATE-012=A` remains Stage05 **CONDITIONAL PASS FOR DEVELOPMENT TRANSITION ONLY**. G05-CP01..08 plus all other Stage02/03/04 CPs ACTIVE, POL01..16 OPEN, budget DEFERRED. Existing Vision V1.0 / PRD-SRS V0.6 / Acceptance V0.4 / Design V0.3 / UI-G01..16 **controlled baseline bytes immutable**.

## The ONLY newly permitted behavior

- **CX04-L01:** Distinct synthetic-only Listening **DEMO/LAB** flow for Parts 1–4 with fake group/item data and visibly labelled unapproved audio/content; real Part1–4 bank stays `NOT_QA_READY`. Do not unlock Full Mock.
- **CX04-L02:** Bundled original **programmatically generated WAV tones** (NOT English speech/TOEIC), one group per Part 1–4; versioned and hash-attributed mapping `part/group/item/audio/order`; local demo play/pause/stop/replay/error states. No streaming/cloud services.
- **CX04-L03:** Fail-closed tests for missing/mismatched/duplicate/out-of-order assets, existing Reading/Part5 regressions, source guards, Kotlin smoke, Gradle build/unit tests, actual command exit codes, safety report.
- **Exactly one** local Android Emulator engineering smoke check of the synthetic audio flow; not a real phone, learner, ECP, QA or official media-integrity proof.
- Reversible implementation details may be decided autonomously. No per-file microapproval requests.

## Explicit STOP / still prohibited

No real or unverified B1/ETS Listening audio/questions, no speech/TTS or licensed/downloaded assets without separate provenance authority, no real Full Mock A/B or official scoring, no clean/comparable attempt or time/replay integrity system. Do not implement `CX05..CX09`, cloud/backend/API/remote DB, authentication, real data, app persistence/durable ACK, authoritative timer, ARCH03 A/B/C selection, ARCH04, PDF/book/audio import, real device, learner tests, QA-01..08, ECP-00..06, pilot, Play Store release, new vendor/paid tooling/spending, or any signed baseline change. Two real B1 200Q forms remain inventoried but not QA cleared.

**Traceability:** FR-003 / AT-03 are bounded design/engineering links, NOT formal PASS. FR-011 / AT-11 are boundaries only and not implemented. DEMO replay must NOT leak into Full Mock.

## Required evidence and handoff

Check the safe branch, compile Android, run existing Alpha/Beta checks and newly added Listening negative-unit checks, and run the one permitted local Android Emulator check when available. Distinguish **PASS / FAIL / BLOCKED / NOT RUN**; do not invent screenshots or auditory observations. Leave APK, emulator screenshots, raw logs and credentials local; repo is **PUBLIC**. Commit only in-scope code, safe synthetic tone fixtures, tests and `docs/STAGE05_CX04_SYNTHETIC_LISTENING_ENGINEERING_REPORT_V0.1.md`. Include changed paths, fixture hashes, actual toolchain/output and remaining evidence gaps. Stop after CX04-L01..03 and the one emulator check.

## Historical authority and preserved engineering work

Alpha CX-00..03 approved in `docs/STAGE05_D05_DEV_GATE_012_A_APPROVAL_RECORD_V1.0.md`, Beta BUI-01..03 authorized under `docs/STAGE05_DEVELOPMENT_BETA_READING_UI_PO_AUTHORIZATION_V0.1.md`, EUI-01..03 under `docs/STAGE05_SYNTHETIC_ANDROID_EMULATOR_UI_CHECK_AUTHORIZATION_V0.1.md`. Their historical "NO CX04" constraints are superseded **only** by the current explicitly scoped `D05-CX04-013=A`. No old documentary PENDING label overrides the new signed-in-chat PO decision. All other controls remain in force.
