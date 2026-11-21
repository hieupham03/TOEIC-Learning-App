# CX-04 Audio Output Evidence Report V0.1

**Review date** 2026-11-22 (Asia/Saigon). **Authority** [D05-CX04-AUDIO-014=A](STAGE05_D05_CX04_AUDIO_014_A_APPROVAL_RECORD_V1.0.md). Branch `validation/cx04-audio-output-rights` checked out and fast-forward-only pull up to date at `7cc5d33354a9b11734c50cb3a3de2e3fd0868c99`. CX-04 source baseline `94f77184e810a077130539e6895a3d9acf7a5726`.

## AOV-01 — Method registered before capture

Use the existing local Android Emulator 37.2.13 on Windows with WHPX and the previously used Android 14 / API 34 x86_64 test AVD. Capture via the emulator's authenticated gRPC `EmulatorController/streamAudio` on loopback. This taps virtual speaker output from the Android guest. The gRPC reference describes frames produced by the emulated device. [Android Emulator console commands](https://developer.android.com/studio/run/emulator-console) and [official emulator protocol](https://android.googlesource.com/platform/prebuilts/android-emulator/+/master/linux-x86_64/lib/emulator_controller.proto).

Request 16 kHz mono signed 16-bit little-endian PCM. Collect an idle control and one bounded capture window per app-selected synthetic tone. Record actual format, duration, signal measurements and local WAV SHA-256. Use the synthetic-only AVD with guest network off and notification/touch sounds disabled. Use no microphone or desktop mix. Keep all captures, test scripts and raw logs in Git-ignored local storage.

Use 100 ms non-overlapping Hann-windowed blocks. Count a block as an expected tone when its RMS exceeds -55 dBFS, the interpolated dominant peak is within ±3 Hz of the expected frequency, and the fundamental is at least 15 dB above the strongest alternate fixture band (±3 Hz around the other three fixture frequencies). Require at least five distinct tone bursts separated by ≥100 ms, 3.0–4.8 seconds of matching blocks, an elapsed span of 5.1–6.2 seconds from first to last matching block, and zero full-scale clipped samples. The idle control must have no samples or no signal blocks above -55 dBFS. The four tested frequencies are 330, 440, 550 and 660 Hz. This checks frequency linkage and gross loss, noise and clipping. Gain and resampling can differ from the fixture bytes.

Record `PLAYER_STATE_OBSERVED`, `OUTPUT_CAPTURED_AND_ANALYZED` and `HUMAN_AUDIBLY_OBSERVED` separately. If the output route or sample integrity cannot be established, mark the output check **BLOCKED**. Speaker hardware performance, human listening and formal QA are separate evidence.

## AOV-01 — Source and build evidence

`git diff --exit-code 94f77184 -- android-app` returned `0`. The six Vision/requirements/design/guardrail hashes match the [controlled manifest](STAGE05_ALPHA_CX00_CX03_SOURCE_AND_CONTROL_MANIFEST_V0.1.md). The CX-04 guard regenerated and compared the four trusted tone byte streams on the workstation.

| Part | Nominal frequency | Bundled WAV SHA-256 |
| --- | ---: | --- |
| 1 | 330 Hz | `97b157773f1c7e52461a37d2fb25420651725b34f2a00c4f092b0a34d3a24f2c` |
| 2 | 440 Hz | `4ca4ac157e335a9e1e9dd1093e363896b346b8d4128f7a2d43d02fbb5fb98305` |
| 3 | 550 Hz | `a0188fd2f8f5f3bf6a79a5cd40dd735c60e82e5f44326516c0d1767a83a2bb38` |
| 4 | 660 Hz | `d43097ce9535f521be144e20ce7c26717fd283d80e7fbc69d3ceb7c68a05c932` |

Windows, Temurin JDK 17, Android SDK 36, Gradle wrapper 8.13 and Kotlin CLI 2.2.21. Commands ran from `android-app` unless indicated.

| Command | Result | Exit |
| --- | --- | ---: |
| `python scripts/check_alpha_scope.py` | PASS, 10/10 | 0 |
| `python scripts/check_beta_reading_ui_scope.py` | PASS, 11/11 | 0 |
| `python scripts/check_cx04_listening_scope.py` | PASS, 9/9 | 0 |
| `.\scripts\run_pure_kotlin_core_checks.ps1 -KotlinHome .tooling\kotlin-compiler-2.2.21\kotlinc -JavaHome .tooling\jdk17` | PASS, 25 assertions | 0 |
| `.\gradlew.bat --offline --no-daemon --console=plain :app:assembleDebug :app:testDebugUnitTest --rerun` | PASS, Debug assembly up to date and JVM task rerun. JUnit XML recorded 4 Alpha + 7 Listening tests, 0 failures/errors/skips. | 0 |
| `aapt dump permissions app/build/outputs/apk/debug/app-debug.apk` | PASS, only the generated app-local dynamic receiver permission. No INTERNET permission. | 0 |

Installed Debug APK SHA-256 `b1b5afde1377724335c935b2cff5d35e899d3941255918b5f9996eb33990f38b`. `adb install -r` succeeded.

## AOV-01 — Captured output results

One existing API 34 emulator boot ran at 1080 × 2160 px, 480 dpi and media volume 5/15. Start options included `-no-window -no-snapshot -gpu swiftshader -grpc 8556 -grpc-use-token`. The listener was confirmed on `127.0.0.1` only. Emulator audio was enabled. Guest Wi-Fi and mobile data were disabled, touch sounds turned off, and notification and system volumes set to zero. The collector requested the authenticated virtual speaker stream using Node.js 22's built-in HTTP/2 client. Python with NumPy analyzed the returned PCM. Each trial requested a 9 s collection window and started app playback about 1 s into that window.

The app started but a System UI ANR dialog blocked the first launch observation (exit `1`). Dismissing the dialog restored app focus. The initial request used the emulator console credential and returned gRPC status 16 (exit `1`). The collector then read the active server's gRPC credential from local discovery metadata. The final capture ran in the same boot. It returned HTTP 200 for all four trials. Each returned packet explicitly matched the requested 16 kHz mono signed 16-bit format. The collector canceled each stream at the intended local deadline with zero partial bytes buffered.

**Idle control PASS.** The same route delivered zero PCM packets over 2 s with playback idle. The later active trials established route availability. This idle result records absence of delivered frames, so it provides no measured noise floor.

| Part | Peak (Hz) | PCM seconds / packets | Peak / max 100 ms RMS (dBFS) | Min. alternate-band margin (dB) | Matching seconds / span seconds | Threshold groups | Clipped samples | Result |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 330.000 | 6.8510 / 638 | −45.70 / −50.46 | 30.15 | 3.5 / 5.7 | 11 | 0 | PASS |
| 2 | 440.000 | 7.7308 / 719 | −45.70 / −50.47 | 27.72 | 3.3 / 5.7 | 11 | 0 | PASS |
| 3 | 550.000 | 7.7419 / 721 | −45.70 / −50.46 | 27.80 | 3.4 / 5.8 | 14 | 0 | PASS |
| 4 | 660.000 | 7.7561 / 715 | −45.70 / −50.47 | 27.18 | 3.5 / 5.7 | 10 | 0 | PASS |

Total PCM duration includes non-tone frames. The 100 ms frequency gate can split a pulse into multiple threshold groups. A supplementary comparison aligned each six-second fixture's 10 ms RMS envelope to the capture by maximum Pearson correlation. In Part order the correlations were **0.994, 0.993, 0.992 and 0.993**, all at a 40 ms offset inside the saved PCM. Each of the six expected 700 ms tone intervals per fixture had 67–68 of 70 RMS blocks above −55 dBFS. This corroborates the pulse sequence despite conservative spectral threshold fragmentation. No full-scale clipping or gross truncation was detected. The measured digital levels reflect this route and volume setting. Acoustic distortion and physical noise floor were NOT RUN.

| Local output capture | WAV SHA-256 |
| --- | --- |
| `part-1.wav` | `a3e5fe1f0e611faeba642f093a3ba9f8b0fb75548302f5083db07eb6dcf61a29` |
| `part-2.wav` | `2243dc2ed6e52bf2630bfa9d0f28e6affccaa95b1cafacb99c530f8041b32a86` |
| `part-3.wav` | `7c43d791345e56dc5c49547694cec88165ec29bb63dd0ab0703f94a2f2b3c1aa` |
| `part-4.wav` | `8533b4f9bd37545d00768053b1aeb8917c8020281b62a55c792770d897d1eda7` |

## AOV-02 — Outcome and regression

- **PASS / `OUTPUT_CAPTURED_AND_ANALYZED`** for four of four synthetic tones at the emulator's virtual speaker output. The local Python capture harness, FFT analysis and supplementary envelope comparison each exited `0`.
- **PASS / `PLAYER_STATE_OBSERVED`** for play and natural completion in all four Parts. Part 1 also exercised replay, pause, resume and stop. The crash buffer was empty and the inspected logs contained no app crash or ANR event.
- **NOT RUN / `HUMAN_AUDIBLY_OBSERVED`**. Physical host playback, real Android hardware, learners, spoken-English effectiveness, formal AT-03/AT-11 and formal ECP/QA were not exercised.
- **PASS for engineering regressions** in the existing build, unit tests and guards. No repeatable CX-04 source defect was demonstrated. App source and files match the baseline commit. G05-CP01..08 remain active and budget is DEFERRED.

The captures, screenshot evidence, PCM packet metadata, analysis code and raw logs are in ignored `android-app/.tooling/cx04-audio-output/`. APK and test XML are in ignored `android-app/app/build/`. This report and the [rights screening register](STAGE05_LISTENING_AUDIO_SOURCE_RIGHTS_SCREENING_REGISTER_V0.1.md) are the publication artifacts. Any later spoken-content experiment requires a PO decision for an identified asset with its permissions and territory established.
