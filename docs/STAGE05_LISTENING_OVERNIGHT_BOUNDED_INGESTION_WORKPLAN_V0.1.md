# Stage05 — Bounded Overnight Listening Sample Ingestion Workplan V0.1

**Status:** PO-directed bounded expansion of one-sample preparation, **not** approval for mass crawling, distribution, integration of third-party assets into APK, or content QA PASS.

**Product Owner instruction (2026-11-22):** "prompt này tôi sẽ treo codex qua đêm, hãy cho 1 lượng công việc phù hợp". Interpreted together with the previous explicit PO instruction to **find/crawl one sample** and their repeated source-rights affirmation: authorize a *small representative acquisition and local validation batch*, a robust generalizable ingestion tool and report, not indefinite unattended crawling.

**Branch:** `ingestion/listening-overnight-bounded`, forked from `ingestion/one-zenlish-p3-32-34` at `f37c0a72ee0a914c9c1c16cf648a35bb2cb67f9e`.

## Fixed safety caps for the overnight run

- **At most 4 separate Listening question/audio groups in total, including the already identified Zenlish Part3 Q32–34 group**, preferably one candidate each for Part1, Part2, Part3 and Part4 when publicly accessible and traceable. At most **15 individual questions**, max **24 HTTP requests** across pages/media, max **32 MiB total media/page downloads**, max **12 MiB per media file**. No full exam, pagination through catalogs, bulk extraction, unrestricted discovery or repeated background polling.
- Allowed named sources only, consistent with the PO's prior declaration: `zenlishtoeic.vn`, `test.thetoeiclab.vn` and `study4.com`. Search discovery can identify appropriate URLs from those sources, but fetch only candidate pages/media for the bounded groups. Record actual source site and exact asset URL; do not invent IDs or media links.
- Min. **3 seconds between HTTP requests to the same host**, timeout 20 seconds, at most 2 retries for transient server/network faults with bounded backoff; **stop that source on HTTP 403/429, login, CAPTCHA, robots/site restrictions, or explicit anti-automation block**. No browser-stealth plugins, login, API keys, reverse-engineering protected endpoints, access-control bypass, proxy rotation, credential import, paid services, or automated vendor contact.
- HTML/JS rendered in an ordinary browser may be inspected **only if openly accessible** and consistent with site restrictions; if the user must authenticate or bypass controls, stop. Distinguish `DISCOVERED_ONLY`, `FETCHED`, `PARTIAL`, `BLOCKED` and `NOT_VERIFIED`.
- **No writes of original third-party audio, question text, scraped HTML, images or transcriptions to this PUBLIC GitHub repository.** Keep raw downloaded media, original questions, parser traces, browser screenshots, full transcripts, and keys only under ignored `android-app/.tooling/listening-overnight/`. The existing root `.gitignore` already ignores `android-app/.tooling/`; verify before any commit. No real learner personal data or app credentials.
- Rights: **PO AFFIRMED** for the named sources as a user declaration. Keep per-file license/evidence status separate; no automatic `VERIFIED_FOR_SCOPE` or release-ready QA. **No production Part1–4 unlock, no bundling real audio into `app/src/main/assets`, no Full Mock**, no changes to controlled baselines.

## Sequential autonomous backlog

### `NLI-01` — Repair and harden one-sample acquisition (P0)

- Re-run current `scripts/crawl_one_zenlish_part3_group.py --self-test` and its single-page fetch. Detect stale assumptions about JSON markup, group IDs, choice formats or direct audio URLs; do not treat a successful `--self-test` as proof real page retrieval works.
- Improve resilient parsing of public HTML/JSON and safe media validation, clean CLI arguments, explicit bounded network/error handling, reproducible provenance, no logging of cookies, and idempotent local output. Add **offline tests** of valid/missing/malformed group/choices, media redirection, wrong media type, truncated media, duplicate IDs, absent keys, changed structure and forbidden hosts.
- If real Zenlish page/audio are unreachable, report actual HTTP/DNS outcomes and proceed with offline test infrastructure; do not force source access.

### `NLI-02` — Small diverse Listening sample batch (P1)

- Try at most 4 accessible groups **total**, including known Zenlish `41021` / Part3 Q32–34. Prioritize testing the distinct data structures Part1 photo/audio, Part2 question-response, Part3 conversation group and Part4 talk group. If one Part is inaccessible under constraints, do not violate caps merely to complete the four-part checklist; report coverage gaps.
- Each local asset manifest must record: source, public page URL, exact group/item IDs, ordered question indices, number of choices, media URL where available, byte-size, SHA-256, MIME/magic, decoded duration, channels and sample rate where tools are installed, duplicate/empty media flags, response status, retrieval date, and file-level rights evidence status (`PO_DECLARED_NOT_INSPECTED`). Do not invent answer keys. Mark `ANSWER_KEY_UNVERIFIED` unless an authoritative, attributable answer key is actually present.
- Prefer standard library and existing local tools (`ffprobe`/`ffmpeg` if already installed); avoid new paid dependencies or external AI/cloud services. If not installed, log `NOT_RUN` for codec checks instead of silently skipping.
- Do **not** copy real questions/audio into the public source tree or app. If a desired mapping is missing, mark `PARTIAL` or `BLOCKED`, not PASS.

### `NLI-03` — Offline import-preparation and quality checks (P1)

- Create a **generic, source-agnostic local-only import manifest schema and offline validation CLI**, supporting Part1 image relationship and Parts2–4 group-to-items-to-audio mapping, source-version and hash, playback-format metadata, QA and provenance states.
- Tests on **synthetic generated fixtures only** for malformed media signatures, missing/duplicate IDs, wrong group ordering, missing questions, broken mapping, hash mismatch, absent audio, missing Part1 image, missing answer keys and differences between `retrieved`, `mapped`, `QA_READY`. Never promote any downloaded sample to `QA_READY`.
- Design a **dry-run adapter contract** describing how a later PO-authorized CX-04 integration could consume local manifests and safe content fixtures; no new Android production code, no SQLite/backend, no unapproved asset bundling or extra Part availability.
- Must be repeatable with no network access after the initial bounded retrieval: offline test command and fixture data kept synthetic.

### `NLI-04` — Local report, tests and publication (P0)

- Run the crawler self-test and all new offline tests, record command, exit code, count and failures. Re-run existing Alpha, Beta and CX04 source guards and Gradle unit/build **if** app code/toolchain is touched; app source should normally remain unchanged.
- Produce safe text-only `docs/STAGE05_LISTENING_OVERNIGHT_INGESTION_ENGINEERING_REPORT_V0.1.md` with per-Part `FETCHED / PARTIAL / BLOCKED / NOT_RUN`, number of groups/questions, actual IDs/hashes/sizes, parser errors, QA and rights gaps, test outcomes, exact file paths relative to ignored local directory, and what the next single PO decision would be. Do not paste question text, direct copyrighted content, raw HTML or audio into report.
- Commit and push **only** crawler/validator source, synthetic tests/fixtures, manifest *schema*, docs and safe metadata; no captured copyrighted content, screenshots, APK, raw logs, personal/secret data or absolute private paths.
- Stop after the capped batch and documentation, **even if time remains**. Do not spin/sleep/retry indefinitely, start a second batch automatically or ask PO minor technical questions.

## Gate preservation

Stage05 is `CONDITIONAL PASS FOR DEVELOPMENT TRANSITION ONLY`; G05-CP01..08 and earlier conditions ACTIVE, POL01..16 OPEN, B1 2×200 content QA NOT VERIFIED, budget DEFERRED. No formal QA/ECP, real phone/learner, pilot/release, paid tools, new CX05+, Full Mock, backend, durable ACK, or real media integration into the Android app.

**Completion means a truthful finite sample + validated reusable ingestion preparation, not an operational production corpus.**
