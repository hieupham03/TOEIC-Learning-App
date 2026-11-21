# V0.5 → V0.6 Reconciliation and Deferred-Issue Ledger V0.1

**Business decisions APPROVED:** D03-SCOPE-009 S1-A/S2-A/S3-A. **Documents:** V0.6 BASELINE CANDIDATES; D03-BASELINE-010 PENDING.  
**Reconciliation method:** keep stable FR/NFR and AT IDs, retain historical V0.5 untouched, replace prior candidate-language in new V0.6 only. No autonomous feature additions, technical design or implementation.

| Delta | Prior PRD/SRS V0.5 | V0.6 candidate after D03-SCOPE-009 | Source / effect |
|---|---|---|---|
| D01 | MVP IN/OUT was candidate with P1/P2 informal labels | M01..M07+M09 **IN**, M08 curated explanation **conditional**, X01..X05 **OUT** | S1-A APPROVED; FR-014 is IN, not silently dropped |
| D02 | Full Mock B1 direction; many policy TBDs | B1 preserved, no pause/replay for comparable mock, ordered Listening (~45m), 75m Reading, explicit integrity labels | S2-A P01..05 APPROVED; tests later |
| D03 | Network and saved answers guardrail only | Durable acknowledgment required before “saved”; pending status on uncertain network; never silently reset time | S2-A P05/06 APPROVED |
| D04 | Result finalization, scoring/validity not entirely fixed | One finalized result; raw L/R/Part/attempt, blank count and non-comparable labels; no official ETS score | S2-A P07/08 APPROVED |
| D05 | Pilot data deletion and retention numerical targets TBD | Verified request ≤**7 calendar days**, routine retention ≤**30 days after pilot** with documented exceptions | S2-A P09 APPROVED; account mechanics later |
| D06 | AC/PM numeric values were proposals only | AC-01..08 and PM-01..06 **APPROVED targets** and verification phases; zero-known-critical applies AFTER QA, not now | S3-A APPROVED; AT execution NOT RUN |
| D07 | Content supply considered, mock sources PO reported | Two inventories PO-complete; 400 item/asset/duplicate QA remains OPEN; distinct Part bank still content-gated | B1, CP-03/04; no fake content PASS |
| D08 | Budget removed from active analysis | Budget remains **DEFERRED BY PO**, CP-04 retained; no new cost estimates or approval sought | D03-BUDGET-005 unchanged |
| D09 | No traceability full for every critical NFR | Mapped 19 included FR, 13 NFR to AT/QA/governance and due gate | AC-01 self-audit before baseline |

## Open issues: NOT Stage03 business-scope blockers if accepted as future evidence gates

| Open ID | Issue and status | Due by | Hard rule |
|---|---|---|---|
| O-01 | Content answer/audio/image/passages and cross-form duplicate QA **NOT VERIFIED** | Before pilot content release | Cannot mark either Full Mock ready until all QA-01..06 relevant checks pass |
| O-02 | Practice bank independently sourced/QA and no mock item exposure **OPEN** | Before pilot practice release | Approved Part1–7 IN cannot be silently removed |
| O-03 | Application result/timer/persistence/long Reading and family isolation tests **NOT RUN** | Before pilot application release | AC-05/06 blocking defects must be resolved |
| O-04 | Quantitative time/network/save/recovery/performance thresholds **TBD** | Before software test-plan baseline | No fake thresholds or waiver of integrity obligations |
| O-05 | Account identity verification, lawful deletion exceptions and access policy operationalization **TBD** | Before pilot and platform publication as relevant | Signed 7d/30d policy unchanged |
| O-06 | Key correction recomputation/appeal procedure **TBD** | Before any historical results can be recalculated | No silent historic overwrites |
| O-07 | Budget controls **DEFERRED BY PO** | Explicit PO reopening before spend/relevant operation | CP-04 remains active; not present lock blocker |
| O-08 | Stage03 formal baseline and Gate decisions **PENDING** | D03-BASELINE-010, then Stage03 Gate | No unauthorized Stage04/architecture/UI/code |

## Baseline-readiness recommendation

**READY FOR OWNER'S DOCUMENT BASELINE DECISION, with recorded future-evidence obligations.** It would be misleading to request content/device QA PASS to sign a Requirements document before implementation; however the obligations and blocking effects **must remain explicit**, not erased. If Product Owner finds that a future TBD changes a material business decision, amend V0.6 before approving D03-BASELINE-010. **Stage03 Gate must be a separate approval.**
