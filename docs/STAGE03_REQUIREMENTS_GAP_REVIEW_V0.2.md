# Stage03 Requirements Gap & Consistency Review — V0.2

**Scope:** compare V0.4 against newly approved D03-REQ-007; update PRD/SRS V0.5, test catalogue and evidence mapping. **No code/UI/architecture.**

| Review check | Finding / remediation | Result for document review, NOT feature QA |
|---|---|---|
| DEC-01 D03-REQ-007 | R1–R4 previously PENDING; formally marked APPROVED as drafting principles, retaining sub-TBD | RESOLVED in V0.5 |
| DEC-02 two forms | Existing PO-inventoried A/B kept; not wrongly marked as missing or QA-PASS | RESOLVED as wording |
| DEC-03 QA status | Approved QA-01..08 framework vs actual audit/test NOT VERIFIED explicitly separated | RESOLVED as wording |
| DEC-04 budget status | Budget tasks remain DEFERRED; no pricing, ceilings or effort budgets requested | RESOLVED as scope |
| REQ-01 Mock time policy | 45/75 referenced; mock vs practice & valid/invalid behavior testable conceptually; replay/grace/timeout still TBD | PARTIAL — PO behavioral choice needed |
| REQ-02 Score meaning | Raw scoring + section/Part aggregates and comparison warnings; no ETS scaled claim | REVIEW DRAFT (test pending) |
| REQ-03 Content/key correction | Versioning, no silent rewrite of past results, disabled broken content | REVIEW DRAFT (test pending) |
| REQ-04 Learning loop | No fabricated explanations; explicit fallback to learner choice; AI deferred | REVIEW DRAFT (coverage TBD) |
| REQ-05 Reliability | Answer acknowledgment and network/offline/no duplicate submit edge cases now test designs | PARTIAL — acknowledgment threshold/TBD |
| REQ-06 Family/privacy | Data isolation and deletion obligations; retention/account policy not chosen | PARTIAL — pre-pilot resolution needed |
| REQ-07 Android reading | Long/passage/table completeness, readability on real phones specified | PARTIAL — handset/measurement TBD |
| REQ-08 Traceability | FR-001..019 ↔ AT-01..19, QA-01..08, product journeys; FR-020..023 explicitly deferred | DOC REVIEW PASS, not QA execution |
| REQ-09 Pilot measurement | 2–5 family users, 4 weeks, metrics candidate; score gain not assured | PARTIAL — KPI thresholds and method to be approved |
| CP-01..05 | Carried forward; no MVP lock or hidden release authorization | CONTROLLED |

## Policy-level decisions for one bundle before formal Gate review

- `P1`: strict mock vs flexible practice, pause/replay/timeout/interruption validity rules (business behavior, not UI).
- `P2`: pilot data retention/deletion principle; choice of account creation (if any) and access policy deferred to separate scope approval.
- `P3`: how to evaluate pilot success without claiming statistically validated score gain, and when detailed QA/device proof is due.

**No content item-level QA, Android test, or performance measurement was performed in this Requirements review.**
