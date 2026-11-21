# Product Requirements Document — TOEIC Learning App — BASELINE CANDIDATE V0.6

**Status:** **FOR D03-BASELINE-010 PRODUCT OWNER REVIEW — NOT BASELINED/APPROVED.**  
**Created:** 2026-11-21 · **Stage03 Requirements IN PROGRESS** · **Business scope source:** D03-SCOPE-009 APPROVED S1-A + S2-A + S3-A.  
**No UX/UI, software architecture, APIs/databases, vendor selection or code authorized.**

## 1. Product context and approved intent

- **Vision:** Android smartphone TOEIC Listening & Reading learning for Vietnamese learners, online-first pilot with 2–5 family members over 4 weeks. Later potential Google Play launch. Product Vision V1.0 remains approved/unaltered.
- **Pain:** disjoint PDF/audio/answer-checking; irregular free time; difficult long Part7 reading on phone, including eye strain.
- **Outcome:** integrated Part1–7 practice, two full timed mock tests, error review, quick-session learning and transparent raw performance tracking; a family pilot measuring usability, habit and early exploratory result, **not** promised TOEIC score gain.
- **Sampling limitation:** ~550 self mock and ~650 official TOEIC baseline from different people and assessment instruments cannot be naively compared.

## 2. Approved governance and scope classification

| Decision | Authority | Meaning |
|---|---|---|
| D03-SCOPE-009 | **PO APPROVED** | **MVP BUSINESS SCOPE LOCKED** S1-A; business rules S2-A; acceptance S3-A. This PRD is not thereby baseline-approved. |
| D03-LOCK-001 = B1 | **PO APPROVED** | Two separate full L&R mock forms mandatory; no one-form or Part-only fallback without new PO decision. |
| D03-QA-006 | **PO APPROVED framework** | QA-01..QA-08 framework, no QA execution PASS asserted. |
| D03-REQ-007 | **PO APPROVED principles** | R1–R4 drafting principles incorporated, superseded by signed S2 details where specified. |
| D03-SOURCE-004 | **PO SELF-REPORT** | Two Full Mock inventories complete. Item/media/key QA **not independently verified**. |
| Rights declaration | **PO SELF-ATTESTED** | Reuse rights for STUDY4, Zenlish, The TOEIC Lab and additional sources; asset mapping/QA still needed. |
| D03-BUDGET-005 | **DEFERRED BY PO** | Do not reopen monetary work; CP-04 tracked at appropriate later authorization. |
| Stage02 Gate | CONDITIONAL PASS | CP-01–CP-05 remain active; no implied design/coding authorization. |

## 3. Approved MVP — IN / CONDITIONAL / OUT

### IN, with quality dependencies before the pilot

1. **M01 Profile and goal:** minimal separate participant context, self-reported goal and available study duration; no data beyond pilot purpose.
2. **M02 Part 1–7 practice:** learner chooses Part; correct audio-group/media, reading passages and answer relations. A QA-cleared practice bank **separate from protected Full Mock items** must be available before pilot. Missing bank is an OPEN content dependency, not scope removal.
3. **M03 Full Mock A/B:** two mandatory independent L&R forms, each 200 questions and 7 Parts; 100 Listening (~45m) + 100 Reading (75m); strict evaluative integrity, clear attempt states and version identity.
4. **M04 Results and mistakes:** acknowledged answers persist, vetted answer keys, right/wrong/blank counts by Part and L/R, error history and limited raw A/B view with accuracy caveats.
5. **M05 Flexible microlearning:** one-item quick session; simple explainable rule-based suggestion grounded in goals, available time and weak Parts, optional for learner (not AI).
6. **M06 Content integrity:** authorized curated content, source/version and QA state, withdraw broken items, protect historical result integrity if keys change.
7. **M07 Family trust and Android use:** isolate learner data, account/data deletion policy, honest network/save state, preserve confirmed answers and mobile long-Reading completeness/readability.

### CONDITIONAL content availability

- Curator-verified explanations may be shown only where available; otherwise say that no verified explanation exists; do not fabricate.
- Full Mock and separate practice content cannot be declared RELEASE READY without required QA-01..06 evidence. PO-reported inventory alone is not a QA PASS.

### OUT of this pilot MVP

- Automatic PDF/audio/answer extraction, runtime AI tutor/generation/advanced adaptation, sophisticated vocabulary notification interactions, offline-first, iOS, S&W, paid subscriptions/ads, any claim of ETS official certification/equivalent scaled 10–990 score. Future backlog only and new PO scope decision required for inclusion.
- Approved content **prepared externally/manually** is an authorized content-input responsibility, not a built-in automated importer.

See `STAGE03_MVP_SCOPE_LOCK_MATRIX_V1.0.md` for M01..M09/X01..X05 mapping.

## 4. Core journeys and testable product outcomes

| Journey | User need | Required outcome | Test link |
|---|---|---|---|
| J01 Quick start | Irregular time, level/goal | Goal/time recorded; learner starts self-selected Part or 1 item and can ignore suggestion | AT-01,02,09,14 |
| J02 Part practice | One flow for questions/audio/Reading | Correct group media and passage, acknowledged answer; invalid content held | AT-02..06 |
| J03 Full timed attempt | Two 200-item evaluations | A/B form selection, timing/validity; do not convert broken attempt into comparable clean test | AT-10,11,13,19 |
| J04 Learn from errors | Review wrong and missing answers | Correct verified keys; explanation only if reviewed; error history available | AT-06..08,15,16 |
| J05 Follow progress | Transparent results | Raw Part/L/R totals and form/version; trend with caveat, no ETS score claim | AT-12,13 |
| J06 Manage content | Prevent corrupt media/keys | Version/source, audit, correction/withdraw without silent history alteration | AT-15..17 |
| J07 Trust & usability | Long reading, interruptions, family | No silent confirmed-answer loss, privacy separation, deletion, readable full passage | AT-04,05,18,19 |

## 5. Approved S2 business policies (P01–P09)

- **Full Mock integrity:** Listening ordered as supplied, ~45 min, Reading 75 min. No discretionary pause or arbitrary audio replay in attempts treated as clean/comparable; flexible Part practice may allow both. Do not indiscriminately truncate mandatory audio at exactly 45:00.
- **Interrupted attempt:** acknowledged answers persist, time never silently resets, status remains honest. If timing/audio integrity is materially disrupted or indeterminate, the attempt is labeled INCOMPLETE or NON-COMPARABLE, never clean-comparable by assumption; timeout/quit/submit distinguishable.
- **Save:** UI language not prescribed, but confirmation of durable save must be truthful; pending/unconfirmed state is not 'saved'. A single finalized result per completed attempt; raw/Part scores, blanks and form-version. No unverified TOEIC equivalence or official improvement claim.
- **Result corrections:** content key changes and score consequences traceable; no silent historical rewrite. Specific recomputation workflow subject to later review before enabling.
- **Privacy:** minimal learner data and strict separation; verified deletion request addressed within **7 calendar days**, applicable lawful exceptions documented, routine retention no more than **30 days after the four-week pilot** unless valid further consent/agreement. Account implementation and detailed exception handling are **TBD before pilot**, not app architectural commitments.

Reference signed full policy: `STAGE03_MOCK_AND_DATA_POLICIES_APPROVED_V1.0.md`.

## 6. Approved S3 — measurable success and acceptance

- **Requirements signoff criterion AC-01:** **100% critical included FR/NFR** traced to an acceptance ID with preconditions, observable expected result and verification phase in `STAGE03_ACCEPTANCE_CATALOGUE_CANDIDATE_V0.4.md`. The catalogue remains BASELINE CANDIDATE until D03-BASELINE-010.
- **Pre-pilot content AC-02..04:** Two Full Mocks 200 items each, 7-Part counts; 100% essential keys/audio/images/passages/source/version coverage; zero known critical content flaws, cross-form overlaps or pre-exposed mock items; verify QA-01..06 before pilot.
- **Pre-pilot device AC-05..07:** Zero known critical answer-loss/scoring/duplicate/unsafe data disclosure/false official-score claims; Part7 legible on at least **two Android phone sizes/contexts**; QA evidence statuses recorded; actual test evidence due later.
- **AC-08:** device/network/performance numeric targets remain **TBD BEFORE SOFTWARE TEST PLAN BASELINE** — not an automatic Stage03 PASS or free pass for pilot release.
- **Pilot PM-01..06:** 2–5 participants / 4 weeks; at least **two** complete **both** Full Mock A/B in declared valid conditions and share feedback; at least **two** use Part practice and give usability feedback; track attempts, raw form outcomes, errors, faults and reading experiences. If paired count short, label progress analysis INCONCLUSIVE. No +100/+200 TOEIC gain claim.
- **Budget:** all budget-related work **DEFERRED**; CP-04 and future spend/release checkpoint remain explicit.

## 7. Known open dependencies and when they are due

| Dependency | Owner/evidence | Required by | Effect now |
|---|---|---|---|
| Content source manifests, key/audio/image/passage relations, A/B overlap, distinct Part bank | Content QA evidence, rights PO-affirmed | BEFORE pilot content release (QA-01..06) | **OPEN — does not falsify PO inventory or unapprove B1** |
| Scoring/Android lifecycle/Reading privacy tests | Implementation and device test logs QA-07..08 | BEFORE pilot | NOT RUN now |
| Technical performance, tolerances, supported devices | Test-plan acceptance decision | BEFORE software test plan baseline | `TBD` with explicit due phase |
| Verified request/identity and deletion exception handling | Pilot privacy/compliance readiness | BEFORE pilot account use | Signed 7d/30d policy intact |
| Key correction recomputation/appeal | Separate material policy if corrections affect scored attempts | BEFORE enabling such recalculation | Preserve history, do not silently recompute |
| Spending and operational constraints | PO future explicit reopening | BEFORE authorizing spend/relevant release gate | **DEFERRED**, no action now |

## 8. Baseline decision and authority

`D03-SCOPE-009` APPROVED is a **business decision**. This document `PRD BASELINE CANDIDATE V0.6` is **NOT APPROVED**. `D03-BASELINE-010` must explicitly accept these precise candidate documents and their deferred evidence gates. Stage03 Gate Review is a later, separate Product Owner decision. No UX/UI, architecture, code or Stage04 transition authorized.

**Reference documents:** Product Vision V1.0, V4.0 S1/S2/S3 proposal package, D03-SCOPE-009 record, SRS V0.6 candidate, acceptance catalogue V0.4, QA framework and source ledger V0.5.
