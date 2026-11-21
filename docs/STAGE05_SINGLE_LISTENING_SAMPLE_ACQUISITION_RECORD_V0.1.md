# Stage05 — Single Listening Sample Acquisition Record V0.1

**Authority:** PO explicitly requested: "hãy tìm, crawl 1 đoạn bất kì, vấn đề bản quyền tôi sẽ xử lý đầy đủ". This authorizes **one bounded, openly reachable Listening group fetch**, not bulk crawling, QA, public redistribution or access-control bypass. PO reaffirmed rights in `docs/STAGE05_LISTENING_PO_RIGHTS_REAFFIRMATION_V0.1.md`. The existing signed baselines, B1 gates and all G05-CP remain unchanged.

## Concrete sample discovered through public web indexing

| Key | Identified value |
|---|---|
| Provider | Zenlish |
| Public test page | https://zenlishtoeic.vn/stm-quizzes/test-1-2022/ |
| Logical group ID | `41021` |
| Part | `Part 3 — Conversations` |
| Question numbers | `32`, `33`, `34` |
| Indexed structure | One group, 3 question prompts, 4 choices each (A–D) |
| Referenced audio | https://zenlishtoeic.vn/wp-content/uploads/2023/04/zenlish-test-01-part-3-32-34.mp3 |
| Answer key | NOT VERIFIED; indexed question answer fields empty |
| Media byte length, SHA256, duration | UNKNOWN until actual successful download |
| Asset-content QA | NOT RUN, `NOT_QA_READY` |
| Rights | PO affirmed rights; exact asset scope/terms to be reconciled by PO |

Source discovery basis: public search indexing of the URL above (2026-11-22). Do not copy full text, choices or MP3 into this **public GitHub repository**.

## Assistant-environment attempt — precise boundary

A single HTTPS GET attempt to the page and a single HTTPS GET attempt to the referenced audio URL **did not succeed**, because DNS resolution of `zenlishtoeic.vn` was unavailable inside the assistant's container. No HTTP status, audio bytes or question HTML were returned; **this is not a website denial**. Discovery of a direct MP3 URL is **not proof of successful retrieval**.

The bounded Python crawler `android-app/scripts/crawl_one_zenlish_part3_group.py` is designed for execution **locally on the PO's Codex workstation**. It targets exactly this known group and audio, validates source IDs/order, records source and media hashes and only writes to ignored `android-app/.tooling/one-listening-sample/`. It does not log in, extract cookies, crawl other groups, bypass CAPTCHA/rate limits or silently substitute assets.

### Execution checklist / end state

1. Run `python scripts/crawl_one_zenlish_part3_group.py --self-test` from `android-app`.
2. Run `python scripts/crawl_one_zenlish_part3_group.py --output .tooling/one-listening-sample`.
3. If the source is publicly reachable, verify the saved MP3 magic, byte size/hash and decode/playback duration, and verify that the three questions are all linked to the same group/audio. Never invent an answer key if the source only exposes blanks.
4. Preserve the downloaded HTML, question JSON and original MP3 **locally**; no public GitHub commit and no additional external distribution. Text-only status, IDs, hashes and proof gaps may be committed to `docs/STAGE05_SINGLE_LISTENING_SAMPLE_CRAWL_REPORT_V0.1.md`.
5. If the page is JS-only or source response is gated/403/429, report BLOCKED with the HTTP status. Do not work around login, CAPTCHA, anti-bot or hidden APIs. Even if audio fetch works while metadata fails, report PARTIAL, not a successful question+audio group.

This instruction is a **one-sample acquisition proof only**. It does not authorize integrating real media into `android-app/app/src/main/assets`, making Part 1–4 available in the real Part picker, marking content QA PASS, distributing copyrighted audio in GitHub, backend, B1 Full Mock, formal QA/ECP, release, spending or any other CX slice.

**Current status:** one group URL and MP3 reference discovered; assistant-local actual download BLOCKED due DNS. Codex local execution PENDING.
