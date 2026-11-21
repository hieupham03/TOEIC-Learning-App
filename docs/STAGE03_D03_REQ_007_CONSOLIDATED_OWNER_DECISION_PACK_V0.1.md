# D03-REQ-007 — One-Packet Requirements Review for Product Owner V0.1

**Prepared:** 2026-11-21  
**Decision status:** **PENDING Product Owner**  
**Scope:** Business behavior / requirement-drafting direction only. Not MVP scope lock, PRD/SRS baseline, UI, architecture, code or acceptance thresholds.

## Confirmed without further questioning

- **B1:** two Full Mock L&R forms mandatory.
- **Source/rights:** PO affirms rights to The TOEIC Lab, Zenlish, STUDY4 and more sources.
- **Inventory:** PO confirmed both mock sets inventoried. We do **not** request re-inventory.
- **QA:** QA-01..08 APPROVED **as framework** by D03-QA-006; actual test pass not asserted.
- **Budget:** all budget-related tasks DEFERRED BY PO; exclude from this approval packet.
- **Pilot:** 2–5 family learners, Android online first, 4 weeks, no guaranteed TOEIC score gain deadline.

## Four bundled product requirement choices — one decision, editable if requested

### R1. Exam integrity and interruptions (RECOMMENDED)

- **Recommended:** Mocks A/B provide a separate *timed evaluation attempt* following TOEIC structure (Listening approximately 45m, Reading 75m); time is not secretly reset when app backgrounds. If an attempt is interrupted in a way that invalidates timing, flag it as *not comparable* rather than silently showing a clean mock result. Part practice remains flexible, including short sessions.
- **Alternative:** Allow pause/resume even in mock but explicitly call it an *untimed/practice attempt* excluded from comparative progress series.
- **TBD after choice:** exact playback/replay rule, tolerance for short phone interruptions, whether timer remains running when disconnected, auto-submit behavior; no UI implementation dictated.

### R2. Results and progress (RECOMMENDED)

- **Recommended:** Show correct/attempted totals and Part + Listening/Reading breakdown, form ID/date, attempt integrity label; two-mock comparison is **descriptive practice progress with limitations**, never automatic ETS 10–990-equivalent or proved increase in competence. Different difficulty/advance exposure warns against direct score comparison.
- **Alternative:** Present two reports independently, with no score trend until form comparability has separate evidence.
- **TBD:** copy wording for within-app progress and requirement for any goal score tracking; do not alter original vision objective.

### R3. Error feedback, recommendations and quick study (RECOMMENDED)

- **Recommended:** Correct answer required; vetted explanation shown only where available, with clear “chưa có giải thích” otherwise. Save wrong-item history; short study session and activity suggestion by transparent rules, plus unrestricted user selection. No AI-generated explanations/auto PDF importer/advanced notifications in current draft.
- **Alternative:** Require QA-approved explanations for every exposed practice item before MVP lock; greater content dependency, still no AI approval.
- **TBD:** whether validated answer explanations are mandatory for Full Mock review or for all practice items.

### R4. Family pilot reliability and privacy (RECOMMENDED)

- **Recommended:** Responses already confirmed must persist across common interruptions without silent reset; no cross-learner history leakage; user data correction/deletion rules to be specified before pilot; Part 7 long text and charts must remain complete/readable on pilot Android devices. This approves behavioral principles, not account systems, database, UI or measurable thresholds.
- **Alternative:** Stage 03 only records these risks and schedules detailed acceptance thresholds for a separate PO review before any test build.
- **TBD:** target devices, session conflict rules and retention period, after requirements-direction approval.

## Analyst recommendation

**APPROVE R1–R4 AS DRAFTING PRINCIPLES WITH OPEN TBDs**, subject to QA-01..08. This gives consistent semantics for writing verifiable requirements without authorizing delivery or skipping content QA.

## Signoff choices

- **A — APPROVE recommended R1–R4 principles for requirements drafting** (recommended); keep all TBDs open; no MVP/PRD/SRS approval.
- **B — APPROVE WITH AMENDMENTS**, group proposed edits into one reply; keep decision pending until reconciled.
- **C — HOLD**, continue desk research on material missing requirements evidence only; no baseline approval.

**If A:** update `D03-REQ-007` to APPROVED *requirements drafting direction*, prepare PRD/SRS for a separate formal scope and Stage 03 Gate review later. No budget actions until PO reopens; no UI/architecture/code.
