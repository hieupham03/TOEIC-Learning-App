# D05-CX04-AUDIO-014=A — Audio Output Evidence and Listening Source-Rights Screening Authorization V1.0

**Status:** APPROVED BY PRODUCT OWNER (project chat, 2026-11-22); **engineering verification + documentary research only**.

**PO response:** "ok phe duyet", immediately after the CX-04 engineering review proposed **a bounded audio-output verification package and identification of potential Listening learning-content sources with clear usage rights**. That reply authorizes only this precise follow-up. It is **not** authorization to ingest, redistribute, synthesize spoken learning content, acquire licenses, implement new product features, perform formal QA, or launch any product or pilot.

**Source baseline:** CX-04 engineering commit `94f77184e810a077130539e6895a3d9acf7a5726`. Execute in **`validation/cx04-audio-output-rights`**. Preserve Alpha, Beta, EUI and CX-04 branch history, signed requirements, approvals, and source baseline hashes.

## 1. Exactly authorized work

### `AOV-01` — Local audio-output evidence (synthetic tone only)

- Verify local build, source hash inventory, no Internet permission, and existing scoped unit/source safety checks.
- On **one existing local Android Emulator** (ideally API34+) with the CX-04 packaged four 6-second programmatically generated WAV tones, check audio controls, MediaPlayer completion and, crucially, an **actual captured audio-output path** when feasible.
- Distinguish `PLAYER_STATE_OBSERVED` from `OUTPUT_CAPTURED_AND_ANALYZED` from `HUMAN_AUDIBLY_OBSERVED`. A state callback is never an audible-output pass.
- Prefer a free, already installed local audio loopback / virtual audio device capture. Record the selected emulator output route, local sample format, duration, captured file checksum and measured signal correlation/spectral peaks versus the four locally generated frequencies (330, 440, 550 and 660 Hz). Set the acceptable measurement approach **before** testing; report noise, truncation, silence and routing blockers. Avoid asserting perfect bit-level equality after OS mixing/resampling.
- If audio route/capture is unavailable, mark `BLOCKED` with exact evidence; **do not use fake/simulated captures** or substitute playback UI callbacks as a PASS. Avoid paid packages or services. Local opt-in listening by the owner is possible if convenient, but no other learner/human usability test is authorized.
- Any host-loopback recording must be limited to a synthetic-only playback window, with other desktop sounds and notifications disabled to the extent practical. Never capture meetings, voices, credentials or unrelated desktop audio. Keep samples, screenshots, logs and APK **LOCAL**, out of the public repository.

### `AOV-02` — Bounded regression and engineering report

- If a concrete defect in the **existing local CX-04 playback** is demonstrated, Codex may make **small reversible fixes only** to existing audio transport/error handling, plus deterministic regression tests.
- Re-run existing Alpha/Beta/CX-04 source guards, Kotlin smoke tests, Android Debug build and Gradle JVM unit tests when changes are made. Record all commands and actual exit codes.
- Publish only text results in `docs/STAGE05_CX04_AUDIO_OUTPUT_EVIDENCE_REPORT_V0.1.md`: AVD/API, output route/capture method, claimed audio-observation level, measured results or blockers, defects and regression status. No "QA-03 PASS", learner audibility, pronunciation quality or production media claim.

### `RGT-01` — Listening content **source-rights screening only**

- Create `docs/STAGE05_LISTENING_AUDIO_SOURCE_RIGHTS_SCREENING_REGISTER_V0.1.md`.
- Identify candidate **source types and, where supported by publicly accessible primary evidence, concrete sources** that *may* later provide Listening practice English speech/audio. Search publicly visible official permissions/terms/license documentation as of the review date, retain source URLs, access dates, rights holder, asset/version specificity and relevant terms for copying, adaptation, bundling into Android, app redistribution, commercial use, attribution, derivative/voice usage and revocation.
- Separate **VERIFIED_FOR_SCOPE** (requires explicit primary-source license evidence for an identified asset and intended Android commercial redistributable use), **CONDITIONAL / LICENSE_REVIEW_REQUIRED**, **UNVERIFIED**, and **NOT_ALLOWED**. Do not claim VERIFIED if asset-level rights or commercial distribution permission is missing. Distinguish free-to-listen from free-to-redistribute, public-domain status from royalty-free marketing, and licensed TTS/voice model from licensing of generated output and scripts.
- The register is a **research and decision-preparation artifact**, **not a legal opinion, agreement, content ingest, QA pass or PO source selection**.
- **Do not download, scrape, record, generate English speech/TTS, upload the user's personal material, or bundle any candidate audio** under this authority. Do not use ETS trademarks/content as evidence of a blanket license. No paid research or vendor sign-up.

## 2. Explicit exclusions / control retention

No real Android phone or external tester, no learner testing, no formal ECP/QA-01..08, no live TOEIC/B1 media or questions, no actual English speech/TTS integration or content QA, no backend/API/cloud/audio streaming, no accounts, no durable answer ACK, no official Full Mock or timing integrity, no CX-05..09, ARCH03 A/B/C selection, pilot/release or purchase. Avoid altering any approved Vision/PRD/SRS/Acceptance/Design baseline bytes.

**D05-DEV-GATE-012=A remains Stage05 CONDITIONAL PASS FOR DEVELOPMENT TRANSITION ONLY.** All Stage02/03/04 conditions, G05-CP01..08, POLICY/POL01..16 open choices, B1 QA blockers and **DEFERRED budget** remain unchanged.

## 3. Completion, status labels and next material decision

- Codex may autonomously select reversible internal test/analysis methods within the boundary, without microapproval. Work only on the stated branch.
- Deliver `AOV-01`, `AOV-02`, `RGT-01` reports and any minimal justified playback fix in a separate commit; no build outputs, captures, unlicensed media or sensitive details in Git.
- If output capture cannot be completed with available tools, the **check remains BLOCKED** (even if paperwork is complete). Do not close it as "output verified."
- Sound quality on real phones, spoken-English pedagogy, audio rights for actual content, formal AT-03/AT-11 and any release claim remain **NOT VERIFIED** unless separately evidenced.
- Next material PO decision: whether to authorize an **identified, verified-rights spoken Listening content pilot asset** or other development; this approval does not authorize such use.

**Authority classification:** One narrowly scoped **technical audio-output evidence + public-source rights screening** exception, **not** an extension of CX-04 to production content.
