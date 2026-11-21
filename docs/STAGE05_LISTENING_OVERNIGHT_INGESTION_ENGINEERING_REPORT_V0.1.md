# Listening Overnight Ingestion Engineering Report V0.1

Work ran on `ingestion/listening-overnight-bounded` after a fast-forward-only pull. The starting commit was `3ae1b8c`. The finite batch followed the [workplan](STAGE05_LISTENING_OVERNIGHT_BOUNDED_INGESTION_WORKPLAN_V0.1.md) and [GitHub Issue #6](https://github.com/hieupham03/TOEIC-Learning-App/issues/6). Source rights are recorded as `PO_DECLARED_NOT_INSPECTED` under the [PO reaffirmation](STAGE05_LISTENING_PO_RIGHTS_REAFFIRMATION_V0.1.md).

## NLI-01 — Live evidence and crawler changes

The original synthetic self-test passed. The first hardened live attempt fetched robots.txt (HTTP 200, 119 bytes) and the [specified Zenlish page](https://zenlishtoeic.vn/stm-quizzes/test-1-2022/) (HTTP 200, 223,967 bytes). It returned **PARTIAL**, exit `2`, before requesting audio. The selected group lacked a separate child index and choice field in this page variant. On the saved HTML, Q32–34 appeared as explicit numbers in the title fields and the `answer` field contained choices rather than the key.

The parser now recognizes that shape, HTML attributes, wrapped JSON and JSON with reordered fields. It rejects conflicting numbering, ambiguous groups, broken choices, duplicate item IDs and media not bound to the named clip. The one allowed continuation checked the saved HTML against its original hash, carried forward the HTTP and byte ledger, and fetched the matching Part 3 MP3 without refetching the quiz page. That continuation returned **FETCHED**, exit `0`.

Transport checks the robots policy, same-host HTTPS redirects, timeout, throttle and byte/attempt budgets. Offline tests exercise timeout and TLS failures, retry limits, 403/429, redirects, incomplete responses and wrong or truncated media. The actual requests all returned HTTP 200.

## NLI-02 — Finite sample results

**4 groups, 8 question records, 4 MP3 files and 1 PNG.** All came from the same saved Zenlish page. The ledger recorded **9 / 24 HTTP attempts** and **3,784,023 body bytes (3.61 MiB) / 32 MiB**. The largest media file was 1,305,325 bytes, below the 12 MiB cap. The request breakdown is three robots checks, one page, four audio files and one image. TheToeicLab and Study4 were **NOT RUN**. Four representative groups were already accounted for.

| Part | Acquisition | Source group | Displayed question numbers | Available text and media |
| --- | --- | ---: | --- | --- |
| 1 | **PARTIAL** | `40911` | 1 | Four choice labels, no separate stem or choice text, one bound PNG and MP3. |
| 2 | **PARTIAL** | `40943` | 7 | Three choice labels, no separate stem or choice text, one MP3. |
| 3 | **FETCHED** | `41021` | 32–34 | Three written stems, four choices per item and one linked MP3. |
| 4 | **FETCHED** | `41104` | 71–73 | Three written stems, four choices per item and one linked MP3. |

The page supplied source group IDs and displayed question numbers. It supplied zero separate child IDs, so the normalizer records a null source item ID and derives local keys such as `zenlish:41021:32` from the observed group and number. There were **0 attributable answer keys for 8 items** and all are `ANSWER_KEY_UNVERIFIED`. Part 1 was the only group with an associated image.

| Part | Observed asset basename | Bytes | MPEG-frame duration estimate | SHA-256 |
| --- | --- | ---: | ---: | --- |
| 1 | `zenlish-test-01-part-1-1.mp3` | 440,034 | 23.196735 s | `223b4cab3e6382f21f7b7056bb48a781f0db14a0247efb13417980f5373ce9a3` |
| 2 | `zenlish-test-01-part-2-7.mp3` | 407,508 | 21.159184 s | `ac324f03ba0d0573df50b9dda29f5bf177e750dc28a31ebb200693e81908038f` |
| 3 | `zenlish-test-01-part-3-32-34.mp3` | 1,265,710 | 74.919184 s | `cf77cbe460cfe87cf4a396fcb9b90194773c7bfeeb97f98e333e494fb2dcae4b` |
| 4 | `zenlish-test-01-part-4-71-73.mp3` | 1,305,325 | 77.400816 s | `f226785958cf1a5555725500bd890331892d681dcd497d9556042b5c36a5c5e3` |
| 1 | `zenlish-1-3.png` | 141,122 | — | `ae739010604b7de17f64065434d3bcaec3861596731ab53ee8f3797a166cbcac` |

- **PASS for local structure and integrity.** All four audio files matched the `audio/mpeg` response MIME and MPEG Layer III frame inspection found 44.1 kHz stereo streams with distinct SHA-256 values. The PNG passed its chunk-length and CRC checks. The saved HTML SHA-256 is `2db58276d138f6d1374698c150fc518765a3d9cd4f84c77765a33e9f44556c14`.
- **NOT RUN for codec probe/full compressed decode.** `ffprobe` and `ffmpeg` were unavailable on the execution PATH. Durations are frame estimates. Semantic audio-to-question accuracy, media listening and formal content QA are **NOT RUN**.
- Exact media URLs, response metadata, retrieval timestamps, original question text and private receipts are under ignored `android-app/.tooling/listening-overnight/`. The paths within it are `zenlish-p3-q32-34/`, `representative-continuation/part-{1,2,4}/`, `representative-continuation/batch.json`, `normalized_manifest.json` and `validation_summary.json`.

## NLI-03 — Offline preparation

The [manifest schema](../android-app/scripts/listening_manifest.schema.json) and [dry-run contract](STAGE05_LISTENING_OFFLINE_DRY_RUN_CONTRACT_V0.1.md) separate acquisition, structural mapping and review. The generic validator checks local file existence, containment, media type, hash, media-to-group and item references, unique IDs, required Part 1 image, ordered indices and review declarations. The Zenlish normalizer rechecks the saved source hash and binds the exact four sampled groups to this contract.

The live batch normalized successfully. The offline validator reported **4 MAPPED groups, 0 structural errors, 24 holds and `eligible_for_app: false`**, exit `2`. The holds include two partial acquisitions, two labels-only items, eight unverified answers, four compressed decodes not run, four QA reviews and four rights reviews.

## NLI-04 — Verification and handoff

Run from `android-app/`.

| Command | Actual result | Exit |
| --- | --- | ---: |
| `python -B scripts/crawl_one_zenlish_part3_group.py --self-test` | PASS, synthetic parser smoke | 0 |
| `python -B -X utf8 scripts/crawl_one_zenlish_part3_group.py` | PARTIAL on the initial live page parse | 2 |
| `python -B -X utf8 scripts/crawl_one_zenlish_part3_group.py --resume-local-page` | FETCHED, Part 3, cumulative 4 requests | 0 |
| `python -B -X utf8 scripts/crawl_zenlish_representative_groups.py` | Bounded batch complete with Part 1/2 partial, cumulative 9 requests | 2 |
| `python -B -m unittest discover -s tests/ingestion -v` | PASS, 36 synthetic tests, 0 failures/errors | 0 |
| `python -B -m json.tool scripts/listening_manifest.schema.json` | PASS, schema document parses as JSON | 0 |
| `python -B -X utf8 scripts/normalize_zenlish_batch.py` | PASS, 4 groups normalized offline | 0 |
| `python -B -X utf8 scripts/listening_manifest.py .tooling/listening-overnight/normalized_manifest.json` | HOLD, 0 structural errors | 2 |
| `python -B scripts/check_alpha_scope.py` / `check_beta_reading_ui_scope.py` / `check_cx04_listening_scope.py` | PASS 10/10, 11/11 and 9/9 respectively | 0 each |
| `.\scripts\run_pure_kotlin_core_checks.ps1 -KotlinHome .tooling\kotlin-compiler-2.2.21\kotlinc -JavaHome .tooling\jdk17` | PASS, 25 assertions | 0 |
| Android Gradle build/JVM tests, emulator, formal QA/ECP | NOT RUN for the ingestion change. The Android app and its toolchain files were untouched. | — |

Changed paths are the existing `android-app/scripts/crawl_one_zenlish_part3_group.py`, new `crawl_zenlish_representative_groups.py`, `listening_http.py`, `listening_media.py`, `normalize_zenlish_batch.py`, `listening_manifest.py` and `listening_manifest.schema.json` in the same scripts directory, two synthetic suites under `android-app/tests/ingestion/`, the dry-run contract and this report. All six signed baseline and UI guardrail hashes matched the [controlled manifest](STAGE05_ALPHA_CX00_CX03_SOURCE_AND_CONTROL_MANIFEST_V0.1.md). G05-CP01..08 are active and budget is DEFERRED.

Next PO decision is whether to authorize a separate asset-level review of **one identified group** with explicit offline-use rights, an attributable key, decoded audio verification and human content review. This batch stopped after the four samples. Content remains held locally.
