# Requirements Acceptance Catalogue — DRAFT V0.3

**Status:** REVIEW CANDIDATE; D03-REQ-007 R1–R4 **APPROVED PRINCIPLES**, NOT actual acceptance threshold approval. QA-01..08 framework APPROVED, tests **NOT RUN**. Two Full Mock inventories PO-reported complete. Budget DEFERRED. This is a **test design**, not test execution evidence.

## 1. Acceptance cases for Stage03 drafting

**Meaning of each row:** a prospective future test. `Outcome` is expected behavior, not observed PASS. `Timing` identifies appropriate verification phase. `Metric/threshold` is either proposed or explicitly TBD. **No screen, API, database or technical design is required.**

| Case | Intent | Requirement | QA | Preconditions/data | Action | Expected outcome | When tested | Proposed threshold/status |
|---|---|---|---|---|---|---|---|---|
| AT-01 | Onboarding / goals | FR-001 | QA-08 | One learner with no goals; one with saved goals | Set/edit goal and available study duration; return later | Correct current values reflected; no cross-person override | Functional build, not now | Candidate |
| AT-02 | Part practice coverage | FR-002 | QA-01/06 | At least one QA-ready Part and one unready Part | Attempt to start both | Ready items accessible; unready Part clearly unavailable, never falsely READY | Content gate then build | Candidate |
| AT-03 | Listening media mapping | FR-003 | QA-03 | Known group/item/audio relation plus deliberately broken mapping | Compare groups, play clips and inspect sequence | Matched media plays in correct order; malformed group blocked and logged | Content + system later | Proposed zero known wrong-group clips |
| AT-04 | Reading relationship | FR-004 | QA-04/08 | Known Part 6/7 multi-passage, tables, image assets and missing one asset | Read item/group and audit asset relations | All required passages/figures complete and ordered; missing essential media blocks form readiness | Content + device later | Proposed no missing required passage |
| AT-05 | Answer preservation | FR-005 | QA-08 | Two test learners, form/item IDs, answered item | Confirm answer, change item, leave/relaunch/return | Only most recent confirmed answer is present on correct learner and attempt; no silent loss | Software test later | Exact acknowledgment policy TBD |
| AT-06 | Correct-key scoring | FR-006 | QA-02/07 | Known answers: correct, incorrect, blank, missing-key, wrong version | Submit and compute separately | Known-key correct counted once, blank counted as unattempted; missing/broken key not silently graded | Content + scoring test later | Proposed no inaccurate scored item |
| AT-07 | Vetted explanation | FR-007 | QA-02/06 | One item with vetted explanation and one without | Review both incorrect responses | Correct key consistent; vetted explanation rendered where available, else clearly unavailable; no invented text | Content + build later | Coverage TBD |
| AT-08 | Per-learner history | FR-008 | QA-07/08 | Two learners with divergent answers/attempts | Review and switch authorized learner context | Each sees own history and errors; no cross-learner access | System/security test later | Zero known cross-user exposure |
| AT-09 | One-question session | FR-009 | QA-08 | Ready practice content | Start a short Part session, answer one item and finish | Correct answer and session state recorded; not mistaken for full mock | System later | Candidate |
| AT-10 | B1 two-form gate | FR-010 | QA-01..06 | PO-inventoried A/B and quality/exception manifest | Check Part counts, unique form IDs, key/media/asset exceptions; attempt to mark unpassed ready | A,B each exactly 200 with ETS Part distribution; failed form cannot be claimed ready | Content audit pre-pilot | Threshold release hold proposed; QA execution NOT VERIFIED |
| AT-11 | Timed mock integrity | FR-011 | QA-08 | Mock with simulated background/exit/timeout; controlled clock | Start Listening/Reading, interrupt, return, submit/timeout | No silent timer reset; attempt clearly complete/incomplete/invalid per approved policy; no duplicate finish | System later | Timer/grace/replay specifics TBD |
| AT-12 | Raw result arithmetic | FR-012 | QA-02/07 | Known answer masks for two sections and 7 Parts | Score completed mock with blanks and incorrect answers | Section/Part totals sum correctly, correct/attempted/unanswered consistent, labeled practice only | Scoring test later | No ETS-equivalent claim |
| AT-13 | Form comparison restraint | FR-013 | QA-05/07 | One comparable pair, one exposed/untimed attempt, different form versions | Request trend comparison | Unqualified attempt excluded/flagged; form differences and no official TOEIC inference disclosed | System later | Equating unavailable |
| AT-14 | Rule recommendation | FR-014 | QA-07 | First-time learner and learner with weak Part | Ask for next practice; reject suggestion | Fallback for no data; rule reason traceable; learner retains free choice | System later | Rule specifics TBD |
| AT-15 | Content approval/correction | FR-015 | QA-02/03/04/06 | QA-approved item, item with wrong key/audio, version change | Attempt to publish then correct and re-review | Blocking bad content held, version/source traceable, withdrawal recorded | Content gate | Zero known critical content failures proposed |
| AT-16 | Revision vs historic result | FR-016 | QA-02/07 | Attempt scored using answer-key version 1; key changes in version 2 | Review old and new reports | Revision apparent; historic result not silently overwritten, affected reports identifiable | System later | Policy TBD |
| AT-17 | Unavailable form | FR-017 | QA-01..06 | Form missing media, Part withdrawn, or no service connectivity | Attempt to open form | Does not claim ready; gives clear non-deceptive status and retry/replacement where permitted | System later | Candidate |
| AT-18 | Privacy/deletion | FR-018 | QA-08 | Two pilot learners; account/identity approach TBD | Access, correct and request deletion of own data | No cross-person access; deletion responds per agreed policy and records exception if legally retained | System later | Retention/identity TBD |
| AT-19 | Lifecycle/network edge | FR-019 | QA-08 | App background, rotation, process termination, network drop after confirmed answer | Reopen and inspect status and last acknowledged answer; attempt duplicate submit | No silent confirmed-answer loss; clear pending/network state; consistent timer; one completion | Device/system later | Recovery targets TBD |

## 2. Proposed release-blocking vs non-blocking criteria (NOT PO-approved)

| Class | Example | Proposed action |
|---|---|---|
| Blocking content error | Wrong/unknown key, wrong audio group, missing indispensable passage/table, form not 200 questions | Do NOT release affected Full Mock; correct then recheck before pilot |
| Blocking integrity/data error | Confirmed answer lost silently, incorrect score, another learner's data shown, misleading official score | Do NOT mark corresponding function ready for pilot; fix then regression test |
| High-severity reading/usability problem | Part 7 passage unreadable/clipped on pilot phone | Repair/re-test before pilot on target devices |
| Non-blocking missing explanation | Answer key valid but no vetted explanation | May show "chưa có giải thích" **only if PO approves coverage rule** |
| Unknown threshold | Interruption grace, response-time SLA, number of target phone sizes | Mark `TBD`, do not present as approved requirement |

## 3. Edge-case matrix requiring policy signoff

| Case | Unresolved business decision | Candidate analyst default (not approved) | Consequence if left unresolved |
|---|---|---|---|
| E-01 | Pause in Full Mock | Strict evaluative attempt does not allow voluntary pause; flexible practice does | Cannot label valid timed attempts consistently |
| E-02 | Listening replay in evaluative mode | No arbitrary replay except where content/test format explicitly requires it | Questionable comparability; do not choose player UI now |
| E-03 | Background/process termination | Continue timer per approved policy; preserve acknowledged choices; label violated attempts | False completion labels; potential silent answer loss |
| E-04 | Network loss before answer acknowledgment | Do not claim answer safely recorded if unconfirmed; disclose pending status | False assurance in online-first product |
| E-05 | Timed section transition/timeout | Defined automatic end/transition and no double submission; exact grace TBD | Score/time ambiguity |
| E-06 | Key changed after a completed attempt | Preserve history/version and disclose impact; decide recomputation policy | Silent altered results |
| E-07 | Comparison after exposed mock | Mark non-comparable and exclude from validated improvement trend | Confounded progress metric |
| E-08 | Account deletion / data retention | Policy derived from eventual account feature and applicable Play requirements | Cannot write full acceptance test or publish compliant privacy statement |
| E-09 | Reading long text/zoom/font size | Preserve whole text and relation to question; validate on pilot devices | UX quality risk from prior actual use |

## 4. Stage03 definition of 'acceptance-ready' vs later test PASS

- **Stage03 acceptable draft:** each critical behavior has a test ID, precondition, expected result, reason for any TBD, and future verification phase.
- **Not Stage03 evidence:** signed content audit; runnable Android tests; Play compliance review of released app; measured device accessibility; verified scaled-score calibration.
- **Gate review must not claim:** two PO-inventoried mocks have passed all QA; a production-ready full mock exists; cost estimates are approved; the MVP has been locked.

## 5. Source and provenance

Mapping uses approved Vision and PO decisions; official ETS exam format, Android process lifecycle, Google Play data/account-deletion conditions. See evidence ledger V0.5.
