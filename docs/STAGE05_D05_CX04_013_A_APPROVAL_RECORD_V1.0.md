# D05-CX04-013=A — Product Owner CX-04 Synthetic Listening Development Authorization V1.0

**DECISION: APPROVED BY PRODUCT OWNER — 2026-11-21.**

**Authoritative PO statement (in project conversation):** "Tôi phê duyệt D05-CX04-013=A theo đúng đề xuất CX-04 V0.1. Hãy ghi nhận quyết định, chuẩn bị nhánh Development và handoff cho Codex."

**Exactly approved option:** A in `docs/STAGE05_D05_CX04_013_LISTENING_DEVELOPMENT_DECISION_PROPOSAL_V0.1.md`, **without expansion**. This record supersedes the proposal's historical **PENDING** decision placeholder and the historical Alpha/Beta/EUI *no-CX04* restrictions only for the precise scope below, on `development/cx04-listening-synthetic`. The proposal remains preserved as the approved specification, not itself an execution authority.

## 1. Permitted bounded development

- **CX04-L01 — Synthetic Listening Part 1–4 DEMO:** a distinct clearly marked DEMO/LAB route, synthetic group/item IDs, item/answer UI and Part 1 image placeholder if needed. Real Part1–4 bank remains `NOT_QA_READY`; Full Mock A/B never unlocks.
- **CX04-L02 — Local test playback + mapping contract:** self-generated, programmatically synthesized **WAV tones only** (one distinct fixture group for each of Parts 1–4), bundled locally without Internet. Implement and inspect deterministic `groupId/itemId/audioId`, group order/version/hash mapping and local play/pause/stop/replay/error UI **for DEMO practice only**; guard absent/mismatched/invalid media.
- **CX04-L03 — Negative controls, engineering tests and report:** malformed group/media mapping, missing asset, duplicate IDs, wrong sequence and Full Mock isolation must fail closed. Run local Kotlin smoke, Alpha/Beta source guards, Debug Gradle build and local unit tests, and new Listening scoped tests; report actual exit codes and genuine observed outcomes.
- **One local Android Emulator engineering check** with the already available zero-cost environment, preferably an existing Android 14/API34+ AVD. Observe the synthetic flows, control state, media linkage, errors, Part5–7 regressions and note whether audible output is genuinely observed versus UI/transport only. The check is NOT a formal device/QA PASS.

Within these boundaries, Codex may make minor reversible technical implementation decisions autonomously, without micro-approval, using the existing Kotlin/Jetpack Compose client and Design V0.3 source style. No new vendor, paid service, or product-wide trusted architecture selection is implied.

## 2. Provenance and terminology

The WAV tone fixtures are **original test signals**, not human speech, not legitimate TOEIC lessons and not QA-READY learning content. Do not claim pronunciation, comprehension, sound quality, pedagogical validity or that FR/AT is accepted as PASS. The approved proposal requires any later synthetic spoken dialogue/TTS material to have a **separately recorded provenance/rights/safety review before inclusion**. No downloaded voice assets, external TOEIC audio or cloud TTS under this authority.

FR-003/AT-03 are bounded engineering trace targets for media relation and negative guards **only**; formal content/QA-03 remains OPEN. FR-011/AT-11 are **boundary identifiers only**, with no Full Mock clock/integrity, replay restriction engine or formal QA-08 acceptance delivered.

## 3. Carried-forward controls — DO NOT OVERRIDE

The Stage05 Gate state is still **CONDITIONAL PASS FOR DEVELOPMENT TRANSITION ONLY** under `D05-DEV-GATE-012=A`. All Stage02/Stage03/Stage04 carry-forward conditions and G05-CP01..08 stay ACTIVE, particularly B1 two independent PO-inventoried 200Q forms, no real content before QA, no architecture winner, and budget DEFERRED. All POL01..16 concrete decisions OPEN.

**Not authorized:** unreviewed real B1/TOEIC content/audio, educational English speech/TTS without a distinct new provenance approval, Full Mock A/B or clean/comparable status, official scoring, import PDF/books/audio, new CX-05..09, any production persistence/ACK, accounts, remote API/backend/DB, time authority, ARCH03 A/B/C selection, ARCH04, learner/real phone tests, ECP-00..06, QA-01..08, pilot/release, paid tooling/contracts/spend, or edits to signed Vision/PRD/SRS/Acceptance/Design/UI guardrail baseline bytes.

Previous Beta/Android UI engineering outputs remain internal evidence, not formal QA proof.

## 4. Working branch / evidence / stop rule

- Development branch: `development/cx04-listening-synthetic`, based on the validated Android source checkpoint `52e0af4a051edb5832262a0720f1dd486012a4f5` and the approved CX04 proposal document.
- Codex must consult `AGENTS.md` and `codex_handoff/CX04_SYNTHETIC_LISTENING_AUTHORIZED_EXECUTION_V0.1.md` on this branch before implementation.
- Deliver controlled source, tests, self-generated safe local tone fixtures and `docs/STAGE05_CX04_SYNTHETIC_LISTENING_ENGINEERING_REPORT_V0.1.md`. Commit only safe assets; do not push APK, screenshots, logcat, secrets, machine identifiers or private evidence, because the repository remains PUBLIC.
- All claims **PASS / FAIL / BLOCKED / NOT RUN** must correspond to actual observations and exit codes; if emulator/audio output unavailable, mark BLOCKED rather than fabricate.
- Stop at CX04-L01..03 and this single engineering emulator check. Any real speech/TTS, formal QA/ECP, other CX task, additional spend or scope change requires a new material PO decision.

**Engineering completion is not formal QA, pilot readiness, release approval or Stage05 unconditional PASS.**
