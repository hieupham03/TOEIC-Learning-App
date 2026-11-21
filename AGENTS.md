# Active Development Beta (PO chat-confirmed, bounded)

Read `docs/STAGE05_DEVELOPMENT_BETA_READING_UI_PO_AUTHORIZATION_V0.1.md` **before any coding**. The PO approved bounded *synthetic Reading UI development only* following Alpha Closure V0.3. Scope IDs: **BUI-01 / BUI-02 / BUI-03**, **NOT CX-04** (CX-04 remains Listening/media and is NOT authorized). Work on `development/beta-reading-ui` only. Permitted: synthetic Compose Reading UI/layout, source-level accessibility hardening, tests, Gradle build, optional local Compose Preview (engineering observations only). Not permitted: device/emulator/learner tests, formal ECP/QA, backend/API, persistence/ACK, clock, real B1/Full Mock, media, other CX-04+, costs, or signed baseline edits. Do not claim a QA PASS. Continue to obey all former G05-CP and baseline restrictions. Previous Alpha-only stop rule below is historical for the Alpha branch and is superseded **only for the narrowly authorized BUI-01..03** on this Beta branch.

---

# AGENTS.md — TOEIC Learning App / Codex instructions (latest)

## Current signed authority

PO **D05-DEV-GATE-012=A APPROVED** Stage05 Gate CONDITIONAL PASS *FOR DEVELOPMENT TRANSITION ONLY*, G05-CP01..08 **ACTIVE**, Alpha **CX-00..03 authorized** for Kotlin + Jetpack Compose, synthetic practice/Reading UI and internal engineering build/unit tests. See `docs/STAGE05_D05_DEV_GATE_012_A_APPROVAL_RECORD_V1.0.md`. Previous V6.7 handoff `PENDING` headings are historical and superseded, not permission for CX04+.

## First reads

Read `docs/PROJECT_STATE.md` first current top block, `codex_handoff/ALPHA_CX00_CX03_AUTHORIZED_CONTINUATION_V0.1.md`, signed PRD/SRS/Acceptance/Design V0.3 and UI-G01..16. **Never edit approved baseline bytes.**

## What can be done without another PO question

Within CX00..03, fix Android compile/build tooling, UI layout, synthetic Part selection/Part5 practice/Part6–7 Reading, unit tests and in-scope local engineering checks. Report evidence honestly; do not claim Android build PASS unless actually executed. Kotlin/Compose is only a scoped Alpha client technology choice.

## Explicit stop conditions

**NO** CX04+, actual media/Full Mock B1, real account/data, production storage/ACK, remote API/backend/DB/authentication, clock authority, ARCH03 A/B/C trust choice, ARCH04, formal ECP/QA, real-device/learner testing or spending. All POL01..16 concrete decisions remain OPEN. B1 two independent PO-inventoried 200Q mocks mandatory but unverified; do not copy real content or claim ETS equivalence. P05–P08 documentary rule subsets only. Budget remains DEFERRED.

## Required progress report

List file paths changed, FR/AT links, commands and actual PASS/FAIL/NOT RUN, usability/technical risks, then next **material** PO decision only if needed. No repetitive micro-approvals.
