# CX-04 Synthetic Listening Engineering Report V0.1

Work took place on `development/cx04-listening-synthetic` under [D05-CX04-013=A](STAGE05_D05_CX04_013_A_APPROVAL_RECORD_V1.0.md). The checkout and fast-forward-only pull started at `d6d422c25ee1ee9a6c52de9b1ab3409a441cd0d4`.

## Delivered scope

| Slice | Implementation |
|---|---|
| CX04-L01 | A separate Listening DEMO entry on the Task Hub opens a Part 1–4 picker. Each part shows its group, item and audio ID. Part 1 has a text image placeholder. The sample answer selection is in memory. The existing part bank still blocks Parts 1–4 and the Full Mock entry still opens the blocked information screen. |
| CX04-L02 | One versioned WAV per part. Playback checks the selected group and exact fixture bytes before preparation, and displays loading, playing, paused, stopped, completed, missing, invalid and player-error states. Play from stopped or completed starts at the beginning. Pause resumes from the current position. The screen releases its player on exit and when the activity pauses. Audio is local and uses Android `MediaPlayer`. [Android MediaPlayer reference](https://developer.android.com/reference/android/media/MediaPlayer) |
| CX04-L03 | JUnit verifies fixture identity, byte hashes, missing group and asset, duplicate IDs, wrong group/item/audio/version/hash, wrong order, playback transitions and retained content locks. The dedicated source guard compares each checked-in WAV against the generator and the declared hash. |

FR-003 / AT-03 are engineering trace targets for the synthetic mapping and negative checks. FR-011 / AT-11 define the Full Mock boundary. Design V0.3 governs spacing, colors and visible control labels.

## Fixture provenance and identity

`python scripts/generate_listening_tones.py` generates 6-second, 16 kHz mono, 16-bit PCM triangle-wave pulses with short fades. The generator uses only the standard library and integer arithmetic. Each WAV is 192,044 bytes. The assets contain original test signals generated from the frequencies below. Group IDs are `CX04-DEMO-P{part}-G01`. Each item's ID appends `-I01` to its group ID. Order is 1–4 and all fixtures are version 1.

| Part / order | Audio ID | Frequency | SHA-256 |
|---|---|---:|---|
| 1 | `cx04_tone_p1_v1` | 330 Hz | `97b157773f1c7e52461a37d2fb25420651725b34f2a00c4f092b0a34d3a24f2c` |
| 2 | `cx04_tone_p2_v1` | 440 Hz | `4ca4ac157e335a9e1e9dd1093e363896b346b8d4128f7a2d43d02fbb5fb98305` |
| 3 | `cx04_tone_p3_v1` | 550 Hz | `a0188fd2f8f5f3bf6a79a5cd40dd735c60e82e5f44326516c0d1767a83a2bb38` |
| 4 | `cx04_tone_p4_v1` | 660 Hz | `d43097ce9535f521be144e20ce7c26717fd283d80e7fbc69d3ceb7c68a05c932` |

## Local engineering verification

Windows, Temurin JDK 17.0.21.1, Android SDK 36 / build-tools 36.0.0, Gradle wrapper 8.13 and Kotlin CLI 2.2.21. Commands run from `android-app`.

| Command | Result | Exit |
|---|---|---:|
| `python scripts/check_alpha_scope.py` | PASS, 10/10 checks | 0 |
| `python scripts/check_beta_reading_ui_scope.py` | PASS, 11/11 checks | 0 |
| `python scripts/check_cx04_listening_scope.py` | PASS, 9/9 checks | 0 |
| `.\scripts\run_pure_kotlin_core_checks.ps1 -KotlinHome .tooling\kotlin-compiler-2.2.21\kotlinc -JavaHome .tooling\jdk17` | PASS, 25 assertions | 0 |
| `.\gradlew.bat --offline --no-daemon --console=plain :app:assembleDebug :app:testDebugUnitTest --rerun` | PASS, both tasks executed. Gradle reported `BUILD SUCCESSFUL in 3m 9s`. | 0 |

JUnit XML under `app/build/test-results/testDebugUnitTest/` reports 4 Alpha tests and 7 Listening tests, with 0 failures, errors or skips. `aapt dump permissions` lists only the app's generated dynamic-receiver permission. The six signed baseline and guardrail hashes match the [controlled manifest](STAGE05_ALPHA_CX00_CX03_SOURCE_AND_CONTROL_MANIFEST_V0.1.md).

Debug APK SHA-256 is `b1b5afde1377724335c935b2cff5d35e899d3941255918b5f9996eb33990f38b`.

## One local emulator session

Android Emulator 37.2.13 with WHPX and the existing local Android 14 / API 34 x86_64 AVD. The display was 1080 × 2160 px at 480 dpi (360dp) and font scale 1.0. The session used `adb install -r`, `adb shell am start -W`, input taps/swipes/Back, UI hierarchy dumps and local screenshots.

- **Initial FAIL (environment)**. The normal and missing-asset first checks each exited `1` while an Android System UI ANR dialog covered the app. Dismissing the dialog restored app focus on the same AVD boot.
- **OBSERVED (missing media)**. A separate local APK omitted only `assets/listening_demo/cx04_tone_p4_v1.wav` and was aligned, re-signed with the local debug key and installed on the emulator. Part 4 displayed “Thiếu tệp âm thanh thử nghiệm. Không thể phát.” and did not enter the playing state. Android Back returned to the picker. The recheck exited `0`. The standard APK was then installed for the normal check.
- **OBSERVED (normal transport)**. All four Part routes displayed the expected group, item and clip ID, entered the playing state and returned to the picker. Part 1 additionally exercised pause/resume, stop, replay, natural completion and Back while playing. Reopening Part 1 returned to the idle state. Parts 2–4 exercised Stop. The Part 1 image placeholder and sample answer controls were visible.
- **OBSERVED (regression)**. The three tabs remained navigable, Parts 1–4 remained disabled in the existing part bank, and Full Mock A/B opened the blocked-information screen. Part 5 showed the synthetic explanation after the explicit reveal action. Part 6 and Part 7 returned to the recorded scrolled passage positions after switching questions. The normal recheck exited `0`. The sampled crash buffer was empty and the inspected logs contained no app crash or ANR event.
- **BLOCKED (audibility)**. The headless emulator check recorded control and player callback states. Audible host output and sound quality were unverified.

APK variants, screenshots, UI XML and raw logs are stored locally. Build outputs are in ignored `android-app/app/build/`. Emulator evidence is in ignored `android-app/.tooling/cx04-listening/`, with the initial failure and recheck runs in separate directories.

**NOT RUN** applies to real Android devices, learner testing, formal QA/ECP, formal accessibility and actual TOEIC learning/audio effectiveness. G05-CP01..08 are ACTIVE and budget is DEFERRED.

## Changed paths

- `android-app/app/build.gradle.kts` keeps WAV assets uncompressed for descriptor-based playback.
- `android-app/app/src/main/assets/listening_demo/` contains `cx04_tone_p1_v1.wav`, `cx04_tone_p2_v1.wav`, `cx04_tone_p3_v1.wav` and `cx04_tone_p4_v1.wav`.
- `android-app/app/src/main/java/vn/toeiclearning/alpha/domain/ListeningDemo.kt` defines the inventory, asset verification and playback state transitions.
- `android-app/app/src/main/java/vn/toeiclearning/alpha/ui/AlphaApp.kt`, `ListeningDemoScreen.kt` and `LocalListeningPlayer.kt` wire the separate route, controls and platform player. The latter two files are in the same UI directory.
- `android-app/app/src/test/java/vn/toeiclearning/alpha/domain/ListeningDemoTest.kt` contains the Listening JVM tests.
- `android-app/scripts/generate_listening_tones.py` and `android-app/scripts/check_cx04_listening_scope.py` reproduce and check fixtures. `check_alpha_scope.py` and `check_beta_reading_ui_scope.py` clarify the existing MP3 guard label.
- `docs/STAGE05_CX04_SYNTHETIC_LISTENING_ENGINEERING_REPORT_V0.1.md` records this run.
