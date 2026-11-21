# Software Requirements Specification — TOEIC Learning App — BASELINE CANDIDATE V0.6

**Status: D03-BASELINE-010 PENDING. NOT APPROVED / NOT BASELINED.**  
**Scope authority:** D03-SCOPE-009 APPROVED S1-A/S2-A/S3-A on 2026-11-21. Stage03 IN PROGRESS; no UI/UX, API, DB schema, architecture or code defined.

## 1. Normative interpretations

- **`SHALL` below** expresses approved *business behavioral intent* transcribed into **candidate baseline specification**, not separately signed document text. After D03-BASELINE-010 approves the exact version, wording becomes controlled baseline.
- **B1:** two independent 200-item L&R full mocks mandatory; PO confirms inventories complete. Item-by-item key/media/source/overlap QA **NOT VERIFIED**. Rights to specified websites PO self-attested, no per-asset audit evidence claimed.
- **QA-01..08:** approved quality framework; actual results **NOT RUN/NOT VERIFIED**. **Budget DEFERRED** per PO, CP-04 remains in force. All financial/vendor considerations excluded from this Requirements review.
- **Scope:** FR-001..019 **IN** including basic rule-based FR-014; FR-007 explanation branch **CONDITIONAL**. FR-020..023 **OUT**, without losing traceability of future backlog.
- **Severity and verification:** `blocking` means not eligible for pilot until relevant QA passes, **not** that content is currently known broken.

## 2. Normative business rules

| ID | Requirement (implementation-neutral) | Decision/test |
|---|---|---|
| BR-01 | Two independent mock forms A/B, **each 200**: P1=6, P2=25, P3=39, P4=30, P5=30, P6=16, P7=54. Each has 100 Listening questions (~45 min ordered audio) and 100 Reading questions (75 min). | B1; QA-01, AT-10 |
| BR-02 | Full Mock is evaluative, separate from Part/one-question practice. No voluntary pause or arbitrary Listening replay for an attempt represented as clean/comparable. | S2 P01,03,04; AT-09,11,13 |
| BR-03 | Essential content/answer/media/asset and form/version provenance MUST pass authorized-content QA before pilot publication. Inventory completion alone does not imply approved content. Part bank MUST not expose A/B evaluative items in advance. | S1 M02/M03/M06; S3 AC-02..04 |
| BR-04 | Listening ordered/audio segment not cut solely at 45:00; Reading 75 min. No silent reset/time grant when interrupted. If time or audio integrity indeterminate/materially affected, attempt INCOMPLETE/NON-COMPARABLE rather than clean-comparable. | S2 P02/05/07; AT-11,19 |
| BR-05 | Saved-answer success only after durable acknowledgement. On uncertain network state, distinguish pending/unsaved; user action must not create a false saved-success claim. | S2 P06; AT-05,19 |
| BR-06 | A finalized attempt has at most one result. Report correct/attempted/unanswered by Part, Listening, Reading, total, form/version/date and integrity state. No official ETS 10–990 score equivalence or scientifically validated gain inferred from unmatched forms. | S2 P07/08; AT-12/13 |
| BR-07 | Key and media revisions preserve traceable historical attempt context; no silent historical score rewrite. Verified explanations only; absent vetted explanation disclosed. | S2 P08; AT-07/16 |
| BR-08 | Family participant data isolated. Deletion of verified learning-data request within **7 calendar days** subject to lawful exceptions; routine retention ≤**30 days after pilot** unless legitimate consent/exception. Identity implementation TBD before pilot. | S2 P09; AT-18 |
| BR-09 | Pilot is 2–5 invited learners over 4 weeks; minimum **2 participants** completing valid pair A/B and reporting usability + **2 participants** using practice and giving feedback; insufficient pair evidence marked INCONCLUSIVE. | S3 PM-01..06 |
| BR-10 | Content and software QA evidence logged and associated with readiness statuses, not inferred from framework approval. Budget work DEFERRED until PO explicitly reopens; CP-04 retained. | QA-01..08, S3 AC-07, CP-04 |

## 3. Functional requirements — stable FR identifiers

| FR | MVP classification | SHALL/expected observable behavior | Acceptance / quality link |
|---|---|---|---|
| FR-001 | **IN** M01 | Learner may provide/edit goal, self-reported level and available duration; active values are associated only with that learner and can be used for basic guidance. | AT-01; QA-08 |
| FR-002 | **IN**, gated M02 | Learner can choose practice Part1–7 from QA-READY bank **separate from Full Mock A/B**. Content unavailable/unreviewed cannot be falsely presented as ready. | AT-02,10/13; QA-01/05/06 |
| FR-003 | **IN**, gated M02 | Listening groups/items map to correct audio/sequence and do not publish missing/wrong critical audio. Full Mock replay obeys P04; practice can be flexible. | AT-03,11; QA-03 |
| FR-004 | **IN** M02/M07 | Reading passages/tables/images and associated item groups remain complete, ordered, readable, and not silently altered at long lengths. | AT-04; QA-04/08 |
| FR-005 | **IN** M04/M07 | Confirmed answers stay on correct learner/form/attempt/Part/item across navigation and interruption. Save success only after durable confirmation, otherwise pending/uncertain. | AT-05,19; QA-08 |
| FR-006 | **IN** M04 | Score using QA-verified key of the appropriate content version; missing or mismatched key not silently graded. | AT-06,12; QA-02/07 |
| FR-007 | **IN key; CONDITIONAL explanation** M04/M08 | Review shows vetted correct key; explanation only when curator-verified; when not available, explicitly no verified explanation, never fabricated. | AT-07; QA-02/06 |
| FR-008 | **IN** M04 | Learner can review own wrong-answer and attempt history, associated with Part/form/date and source version; no other learner's data. | AT-08; QA-07/08 |
| FR-009 | **IN** M05a | Learner can complete a one-item or Part practice session under flexible rules without misrepresenting it as comparable full mock. | AT-09; QA-08 |
| FR-010 | **IN — B1 MANDATORY**, gated M03 | Both forms A/B meet BR-01; unable to mark one or both available for pilot until QA content gate PASS. One-form fallback forbidden without PO change. | AT-10; QA-01..06 |
| FR-011 | **IN** M03 | Timing/Listening/Reading and exit/timeout/submit follow P01..07; don't grant silent extra time or replay to clean attempt; explicit complete/non-comparable/incomplete outcomes. | AT-11,19; QA-08 |
| FR-012 | **IN** M04 | Display factual right/answered/blank counts by Part, L/R and total, plus form/attempt/version/integrity label; no ETS official converted score. | AT-12; QA-07 |
| FR-013 | **IN** M03/M04 | Exposed, assisted, paused or integrity-compromised attempts are marked non-comparable/excluded from clean trend. Cross-form raw differences not asserted as calibrated ability improvement. | AT-13; QA-05/07 |
| FR-014 | **IN** M05b | Optional explainable rule-based next Part suggestion from goal, available time and weak Part; missing-data fallback and user override. No runtime AI. | AT-14; QA-07/08 |
| FR-015 | **IN** M06/M09 | Authorized source/version/QA status recorded; broken key/audio/asset cannot silently become READY, withdrawal and review recorded. | AT-15; QA-02..06 |
| FR-016 | **IN** M06 | Detect affected historic attempts when key/content version changes; do not silently overwrite reports or silently rescore them. | AT-16; QA-02/07 |
| FR-017 | **IN** M06 | Block unavailable/unready content from starting clean Full Mock and transparently explain availability state. | AT-17; QA-01..06 |
| FR-018 | **IN** M01/M07 | Family learner access/history/error data isolated; verified requests for deletion processed to BR-08 timeline with transparent exceptions. | AT-18; QA-08 |
| FR-019 | **IN** M07 | For app background/process termination/network loss, preserve confirmed answers and correct time/attempt integrity; do not duplicate final result or show false saved state. | AT-19,05; QA-08 |
| FR-020 | **OUT** X01 | Future idea: automatic PDF/audio/answer ingestion — NOT included in pilot. | Not MVP |
| FR-021 | **OUT** X02 | Future idea: runtime AI tutor/generation/adaptive AI — NOT included in pilot. | Not MVP |
| FR-022 | **OUT** X03 | Future idea: advanced interactive vocabulary notifications — NOT included in pilot. | Not MVP |
| FR-023 | **OUT** X04 | Future idea: offline-first/iOS/TOEIC S&W/monetization — NOT included in pilot. | Not MVP |

## 4. Non-functional requirements — proposed controlled baseline

| NFR | Business target / quality rule | Acceptance / due milestone |
|---|---|---|
| NFR-001 | **100% essential published Full Mock content** traceable to authorized source/answer/media/passages/version and reviewed. | AC-03; QA-01..06 BEFORE pilot content release |
| NFR-002 | No known critical wrong-group Listening audio or missing indispensable media in published mock forms. | AC-04, AT-03; QA-03 BEFORE pilot |
| NFR-003 | **Zero known critical** silent confirmed-answer loss or incorrect attribution before pilot. | AC-05, AT-05/19; device test BEFORE pilot |
| NFR-004 | Strict Full Mock integrity: consistent timing, no silent reset/duplicate result; device timing/grace tolerance TBD test-plan checkpoint. | AT-11/19; QA-08 BEFORE pilot |
| NFR-005 | Reading full passages/groups/tables intact; **at least 2 Android phone sizes/contexts** tested for legibility/answerability. | AC-06, AT-04 BEFORE pilot |
| NFR-006 | Zero known critical cross-learner disclosure; verified deletion request within 7 calendar days subject to lawful exceptions; routine deletion ≤30 days post-pilot. | AC-05, AT-18 BEFORE pilot; privacy exception mapping due pilot |
| NFR-007 | Transparent raw scoring and integrity labels, no unsupported ETS-equivalent or gain claims. | AC-05, AT-12/13 BEFORE pilot |
| NFR-008 | Historical result versions and corrections auditable; no silent recomputation. | AT-16 BEFORE pilot; specific correction review before policy execution |
| NFR-009 | **100% critical MVP FR/NFR** mapped to an AT with prerequisites, expected outcome and future verification phase. | AC-01 BEFORE D03-BASELINE-010/Stage03 Gate |
| NFR-010 | Basic Android reading/accessibility readability; specific device/contrast/font numeric targets TBD with test plan. | AC-06/08, AT-04 BEFORE pilot |
| NFR-011 | Accurate online connectivity, pending/saved and retry/recovery state; no full offline claim. | AT-19 BEFORE pilot |
| NFR-012 | Public app name/content copy must not suggest ETS sponsorship or official score validity without permission. | Copy/policy review BEFORE public release |
| NFR-013 | Budget/operating cost controls under CP-04 **DEFERRED BY PO**; no current costs or spend authorization. | Reopened by PO before relevant spend/release gate; not a present baseline blocker |

## 5. QA, acceptance and pilot milestones (S3-A approved)

| Gate | Approved requirement | Evidence status now |
|---|---|---|
| **Stage03 Requirements** | AC-01 100% critical FR/NFR traceable to AT/QA and verification phase | Mapping created; mapping self-audit due before D03-BASELINE-010; no app test PASS asserted |
| **Before mock pilot content** | AC-02..04 2×200 + exact 7 Part, essential asset/key/source coverage 100%, zero known critical content defects/overlap/exposure | **NOT VERIFIED** beyond PO-reported inventory |
| **Before pilot software use** | AC-05/06 zero known critical scoring, answer loss, privacy leaks; Reading on 2 Android contexts | **NOT RUN** |
| **Every QA checkpoint** | AC-07 log `PASS/FAIL/NOT RUN/BLOCKED/EXCEPTION`, evidence and reviewer | Framework approved, actual log not populated |
| **Test-plan milestone** | AC-08 quantitative performance/timing tolerances/devices targets to be approved before test-plan baseline | **TBD, DUE LATER**, not assumed PASS |
| **4-week pilot** | PM-01..06 2–5 invited people; ≥2 valid paired mock completions, ≥2 Part practice feedback, honest inconclusive label | **NOT RUN**, no artificial score gain target |

## 6. Edge policy and implementation-neutral unfinished work

| Issue | Approved guardrail | Open detail / due |
|---|---|---|
| Listening ~45m | Preserve ordered form-specific audio | exact device tolerance/asset timing test plan BEFORE pilot |
| Network/grace | No silent time reset, false save or false comparable attempt | numerical tolerance and recovery UX wording BEFORE test-plan baseline |
| Key correction | Preserve versions/history, no silent score rewrite | recomputation/appeal process before enabling any feature that changes scored results |
| Account deletion | ≤7d after verified request, routine ≤30d post-pilot | identity verification, legal exceptions, deletion method BEFORE pilot |
| Device accessibility | long Part7 fully legible/answerable in ≥2 Android contexts | actual devices and quantitative font/contrast targets BEFORE test-plan baseline |
| Data latency/stability | truthful save/interrupt recovery | numeric latency, endurance/network thresholds BEFORE test plan |
| Practice bank | distinct from mock forms, valid rights/content QA | bank item content QA BEFORE pilot |
| Budget | deferred | explicit PO reopening at future operational decision, CP-04 active |

**Material business-policy changes (pause/replay/7d/30d/two-mock/2-participant thresholds) require new PO approval; technical test-specific targets cannot weaken signed business integrity.**

## 7. Baseline and Gate status

- `D03-SCOPE-009` APPROVED business scope/policy/targets, **not this exact document**.
- `D03-BASELINE-010` PENDING — user to sign this `SRS BASELINE CANDIDATE V0.6` plus `PRD BASELINE CANDIDATE V0.6`/AT catalogue and accept tracked later QA/technical dependencies.
- `Stage03 Gate` NOT STARTED/NOT PASSED; separate decision **after baseline**. Content and software QA test PASS cannot be implied.
- No UX/UI, architecture, database/API/cloud selection, source extraction, payment or app code authorized.
