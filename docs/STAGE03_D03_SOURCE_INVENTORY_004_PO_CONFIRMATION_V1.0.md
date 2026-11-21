# D03-SOURCE-004 — PO Confirmation: Two Full Mocks Inventoried

**Date:** 2026-11-21  
**Decision source:** Product Owner's direct statement: **“2 bộ đề đã kiểm kê xong, các bước liên quan tới ngân sách tạm thời bỏ qua.”**  
**Record status:** CONFIRMED AS PO REPORT / NOT AN INDEPENDENT QA AUDIT.

## 1. Recorded facts and decisions

1. **Two mock exam sets have been inventoried:** confirmed by Product Owner. Set source IDs, Part counts, manifest file, mapping quality, content overlap and QA artifacts were not provided in this conversation. DO NOT demote the owner's clear report to “not inventoried”; DO NOT claim item-level verification or full 400-item QA.
2. The earlier **PO self-attestation of rights** for all three named websites and other sources remains in force. No request to repeat it is warranted. Content/item-level provenance remains a downstream quality gate.
3. **Budget-related steps are DEFERRED BY PRODUCT OWNER**: no further budget questionnaires, cost projections, quotes, vendor selection or approval of caps until PO resumes. This is a scope-of-current-work decision, not approval of unlimited expenditure or waiver of CP-04.
4. **B1 is unchanged**: two Full Mocks are still compulsory. This status is an input to Requirements, not an MVP scope lock.

## 2. Gate update

| Gate | Current evidence | New state | Do not assert |
|---|---|---|---|
| G-SOURCE / inventory | PO confirms two mock sets inventoried | **PO-REPORTED COMPLETE** | That a project manifest is available to the analyst or source assets were accessed |
| G-RIGHTS | PO states rights to all three source sites and more | **PO-AFFIRMED** | That every 3rd-party audio/image/trademark/export condition has passed audit |
| G-MOCK | Two sets inventoried as reported | **INVENTORIED — QA PENDING** | 400 mapped nonduplicated scored items were independently checked |
| G-QA | No structured audit result supplied | **OPEN — NOT VERIFIED** | Answer keys, audio grouping, imagery and scoring have passed |
| G-PRACTICE | No separately approved practice bank manifest | **OPEN** | Full Mock items can safely be reused for practice |
| G-COST | PO defers all budget work | **DEFERRED — NOT WAIVED** | Costs approved, zero or unlimited |
| MVP LOCK | PO did not approve it | **HOLD** | Scope or PRD/SRS is approved |

## 3. Working instructions

Continue Requirements drafting with mock-availability expressed as **PO-inventoried, pending objective QA**. Do not run a new sourcing investigation solely to re-establish inventory; focus on testing readiness, necessary acceptance criteria, answer/audio/passage mapping and requirements traceability. Review budget only when PO explicitly reopens; the formal financial gate remains open for later stage-gate decision. Keep CP-01..05 active.
