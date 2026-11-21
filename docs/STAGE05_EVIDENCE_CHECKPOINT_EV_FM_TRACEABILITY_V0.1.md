# Stage05 — ECP Proposal Full EV/FM Traceability V0.1

**Status:** PROPOSED MAP ONLY — no actual test or M3/M4 evidence; **12/12 EV mapped and 18/18 FM mapped, 0 executed**. The checkpoint IDs here are future checkpoints, not currently authorized activities. Every candidate ARCH03-A/B/C faces the same questions.

## I. EV-01..EV-12 → proposed checkpoint

| EV | Claim needing evidence | Negative cases | Proposed ECP | Evidence status NOW |
|---|---|---|---|---|
| EV-01 | Continuity despite clock changes | FM-03/04 | ECP-00, ECP-01 | M2 / 0 real proof |
| EV-02 | UI restore is not proof of clean attempt | FM-01/02 | ECP-01, ECP-02 | M2 / 0 real proof |
| EV-03 | Reboot duration trust | FM-03/04 | ECP-00, ECP-01 | M2 / 0 real proof |
| EV-04 | Listening progression and replay control | FM-01/05/18 | ECP-01, ECP-05 | M2 / 0 real proof |
| EV-05 | Durable confirmed answer | FM-07/02 | ECP-02 | M2 / 0 real proof |
| EV-06 | Lost ACK and safe retry | FM-08/14 | ECP-02 | M2 / 0 real proof |
| EV-07 | Shared phone learner isolation | FM-09 | ECP-03 | M2 / 0 real proof |
| EV-08 | Deletion across copies | FM-10/11 | ECP-03 | M2 / 0 real proof |
| EV-09 | Content release readiness | FM-06/16 | ECP-04 | M2 / 0 real proof |
| EV-10 | Historical results after key correction | FM-12/14/17 | ECP-04 | M2 / 0 real proof |
| EV-11 | Mock practice-bank isolation | FM-13 | ECP-04 | M2 / 0 real proof |
| EV-12 | Long Reading and accessibility | FM-15/18 | ECP-05 | M2 / 0 real proof |

## II. FM-01..FM-18 → proposed checkpoint

| FM | Falsifier / scenario | EV link | Proposed ECP | Runtime status NOW |
|---|---|---|---|---|
| FM-01 | App switch during Listening | EV02/04 | ECP-01 / ECP-05 | NOT RUN |
| FM-02 | Process reclaimed during Reading | EV02/05 | ECP-01 / ECP-02 | NOT RUN |
| FM-03 | Reboot during Reading | EV01/03 | ECP-01; ECP-00 policy | NOT RUN |
| FM-04 | Device clock changed | EV01/03 | ECP-01; ECP-00 policy | NOT RUN |
| FM-05 | Audio focus stolen | EV04 | ECP-01 | NOT RUN |
| FM-06 | Wrong/missing media | EV09 | ECP-04 | NOT RUN |
| FM-07 | Answer selected without connection | EV05 | ECP-02 | NOT RUN |
| FM-08 | Commit succeeded, ACK lost | EV06 | ECP-02 | NOT RUN |
| FM-09 | Switch family learner with pending save | EV07 | ECP-03 | NOT RUN |
| FM-10 | Verified deletion request | EV08 | ECP-03 | NOT RUN |
| FM-11 | >30 days after pilot retention | EV08 | ECP-03 | NOT RUN |
| FM-12 | Released answer key corrected | EV10 | ECP-04 | NOT RUN |
| FM-13 | Practice overlaps Mock A/B | EV11 | ECP-04 | NOT RUN |
| FM-14 | Duplicate attempt submission | EV06/10 | ECP-02 / ECP-04 | NOT RUN |
| FM-15 | Long Reading/text enlargement/background | EV12 | ECP-05 | NOT RUN |
| FM-16 | Unverified explanation shown | EV09 | ECP-04 | NOT RUN |
| FM-17 | Raw scores across different forms | EV10 | ECP-04 | NOT RUN |
| FM-18 | Android target background behavior changes | EV04/12 | ECP-01 / ECP-05 | NOT RUN |

## III. Common checkpoint evidence and veto semantics

- **ECP-00** is prerequisite PO policy on numeric tolerances and evidence authorities, especially EV01..04/FM03..04; zero such thresholds chosen here.
- **ECP-01..05** require independent scoped permission and later signed QA; evidence that a candidate *might* satisfy an FM is not a passing observation.
- **ECP-06** cannot award feasibility PASS or recommend a winner by counting document mappings. Any claims unsupported by actual artifacts remain `NO APP EVIDENCE`, even if M0/M1/M2 are comprehensive.
- Retain QA-01..08 as approved framework; future QA-01..06 per-item/source/audio/key content, QA-07 result semantics, QA-08 Android/reading/privacy testing at relevant gates.
- The 2 Full Mocks were already PO-inventoried. Do not request re-inventory, rescrape sources or infer content QA PASS.

## IV. Original sources of truth

- `STAGE05_ARCH03_EV01_EV12_OPTION_TRACEABILITY_V0.1.md`
- `STAGE05_ARCH03_FM01_FM18_CANDIDATE_CHALLENGE_V0.1.md`
- `STAGE05_EVAL004_EVIDENCE_GAPS_AND_HANDOFF_CHECKPOINTS_V0.1.md`
- Signed PRD V0.6, SRS V0.6, Acceptance Catalogue V0.4 and Design-Spec V0.3.
