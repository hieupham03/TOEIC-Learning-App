# S1-A — Approved Business MVP IN/OUT Matrix V1.0

**Authority:** D03-SCOPE-009 = APPROVED (2026-11-21). **Status:** BUSINESS SCOPE LOCKED, **not** PRD/SRS baseline, tested build or pilot release.  
**Prerequisites:** B1 two full mocks mandatory; QA-01..08 framework; CP-01..05; two mock inventories PO-reported completed, content QA evidence open; budgets deferred.

| Group | Business scope status | Description | Stable FR/NFR | Required AT / gate |
|---|---|---|---|---|
| M01 | **IN** | Android, online-first pilot learner profile, goal/available study time; family 2–5 | FR-001; NFR-006 | AT-01, AT-18 |
| M02 | **IN, content-release contingent** | Part1–7 separate practice bank with valid audio/Reading source relations | FR-002..004 | AT-02..04; QA-01,03,04,05,06 |
| M03 | **IN — B1 MANDATORY** | Two separate 200-item Full Mock A/B, 7 Parts, exam-like timed evaluation | FR-010,011,013 | AT-10,11,13; QA-01..08; no one-form fallback |
| M04 | **IN** | Acknowledged answers, verified key, raw score, per-Part score, errors/history | FR-005..008, FR-012 | AT-05..08,12 |
| M05a | **IN** | One-question short session independent of mock integrity rules | FR-009 | AT-09 |
| M05b | **IN** | Basic transparent **rule-based** next-practice suggestion, can be ignored | FR-014 | AT-14 |
| M06 | **IN** | Content QA/version/source, correction and withdrawal, protection of historical attempt context | FR-015..017; NFR-001/008 | AT-15..17; QA-02..06 |
| M07 | **IN** | Recover saved answers, isolate pilot learners, Reading content usable and privacy controls | FR-018..019; NFR-003..011 | AT-18..19 and AT-04/05 |
| M08 | **CONDITIONAL ON CONTENT** | Only vetted explanations when supplied; otherwise state unavailable, not invented | FR-007 | AT-07 |
| M09 | **IN AS CONTENT RESPONSIBILITY** | Rights-cleared curated/authorized source input **without built-in automatic PDF importer** | BR-03; FR-015 | QA-06, AT-15 |
| X01 | **OUT** | Automatic PDF/audio/answer ingestion/extraction | FR-020 | Later PO change request |
| X02 | **OUT** | AI-run explanations, generated question bank, adaptive AI learning | FR-021 | Later PO change request |
| X03 | **OUT** | Advanced interactive vocabulary notifications | FR-022 | Later PO change request |
| X04 | **OUT** | Offline-first, iOS, TOEIC S&W, monetization | FR-023 | Later PO change request |
| X05 | **PROHIBITED CLAIM** | Official ETS 10–990 equivalent score/certification/endorsed claims without separate verified approval | BR-05; NFR-007/012 | AT-12/13 and copy verification |

**Key boundaries:** The two Full Mock sets are already inventoried **according to the PO**; neither item-level QA nor a QA-cleared separate Part bank is asserted. Gate exceptions may prevent pilot launch, but **cannot silently remove an approved IN feature or change B1**. A later scope change requires new PO decision. No mobile screen, account architecture, datastore, provider, payment or parser is chosen by this matrix.
