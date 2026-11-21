# Stage05 — D05-CX04-013 Listening Development Decision Proposal V0.1

**STATUS: PROPOSAL — PO DECISION PENDING. NOT AN EXECUTION AUTHORIZATION.**

Prepared after the 2026-11-21 synthetic Android Emulator engineering check. The PO asked to **start finalizing** the next step; this does NOT constitute a grant to develop CX-04. Do not change `AGENTS.md`, mark this record APPROVED, run CX-04, or edit the controlled baselines until the PO expressly selects a scope decision.

## 1. Source of authority and baseline

- Current gate: `D05-DEV-GATE-012=A`, Stage05 CONDITIONAL PASS **for Development transition only**, with G05-CP01..08 and previous Stage02/03/04 CPs ACTIVE.
- Previous approved execution: Alpha CX-00..03; separate bounded Beta BUI-01..03; one bounded synthetic Android Emulator EUI-01..03 check. None authorizes CX-04.
- Latest technical source checkpoint: `validation/android-ui-synthetic` commit `52e0af4a051edb5832262a0720f1dd486012a4f5`; source has not been formally QA accepted. Do not modify existing history or signed baseline bytes.
- Existing Stage05 V6.7 backlog assigns **CX-04 = Listening Part sequence and media playback contract**, referencing **FR-003 and FR-011, AT-03 and AT-11**. The application’s signed Design V0.3 says Listening practice may replay flexibly and **must not** be confused with evaluative Full Mock.
- **Scope interpretation:** FR-003 / AT-03 are engineering *trace targets* for local media mapping and negative guards, **NOT a content or formal QA PASS**. FR-011 / AT-11 are **boundary references only**: Full Mock timing, replay restrictions, clean/comparable integrity and policy-dependent behavior are explicitly NOT implemented under this candidate.

## 2. Recommended PO option A — bounded CX-04 synthetic Listening foundation

**If, and only if, PO explicitly selects A, authorize one local-only engineering development slice:**

| Slice | Authorized behavior | Proof required |
|---|---|---|
| `CX04-L01` | **Listening Part 1–4 DEMO route**, with clearly synthetic group/item identifiers, Part 1 synthetic visual *placeholder* where needed, navigation and item-choice UI; existing Full Mock A/B remains blocked | Source diff and local unit checks; explicit synthetic / NOT-QA UI wording |
| `CX04-L02` | **Local packaged test audio** with separate original **programmatically generated WAV tones** for at least one DEMO group per Part 1–4. Bind each `groupId/itemId` to a known `audioId`, group sequence and declared audio version/hash; implement controlled play/pause/stop/replay **only inside DEMO practice**. Provide loading/finished/missing/unavailable/error states | Deterministic fixture inventory, checks of IDs, ordering, file presence and hash, source-level state tests, no network permission or external audio service |
| `CX04-L03` | **Fail-closed safety + internal engineering checks**: deliberately missing, mismatched, duplicate or wrong-order audio never plays as a valid group; maintain clean separation between DEMO Part practice and Full Mock. Re-run local Kotlin smoke, Alpha/Beta scope guards, `:app:assembleDebug`, `:app:testDebugUnitTest` and newly scoped Listening tests. | Actual PASS/FAIL/BLOCKED/NOT RUN with exit codes, Git commit SHA, local APK SHA-256, report; no QA-pass labels |

**Critical product distinction:** The WAV tones are *transport and mapping fixtures*, **not English speech** and **not usable TOEIC Listening lessons**. They may prove that playback, grouping, UI transitions and errors are wired correctly but cannot prove Listening pedagogy, speech clarity, pronunciation, TOEIC difficulty, content QA, or any learning outcome. Never promote the Listening DEMO to “QA-READY Part bank”. Any real/synthetic **spoken dialog** or TTS asset integration requires a separately recorded rights/license/provenance and safety review before inclusion; no unapproved TOEIC audio, downloaded voices, licensed content or cloud TTS.

### Allowed low-level technical choices

- Android Kotlin + Jetpack Compose, established local JDK 17 / Android SDK 36 / Gradle 8.13 environment, existing restrained Design V0.3 tokens.
- Codex may select a reversible **local Android playback API** without network service or paid dependency. Do not infer that this chooses any product-wide architecture, ARCH03 A/B/C, recording service, background service, official mock audio engine, or clock authority.
- Existing synthetic Part 5–7 behavior and current Android Reading changes must not regress; Part 1–4 may expose a distinct *DEMO/LAB* route but must remain **NOT QA READY** for real learning content. Full Mock stays disabled.
- Only original programmatic tone assets may be checked into the repo, after verifying they contain no sensitive/vendor/licensed data. Keep APK, screenshots, temporary logs and machine paths ignored.

## 3. Proposed one-time internal emulator permission included in option A

To avoid another microapproval, option A also includes **one local Android Emulator engineering smoke check** for synthetic audio playback, on **one available AVD/API 34+ context**. Observe Part 1–4 DEMO navigation, local audio start/stop/replay, item-to-audio mapping, missing-asset errors, return/back behavior and regressions to Part 5–7. Record real emulator/API/audio state and any blockers, with no assertion of sound quality if no output audio was captured. If emulator/audio routing is unavailable, record **BLOCKED**, not PASS.

The permission is limited to local emulator engineering observations; **no real Android phone, learner, paid/cloud test farm, formal accessibility certification or QA-03/QA-08/ECP execution** is authorized.

## 4. Mandatory negative cases and engineering definition of done

1. At least **one synthetic group for each of Parts 1–4** contains a distinct audio fixture and group/item identifiers, all explicitly non-production.
2. Test negative mappings: missing asset, wrong group ID, malformed sequence, duplicate media/group IDs, and inappropriate Full Mock launch. Fail closed without silently substituting audio.
3. State transitions for play/pause/stop/replay/end/error are deterministic in tests and/or observed locally; UI must never describe sample choices as durably saved. The optional practice replay must not be available as an evaluative Full Mock behavior.
4. Existing Alpha/Beta / synthetic Android UI regressions do not worsen; source guard, Kotlin smoke, Debug build and local JVM unit tests log actual results.
5. Deliver **CX-04 Listening Engineering Report V0.1** with changed file paths, FR/AT trace, test commands/exit status, emulator observations, synthetic audio provenance/hash, known limitations, and unresolved QA/policy gates. No claim of FR-003, FR-011, AT-03 or AT-11 acceptance PASS.

## 5. Retained STOP conditions

**Always excluded:** unverified B1 A/B, actual TOEIC questions/keys/audio, real media sourcing, ingestion from user books/PDF/audio, internet permission, cloud/online TTS, authentication/account/real user data, storage/production answer ACK, backend/API/remote DB, timer/clock authority, clean Full Mock/evaluative replay/integrity engine, official scoring, ARCH03 A/B/C selection, ARCH04, CX-05..09, external learners, real phones, formal ECP/QA, pilot/release, procurement/budget spending or modifications to approved Vision/PRD/SRS/Acceptance/Design/UI guardrail bytes.

G05-CP01..08 and all previous CPs remain **ACTIVE**, with **only the explicitly approved CX-04 local synthetic engineering exception** possible upon a new PO decision. POL01..16 remain OPEN. Budget remains DEFERRED. No automated future-authority template or blank candidate may itself authorize work.

## 6. Decision sheet — select ONE

- **A — APPROVE BOUNDED CX-04 SYNTHETIC LISTENING DEVELOPMENT + ONE LOCAL EMULATOR ENGINEERING CHECK.** No formal QA or real Listening content.
- **B — REVISE:** narrow/change the candidate scope before approval.
- **C — HOLD:** no CX-04 development; continue documentary review only.

**PO decision:** `PENDING`.

If PO selects A in the chat, record `D05-CX04-013=A` with that exact authorization in a **new approval record**, create a separate development branch from validated source, amend `AGENTS.md` on the new branch only, then issue a Codex handoff. Do not infer permission from this proposal document or an earlier generic approval.
