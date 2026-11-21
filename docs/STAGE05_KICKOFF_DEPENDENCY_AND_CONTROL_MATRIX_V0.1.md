# Stage05 Kickoff — Inputs, Constraints and Control Matrix V0.1

**State:** PROPOSED, for decision `D05-KICKOFF-001`; Stage05 NOT STARTED. This is an input/approval matrix, **not an architecture, feature plan or actual QA results**.

## 1. Approval and carry-forward map

| Control | Approved source | Planned Stage05 handling if kickoff is allowed | Owner/checkpoint |
|---|---|---|---|
| Product scope | Vision V1.0 + D03-SCOPE-009 S1/S2/S3 | Treat as frozen and identify architectural drivers, no new features | Analyst ARCH-01; PO for changes |
| Two Full Mocks B1 | D03-LOCK-001 and D03 baseline | Keep two independent 200-item form requirements; content QA eventually required | Future content/QA owner, before pilot |
| Requirements | PRD V0.6, SRS V0.6, Acceptance V0.4 | Trace 19 FR +13 NFR and AT to future option/verification plan; do not rewrite signed baseline | ARCH-01, change PO-only |
| UI | D04 design-spec baseline V0.3, UI-G01..16 | Translate UI semantics to constraints only; do not change UI without PO impact review | ARCH-01, PO for change |
| UX04-I01..I08 | Stage04 issue register | Carry pending issues to appropriate later architecture/test checkpoints | Later evidence owner, not PASS now |
| UIA-01..UIA-08 | Stage04 handoff register | Ensure truthful UI content and accessibility acceptance criteria are preserved | Later Android/UX QA owner |
| Stage02 CP01..05 | Signed Stage02 Gate | Active; preserve scope, evidence, budgets as previously signed | PO at relevant checkpoint |
| Stage03 G03-CP01..07 | Signed Stage03 Gate | Active; content QA, reliability, privacy, change and deferred budget remain | PO and test/content owners |
| Stage04 G04-CP01..08 | `D04-GATE-009` approval of exact proposal | **Now active**; includes separate Stage05 kickoff and no implementation inference | PO + appropriate future owner |
| QA01..08 | D03-QA-006 quality framework | Prepare later test/evidence ownership; do not mark PASS from documents | Actual QA later before pilot |
| Financial | Explicit PO deferral | Do not discuss quotes, budgets, vendors, purchases or spend | PO-only future reopening |

## 2. Evidence bar for any future decision

- `APPROVED PRODUCT POLICY` is not the same as `IMPLEMENTATION SELECTED`.
- `DESIGN BASELINE APPROVED` is not the same as `ANDROID SCREEN IMPLEMENTED`.
- `QA FRAMEWORK APPROVED` is not the same as `TEST EXECUTED/PASS`.
- `PO-REPORTED CONTENT INVENTORY` is not the same as `QUESTION/AUDIO/ANSWER QUALITY AUDITED`.
- `STAGE04 CONDITIONAL PASS` is not `STAGE05 AUTHORIZED`.
- Any future technical alternative must be evaluated against signed requirements and preserve available options until an explicit PO decision.

## 3. Pre-kickoff checks (document-only)

| Check | Status today | Blocking condition |
|---|---|---|
| D04-GATE-009=A accepted | **YES** | No |
| Exact G04-CP01..08 active | **YES** | No |
| Requirements/Design Baselines immutable | **YES** (checked) | No |
| Two mock inventories PO affirmed | **YES (PO reported)** | Do not recheck inventory |
| Real QA and devices | **NOT VERIFIED** | Future quality checkpoint, not kickoff paperwork |
| Budget | **DEFERRED** | No spend authorized; not a kickoff budget question |
| **D05-KICKOFF-001** | **PENDING** | **BLOCKS Stage05 and ARCH-01** |

**No future architecture or technical choice is implied by this index.**
