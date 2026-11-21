# S1 — MVP Candidate IN/OUT Matrix V0.1

**Status:** PROPOSED / D03-SCOPE-009 PENDING. No locked MVP. Refer to SRS Draft V0.5; `P1` is analyst priority, not approved IN.

| Bundle | IDs in SRS V0.5 | Candidate | Acceptance relationship | Important gate |
|---|---|---|---|---|
| M01: Pilot account/profile minimal | FR-001; NFR-006 | **IN (proposal)** | AT-01/18 | Identity/privacy rules must be signed before pilot; no design decision |
| M02: Part 1–7 practice, distinct pool | FR-002/003/004 | **IN (proposal)** | AT-02/03/04 | QA-ready practice bank distinct from mock A/B required before pilot |
| M03: Full Mock A/B, 2x200 | FR-010/011/013 | **B1 MANDATORY; IN proposed** | AT-10/11/13 | Inventories PO complete; QA-01..06 **not verified**; cannot substitute one mock |
| M04: Answer, scoring and errors | FR-005/006/007/008/012 | **IN (proposal)** | AT-05/06/07/08/12 | Correct validated keys; explanations conditional on vetted availability |
| M05a: One-question short session | FR-009 | **IN (proposal)** | AT-09 | Distinguish from evaluative Full Mock |
| M05b: Simple rules for next lesson | FR-014 | **IN (proposal), removable** | AT-14 | Default for no history, no AI or forced route |
| M06: Content quality/version safeguards | FR-015/016/017 | **IN (proposal)** | AT-15/16/17 | Content correction must not corrupt prior scores |
| M07: Recovery, family separation, long Reading | FR-018/019; NFR-003..011 | **IN (proposal)** | AT-18/19 and AT-04/05 | No silent answer loss; no cross-learner leakage; real Android QA later |
| M08: Curated explanation | subset FR-007 | **CONDITIONAL** | AT-07 | Only if verified; missing explanation disclosed rather than fabricated |
| M09: Manually curated rights-cleared content inputs | BR-03, FR-015 | **IN as content-supply responsibility, not PDF import feature** | QA-06/AT-15 | PO rights attested; per-item source and version audit before pilot |
| X01: Auto PDF/audio parser/answer mapping | FR-020 | **OUT / later** | N/A | Not inferred from personal-library vision |
| X02: AI runtime tutoring/generation/advanced adaptive AI | FR-021 | **OUT / later** | N/A | Requires separate QA and funding consent |
| X03: Advanced interactive vocab notifications | FR-022 | **OUT / later** | N/A | Android permission/timing needs later study |
| X04: iOS, offline-first, TOEIC S&W, payments, ads | FR-023 | **OUT / later** | N/A | Android L&R online-first pilot only |
| X05: TOEIC official scaled-equivalence or endorsed score | BR-05, NFR-007 | **EXPLICITLY OUT** | AT-12/13 | Never imply ETS 10–990 without defensible calibration and rights |

**Not a hidden commitment:** A proposed `IN` does not attest implementation, QA pass or scope approval. Source library should not silently expand to automated import. M05b can be removed in one amendment; M03 cannot be removed without separate PO change to B1.

**Pilot learning-path value:** M01+M05a+M05b give minimal flexible personalization; full long-term adaptive roadmap remains future.  **Distinct practice bank:** already PO-inventoried mock sets do not establish the practice bank; verify this *without asking to redo mock inventory*.

**Recommended S1-A:** adopt rows as drafted; review scope against core user jobs J01–J07 and vision. **Alternative S1-B:** move M05b rules to OUT while preserving short learning. **No feature deletion automatically authorized.**
