# Stage05 — Evidence, Contradiction & Uncertainty Review Matrix V0.1

**Classification:** example claims to *review later*, **NOT** selected architecture, software contract, measured behavior, or new signed business rule.  
**Authority:** D05-TECH-003=A approved creation of this evaluation-brief aid only.

| Ref | Claim under review | Conflicting / absent evidence scenario | Truthful interpretation for future review | Falsifier / relevant signed guard | Verification status |
|---|---|---|---|---|---|
| EV-01 | Mock elapsed time consistent | Device clock reconfigured mid-form | Cannot silently allow extra time; reconcile or retain uncertain/noncomparable | FM04, FR010/011/019 | NOT TESTED |
| EV-02 | Mock continuity over process loss | App dies, UI returns but continuity proof absent | Restored screen ≠ proven valid mock | FM02, QA08 | NOT TESTED |
| EV-03 | Mock continuity over reboot | Device restarts with missing duration history | No clean/comparable claim without support | FM03, AT11 | NOT TESTED |
| EV-04 | Audio intact and in order | Audio focus loss, partial replay or resumed media offset | Distinguish audio experience from clean-mock evidence | FM01/05/18, QA03/08 | NOT TESTED |
| EV-05 | Answer confirmed saved | Choice selected, reply still pending | **Pending**, not confirmed | FM07, FR005 | NOT TESTED |
| EV-06 | Answer saved after retry | Write may have succeeded but ACK was lost | **Cannot yet confirm** until reconciled; retry must not double count | FM08, AT05 | NOT TESTED |
| EV-07 | Family data isolated | Learner A logs out while a pending operation exists | No access/credit to learner B without authorization | FM09, FR018 | NOT TESTED |
| EV-08 | Deletion fulfilled | Request marked done but copies may remain | Proof/exception needed; signed 7-calendar-day bound applies | FM10/11 | NOT TESTED |
| EV-09 | Released content valid | Audio mismatch or unknown key QA | Content not releasable until actual QA | FM06/12/16, QA01..06 | NOT TESTED |
| EV-10 | Historical raw score truthful | Key corrected or submission duplicated | Preserve version/attempt context, no silent overwrite/duplication | FM12/14/17, QA07 | NOT TESTED |
| EV-11 | Mock item independence | Practice bank overlaps mock A/B | Restrict release until duplicate/overlap QA | FM13, QA05 | NOT TESTED |
| EV-12 | Reading context preserved | Enlarged text or background loses anchor | Needs actual Android UX confirmation | FM15, UIA/UX04-I | NOT TESTED |

### How to use (future reviewers)

1. Refer to each `EV-*` only as a **review question**; never mark a result PASS based solely on this table.
2. Distinguish **missing**, **contradictory**, and **genuinely disproven** evidence; do not equate timeout with durable failure.
3. Mark the actual later owner/checkpoint from FM-01..18. Do not invent implementation logging, persistence schema, events or API responses here.
4. Maintain all three conceptual families as challengers. Even a reconciliation-heavy explanation can fail when no independent proof is available.
5. Any new threshold affecting a learner's mock validity requires the separate approved decision channel and acceptance control; this matrix is not policy amendment.

**Current status:** 12 review claims defined, zero executions and zero independently verified results.
