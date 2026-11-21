# Stage05 ARCH-01 — Controlled Requirements-to-Drivers Traceability V0.1

**Status:** ARCH-01 document mapping, NOT a test execution report. **Source of truth:** signed PRD V0.6/SRS V0.6/Acceptance V0.4. The older traceability V0.6 contains historical 'candidate' headings superseded by D03-BASELINE-010.

## 1. Functional requirements — 19/19 included MVP

| FR | Signed MVP group | User journey | AT | QA | Driver(s) | Future evidence / checkpoint |
|---|---|---|---|---|---|---|
| FR-001 | M01 | J01 | AT-01 | QA-08 | AD-05/11 | Pre-pilot system |
| FR-002 | M02 | J02 | AT-02 | QA-01/05/06 | AD-07/08 | Pre-pilot content |
| FR-003 | M02 | J02 | AT-03 | QA-03 | AD-02/07 | Pre-pilot content |
| FR-004 | M02/M07 | J02/J07 | AT-04 | QA-04/08 | AD-10/07 | Pre-pilot content |
| FR-005 | M04/M07 | J02/J07 | AT-05 | QA-08 | AD-03/04/12 | Pre-pilot system |
| FR-006 | M04 | J04 | AT-06 | QA-02/07 | AD-09/07 | Pre-pilot system |
| FR-007 | M04/M08 conditional explanation | J04 | AT-07 | QA-02/06 | AD-11/09 | Pre-pilot system |
| FR-008 | M04 | J04 | AT-08 | QA-07/08 | AD-05/09 | Pre-pilot system |
| FR-009 | M05a | J01 | AT-09 | QA-08 | AD-11/08 | Pre-pilot system |
| FR-010 | M03 B1 | J03 | AT-10 | QA-01..06 | AD-01/02/08 | Pre-pilot content |
| FR-011 | M03 | J03/J07 | AT-11 | QA-08 | AD-01/02/04 | Pre-pilot system |
| FR-012 | M04 | J05 | AT-12 | QA-07 | AD-09/12 | Pre-pilot system |
| FR-013 | M03/M04 | J03/J05 | AT-13 | QA-05/07 | AD-01/09 | Pre-pilot system |
| FR-014 | M05b | J01 | AT-14 | QA-07/08 | AD-11 | Pre-pilot system |
| FR-015 | M06/M09 | J06 | AT-15 | QA-02..06 | AD-07/15 | Pre-pilot content |
| FR-016 | M06 | J06 | AT-16 | QA-02/07 | AD-09/15 | Pre-pilot system |
| FR-017 | M06 | J06 | AT-17 | QA-01..06 | AD-07/12 | Pre-pilot content |
| FR-018 | M01/M07 | J07 | AT-18 | QA-08 | AD-05/06 | Pre-pilot system |
| FR-019 | M07 | J07 | AT-19 | QA-08 | AD-01/03/04/12 | Pre-pilot system |

## 2. Non-functional requirements — 13/13 including deferral governance

| NFR | Acceptance/quality control | QA | Driver(s) | Future checkpoint |
|---|---|---|---|---|
| NFR-001 | AC-03; AT-15 | QA-01..06 | AD-07/08 | Before relevant QA/release gate |
| NFR-002 | AC-04; AT-03 | QA-03 | AD-02 | Before relevant QA/release gate |
| NFR-003 | AC-05; AT-05/19 | QA-08 | AD-03 | Before relevant QA/release gate |
| NFR-004 | AC-05/08; AT-11/19 | QA-08 | AD-01/04 | Before relevant QA/release gate |
| NFR-005 | AC-06; AT-04 | QA-04/08 | AD-10/13 | Before relevant QA/release gate |
| NFR-006 | AC-05; AT-18 | QA-08 | AD-05/06 | Before relevant QA/release gate |
| NFR-007 | AC-05; AT-12/13 | QA-07 | AD-09/12 | Before relevant QA/release gate |
| NFR-008 | AT-16 | QA-02/07 | AD-09/15 | Before relevant QA/release gate |
| NFR-009 | AC-01; traceability audit | QA-01..08 | AD-15 | Before relevant QA/release gate |
| NFR-010 | AC-06/08; AT-04 | QA-08 | AD-10/13 | Before relevant QA/release gate |
| NFR-011 | AT-19 | QA-08 | AD-03/04 | Before relevant QA/release gate |
| NFR-012 | AT-12/13; release copy review | QA-07 | AD-09/16 | Before relevant QA/release gate |
| NFR-013 | CP-04 deferred, future PO checkpoint | N/A; deferred | AD-16 | Deferred with PO approval |

## 3. Interpretation and coverage notes

- FR-007 correct-key display is IN while long-form vetted explanation is CONDITIONAL on content QA; driver AD-11 does not turn it into generated-AI scope.
- FR-020..FR-023 are **OUT** by signed baseline and excluded from 19/19 coverage; changes require PO approval.
- NFR-013 is a **deferred governance cost control**, not a software QA test to fake as PASS.
- Checkpoint `Pre-pilot` means a future evidence owner/test; it does not mean the current Stage05 work executed QA.
- This is an **index-level trace check**. Detailed quality test designs remain AT-01..AT-19; the 19 FR and 13 NFR checks appear once each.
- UX04-I01..08 and UIA-01..08 are traced through AD-10/12/13, with unclosed status; no claim of completed device/user evaluation.

**ARCH-01 traceability result:** 19/19 included FR plus 13/13 NFR mapped to at least one architecture driver and existing accepted AT/QA or governance checkpoint. This is a **document consistency check**, not proof of technical feasibility.
