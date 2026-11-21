# Stage 05 — Consolidated Policy Critical Path & Decision Dependencies V0.1

**Status: PROPOSED DOCUMENTARY SYNTHESIS ONLY — NOT AN APPROVAL OR EXECUTION REQUEST.**
**Preparation authority:** PO's 2026-11-21 instruction to prepare one consolidated Stage05 decision pack, after D05-POL-010=A. **No new policy values are signed.**

## I. Why consolidate now

The four signed documentary rule subsets P05-R1..R3, P06-R1..R4, P07-R1..R3 and P08-R1..R4 already establish honest ACK/UNKNOWN review and evidence provenance/conflict handling. Fourteen signed reviewer rules **do not** demonstrate that any application feature works; producing separate small policy approvals without a scoped observation would not provide stronger technical evidence. This pack groups only decisions that can *actually* block a proposed bounded verification, separates those needed before descriptive observation from those necessary for a PASS, and defers architecture selection.

## II. Three readiness levels (not Stage 05 Gates)

| Level | Allowed interpretation | Mandatory conditions | Current |
|---|---|---|---|
| **L0 — documentary preflight** | Read, trace, challenge hypotheses and prepare unexecuted test request | Signed baseline + reviewer rules; no new experimental work | Current controlled scope for this packet |
| **L1 — bounded exploratory observation, later** | Gather actual evidence for a *specific* EV/FM without claiming requirement PASS; only if future PO expressly allows specific execution and any tools/POC it needs | Explicit PO test permission, exact observation/data scope, ethics/privacy, source provenance, qualified owner, stop rules, any needed resource authorization | **NOT AUTHORIZED** |
| **L2 — bounded claim verification, later** | Only make a restricted PASS/FAIL/INCONCLUSIVE claim tied to a signed requirement, version, scope and evidence | Everything at L1 **plus** relevant numeric or categorical acceptance criteria and approved authority where necessary, actual artifacts and QA sign-off | **BLOCKED / NOT RUN** |

**L1 permission never implies L2 PASS.** Any future need for code, a prototype, an Android device, media testing, paid service or participant work requires its own explicit authorization. The current instruction is only L0 document preparation.

## III. P0 critical-path lanes — decisions before a bounded test request

| Lane | Linked evidence & acceptance | What is already locked | What a single future scoped decision must specify | Stop consequence |
|---|---|---|---|---|
| **K1 Mock time & Listening** | POL01..04; EV01..04; FM01..05/18; BR02/04, FR003/011/019, AT03/11/19 | No silent timer reset, no unauthorized pause/replay, uncertain integrity ≠ clean | What a proposed test would observe, Android context, interruption/reboot/clock/audio coverage, claim-specific numerical tolerance/authority **only if PASS sought** | No clean/comparable PASS absent credible scoped proof |
| **K2 Durable answer & retry** | POL05/06/07/08/09; EV05/06/07; FM02/07/08/09/14; FR005/019, AT05/19 | Genuine durable ACK required, missing ACK=UNKNOWN, no wrong-learner binding; signed reviewer rules | Proposed admissible durability observation and proof of no duplicate logical effect; relevant ownership/context, independent or correlated provenance; **no source selected now** | No `Đã lưu` certification without valid evidence |
| **K3 Learner privacy & deletion** | POL09/10/14; EV07/08; FM09..11; FR018, AT18, NFR006 | Isolation, verified request ≤7 calendar days, routine post-pilot retention ≤30 days absent valid exception | Actual in-scope data copies, backup/exceptions, test data and consent boundaries, deletion observation artifact/owner **if later scoped** | No privacy PASS without scope/copy accounting |
| **K4 Content & result provenance** | POL11/12; EV09..11; FM06/12..14/16/17; FR006/010/015/016 | B1 two distinct 200-item forms already PO inventoried; rights attested; content QA not passed; raw scores not ETS equivalent | Item/media/key/version QA evidence and history-correction review plan for *relevant content checkpoint*; do not re-open inventory | No QA-ready or score-correction PASS without artifacts |
| **K5 Android & evidence accountability** | POL13/14/15; EV04/12; FM15/18; AT04/19 | Design Baseline V0.3, UI-G01..16; ≥2 Android contexts required before pilot | Named environment/versions, accessibility tasks, evidence custodian/QA approver, consent and defect reporting | No Android/accessibility PASS without scoped tests |
| **K6 Option selection & governance** | POL16; EV01..12; FM01..18; ARCH03-A/B/C | Candidates remain equally unselected; no unearned overall winner | Later PO architecture-selection decision based on admissible scope-limited results; *not an execution precondition for every descriptive research observation* | No default selection or ARCH-04/Stage05 Gate |

## IV. Minimal future decision sequence — avoid policy-by-policy churn

1. **Now:** This one consolidated pack identifies **which** POL question binds **which** proposed observation; **no POL value or source is being decided**.
2. **If PO later chooses a particular limited verification objective:** fill **one combined policy-and-execution request** for that objective (the supplied template); use already signed reviewer rules instead of reapproving them.
3. **Only after a separate explicit PO decision:** a named scoped test could run within its allowed environment, content/privacy safeguards, QA and resource limits. A requested PASS additionally needs preapproved criteria and evidence source interpretation applicable to that claim.
4. **Only after signed evidence:** compare ARCH03-A/B/C fairly; any architectural choice, ARCH-04 entry, or Stage05 Gate remains an independent PO decision.

**No automatic loop:** Future files, detailed experiments, or any new decision pack must not be created on the assistant's own initiative after this packet; only explicit subsequent PO instruction may authorize that work.

## V. Not blockers to *every* exploratory observation

- A numeric clock-skew/grace value (POL02) is required for a time-integrity PASS where applicable, **not** for a future separately authorized descriptive observation that expressly forbids PASS.
- Content QA of all 400 B1 items (POL11) remains mandatory before pilot, **not** a prerequisite for a future isolated synthetic-data ACK observation that never publishes content.
- Device selection (POL13), participant consent (POL14) and data-copy inventory (POL10) are **scoped to the requested activity**; privacy and safety permissions never disappear.
- Architecture choice (POL16) cannot be used as a default precondition to force adoption of any one research candidate, although a later executable test may require a separately approved bounded artifact.


**Tình trạng dự án áp dụng cho mọi bảng:** Stage05 IN PROGRESS; ARCH03-A/B/C UNSELECTED; ARCH-04 chưa mở; ECP00..06 PLAN ONLY; EV01..12 document reviewed/0 verified app claims; FM01..18 NOT RUN; QA01..08 actual PASS=0; Android/learners n=0; budget DEFERRED. Không tự mở công việc mới, không đổi các Requirements/Design Baseline.
