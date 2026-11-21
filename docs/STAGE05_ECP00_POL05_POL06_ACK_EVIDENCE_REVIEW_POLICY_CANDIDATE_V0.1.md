# POL-05 / POL-06 — Durable Answer-ACK and Late/Unknown Evidence Review Policy Candidate V0.1

**Status:** **CANDIDATE / PENDING D05-POL-010**. NOT SIGNED. This is a review-scope document, not a persistence design, API, data schema or code.  
**Preparation authority:** D05-POL-009=A explicitly allows only a **reasoned next specific policy decision packet**.  
**Why a packet is warranted:** D05-POL-009 approved how reviewers classify origin and contradiction (P07/P08), but **ECP-02** cannot define a credible claim-to-proof boundary for *durable saved answers* and *lost/late ACK* while POL-05/06 documentary interpretations remain unreviewed. The already-signed UI rule forbids `Đã lưu` without durable ACK, and an absent ACK must not be interpreted automatically as success or failure. The packet supplies decision-ready evidence criteria **without selecting an ACK source, storage technology, retry mechanism or running a test**.

## Context is inherited, not newly decided

- Signed B1 two separate 200-item Full Mock forms A/B; practice Part1–7 separate; maintain learner/form/attempt/item/version context where applicable.
- Preserve already-acknowledged answers and truthful pending/unknown/confirmed UI states; user actions, screen recovery and response delivery alone do not prove durable answer persistence.
- Signed P07-R1..R3/P08-R1..R4 apply to evidence provenance and contradictions; they do not confer correctness or authority by themselves.
- All quantitative timings, retry counts, quorum/precedence, device/backend/database choice, identity design and actual proof remain unresolved.

## Seven *proposed* bounded documentary review rules — none is approved by this file

| Rule | Proposed reviewer discipline | Mandatory trace | Decision explicitly NOT made |
|---|---|---|---|
| **P05-R1** | Limit each `saved/acknowledged` claim to the **specific learner, test form, attempt, item, answer version**, where applicable, and the signed requirement. | FR/AT + EV-05, FM-07; P07 provenance classification | No ID or storage schema, no API, no identity-provider selection |
| **P05-R2** | Do **not** infer durable persistence from tapping an answer, optimistic UI, restored screen, an unverified response, or copies of one log. | Record exactly which independent/durable observation would need **separate PO approval** before an eventual positive verdict | No authoritative ACK event, host, service, local/remote priority, test PASS |
| **P05-R3** | Classify presentation claim as `đang xác nhận` / `đã xác nhận` only when evidenced / `chưa thể xác nhận`; label review proof `not demonstrated` when no admissible observation exists. | Show state-to-claim mismatch and required verification; protect signed approved UI copy | No automatic UI state machine or persistence implementation |
| **P06-R1** | An absent, delayed or lost ACK is **UNKNOWN**, not automatically committed or failed; record timing/context without inventing grace. | EV-06, FM-08, P08-R2 | No clock authority, retry timeout, elapsed limit or assumed failure |
| **P06-R2** | A `retry succeeded without duplicate logical answer` claim requires later proof of both the intended logical answer and all relevant effects; duplicated screenshots/messages alone cannot establish deduplication. | FM-08/FM-14, dependent provenance and relevant bounded observation | No idempotency key design, dedupe algorithm, API or database |
| **P06-R3** | Late observations after learner switch, attempt closure or answer revision must be **reviewed against original context**; otherwise keep ownership/ordering unresolved. | EV-06/EV-07, FM-09/FM-14, privacy obligations | No session model, conflict resolution algorithm or live merge behavior |
| **P06-R4** | Materially contradictory save/retry evidence is preserved and escalated according to approved P08 rules; one positive receipt cannot outweigh a credible falsifier by arithmetic majority. | Original negative artifact, applicable scope, evidence owner and separate PO policy approval where needed | No automatic arbitration or product-wide FAIL/PASS |

## Open questions and required future proof (not yet authorized)

| Open question | What future bounded evidence must establish | Present status |
|---|---|---|
| What observation proves a *durable* answer? | Separately signed source/authority and test conditions, not assumed from a UI response | POL-05 OPEN |
| How is a late/lost ACK correlated with the original answer? | Bound learner/form/attempt/item/version and actual proof in an authorized run | POL-06 OPEN |
| How are duplicate effects ruled out? | Signed acceptance and future falsifier including retry and answer modification | POL-06 OPEN |
| How is wrong-learner attribution avoided on shared device? | Separately authorized privacy/identity proof under POL-09 | POL-09 OPEN |
| What happens if sources disagree? | Already approved P07/P08 *documentary* handling + future signed authority/proof | POL-07/POL-08 residual OPEN |

## Verdict taxonomy and limitations

All **FM-01..18 = NOT RUN** today. A future signed run blocked by a missing authority/policy is `BLOCKED`; an authorized run with material missing/conflicting proof may be `INCONCLUSIVE`; `FAIL`/`PASS (bounded)` require later execution and properly signed criteria. No hypothetical examples can be reported as tests or as application correctness proof.

**Approval semantics if PO later selects D05-POL-010=A:** the seven proposed rule IDs become a **controlled documentary *review* policy only**, while POL-05/POL-06 authoritative durability source, matching/ordering, numeric acceptance criteria, empirical proof and implementations remain OPEN. It must not be read as authorization for ECP-02 execution, architecture selection or code.
