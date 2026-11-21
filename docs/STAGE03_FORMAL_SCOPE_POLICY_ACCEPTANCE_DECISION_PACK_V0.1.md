# D03-SCOPE-009 — Formal MVP / Policy / Acceptance Decision Pack V0.1

**Stage03 Requirements · 2026-11-21 · FOR PRODUCT OWNER SIGNOFF — PENDING**  
**Prepared under:** D03-READY-008 = A APPROVED.  
**References:** PRD Draft V0.5, SRS Draft V0.5, AT-01..19 V0.3, Product Vision V1.0, B1, R1–R4 and QA-01..08.

> The options below are **analyst proposals**, not approvals. One PO response may approve, amend or hold all three sections. **A decision here does not automatically baseline PRD/SRS or pass Stage03 Gate**; reconcile the signed choices back into a candidate PRD/SRS baseline and seek a separate final Gate decision.

## Decision summary — one bundled signoff

| Group | Preferred analyst choice | Important limit | Status |
|---|---|---|---|
| **S1 — MVP boundary** | **S1-A Balanced Core**: 7-Part practice, two B1 Full Mock A/B, scoring, errors/history, short study & simple rule guidance, minimal licensed content pipeline and resilience | Practices require a distinct QA-ready practice bank; Full Mock release waits content QA | PENDING PO |
| **S2 — Business policies** | **S2-A Strict evaluative Full Mock** with no voluntary pause/replay, timer consistency, honest invalid attempts, raw-only result, conservative privacy | Alternative flexible practice available; no promised offline feature | PENDING PO |
| **S3 — Acceptance & pilot** | **S3-A Quality-first conditional thresholds**, test-spec completeness at Stage03 and actual QA before pilot, 2–5 users for 4 weeks | No mandated TOEIC score gain; budget DEFERRED | PENDING PO |

**Recommended combined package:** `S1-A + S2-A + S3-A`, with all explicit *pre-pilot* quality dependencies tracked. If one aspect should differ, use **APPROVE WITH AMENDMENTS** and name the changed row rather than re-running discovery.

## S1 — Formal MVP IN/OUT candidate

**Proposed IN — required for the pilot only after separate explicit MVP signoff:**

- **M01** — Android smartphone, online-first, two-to-five-family-member pilot, TOEIC L&R; learner goals/time preferences (FR-001).
- **M02** — Part 1–7 practice using a QA-cleared bank **separate from protected Full Mock items**; correct media/passage mapping (FR-002/003/004).
- **M03** — Two independent Full Mock A and B, **each 200 items/7 Parts**, evaluation timer and attempt status (FR-010/011/013). *B1 is already a mandatory direction, not evidence of actual QA PASS*.
- **M04** — Confirmed answer preservation and honest answer submission status, vetted answer-key scoring, correct/attempted/unanswered by Part/section, history and error review (FR-005/006/007/008/012/019).
- **M05** — Short practice ending after one item and basic explainable **rule-based** next-lesson suggestion (learner can override; FR-009/014). This is a *candidate* inclusion to preserve the product's flexible-study value; no AI.
- **M06** — QA-reviewed content status/version, revocation of broken content, corrections with reproducible history, data separation among family users (FR-015/016/017/018).
- **M07** — Long Reading completeness/readability, network status, pilot privacy/data deletion policy at requirements level (NFR-003..011); not a selected UI or architecture.

**Proposed CONDITIONAL, not guaranteed by available assets:** curated explanations when verified; otherwise clear “no verified explanation”; separate practice item bank must be audited before claiming M02 fully ready. **Mock A/B must not be cut to one form if either fails; B1 remains a blocker for that pilot release until PO changes B1 explicitly.**

**Proposed OUT/DEFERRED:** automatic PDF/audio/answer extraction; AI runtime explanations/question generation, advanced adaptive AI roadmap, interactive vocabulary notifications, iOS, offline-first mode, TOEIC S&W, paid subscription/advertising, claim of official ETS-scaled score. Manual/authorized preparation of content is a **business input**, not a built-in PDF importer. Backlog only.

**S1-A (recommended):** approve IN/OUT as above subject to content/device QA before pilot.  
**S1-B (alternative):** move minimal rule-based suggestion M05 into OUT while retaining one-question practice, to reduce requirements scope.  
**S1-C:** request alterations; **not** permission to remove either Full Mock without distinct revision of B1.  
**S1-HOLD:** don't lock MVP yet, continue Requirements analysis.

## S2 — Business policy signoff, implementation-neutral

Recommendation **S2-A = choose candidate defaults P01–P09** in `STAGE03_MOCK_AND_DATA_POLICY_PROPOSALS_V0.1.md`, subject to edits. Main rules:

1. Full Mock is **exam-like evaluation**, distinct from flexible Part practice. Listening follows ordered media about 45 minutes; Reading has 75-minute limit. Duration/cue specifics should be validated against the licensed form; do not assume abrupt interruption of a valid audio segment at exactly 45:00.
2. In an evaluative attempt, no discretionary timer pause and no discretionary audio replay; user may quit or choose flexible practice, but reclassified/assisted attempts cannot masquerade as clean comparison attempts.
3. An interrupted attempt **preserves acknowledged answers**, does not silently reset time, and gets an explicit comparable/incomplete/non-comparable outcome. A network-disconnected answer must not be represented as securely stored until confirmed. No full offline feature implied.
4. Raw results and 7-Part statistics, clear form/version, no ETS-equivalent 10–990 or proof of comparable gain; exposed test attempts must be flagged for trend analysis.
5. Family pilot keeps minimal person-level data, isolates participants, and permits deletion requests. Proposed exact retention/delete targets require PO confirmation; choose no provider, account screen or database here.

**S2-A:** approve proposed subpolicy defaults (and clear defined TBDs to later QA) as requirements rules.  
**S2-B:** approve with amendments (e.g., permit voluntary pause but classify the attempt as non-comparable).  
**S2-HOLD:** keep rules TBD and do not baseline affected requirements.

## S3 — Acceptance, QA timing and four-week pilot

Recommendation **S3-A** in `STAGE03_ACCEPTANCE_AND_PILOT_SIGNOFF_PROPOSALS_V0.1.md`:

- At Stage03, validate that **each included critical FR/NFR has a mapped AT test, preconditions, observable expected result and verification phase**; no fake test PASS.
- Before protected Full Mock is offered to pilot, audit all 400 source items and essential answer keys/media/passages, no known blocking issue, no duplicates across A/B, no contamination by a practice bank; record QA-01..06 evidence and exceptions, not just inventory claim.
- Before pilot, execute scoring, lifecycle, learner isolation and long Reading device tests QA-07/08; **zero known blocking defect** on critical score/answer/media/privacy/timer flows is a candidate release gate.
- Pilot: 2–5 invited participants, 4 weeks; candidate evaluability criterion: **at least two participants** independently complete Full Mock A and B in valid attempts and give usability feedback. Otherwise label pilot **insufficient evidence**, not proven improvement; document engagement and Part practice counts without promising score increase.
- Quantitative performance thresholds needing test devices, networks and content specifics remain labeled **TBD FOR PRE-PILOT VALIDATION**, rather than inventing latency SLAs at Requirements time.
- Money and effort thresholds **DEFERRED BY PO**, CP-04 tracked but no present cost work.

**S3-A:** approve quality-first acceptance *targets and their later evidence deadlines*, not that the tests have passed.  
**S3-B:** approve framework but request alternative numeric pilot completion target.  
**S3-HOLD:** retain current draft thresholds unapproved.

## Explicit distinction between two decisions

`D03-SCOPE-009 APPROVED` (if PO later chooses) would define **the business scope and policy/acceptance choices** and authorize reconciliation into PRD/SRS **candidate baseline**. It does not, by itself, approve the revised documents or Stage03 Gate.

`D03-BASELINE-010` (future, separate) must review the reconciled exact PRD/SRS revisions and open conditions, before the Stage03 Gate package. **No authority** for UX/UI, architecture or code is inferred at either step.

## Signoff panel for Product Owner — currently blank

- Decision `D03-SCOPE-009`: **PENDING**
- Candidate package: `S1-A + S2-A + S3-A` (**analyst recommendation**, not approved)
- Available dispositions: `APPROVE PACKAGE` / `APPROVE WITH AMENDMENTS` / `HOLD`
- If amended: identify S1/S2/S3 rows, leave previously approved governance unaltered unless explicitly revised.
- PO signed decision, date, affected version: `NOT PROVIDED`.

## Non-authorizations and carry-forward

Keep CP-01..05, B1 2 Full Mocks, QA-01..08 framework, R1–R4. Two forms PO-reported inventoried, not QA tested; PO-attested reuse rights, not item/asset audit. Budget steps DEFERRED, not waived. No UX/UI, technical architecture, coding, scraping, supplier outreach, payment, app deployment or Stage04.
