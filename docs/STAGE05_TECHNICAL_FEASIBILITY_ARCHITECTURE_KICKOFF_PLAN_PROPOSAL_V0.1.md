# Stage05 — Technical Feasibility & Architecture — KICKOFF PLAN PROPOSAL V0.1

**Project:** TOEIC Learning App  
**Prepared:** 2026-11-21 (Asia/Bangkok)  
**Governance:** Stage04 **CLOSED — CONDITIONAL PASS** (`D04-GATE-009 = A`); G04-CP01..08 ACTIVE.  
**Current Stage05 status:** **NOT STARTED; NO EXECUTION AUTHORIZED**.  
**Next decision:** `D05-KICKOFF-001 = PENDING PRODUCT OWNER`.

## 1. Purpose and exact boundary

This is a **plan for a future technical feasibility and architecture stage**, not a technical architecture, stack recommendation or software specification. It is written solely to obtain separate Product Owner authorization, consistent with G04-CP01. **Preparing this plan does not begin Stage05.**

Goal *if later authorized*: evaluate feasibility and develop a traceable, testable future architecture for the **approved** Android, online-first TOEIC Listening & Reading MVP; preserve the distinction between product requirement, UX specification, implementation hypothesis, and test result. Bring all material options/risks back to the PO in a grouped review before design decisions become authoritative.

**Explicitly excluded from this current proposal's execution:** drawing actual system/deployment/data-flow diagrams, choosing Flutter/native/any framework, cloud/backend/database/auth providers, drafting APIs, writing ADR decisions, coding/Codex, making a proof-of-concept, configuring services, scraping/ingesting the two mock corpora, obtaining quotes, running paid experiments, commissioning user tests or purchasing hardware/services. These become *possible* later activities only within separately granted Stage05 authority and future checkpoints.

## 2. Immutable signed inputs

| Input | What Stage05 must respect if it starts |
|---|---|
| Product Vision V1.0 | Android L&R, family 2–5 pilot four weeks, online-first, no unsupported score-increase promise |
| MVP `D03-SCOPE-009` S1/S2/S3 | Part1–7 practice plus **two independent B1 200-question Full Mocks**, validated answers, results/errors/history, rule-based suggestions, privacy/recovery |
| Requirements Baseline (`D03-BASELINE-010`) | Signed PRD V0.6, SRS V0.6, Acceptance V0.4; 19 in-scope FR/13 NFR as referenced in control matrix |
| Stage03 business rules | Mock Listening 100 (~45 min) + Reading 100 (75 min), no unapproved voluntary pause/replay for comparable attempts, transparent interruptions; raw-score-only reporting |
| Privacy/deletion | Isolated learner data; verified delete request within 7 calendar days and routine retention ≤30 days after pilot absent valid exception/consent |
| Design Baseline (`D04-UI-008`) | Signed V0.3 design spec/copy, 19 documented state classes, UI-G01..16, nine illustrative state images (illustrative not production UI) |
| Active CP registers | Stage02 CP01..05, Stage03 G03-CP01..07, Stage04 G04-CP01..08 |
| QA and content facts | QA01..08 approved as framework, actual QA pending; PO confirms two mock inventories and content rights (do not re-request) |
| Budget | **DEFERRED by PO**, no costing, quotation, service buying or vendor outreach as a plan prerequisite |

**Out of MVP unless a new PO change decision:** runtime AI tutor or question generator, automatic PDF/audio importer, advanced notifications, iOS, offline-first, TOEIC Speaking/Writing, billing and ETS-equivalent official scores.

## 3. Proposed Stage05 work packages — conditional future work only

| Work package | Intended *future* activity if Stage05 kickoff is authorized | Expected *future* document/evidence | Approval/checkpoint boundary |
|---|---|---|---|
| **ARCH-01 — Architecture drivers & traceability** | Extract approved FR/NFR/AT/Design constraints, quality drivers, data privacy and external content dependencies; tag implementation-dependent TBDs and external QA duties | Architecture Driver Register, scope/constraint/evidence map, contradiction list | **First work package only** after `D05-KICKOFF-001=A`. No stack/design selected |
| **ARCH-02 — Feasibility options for material drivers** | Later prepare small number of feasible alternatives and trade-offs for timing/media, answer persistence, family isolation, content versioning and Reading performance | Evidence-first option matrix with risks/assumptions; PO grouped choice `D05-ARCH-002` | *Separate PO direction review before any material technical path is locked* |
| **ARCH-03 — Architecture description candidate** | Only after option review, document future proposed boundaries, information flow, availability/recovery/security considerations and requirements-to-components allocation | Architecture Candidate and design decision log (not implemented) | No architecture baseline without separate PO review/approval |
| **ARCH-04 — Verification & risk plan** | Propose falsifiable checks for long Full Mock, timer/audio state, durable ACK, offline interruption recovery, 2 Android contexts, accessibility, privacy/deletion, content version/QC | Test/evidence checkpoint plan linked to QA01..08, UX/UI risks and CPs; real-device/user tests later as appropriate | No claim of tested PASS from plan text; any POC requires later authorization |
| **ARCH-05 — Stage05 readiness / Gate** | Reconcile future architecture decisions, assumptions, verification plan, controlled baselines and deferred conditions | Stage05 Gate Review and separately signed PO decision | Does not auto-open Stage06/07 implementation or budget |

**Recommended immediate sequence if PO approves kickoff:** authorize **ARCH-01 only**, produce one consolidated driver/evidence document, then present a separate grouped `D05-ARCH-002` feasibility-option packet. This plan deliberately does **not** pre-select any architecture or framework.

## 4. Planned focus and phase responsibilities (not architecture answers)

| Quality driver / risk | Future analysis obligation | Evidence/status NOW |
|---|---|---|
| 120-minute evaluative Mock A/B | Define later measurable integrity/suspension/timer/audio validation plan consistent with signed mock policies | **TBD implementation**, no app exists |
| Listening Part1–4 and long Reading Part6–7 | Validate future media mapping, interrupted playback, long passage/table/image and position restoration | **No real-device evidence** |
| Durable acknowledgement | Identify later what constitutes truly persisted answer vs locally selected/pending/unknown; align user-facing copy | **Unverified runtime**, design copy approved only |
| Family and data deletion | Plan subsequent account separation, privacy controls, deletion/retention verification and audit evidence | **No technical mechanism selected** |
| Licensed content and form isolation | Keep practice questions apart from Mock A/B, version release and answer/audio QA evidence requirements | **Two inventories confirmed PO; audit later** |
| Raw score interpretation | Plan form- and attempt-state-aware grading verification with no ETS score equivalence | **No score engine tested** |
| Android accessibility | Require future real-device text scale, TalkBack, contrast, touch, longform stress checks | **n=0 real devices, n=0 learners** |
| Privacy + change control | Trace G03/G04 and UX04/UIA issues to assigned later evidence checkpoints | **OPEN** until actual test and PO closure where required |

## 5. Proposed Stage05 Gate exit criteria (NOT approved now)

Before any future Stage05 Gate, the PO should receive: (i) mapped architecture drivers and approved technical choice record, (ii) a coherent candidate architecture description *created only under future authorization*, (iii) requirements/design impact matrix and mitigation of contradictions, (iv) plan for QA01..08 and Android/user checks without claiming they ran, (v) an explicit ledger of remaining CP/UX/UIA constraints and ownership, (vi) no unauthorized budget activation or scope creep. The PO alone would decide PASS/CONDITIONAL PASS/HOLD.

**Not required for mere Stage05 kickoff approval:** real Android test PASS, 400-item content QA completion, user usability evidence, cost ceiling, cloud subscriptions, a framework decision or architecture diagram. Those follow their own checkpoints and approvals.

## 6. Decision requested now

**`D05-KICKOFF-001`** — A approve Stage05 plan and permit **ARCH-01 only**, B amend plan before start, C HOLD. Approval of the plan would not decide any technical path, release quality or coding authority.

**CURRENT STATUS:** This complete file is a **PROPOSAL ONLY**. Stage05 **NOT STARTED**; no architecture diagrams, stack comparisons, schemas, APIs or code were produced.
