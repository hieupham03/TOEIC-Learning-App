# AGENTS.md — One public Listening sample fetch (PO-authorized)

**Current user direction:** The Product Owner explicitly requested to find/crawl **one arbitrary Listening sample** and confirmed that the PO will handle the rights. Prior PO rights affirmation is recorded in `docs/STAGE05_LISTENING_PO_RIGHTS_REAFFIRMATION_V0.1.md`. The scope here is a **single narrowly bounded source acquisition**, not a new content distribution, QA or development approval.

## Exact working instructions

- Branch: `ingestion/one-zenlish-p3-32-34`.
- Read `docs/STAGE05_SINGLE_LISTENING_SAMPLE_ACQUISITION_RECORD_V0.1.md`.
- Candidate: Zenlish `TEST 1 – 2022` / **Part 3 question group 32–34**, group ID `41021`.
- Public page: `https://zenlishtoeic.vn/stm-quizzes/test-1-2022/`.
- Direct referenced MP3: `https://zenlishtoeic.vn/wp-content/uploads/2023/04/zenlish-test-01-part-3-32-34.mp3`.
- Run `python scripts/crawl_one_zenlish_part3_group.py --self-test` then `python scripts/crawl_one_zenlish_part3_group.py --output .tooling/one-listening-sample` from `android-app/`.
- Verify 3 questions, group/item relation, A–D choices, local MP3 header, byte count, hash, and playable file duration if a local decoder is available. The indexed correct-answer fields are blank: mark `ANSWER_KEY_NOT_VERIFIED` and `NOT_QA_READY`, never invent answers.
- Save source HTML, full questions/choices, MP3 and any original private proofs **only under ignored local `.tooling/`**. **Never push real audio, scraped question text or source HTML to this PUBLIC GitHub repo**.
- Commit a text-only `docs/STAGE05_SINGLE_LISTENING_SAMPLE_CRAWL_REPORT_V0.1.md` reporting truthful PASS/PARTIAL/BLOCKED, source URL, group ID, timestamps, sizes/hashes, local path and outstanding QA/provenance gaps. Do not claim the site refused access merely because the assistant environment had unavailable DNS.
- Do not bypass login, CAPTCHA, robots/anti-abuse measures, access restrictions or paywalls, and do not crawl further groups. If HTML/API is inaccessible, report the blocker. No vendor contact or payment.

**Not authorized:** integrating this third-party MP3 into `app/src/main/assets`, changing `SyntheticCatalogue` readiness, exposing B1 Full Mock, uploading content to public app distribution, formal QA/ECP, new CX features, backend, durable ACK, clock, real learner or physical-device test, spending or signed baseline modifications. Existing Stage05 CONDITIONAL PASS, G05-CP01..08 ACTIVE and content QA NOT VERIFIED remain unchanged.

Old AOV/CX04 development approvals remain historical facts but do not expand this branch's task beyond **one source group download and private evidence check**.
