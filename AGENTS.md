# AGENTS.md — Current active branch: bounded overnight Listening ingestion

**Active PO direction (2026-11-22):** PO requested a larger amount of **overnight autonomous Codex work** following the prior one-group Zenlish acquisition request. That authorizes a finite **four-group maximum** across already PO-affirmed Listening sources, plus a robust local crawler/parser/QA-preparation tool and safe report, **not** mass crawling or app media integration.

**Branch:** `ingestion/listening-overnight-bounded`. **Binding operational scope:** `docs/STAGE05_LISTENING_OVERNIGHT_BOUNDED_INGESTION_WORKPLAN_V0.1.md`. Read it first. Previous `ingestion/one-zenlish-p3-32-34` branch and one-group restriction remain its historical record, superseded *on this branch only* by the PO-directed finite overnight batch. Avoid changing any older branch history or discarding local changes.

## Work order

1. `NLI-01`: exercise and harden `android-app/scripts/crawl_one_zenlish_part3_group.py` for one known source and build deterministic offline tests. **A passing parser self-test does not prove a live website was crawled**.
2. `NLI-02`: at most **four** Listening groups **in total** (including known Zenlish P3 Q32–34), ideally one of each P1–4, at most **15 questions**, 24 HTTP requests, 32 MiB downloaded combined and 12 MiB per audio. No catalogs/full tests. Allowed sites only: `zenlishtoeic.vn`, `test.thetoeiclab.vn`, `study4.com`. Minimum 3 seconds between requests to each host, bounded retries (not on 403/429). If blocked by login, CAPTCHA, site/robots/anti-abuse, **STOP** that source; never evade.
3. `NLI-03`: implement a *generic local-only* ingestion manifest schema and offline data/media validator with synthetic test fixtures for Part1 image and P2–4 groups and negative mappings. No actual app code/media integration.
4. `NLI-04`: produce only text-only `docs/STAGE05_LISTENING_OVERNIGHT_INGESTION_ENGINEERING_REPORT_V0.1.md` with true outcomes, run tests, commit and push safe scripts/schema/tests/docs, then **STOP**. If live sites inaccessible, continue valuable offline work and report `BLOCKED`/ `PARTIAL` explicitly. Do not idle or expand limits.

## Data safety, licensing and gate

PO reaffirmed rights to named sources in `docs/STAGE05_LISTENING_PO_RIGHTS_REAFFIRMATION_V0.1.md`. Accept the declaration without re-asking; per-asset permission details and content QA are **separate** and must never be silently marked verified. Live HTML/audio/images/question text/audio transcripts/answers and browser screenshots are **LOCAL only**, under ignored `android-app/.tooling/listening-overnight/`. Root `.gitignore` ignores that directory. Repo is PUBLIC. Do not commit real media, copied user-owned material, raw logs, credentials or private paths.

No login bypass, proxy rotation, CAPTCHA solving, password use, unrestricted crawling, new packages requiring payment, automatic vendor contact, remote content processing, public repo assets, Android real Part1–4 unlock, Full Mock, QA/ECP official, live B1, backend, ACK/time authority, CX05+, learner/real-device/pilot/release, signed baseline edits or expenditure. Stage05 CONDITIONAL PASS for development only; G05-CP01..08 active, other CPs active, POL01..16 open, budget deferred. Make minor reversible technical choices without per-task PO confirmation.

**The deliverable is repeatable, finite ingestion readiness with honest evidence—not content publication.**
