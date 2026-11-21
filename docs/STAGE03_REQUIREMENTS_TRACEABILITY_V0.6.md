# Requirements Traceability — BASELINE CANDIDATE V0.6

**Source:** Product Vision V1.0; signed D03-SCOPE-009 S1/S2/S3, R1..04, QA01..08; PRD/SRS V0.6 candidate and AT catalogue V0.4. **Status:** SELF-AUDIT FOR D03-BASELINE-010, NOT PO APPROVED and no test PASS.

## 1. MVP-in functional requirements (19/19 mapped)

| FR | MVP bundle | Vision/user journey | Acceptance | QA | Evidence due |
|---|---|---|---|---|---|
| FR-001 | M01 | J01 | AT-01 | QA-08 | Pre-pilot system |
| FR-002 | M02 | J02 | AT-02 | QA-01/05/06 | Pre-pilot content |
| FR-003 | M02 | J02 | AT-03 | QA-03 | Pre-pilot content |
| FR-004 | M02/M07 | J02/J07 | AT-04 | QA-04/08 | Pre-pilot content |
| FR-005 | M04/M07 | J02/J07 | AT-05 | QA-08 | Pre-pilot system |
| FR-006 | M04 | J04 | AT-06 | QA-02/07 | Pre-pilot system |
| FR-007 | M04/M08 conditional explanation | J04 | AT-07 | QA-02/06 | Pre-pilot system |
| FR-008 | M04 | J04 | AT-08 | QA-07/08 | Pre-pilot system |
| FR-009 | M05a | J01 | AT-09 | QA-08 | Pre-pilot system |
| FR-010 | M03 B1 | J03 | AT-10 | QA-01..06 | Pre-pilot content |
| FR-011 | M03 | J03/J07 | AT-11 | QA-08 | Pre-pilot system |
| FR-012 | M04 | J05 | AT-12 | QA-07 | Pre-pilot system |
| FR-013 | M03/M04 | J03/J05 | AT-13 | QA-05/07 | Pre-pilot system |
| FR-014 | M05b | J01 | AT-14 | QA-07/08 | Pre-pilot system |
| FR-015 | M06/M09 | J06 | AT-15 | QA-02..06 | Pre-pilot content |
| FR-016 | M06 | J06 | AT-16 | QA-02/07 | Pre-pilot system |
| FR-017 | M06 | J06 | AT-17 | QA-01..06 | Pre-pilot content |
| FR-018 | M01/M07 | J07 | AT-18 | QA-08 | Pre-pilot system |
| FR-019 | M07 | J07 | AT-19 | QA-08 | Pre-pilot system |

## 2. Non-functional and governance requirements (13/13 mapped)

| NFR | AT/quality metric | QA | Evidence due |
|---|---|---|---|
| NFR-001 | AC-03; AT-15 | QA-01..06 | Before relevant QA/release gate |
| NFR-002 | AC-04; AT-03 | QA-03 | Before relevant QA/release gate |
| NFR-003 | AC-05; AT-05/19 | QA-08 | Before relevant QA/release gate |
| NFR-004 | AC-05/08; AT-11/19 | QA-08 | Before relevant QA/release gate |
| NFR-005 | AC-06; AT-04 | QA-04/08 | Before relevant QA/release gate |
| NFR-006 | AC-05; AT-18 | QA-08 | Before relevant QA/release gate |
| NFR-007 | AC-05; AT-12/13 | QA-07 | Before relevant QA/release gate |
| NFR-008 | AT-16 | QA-02/07 | Before relevant QA/release gate |
| NFR-009 | AC-01; traceability audit | QA-01..08 | Before relevant QA/release gate |
| NFR-010 | AC-06/08; AT-04 | QA-08 | Before relevant QA/release gate |
| NFR-011 | AT-19 | QA-08 | Before relevant QA/release gate |
| NFR-012 | AT-12/13; release copy review | QA-07 | Before relevant QA/release gate |
| NFR-013 | CP-04 deferred, future PO checkpoint | N/A; deferred | Deferred with PO approval |

## 3. Explicitly OUT and CONDITIONAL

- `FR-020..023` are **OUT** (automatic PDF/audio importing, runtime AI, advanced notifications, offline/iOS/S&W/monetization). They are not counted as MVP critical requirements, but remain backlog/change-control traceable.
- `FR-007` explanation is **CONDITIONAL**; key display and absent-explanation disclosure remain **IN** and testable in AT-07.
- Proposed candidate 100% critical traceability: **19/19 included FR** and **13/13 NFR** mapped to a test or governance checkpoint; NFR-013 is **approved deferred financial work**, not pretended software QA. The mapping is a **document coverage analysis** and not proof the future acceptance tests are adequate or have passed.

## 4. Requirements-stage checklist to review at D03-BASELINE-010

- [x] 19 included FR have stable IDs, tests, QA and planned verification phase.
- [x] 13 NFR map to acceptance, quality or explicitly deferred governance obligations.
- [x] Two Full Mock B1 unchanged; 2 inventories PO-reported, not independently audited.
- [x] S2 includes signed timing/replay, persistence, raw reporting, 7d/30d privacy values.
- [x] S3 includes 100% essential content QA, zero known critical release issues, two Android contexts, 2 participant pair criterion.
- [ ] PO independently approves **exact PRD/SRS V0.6 baseline revisions** in D03-BASELINE-010.
- [ ] Later item QA and mobile app testing; **NOT Stage03 evidence PASS**.
- [ ] Later performance/network SLA and data exception details at respective checkpoints.

No design or code artifacts are traceable as authored or approved.
