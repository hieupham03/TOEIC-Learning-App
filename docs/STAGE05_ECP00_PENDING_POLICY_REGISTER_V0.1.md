# ECP-00 — Inherited Rules vs Undecided Policy Register V0.1

**Status:** REVIEW QUESTIONS ONLY — unresolved items are not approved, estimated, priced or implemented.  
**Owner:** future Product Owner policy decisions; later QA/privacy roles require separately authorized assignment.  
**Rule:** if an unresolved decision affects a future PASS/clean/confirmed verdict, its evidence checkpoint is **BLOCKED** until a signed decision exists.

| ID | Domain and EV/FM links | Binding inherited rule | Decision NOT YET MADE; evidence needed before policy signoff | Effect until signed |
|---|---|---|---|---|
| POL-01 | Mock elapsed-time origin; EV01/03 FM03/04 | Mock time fidelity and non-deceptive clean/comparable status | Identify any acceptable authority/observations across reboot, manual clock change; no preferred local/remote/hybrid source | Time-continuity PASS blocked |
| POL-02 | Skew, drift, grace; EV01/03 FM03/04 | No invented grace, no arbitrary clean-mock pause | Approve justified quantitative criteria only with future bounded applicability; **no numbers proposed now** | Numeric clock judgments blocked |
| POL-03 | Interruptions; EV02/04 FM01/02/05/18 | No voluntary pause/replay in clean mock | Clarify evidence sufficient to distinguish legitimate interruption vs invalid/noncomparable/unknown without changing business policy | Clean verdict blocked if ambiguous |
| POL-04 | Listening sequence; EV04 FM01/05/18 | Audio progression integrity mandatory | Define acceptable observation/provenance for play progress/focus/background, then later Android applicability | Listening proof blocked |
| POL-05 | Durable ACK; EV05 FM07/02 | `Đã lưu` only after genuine durable confirmation | Define proof standard and future owner, independently of where data is kept | `Đã lưu` cannot be asserted from a UI action |
| POL-06 | Lost/late ACK & retry; EV06 FM08/14 | Missing ACK = `chưa thể xác nhận`, not default FAIL | Later adjudication of retries, ordering, binding and duplicate logical submissions | Retry success unverified |
| POL-07 | Corroboration independence; EV01/05/06 FM03/08 | No unearned confirmation from copied evidence | Define what counts as independent, provenance and known dependency; no forced two-source architecture | Independent confirmation unverified |
| POL-08 | Conflict handling; EV01..08 FM03/04/08/09 | Contradiction means INCONCLUSIVE in review | Identify who may resolve specific conflicts, what new evidence required; no authority hierarchy presumed | Contradictory claim stays unknown |
| POL-09 | Learner identity; EV07 FM09 | Family data must remain separate | Later proof of learner/form/attempt identity under switching and pending saves | Learner-isolation PASS blocked |
| POL-10 | Data copies and deletion; EV08 FM10/11 | Verified delete ≤7 calendar days; routine post-pilot retention ≤30 days except recorded valid exception | Identify future copies, backup/exceptions, audit evidence and applicable consent; not choose database | Privacy evidence incomplete |
| POL-11 | Release and B1 QA; EV09/11 FM06/13/16 | Two PO-inventoried independent Full Mocks, practice bank separate, QA01..08 no PASS | Later content-QA artifacts/owners; do not reopen inventory or rights | Content release cannot be certified |
| POL-12 | Raw score provenance; EV10 FM12/14/17 | No official ETS equivalence; history must retain meaning | Future treatment of corrected keys and per-version score evidence | Historical score PASS blocked |
| POL-13 | Android target context; EV04/12 FM15/18 | Design V0.3 and UI-G01..16 apply | Specify later authorized real Android versions/large-text contexts and owner; no target choice now | Device/accessibility claims unverified |
| POL-14 | Real-user/privacy consent; EV07/12 FM09/15 | Family privacy and user data rights apply | Later scope and consent/handling of any participants/actual personal data | Learner testing unauthorized |
| POL-15 | Evidence record and retest; all EV/FM | Plan-approved outcome vocabulary and stop rules apply | Later artifacts, signed owners, appeal/retest, exception/provenance paths | No bounded PASS without artifacts |
| POL-16 | Architecture authority; all EV/FM | ARCH03-A/B/C unselected; ECP-06 equal comparison | Separate future PO architecture selection only after actual evidence or explicit unresolved blockers | All candidates unselected |

## Questions grouped for a future PO policy decision — not asked for answers in this turn

1. **Mock truth:** What would count as sufficient evidence to certify elapsed time and Listening continuity across reboot, process loss, source conflict and audio interruption?
2. **Answer truth:** What *observations* establish a durable ACK bound to the correct learner/form/attempt/item, and how should unknown/late results be presented?
3. **Evidence independence:** How may a reviewer tell corroboration from duplicate dependent reports, and when must a result remain inconclusive?
4. **Privacy & content:** What future logs/copy inventories/deletion proof, item QA and score-history evidence would satisfy the *already signed* business duties?
5. **Test boundary:** Which target/version, scope, consent and QA owner could be authorized **later**, without architecture choice or reopened budget assumptions?

**Hard limit:** This register does not set time numbers, data-copy inventory, data model, protocol, authority source, candidate score, deployment target, implementation or execution permission.
