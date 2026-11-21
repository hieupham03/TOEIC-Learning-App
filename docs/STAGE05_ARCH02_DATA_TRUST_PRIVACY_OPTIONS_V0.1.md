# Stage05 ARCH-02 — Durable Answer Trust, Identity, Privacy & Deletion: Comparative Models V0.1

**Status:** Analytic comparison ONLY; no persistence/provider/account/database scheme, endpoints or implementation chosen.

## A. Signed trust semantics

- Selection of A/B/C/D by the learner is **not equal** to a saved answer. `PENDING`, `ACKNOWLEDGED`, `UNCONFIRMED/UNKNOWN` must have truthful screen copy (Design Baseline V0.3); no invented acknowledgement.
- A confirmed answer must survive relevant interruption within approved reliability criteria. Retrying must not create a second counted answer/attempt or incorrectly report success.
- Two to five family learners' private data must be separated; verified deletion within **7 calendar days**, ordinary retention **no longer than 30 days after the pilot** without a separately allowed exception/consent.
- Account model and any Play distribution dependencies remain unchosen. No assumption that “online-first” means permanent network availability.

## B. Compare durability evidence concepts

| Model | Claim that could justify `Đã xác nhận lưu` | Strength | Major risk / constraint | Evidence required |
|---|---|---|---|---|
| **S-A Device-contained durable confirmation** | A durable, user-bound record is demonstrably retained on the device | May allow quick confirmation and limited connectivity dependency | Device loss/reinstallation, shared device privacy, cross-device access, uncertain ability to fulfill remote deletion expectations | Kill/restart, power cycle, reinstall, account switch, device loss, export/deletion checks |
| **S-B Independently retrievable confirmation** | A durable record is confirmed from a recoverable service/responsibility outside the active UI/process | May help recovery across process/device loss | Connectivity needed at confirmation; slow/unavailable responses; identity/access requirements | Request lost before/after confirmation; duplicate retry; unauthorized learner access; outage |
| **S-C Explicit dual-tier acknowledgement** | Display separately distinguishes temporary local selection from later authoritative durable confirmation | Best semantics for pending vs confirmed when connectivity intermittent | Multi-state UX and reconciliation more complex, choice of authority unresolved | Out-of-order ACK; temporary-only selection; duplicate operations; conflicting confirmation |

**These are competing evidence obligations**, not an approved local/cloud/hybrid architecture or design suggestion. Never label temporary retention as durable saved unless validated to the signed standard.

## C. Recovery & ambiguous retry invariants

| Failure case | Required user-facing truth | Test observation needed later |
|---|---|---|
| Selection exists but confirmation request pending | `Đang xác nhận` or equivalent, NOT `Đã lưu` | Synthetic delayed confirmation then restore |
| Confirmation outcome lost | `Chưa thể xác nhận`; retry without implying duplicate | Ambiguous response after a durable commit |
| Confirmed answer followed by app kill | Previously confirmed state retained | Reopen same learner + item + form/version |
| Multiple retries / duplicate delivery | Only one logical confirmed answer per intended answer version; history not distorted | Replay same intent multiple times |
| Learner switch on shared phone | No access to another learner's attempts/history | Cross-account switch while pending/out of network |
| Account/identity disagreement | Do not accept deletion or sharing without appropriate verification | Negative access and deletion-request tests |

## D. Compare access isolation concepts

| Model | Boundary concept | Trade-off to verify | Not decided |
|---|---|---|---|
| **P-A Device-profile scoped identity** | Delimit each learner within one device context | Shared-device impersonation risk, deletion when device lost | Login/account screen, cryptographic/isolation mechanism |
| **P-B Independent learner-authorized identity** | Each learner verifies own access to history and deletion | Network/identity friction for family pilot, handling recoverability | Identity provider or account architecture |
| **P-C Explicit hybrid evidence** | Local usage convenience plus separate authorization/evidence for sensitive actions | Multiple roles and synchronization risk | Data access topology and technical design |

No model automatically passes user privacy/security controls. OWASP MASVS requires protecting sensitive storage; Google Play account-deletion obligations apply **conditionally if account creation is provided in the app** (E02-07/08/09/10). Neither fact authorizes an account provider selection.

## E. Deletion/retention obligations independent of implementation

- Specify request channel and verified-request time, request status, completion proof and documented lawful exceptions **before pilot use**.
- The **≤7 calendar day deletion target** is signed. Do not extend it due to technical convenience or require an invented user consent.
- The **≤30-day ordinary post-pilot retention** is signed; compare historical progress benefits without silently overriding this rule.
- Test whether a claimed deletion has also removed or appropriately handled all copies within the future approved data model. The statement is an acceptance requirement, not proof that backups/caches/replicas have been handled.
- Do not assume family administrator may read family members' private results unless signed requirements permit it.

## F. Interim finding

All S/P model families need explicit evidence-of-ACK and identity handling. **No family wins without tests**. The recurring P0 risk is *false positive durability*, not only data loss. Android UI-state preservation guidance (E02-01/02) does not itself establish durable answer persistence.
