# Requirements Acceptance Catalogue — BASELINE CANDIDATE V0.4

**Authority:** D03-SCOPE-009 APPROVED **S3-A thresholds and verification phases**. **Catalogue text NOT BASELINED:** D03-BASELINE-010 pending. All actual content/device/app execution **NOT RUN / NOT VERIFIED**; table Expected Outcome does **not** constitute PASS.

## 1. Stable AT-01..AT-19 acceptance cases and business-policy reconciliation

| Case | Intent | Requirement | QA | Preconditions/data | Action | Expected outcome | When tested | Proposed threshold/status |
|---|---|---|---|---|---|---|---|---|
| AT-01 | Onboarding / goals | FR-001 | QA-08 | One learner with no goals; one with saved goals | Set/edit goal and available study duration; return later | Correct current values reflected; no cross-person override | Functional build, not now | S1/S2/S3 APPROVED target, test NOT RUN |
| AT-02 | Part practice coverage | FR-002 | QA-01/06 | At least one QA-ready Part and one unready Part | Attempt to start both | Ready items accessible; unready Part clearly unavailable, never falsely READY | Content gate then build | S1/S2/S3 APPROVED target, test NOT RUN |
| AT-03 | Listening media mapping | FR-003 | QA-03 | Known group/item/audio relation plus deliberately broken mapping | Compare groups, play clips and inspect sequence | Matched media plays in correct order; malformed group blocked and logged | Content + system later | AC-04 ZERO known blocking errors before pilot — APPROVED |
| AT-04 | Reading relationship | FR-004 | QA-04/08 | Known Part 6/7 multi-passage, tables, image assets and missing one asset | Read item/group and audit asset relations | All required passages/figures complete and ordered; missing essential media blocks form readiness | Content + device later | AC-03/04 100% essential assets; zero blocking gaps — APPROVED |
| AT-05 | Answer preservation | FR-005 | QA-08 | Two test learners, form/item IDs, answered item | Confirm answer, change item, leave/relaunch/return | Only most recent confirmed answer is present on correct learner and attempt; no silent loss | Software test later | P06 durable ACK policy APPROVED; technical latency TBD |
| AT-06 | Correct-key scoring | FR-006 | QA-02/07 | Known answers: correct, incorrect, blank, missing-key, wrong version | Submit and compute separately | Known-key correct counted once, blank counted as unattempted; missing/broken key not silently graded | Content + scoring test later | AC-05 ZERO known critical scoring defects before pilot — APPROVED |
| AT-07 | Vetted explanation | FR-007 | QA-02/06 | One item with vetted explanation and one without | Review both incorrect responses | Correct key consistent; vetted explanation rendered where available, else clearly unavailable; no invented text | Content + build later | Coverage TBD |
| AT-08 | Per-learner history | FR-008 | QA-07/08 | Two learners with divergent answers/attempts | Review and switch authorized learner context | Each sees own history and errors; no cross-learner access | System/security test later | Zero known cross-user exposure |
| AT-09 | One-question session | FR-009 | QA-08 | Ready practice content | Start a short Part session, answer one item and finish | Correct answer and session state recorded; not mistaken for full mock | System later | S1/S2/S3 APPROVED target, test NOT RUN |
| AT-10 | B1 two-form gate | FR-010 | QA-01..06 | PO-inventoried A/B and quality/exception manifest | Check Part counts, unique form IDs, key/media/asset exceptions; attempt to mark unpassed ready | A,B each exactly 200 with ETS Part distribution; failed form cannot be claimed ready | Content audit pre-pilot | AC-02..04 APPROVED; QA execution NOT VERIFIED |
| AT-11 | Timed mock integrity | FR-011 | QA-08 | Mock with simulated background/exit/timeout; controlled clock | Start Listening/Reading, interrupt, return, submit/timeout | No silent timer reset; attempt clearly complete/incomplete/invalid per approved policy; no duplicate finish | System later | S2 P01–P07 APPROVED; numeric tolerance due test plan |
| AT-12 | Raw result arithmetic | FR-012 | QA-02/07 | Known answer masks for two sections and 7 Parts | Score completed mock with blanks and incorrect answers | Section/Part totals sum correctly, correct/attempted/unanswered consistent, labeled practice only | Scoring test later | No ETS-equivalent claim |
| AT-13 | Form comparison restraint | FR-013 | QA-05/07 | One comparable pair, one exposed/untimed attempt, different form versions | Request trend comparison | Unqualified attempt excluded/flagged; form differences and no official TOEIC inference disclosed | System later | Equating unavailable |
| AT-14 | Rule recommendation | FR-014 | QA-07 | First-time learner and learner with weak Part | Ask for next practice; reject suggestion | Fallback for no data; rule reason traceable; learner retains free choice | System later | Rule-based optional; model-level weights remain open |
| AT-15 | Content approval/correction | FR-015 | QA-02/03/04/06 | QA-approved item, item with wrong key/audio, version change | Attempt to publish then correct and re-review | Blocking bad content held, version/source traceable, withdrawal recorded | Content gate | Zero known critical content failures proposed |
| AT-16 | Revision vs historic result | FR-016 | QA-02/07 | Attempt scored using answer-key version 1; key changes in version 2 | Review old and new reports | Revision apparent; historic result not silently overwritten, affected reports identifiable | System later | P08 no silent rescore approved; recompute flow before enabling |
| AT-17 | Unavailable form | FR-017 | QA-01..06 | Form missing media, Part withdrawn, or no service connectivity | Attempt to open form | Does not claim ready; gives clear non-deceptive status and retry/replacement where permitted | System later | S1/S2/S3 APPROVED target, test NOT RUN |
| AT-18 | Privacy/deletion | FR-018 | QA-08 | Two pilot learners; account/identity approach TBD | Access, correct and request deletion of own data | No cross-person access; deletion responds per agreed policy and records exception if legally retained | System later | P09 7-day validated-delete / 30-day post-pilot APPROVED; identity/exception mechanism due pre-pilot |
| AT-19 | Lifecycle/network edge | FR-019 | QA-08 | App background, rotation, process termination, network drop after confirmed answer | Reopen and inspect status and last acknowledged answer; attempt duplicate submit | No silent confirmed-answer loss; clear pending/network state; consistent timer; one completion | Device/system later | P05/P06 APPROVED; technical latency due test plan |

## 2. Approved quality and pilot thresholds — S3-A

| ID | Approved threshold or control | Verification milestone | Current evidence |
|---|---|---|---|
| AC-01 | **100% critical included FR/NFR** have AT ID, preconditions, observable expected result, and verification phase | BEFORE Stage03 requirements signoff | Traceability matrix created for review; audit needed at D03-BASELINE-010 |
| AC-02 | Both A/B each 200, seven Parts exactly 6/25/39/30/30/16/54 | BEFORE pilot content release | PO inventory complete; actual detailed QA NOT VERIFIED |
| AC-03 | **100% released essential** items with validated key/source/version/audio/image/passage relationships | BEFORE pilot content release | NOT VERIFIED |
| AC-04 | **ZERO known blocking errors** in keys, media/group, indispensable passages, cross-form duplicates and pre-exposed evaluation items | BEFORE pilot content release | NOT VERIFIED |
| AC-05 | **ZERO known critical** wrong raw scores, silently lost acknowledged answers, duplicate completion, cross-learner exposure or misleading ETS score claim | BEFORE pilot application release | NOT RUN |
| AC-06 | Complete/legible Part7 complex Reading on at least **2 Android phone sizes/contexts** | BEFORE pilot | NOT RUN |
| AC-07 | Every QA-01..08 checkpoint logs PASS/FAIL/NOT RUN/BLOCKED/EXCEPTION, reviewer and evidence | On QA execution | Framework APPROVED; execution NOT RUN |
| AC-08 | Numeric latency/timing/accessibility/device-version and recovery SLAs **TBD, must be PO signed before software test-plan baseline** | BEFORE software test-plan signoff | TBD, not invented now |

| Metric | Approved observation / target | Interpretive guardrail |
|---|---|---|
| PM-01 | **At least 2** of 2–5 learners validly complete both A/B Full Mocks in 4 weeks | Paired data supports exploratory observation only |
| PM-02 | **At least 2** learners practice Parts and report usability feedback | Not market representativeness |
| PM-03 | Record form/version/date, raw L/R/Part, answered, unanswered, integrity state for evaluable attempts | Not equated ETS score |
| PM-04 | Track critical crash, audio, incorrect mapping, answer loss and Reading readability complaints | Zero known blocking issues required pre-pilot, new pilot incidents logged |
| PM-05 | Compare raw results with documented form-difficulty/integrity limitations | No promised formal-score increase |
| PM-06 | If fewer than 2 valid paired mock completions, label progress conclusion INCONCLUSIVE | Don't fake PM-01 success |

## 3. Deferred evidence and release-blocker classification

- **Before the Stage03 baseline decision:** AT catalogue and critical FR/NFR traceability, business rules and known future-test obligations. Technical test execution is **not** a Stage03 output.
- **Before pilot:** conduct actual content QA-01..06, app/scoring/Android QA-07..08, privacy and readability checks. Blocks release if AC-02..06 fail; do not silently shrink B1 scope.
- **At future test-plan baseline:** determine numerical latency, recovery and device-specific tolerances without altering S2 integrity rules. Missing targets cannot be silently called PASS.
- **Privacy:** 7-day valid deletion request and 30-day after pilot retention are PO APPROVED; actual ID validation, lawful exceptions and execution proof due pre-pilot.
- **Budget:** DEFERRED BY PO (CP-04 still applicable at future authorization); not a present signoff request.
- **Case-by-case logging:** the absence of known failures **before any tests** does not imply zero known critical failures confirmed; QA remains NOT RUN.

## 4. Enduring nine edge-case categories (E-01..E-09)

| ID | Approved business decision | Evidence timing |
|---|---|---|
| E-01 | No voluntary pause in clean comparable Full Mock; flexible Part practice may pause | AT-11/13 later |
| E-02 | No discretionary Listening replay in clean comparable Full Mock | AT-03/11 later |
| E-03 | No silent timer reset / confirmed-answer loss after background/process loss; invalid if integrity uncertain | AT-05/11/19 later |
| E-04 | Pending answer under lost connectivity must not be called saved | AT-05/19 later |
| E-05 | Submit/timeout once, blanks preserved; exact clock tolerance TBD at test-plan gate | AT-11/12 later |
| E-06 | Content key version and historical outcomes auditable; no silent recompute | AT-16; detailed correction policy before use |
| E-07 | Exposed/form noncomparable attempt excluded or flagged | AT-13 later |
| E-08 | Data deletion within 7 days verified request, routine ≤30 days post-pilot; identity/exception details due pre-pilot | AT-18 later |
| E-09 | Long Reading passage/tables completely accessible across ≥2 Android contexts | AT-04 later |

**Status:** all AT-01..19 and AC/PM are SPECIFICATIONS/PLANNED TESTS, not observed execution. Respect approved Product Vision, B1, QA-01..08, S1/S2/S3 and CP-01..05. No architecture/UI/code.
