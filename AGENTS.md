# AGENTS.md — Current scoped authority: CX-04 Audio Output + Rights Screening

## Active PO approval D05-CX04-AUDIO-014=A

The Product Owner approved the post-CX04 next step: **local synthetic audio OUTPUT evidence** and **read-only Listening learning-content source-rights screening**. Binding record: `docs/STAGE05_D05_CX04_AUDIO_014_A_APPROVAL_RECORD_V1.0.md`. Codex execution handoff: `codex_handoff/CX04_AUDIO_OUTPUT_AND_RIGHTS_SCREENING_EXECUTION_V0.1.md`. **Read both before work.**

Work only on **`validation/cx04-audio-output-rights`**. Base source commit `94f77184e810a077130539e6895a3d9acf7a5726` was CX-04 engineering closure; it was **not formal QA or verified host audibility**. Do not rewrite existing branches or edit signed baselines. Preserve any uncommitted work.

### Approved scope ONLY

- **AOV-01:** verify source/fixture hashes and capture **real local Android Emulator audio-output evidence** for the existing four programmatically generated synthetic WAV tones; distinguish player callbacks from actual audio-output signal capture. Use safe isolated local capture at no cost, record thresholds and actual outcomes. If impossible, report **BLOCKED**, do not invent output.
- **AOV-02:** report actual method, AVD/OS/capture route, hashes/measurements and PASS/FAIL/BLOCKED/NOT RUN; optional small reversible fix to existing CX-04 transport only if a demonstrable bug, with Alpha/Beta/CX04 static checks, Kotlin smoke and local Gradle unit/build reruns.
- **RGT-01:** read-only research of **public official** Listening content source/license options, source URLs/dates and per-asset rights criteria. Distinguish verified rights for a specific asset versus only a marketing “free” claim. **No media ingest, English speech/TTS generation, vendor contract or content selection.**
- Commit only text reports `docs/STAGE05_CX04_AUDIO_OUTPUT_EVIDENCE_REPORT_V0.1.md` and `docs/STAGE05_LISTENING_AUDIO_SOURCE_RIGHTS_SCREENING_REGISTER_V0.1.md` plus proven small fixes/tests. Keep captured audio, APK, emulator screenshots, raw logs, credentials and user data LOCAL — GitHub repo remains PUBLIC.

### Still STOP — unaffected controls

No new features `CX-05..09`, actual TOEIC/B1 media or English speech/TTS, user PDFs/books/audio ingest, live Full Mock, real Android phone or learner test, formal ECP/QA, release/pilot, backend/API/DB, app account/auth, durable answer ACK, authoritative clock, ARCH03 selection, paid services/budget expenditure, or modifications to approved Vision/PRD/SRS/Acceptance/Design/UI-G baseline bytes. Existing Part1–4 real bank and Full Mock remain NOT_QA_READY/blocked.

Prior approval `D05-CX04-013=A` allowed **synthetic transport development**, not production rights or QA. `D05-DEV-GATE-012=A` remains Stage05 **CONDITIONAL PASS FOR DEVELOPMENT TRANSITION ONLY**. G05-CP01..08 and previous CPs ACTIVE; POL01..16 OPEN; B1 content QA NOT VERIFIED; budget DEFERRED.

**Never equate MediaPlayer state with audible output, and never equate a candidate source with a licensed, ship-ready asset.** Stop after the bounded audio-evidence and rights-screening deliverables.
