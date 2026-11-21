# Stage 03 — Evidence-First Requirements Gap Review V0.1

**Review date:** 2026-11-21. **Status:** ANALYST REVIEW, NOT AN APPROVAL.  
**Scope:** Audit older PRD/SRS V0.3 for stale text, missing acceptance rules, traceability and contradictions; build draft V0.4. No budget research, UI, architecture or code.

## A. Findings resolved in new drafts (not status PASS)

| ID | Finding from prior draft | Severity | Resolution in V0.4 |
|---|---|---|---|
| GAP-01 | FR-010 was still called “BLOCKED because 400 questions not sourced” despite PO reporting two sets inventoried | High — inconsistent with PO | Reworded: *inventory PO-confirmed*, quality mapping/independence still unverified |
| GAP-02 | Old PRD/SRS asked for budget approval and active cost cap after PO explicitly deferred | High — decision mismatch | Segregated financial work as **DEFERRED BY PO**, no current asks; CP-04 retained |
| GAP-03 | QA-01..08 previously marked analyst proposal although PO now approved the framework | High — governance mismatch | Separate approval decision, test evidence remains NOT VERIFIED |
| GAP-04 | Mock timed test vs flexible Part practice and interruption policy undefined | High — can't test reliability/comparable practice | D03-REQ-007 R1 decisions with recommended exam policy, FR-011/019 and AT-11/19 |
| GAP-05 | Raw accuracy/Part reports could be mistaken for official TOEIC-equivalent scoring | High — misleading interpretations | FR-012/013, NFR-007; explicit warning/validation rules, R2 still pending |
| GAP-06 | Correct answer vs vetted explanation coverage not distinguished | Medium — content quality and learning experience | FR-007 explains no fabricated explanation; R3 grouped decision |
| GAP-07 | Practice content could leak mock questions, invalidating before/after comparison | High — content evidence | QA-05, FR-013, separation requirement and test case |
| GAP-08 | Audio/passage/key correction could silently change already reported results | High — data integrity | FR-015/016, NFR-008 and regression AT-15/16 |
| GAP-09 | App background/process death, network loss and long Reading were too generic to test | High — Android reliability | Expanded NFR-003/004/005/010/011, AT-19 and QA-08; thresholds still TBD |
| GAP-10 | Broad “personalization” wording risked inferring AI | Medium — scope | Clear candidate rule-based guidance, user self-choice, AI deferred |

## B. Open product decisions — consolidate, do not ask serial questions

- **R1 Mock integrity** (timer, interruptions, listening replay): choose principle, not UI implementation.
- **R2 Result reporting** (raw scores, Part, comparison disclaimer, invalid attempt labels): choose semantics, not algorithm or ETS equivalence.
- **R3 Learning loop** (explanation policy, rule-based suggestion, micro session): choose behavioral commitment at requirements level.
- **R4 Pilot data/reliability** (answer preservation, long reading, user isolation and data handling): choose quality principles with acceptance thresholds later.

## C. Gaps not provable today; keep open without blocking writing requirements

- Actual item-level QA of two already-inventoried mocks, audio key/passage mapping, duplicate report, practice pool independence. Do not claim passed; stage of audit depends on availability of evidence.
- Quantitative performance thresholds for retention/recovery, font/text-size behavior and target Android devices. Avoid inventing SLA.
- Explanation availability/coverage across sources. Do not fabricate a corpus.
- Privacy/account-retention detail, clarified during later requirements refinement; do not choose login architecture.
- Comparative learning efficacy within 4-week pilot: small sample not representative, not a guarantee of TOEIC score increase.
- Budget: DEFERRED BY PO, no current task; CP-04 not waived.

## D. Review outcome

- `PRD Draft V0.4`: prepared, traceable to Vision and PO decisions.
- `SRS Draft V0.4`: prepared, behavior/test cases with unapproved priority labels.
- `QA framework`: APPROVED but test executions NOT VERIFIED.
- `D03-REQ-007`: PENDING Product Owner one-batch review.
- `MVP LOCK`: HOLD; `STAGE03 GATE`: NOT STARTED; `UI/ARCHITECTURE/CODE`: NOT AUTHORIZED.
