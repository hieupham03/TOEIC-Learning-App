# TOEIC Learning App — Stage 04 UX/UI Kickoff Plan **PROPOSAL V0.1**

**Prepared:** 2026-11-21 (Asia/Bangkok)  
**Stage 03 Gate:** **CLOSED — CONDITIONAL PASS** (`D03-GATE-011` PO APPROVED).  
**Stage 04:** **NOT STARTED**. **Kickoff PENDING PRODUCT OWNER.**  
**Requested decision:** approve/modify/HOLD the *Stage04 plan*, not any UI screens, wireframes, prototypes, architecture, technology or code.

## 1. Purpose and permission boundaries

Plan a user-centered design phase for the **already approved Android TOEIC Listening & Reading MVP**. Deliver coherent mobile learner journeys and testable UI states for short Part practice, long Full Mocks, results, error-review, family privacy, and content failures. UX must implement **signed requirements**, not silently redesign the product.

**IMPORTANT:** This document **does not include actual UX flows, information architecture, navigation tree, layouts, wireframes, style guide, high-fidelity screens, prototype or code**. Those are *future conditional deliverables* only after a separate PO kickoff authorization. Stage 05 technical architecture and Stage 07 development remain out of scope.

### Fixed inputs — do not re-decide

- Official, unchanged Requirements Baseline: `STAGE03_PRD_BASELINE_CANDIDATE_V0.6.md` (approved), `STAGE03_SRS_BASELINE_CANDIDATE_V0.6.md` (approved), `STAGE03_ACCEPTANCE_CATALOGUE_CANDIDATE_V0.4.md` (approved).
- Product Vision V1.0, Stage02 CP-01..05, **activated** Stage03 G03-CP01..07.
- **MVP IN:** Android online-first L&R for 2–5 family learners / 4-week pilot; Part1–7 practice with dedicated bank, two 200-item Full Mocks, results/raw scores, error review, quick-one-item session, explainable non-AI suggestions, controlled content, answer persistence, family data separation.
- **MVP OUT:** runtime AI tutor and generation, PDF/audio automatic import, advanced vocabulary notifications, offline-first/iOS/S&W, paid products and ETS-certified/equivalent score claims.
- **Policy integrity:** Full Mock A/B are evaluative, timing and replay controls follow signed P01..09; results show limitations; validated delete request addressed within 7 calendar days and routine retention within 30 days after pilot absent exception/agreement.
- **Evidence distinction:** two form inventories PO-reported complete; QA-01..08 APPROVED as framework, not executed. Budget work **DEFERRED** and not a Stage04 kickoff question.

## 2. Proposed work packages — NO execution before PO authorization

| WP | Planned analysis or UX activity after kickoff | Deliverables to prepare **only after authorization** | Review/approval boundary |
|---|---|---|---|
| **UX-01 — UX brief & coverage inventory** | Map approved roles, learner goals, journey inventory from FR/NFR/AT, Android touchpoints, critical failure states; identify only UX-relevant unknowns | Stage04 UX Brief V0.1; Journey–Requirements Coverage Matrix; prioritized UX risks | **First execution after kickoff approval**; no wireframes initially |
| **UX-02 — Journey options & policies** | Propose alternatives for Part practice, one-item session, two Mock A/B attempts, answers/results/review, error/correction and family privacy; cover interruptions and deliberate non-comparability | Proposed journey-flow alternatives, state/action inventory, choice tradeoff sheet | Present ONE batch of meaningful UX tradeoffs to PO before finalizing navigation assumptions; no business-policy override |
| **UX-03 — Information architecture & low-fidelity design** | Once UX-02 assumptions reviewed, describe user-facing navigation and lay out low-fidelity wireframes for critical journeys, including empty/loading/error/permission states | Navigation model and low-fidelity wireframe set **after kickoff**, with requirement IDs | Design artifact review, not PRD/SRS baseline modification; technical architecture is excluded |
| **UX-04 — Prototype & pragmatic usability check** | After PO reviews low-fi, prepare interactive prototype for mission-critical paths; inspect long Reading scroll legibility, 120min interruption/status clarity, simple family context separation; desk heuristics first, targeted pilot-like walkthrough only when material | UX prototype candidate, Android mobile context review, usability findings and issue register | No invented user-test PASS; does not build app or execute QA-07..08 |
| **UX-05 — Stage04 Design Gate Review** | Check UX traceability/coverage, interaction clarity, accessibility, failure states, open risks, and consistency with signed S2/S3; recommend PASS/CONDITIONAL PASS/HOLD | Stage04 UX/UI design handoff + Gate Review + PO decision sheet | PO decision separately required before Stage05 architecture or Stage07 code |

**Recommended sequence:** PO approves this plan → **UX-01 only starts** → submit one grouped UX decision pack at UX-02 → prepare low-fi and prototype in stages with reviews → UX-05 Gate, PO approval. The initial authorization does not constitute approval of any UI design output.

## 3. Core UX coverage required (not screen designs)

| Journey category | UX challenge to analyze after kickoff | Trace to approved stage03 intent |
|---|---|---|
| Quick learning / level & time | Get learner to a Part or one-item session with minimal friction and an optional suggestion | M01/M05; AT-01/02/09/14 |
| L&R Part practice | Listening media bound correctly to question groups; Reading full passages/images/tables available; answer/review loop | M02/M04/M06; AT-02..08 |
| Full Mock A/B 120min | Long listening/reading phases, protected no-pause/no-replay integrity, timing, submit/timeout, truthful interrupted/noncomparable states | M03; AT-10..13/19; P01..09 |
| Results / progress | Present raw L/R/Part performance and gaps without misleading ETS equivalence or form improvement | M04; AT-12/13 |
| Lost network / background / app termination | Distinguish unsaved/pending/saved answer state; never hide impact of interrupted mock; predictable recovery affordances | M07; AT-05/11/19 |
| Long Reading visual ergonomics | Android phone-size variance, stable passage/case context, legible typography and accessible content length; check on two contexts | QA-08; AT-04 |
| Family data/privacy | Isolate one learner's records, transparent data deletion request, privacy copy and legally valid exceptions | M07, P09, AT-18 |
| Invalid content/media/keys | Missing/withdrawn question handling; signal issues without silently corrupting results; curator correction future flow | M06; AT-15..17 |

## 4. UX quality and staged evidence gates

- **UX requirements coverage:** 100% of critical included user journeys, signed PRD/SRS FR/NFR and acceptance conditions have at least one explicit UX manifestation, design rationale or documented non-UI owner. Count/coverage is to be established at UX-05, not asserted now.
- **Flow completeness:** map happy, alternate, empty, slow network, media-missing, corrupted content, permission/consent, timeout, interruption and recovery states; do not invent backend behavior.
- **Mobile readability:** inspect long Part6/7 passages and multi-stimulus tables; avoid making ungrounded performance claims or fake lab study.
- **UX ethics:** explicitly describe official-score limitations, result comparability and learner data; no deceptive save confirmations, hidden replay rights, or forced algorithmic suggestions.
- **Accessibility:** consider scalable text/contrast/screen readers and landscape/portrait allowances when not in conflict with signed requirements; propose measurable checks after review instead of imposing unapproved values.
- **Handoff boundary:** design diagrams are not application architecture; technical implementation, database, API contracts, hosting, cloud and code are reserved for later authorization.
- **QA honesty:** future clickable prototype/walkthrough feedback is UX evidence, **not** QA-01..08 full content or Android app PASS. Those are due at later gates under G03-CP02/03.

## 5. Risk and decision management

| Risk | Handling at Stage04 | PO needed? |
|---|---|---|
| Overcomplicated 120min phone journey | Prioritize clarity of exam state and Reading ergonomics; compare a small set of evidence-informed UX options | Only for consequential UX tradeoffs |
| Silent changed mock rules | Anchor every attempt-state design to signed P01..09; escalate any changed rule as change request under G03-CP06 | Yes for scope/policy change |
| Stale or incomplete content | Represent audited/unaudited/missing states in UX; actual content QC before pilot (G03-CP02) | Not an urgent PO request now |
| Family accounts and data deletion | UX for consent, data management and deleted-request tracking while data/technical procedure remains gated by G03-CP04 | Yes only if new business policy needed |
| Scope creep into deferred ideas | Keep AI, auto-import, sophisticated notifications and official score equivalence excluded unless separately approved | Yes for any scope change |
| Budget | **ALL budget work stays DEFERRED by PO**; do not request cost approval to start documentation planning | No at this stage |

## 6. Stage04 Gate exit evidence (proposal)

- All core signed learner journeys and their exceptional states have reviewed flow maps and design states; a navigation model is traceable to requirements.
- PO has reviewed low-fidelity wireframes and key prototype interactions; changes captured in an issue register.
- Long Reading, mock integrity, saved/unsaved/invalid attempt status, score caveat, learner privacy and deletion have explicit usable UX treatment; no conflicts with approved P01..09.
- Any unresolved UX risk has owner, due checkpoint and suitable fallback; no undeserved actual Android app test PASS claimed.
- Stage04 UX/UI Gate proposal is presented for separate PO PASS/CONDITIONAL PASS/HOLD; **Stage05 Technical Feasibility & Architecture is not opened automatically**.

## 7. One pending Product Owner decision — D04-KICKOFF-001

- **A — APPROVE Stage04 Kickoff Plan V0.1:** authorize Stage04 UX/UI to START and perform **UX-01 UX brief/coverage inventory** only as immediate next step, then present UX-02 grouped choices; does **not** approve any wireframes, design system, prototype, Stage05 architecture, code or budget spending.
- **B — APPROVE WITH AMENDMENTS:** user modifies the plan, Stage04 remains NOT STARTED until amended plan is explicitly approved.
- **C — HOLD:** preserve Stage03 CLOSED CONDITIONAL PASS and signed requirements; do not begin Stage04.

**NOT requested now:** re-confirm copyright or two mock inventories, budget ceilings, device test sessions, UI mockups or tech choices. All deferred approvals remain tracked.
