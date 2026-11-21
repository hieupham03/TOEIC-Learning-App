# POL-05 / POL-06 — Answer Evidence Hypothetical Casebook V0.1

**Status:** ILLUSTRATIVE ONLY; prepared for D05-POL-010. No test/device/user run. All real FM retain NOT RUN.

| Case | EV/FM / dependency | Hypothetical observation | Review disposition if a future separately authorized run existed | Unsupported inference to reject |
|---|---|---|---|---|
| HC-ACK-01 | EV-05/FM-07; P05-R2 | Learner taps option, UI renders `Đã lưu`, but persistence observation absent | Durable saved claim **not demonstrated**; review UI-copy mismatch | Button click proves durable write |
| HC-ACK-02 | EV-06/FM-08; P06-R1 | Storage may have succeeded; response disappears during network loss | **INCONCLUSIVE** if signed run, otherwise NOT RUN | Missing response proves failed transaction |
| HC-ACK-03 | EV-05/FM-07; P07-R3 | Two panels show `đã lưu`; both from same unverified source | Correlated evidence; no independent proof | Two panels mean two independent ACKs |
| HC-ACK-04 | EV-06/FM-08/FM-14; P06-R2 | A retry appears successful but a second logical answer exists | Preserve potential duplicate falsifier; later bounded FAIL only if verified | Two responses mean legitimate repeat success |
| HC-ACK-05 | EV-06/07/FM-09; P06-R3 | ACK arrives after switching between two family learners | Original owner not established ⇒ learner/attempt binding unresolved | Active UI learner owns delayed answer |
| HC-ACK-06 | EV-06/FM-14; P06-R3 | Learner revises answer while an earlier ACK remains in flight | Preserve version/order ambiguity; need separately accepted evidence | Most recent delivered message is authoritative |
| HC-ACK-07 | EV-02/05/FM-02; P05-R2 | Android restores a previously selected answer after process reclaim | Restored presentation does not establish persistence | Saved UI state equals durable ACK |
| HC-ACK-08 | EV-05/06/FM-07/08; P06-R4 | One log says committed, another says missing; same artifact lineage unclear | Apply P07 source classification/P08 conflict escalation; no optimistic PASS | Majority of matching logs overrides falsifier |
| HC-ACK-09 | EV-05/FM-07; P05-R1 | Storage proof exists but bound to another attempt or form | Does not prove the **requested claim**; verify scope | Any durable record counts for current attempt |
| HC-ACK-10 | EV-06/FM-08; P06-R1 | A hypothetical receipt arrives minutes after an error notice | Preserve chronology and unknown status until authoritative binding is approved | Response arrival alone proves eventual user-facing `Đã lưu` |

These are conceptual reviewer walkthroughs only. They neither set grace periods nor choose source-of-truth, retry behavior, backend/API/database or clock authority. No QA PASS, architecture promotion or ECP execution results are created.
