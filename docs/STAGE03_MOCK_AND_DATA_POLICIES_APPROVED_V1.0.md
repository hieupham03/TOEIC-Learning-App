# S2-A — Approved Mock, Scoring and Pilot Data Business Policies V1.0

**Decision:** D03-SCOPE-009 = APPROVED S2-A. **Policy-level approval**; technical details and actual test evidence remain open.  
**Scope:** Full Mock, practice, raw results, user privacy — no UI or system design.

| Policy | Approved normative behavior | Evidence/verification | Valid residual TBD |
|---|---|---|---|
| P01 Exam vs practice | Evaluative Full Mock has attempt-integrity requirements. Part/one-item study is flexible and independently reported. | AT-09..11,13 | Media asset delivery method, no UI mandated |
| P02 Time and section | 100 Listening items in ordered audio (~45m), then 100 Reading items in 75m. Listening playback completes segments per form rules, not indiscriminately truncated at minute 45. Visible expiry/end/transition behavior consistent. | AT-10,11 | Device clock tolerance/edge timing test design before test-plan baseline |
| P03 Pause | No discretionary timer pause for a full mock presented as clean/comparable. If accommodations or practice pause are offered, affected attempt is not labeled clean comparable by default. | AT-11,13 | Accessible alternatives can be analyzed without falsifying validity |
| P04 Audio replay | No learner-initiated arbitrary repeat/rewind in comparable evaluative Listening. Practice playback may permit replay. | AT-03,11,13 | Content-embedded mandated replay/order where actually present in form |
| P05 Background/outage | Preserve every acknowledged answer. Never silently restart exam time. If audio/timing integrity materially disrupted or cannot be established, flag **INCOMPLETE / NON-COMPARABLE**, not comparable. | AT-05,11,19 | Numerical grace/tolerances only if integrity rule preserved; due test-plan gate |
| P06 Durable acknowledgement | Report an answer `saved` only with confirmed durable acknowledgment; otherwise expose pending/uncertain state and recovery route. Online-first does not promise full offline use. | AT-05,19 | Numeric save latency/retry/recovery targets at test-plan gate |
| P07 Finalization | Submit/timeout/quit are distinguishable. No duplicate finalized result. Blank answers remain blank. Early/assisted attempt cannot silently count as clean comparison. | AT-11,12,19 | Precise accessibility/accommodation classification approved before corresponding release |
| P08 Score, comparison, version | Count correct/attempted/unanswered per Part, section L/R and total with form/attempt/version/date and integrity label. Exclude/flag exposed and noncomparable attempts in clean trend. **No ETS official-scale equivalence claim.** Key edits auditably affect history, no silent recompute. | AT-12,13,16 | Specific recalculation/appeal workflow needs product rule before such content corrections are released |
| P09 Family data, deletion | Minimal learner data, isolation, transparent access and deletion process. **Delete on verified request within 7 calendar days** subject to applicable lawful retention exceptions. **Routine retention max 30 days after 4-week pilot** unless explicit further agreement/valid exception. | AT-01,08,18 | Concrete login/identity verification and lawful exception mapping must be settled before pilot, not architecture chosen here |

## Attempt integrity categories (approved principles; labels may be refined without changing meaning)

- **COMPLETE — COMPARABLE:** all applicable form and timing/integrity requirements satisfied, no prior exposure/assistance that invalidates clean comparison; no guarantee forms are psychometrically equated.
- **COMPLETE — NON-COMPARABLE:** learner finished/ended but replay, pause, exposure, exceptional timing, audio disruption or other recorded factor makes clean comparison invalid; can display raw practice results with warning.
- **INCOMPLETE:** quit, unresolved timeout/section, missing necessary content, or insufficient attempt completion; display only factual progress/status, not clean comparison result.
- **UNAVAILABLE/BLOCKED:** form/item fails content QA and cannot be represented as eligible mock.

No technical algorithm, storage platform or authentication flow approved by these categories.

## Sensitive edge cases and ownership

1. **Time:** no silent reset or stop; every section transition must avoid cutting ordered required audio. Exact tolerance documented and approved in later QA test plan; in doubt do **not** mark comparable.
2. **Connectivity:** pre-ack network loss cannot be described as safe persistence; recovery reports last confirmed state, not invented success.
3. **Changing answer key:** preserve source/form/key version of earlier result; show if under review. A separate recompute/appeal policy must be approved before automating any change to historical score.
4. **Privacy:** 7 days is from validation of deletion request; 30 days from ending the four-week pilot for routine personal study data, not automatic release-specific extension. Necessary legal exceptions must be explained and tracked; account deletion conditions of distribution platform reviewed when applicable.
5. **Pilot participant protection:** don't share one participant's history or data with another; access permissions must be specified at test-plan/pilot-readiness checkpoint.

**Do not silently reinterpret numeric privacy limits or integrity labels in implementation.** Any material business-rule change returns to Product Owner for formal change control.
