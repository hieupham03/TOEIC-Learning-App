# Stage05 ARCH-02 — Requirements, Driver and Conditional-Gate Traceability V0.1

**Scope:** maps the ARCH-02 **research coverage** to signed requirements and existing condition families. It does not close any QA/UX control or dictate implementation.

| Study domain | Drivers / watch / gap | Signed FR/NFR/AT anchors | Existing QA and Gate obligations | Next evidence owner / stage |
|---|---|---|---|---|
| Time, mock/validity | AD01/04, CW01, EG02/10 | FR-010/011/013/019; NFR-004/011; AT-10/11/13/19 | QA-08; G03-CP01..07; G04-CP01..08 | PO test thresholds then software QA before pilot |
| Audio order and interruptions | AD02, CW01, EG03 | FR-003/010/011/015; NFR-001/002; AT-03/10/11/15 | QA-03/08; UX04-I.. & UIA open | Curator + future Android test owner |
| ACK and resilience | AD03/04, CW02/07, EG04 | FR-005/019; NFR-003/011; AT-05/19 | QA-08; signed Design Baseline truthful states | Future persistence/QA owner |
| Learner separation & deletion | AD05/06, CW05, EG05 | FR-001/008/018; NFR-006; AT-01/08/18 | QA-08; G03/G04-CP privacy | PO privacy checkpoint + future QA |
| Forms & QA release | AD07/08, CW03/04, EG01/06 | FR-002/003/004/015/017; NFR-001/002; AT-02/03/04/15/17 | QA-01..06, B1 2x200; budget DEFERRED | Content curator before pilot |
| Raw scores and correction history | AD09/15, CW06/09, EG07 | FR-006/008/012/013/016; NFR-007/008/012; AT-06/08/12/13/16 | QA-02/07; no ETS conversion | Scoring QA and data owner |
| Practice suggestions & explanations | AD11/12, CW08, EG12 | FR-006/007/009/014; NFR-009; AT-06/07/09/14 | UI-G01..16, content explanation QA | UX/content owner |
| Reading/accessibility/mobile | AD10/13, CW10, EG08/09 | FR-004; NFR-005/010; AT-04 | QA-08, UX04-I01..08, UIA-01..08 | Android and UX device review |
| Pilot validity/governance | AD14/16, EG11/13/14/15/16 | Signed S1/S2/S3, pilot acceptance and PRD/SRS | CP-01..05; G03-CP01..07; G04-CP01..08 | PO / pilot reviewer |

## Control inventory: all ACTIVE, none closed by ARCH-02

- `CP-01..05` Stage02 conditional carry-forward.
- `G03-CP01..07` Stage03 conditional carry-forward.
- `G04-CP01..08` Stage04 conditional carry-forward.
- `QA-01..08` PO-approved **framework**, **actual tests NOT PASSED / NOT VERIFIED**.
- `UX04-I01..08`, `UIA-01..08` open/partial.
- `UI-G01..16` signed design guidance.
- `Budget`: **DEFERRED BY PO**; ARCH-02 research caused no spending and creates no purchase authority.

## Authority fence and baseline immutability

- D05-KICKOFF-001=A authorized ARCH-01; D05-ARCH-002=A authorized ARCH-02 **comparative desk research only**. No other Stage05 work automatically authorized.
- Exact approved Requirements baseline PRD V0.6/SRS V0.6/Acceptance V0.4 and Design Specification V0.3 are UNCHANGED; signed policy prevails over analyst comparisons.
- No architecture diagrams, cloud/runtime selections, endpoints, data models, code, POCs, tests or declarations of feasibility PASS were generated.
- Next PO review `D05-TECH-003` may authorize a research/reference direction only. A later separate authorization is still required for ARCH-03 architecture candidate design.
