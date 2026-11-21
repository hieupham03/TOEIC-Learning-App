# Requirements Evidence & Traceability — V0.4 (Draft)

**Status:** ANALYST DRAFT. PO approved two Full Mock requirement B1 and QA framework D03-QA-006; NOT the full matrix or FR/NFR baseline.  
**Evidence grades:** `APPROVED DECISION`, `PO-REPORTED`, `OFFICIAL PUBLIC REFERENCE`, `ANALYST PROPOSAL`, `NOT VERIFIED`.

| Vision/user need | Evidence grade & source | PRD journey | SRS IDs | QA IDs | Remaining gap |
|---|---|---|---|---|---|
| Full Mock L&R and comparable progress | APPROVED B1; ETS official format | J03/J05 | FR-010/011/012/013; NFR-004/007 | QA-01/05/07/08 | Exam policy, content QA, score semantics TBD |
| 2 forms already inventoried | PO-REPORTED D03-SOURCE-004 | J03/J06 | FR-010/015 | QA-01..06 | Detailed manifest not independently audited; no re-inventory required |
| Audio ↔ item ↔ key in one workflow | Vision; PO prior laptop pain points | J02/J06 | FR-003/005/006/015; NFR-002 | QA-02/03 | Media mapping QA not run |
| Part 1–7 and micro sessions | Vision and Stage 02 benchmark | J01/J02 | FR-002/009/014 | QA-01/08 | Practice bank distinct from mocks not evidenced |
| Reading long text and eyestrain | PO user experience (firsthand) | J02/J07 | FR-004/019; NFR-005/010 | QA-04/08 | Real-phone readability test later |
| Review wrong answers / explanations | Approved Vision, not specific completeness rate | J04 | FR-006/007; NFR-008 | QA-02/07 | Explanation coverage policy pending R3 |
| Personalized by goal & irregular time | Vision; behavioral learning literature as principle | J01 | FR-001/009/014 | QA-08 | Rules/fallback and thresholds pending R3 |
| Rights and provenance for web content | PO attestation for 3 named sites + others; no asset audit | J06 | FR-015/017; NFR-001/012 | QA-06 | Item-level provenance deferred to actual QA |
| Family data and interruptions | Vision online-first; Android official lifecycle state | J05/J07 | FR-005/008/018/019; NFR-003/006/011 | QA-08 | R1/R4 policy pending and tests after software exists |
| 4-week 2–5 learner pilot | Vision Approved | J01..J07 | FR-008/012 | QA-07/08 | Signoff metrics/thresholds pending |
| Budget work | PO explicit DEFERRED | — | NFR-013 DEFERRED | — | CP-04 tracked; must not request budget this turn |
| PDF auto-ingest, AI, interactive notifications | Vision long-term; scope not approved | Future | FR-020/021/022 | — | Separate future PO decision, no pilot commitment |

## Official research references (checked 2026-11-21)

- ETS TOEIC Listening & Reading exam content and 45+75 min: https://www.ets.org/toeic/about/listening-reading.html
- ETS FAQ: 200 questions, 100 + 100, score range/scaled interpretation: https://www.ets.org/toeic/about/faq/product-specific-faq/toeic-listening-reading.html
- Android application process lifecycle (requirements risk, not architecture decision): https://developer.android.com/guide/components/activities/process-lifecycle
- Android save UI states (why clear interruption/recovery requirements are needed): https://developer.android.com/topic/libraries/architecture/saving-states
- Android accessibility tests (future acceptance): https://developer.android.com/guide/topics/ui/accessibility/testing

**No content sourced/copying done in this requirements review.**
