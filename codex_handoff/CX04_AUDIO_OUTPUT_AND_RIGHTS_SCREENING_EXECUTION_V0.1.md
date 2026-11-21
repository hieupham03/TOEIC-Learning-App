# Codex Handoff — CX-04 Audio Output and Listening Content-Rights Screening

**Authorized by PO:** `D05-CX04-AUDIO-014=A`; read `docs/STAGE05_D05_CX04_AUDIO_014_A_APPROVAL_RECORD_V1.0.md` first. Work on **`validation/cx04-audio-output-rights`** exclusively. Head base: `94f77184e810a077130539e6895a3d9acf7a5726` (CX-04 engineering), with this branch carrying authorization docs. **No approval** to put English speech/TOEIC audio into the app, purchase licenses, run a real device or formal QA.

## Execution (do not ask repeated microapproval questions)

1. **Safety/branch checks.** Ensure correct branch and preserve any uncommitted changes, signed baselines, four original SHA-256 WAV fixtures, source locks and manifest. Use only existing local toolchain and installed free emulator packages. If workstation is unsuitable for safe loopback capture, mark blocked and do not improvise paid/cloud services.
2. **AOV-01: Pre-register evidence method** in the report before the run: selected AVD/API/OS, output route, capture backend, sample frequency/format, spectral/correlation analysis and thresholds/limitations, success criteria and privacy controls. Check source permission guard and original four tone hashes.
3. **AOV-01: Test real output** using the **existing Android Emulator** and bundled **original tone WAVs only**, with a local audio output route and captured output if safe/available. Do not use emulator `-no-audio` and then claim audible output. Observe player states, actual capture amplitude/frequency near 330/440/550/660 Hz, duration, silence or distortion, route changes and failure mode; record `OUTPUT_CAPTURED_AND_ANALYZED` only when physical/virtual output path is grounded in captured host/device signal. Record `PLAYER_STATE_OBSERVED` separately. If a human-owner local listen is available, record it separately; never present as a formal learner test.
4. **AOV-02: Minimal fix only if observed bug.** Keep existing CX-04 UI and group/item mapping unchanged unless a small transport fix is necessary and verified. Re-run Alpha, Beta, CX-04 static guards, Kotlin smoke, Debug build and JVM tests after any source changes. Preserve Full Mock blocks, Part1–4 real bank NOT_QA_READY, all synthetic labels, and no INTERNET permission.
5. **RGT-01: Read-only public rights research.** Identify source candidates via official publisher, licensor and documentation pages; link each official page and date accessed. Compare likely content categories such as user-original recorded speech, commissioned speech with contracts, properly documented permissive datasets, and provider-licensed TTS as **future options only**. For each candidate, specify actual right to **copy**, **adapt**, **bundle in Android offline**, **redistribute**, **commercialize**, **attribute**, and **revocation/version rules**. Do not infer permission from a public YouTube upload, download link, “free” claim or marketing. Mark unsupported/contradictory rights UNVERIFIED or NOT_ALLOWED. Do **not** download audio, synthesize any English voices, ingest PDF or choose vendor/platform architecture.
6. **Report & safe publication.** Write:
   - `docs/STAGE05_CX04_AUDIO_OUTPUT_EVIDENCE_REPORT_V0.1.md`
   - `docs/STAGE05_LISTENING_AUDIO_SOURCE_RIGHTS_SCREENING_REGISTER_V0.1.md`
   Include honest `PASS / FAIL / BLOCKED / NOT RUN` per test, commands/exit codes, capture backend, output-specific evidence, URLs and document/access dates, uncertainty and concrete next PO decision. Commit safe text and in-scope *necessary* fixes only, then push the branch. **Never commit captured WAVs, screenshots, raw loopback, logs, APK, credentials, local absolute paths, user media or licenses containing private data.**

## Key distinctions / stop rules

- Audio player says "playing" ≠ audio output audible. Headless/UI state only cannot satisfy output verification.
- A screened public source ≠ clearance for a specific asset or permission to ship. “Open/free” ≠ rights to commercial Android redistribution.
- Asset-level licensing, licensing of a speaker's performance, script copyright and voice model/TTS terms may be separate. Do not invent approvals.
- Real learner/phone, English audio incorporation, formal QA-03/QA-08/ECP, CX-05+, B1 mocks, durable data, authoritative timing, backend and spending remain forbidden.
- If no robust isolated output capture available: report `BLOCKED: actual audio output`; still complete safe documentary screening and close only that subtask, never the audio verification.

**Finish at bounded evidence and recommendations, with no new CX feature.**
