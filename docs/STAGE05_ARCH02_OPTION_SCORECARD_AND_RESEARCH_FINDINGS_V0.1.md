# Stage05 ARCH-02 — Qualitative Comparative Scorecard and Research Findings V0.1

**Classification:** analyst research hypotheses — **not chosen design/stack/architecture**, no actual benchmark or QA score.

## 1. How to read the scorecard

- `Favorable` = conceptual property can directly address one constraint if later evidenced; `Conditional` = cannot infer success without missing proof; `Weak` = material tension with a signed obligation.
- All `Favorable` assessments are **desk hypotheses, NOT test measurements**, and do not outweigh unanswered threat/failure cases.
- Do not add numeric weights, prices, operations costs, technology names or cost estimates while budget work remains PO-DEFERRED.

| Decision axis | Model family | Potential advantage | Most important limitation | Evidence gate | Interim disposition |
|---|---|---|---|---|---|
| Mock time | T-A device-contained | Fewer live-network timing dependencies | Reboot/process loss, tampering, continuity | FM01–04 | CONDITIONAL |
| Mock time | T-B independent corroboration | More external integrity evidence | Network unavailable, reconciliation and privacy | FM01–04 | CONDITIONAL |
| Mock time | T-C multiple signal reconciliation | Detects contradictions; can expose unknowns | More contradictory state complexity | FM01–04 | CONDITIONAL |
| Audio | L-A foreground-bounded | Conservative integrity semantics | More noncomparable interrupted attempts | FM01,05,18 | CONDITIONAL |
| Audio | L-B evidence-based recovery | Better learner continuity possibility | Unintended replay/time advantage risk | FM01,05,18 | CONDITIONAL |
| Answer ACK | S-A device-contained | Local responsiveness possibility | Lost device, isolation, deletion obligations | FM07–10 | CONDITIONAL |
| Answer ACK | S-B independently retrievable | Recovery across app/process possibility | Outage/identity and response latency | FM07–10 | CONDITIONAL |
| Answer ACK | S-C explicit dual-tier state | Strong differentiation of pending vs confirmed | Reconciliation complexity, evidence authority TBD | FM07–10 | CONDITIONAL |
| Learner identity | P-A device-scoped | Simple local pilot usage possibility | Shared-device impersonation and remote deletion | FM09–11 | CONDITIONAL |
| Learner identity | P-B learner authorization | Stronger accountable access path possibility | Setup/identity friction, network dependency | FM09–11 | CONDITIONAL |
| Learner identity | P-C multi-source verification | Can combine user experience and controls | Highest consistency/consent complexity | FM09–11 | CONDITIONAL |
| Content | C-A frozen release | Strong historical form consistency | Corrections/QA process overhead | FM06,12–13 | CONDITIONAL |
| Content | C-B audited revisions | Updates more flexible | Old result meaning threatened if weakly versioned | FM06,12–13 | CONDITIONAL |
| Content | C-C release + amendment evidence | Balances release trace and corrections | Extra governance and proof | FM06,12–13 | CONDITIONAL |
| Results | R-A original-attempt version | Historic scores stable | Separate correction presentation | FM12,14,17 | CONDITIONAL |
| Results | R-B versioned correction view | Corrective reporting possible | Risk of misleading before/after deltas | FM12,14,17 | CONDITIONAL |

## 2. Findings we can safely state now

1. **A device-resident UI clock alone is not sufficient evidence of a clean 120-minute mock** across all lifecycle/reboot/tampering cases; not claiming it is always wrong, but its independent proof is incomplete (E02-01..03).
2. **A choice recorded in UI memory is not durable acknowledgement**. Design copy must reflect an actually verified saving event. Delayed/duplicate/ambiguous acknowledgements remain P0 probes (E02-02; FR-005/019).
3. **Background or interrupted audio cannot be assumed seamless** across target versions/devices. Conservative invalidation vs audited recovery is a separate feasibility and UX question, constrained by no discretionary pause/replay (E02-04..06).
4. **A data-sharing convenience model is not proof of privacy/isolation/deletion compliance**. OWASP and applicable Google Play duties imply negative access/deletion tests (E02-07..10).
5. **Content inventory is not content QA**. Two 200-item forms remain inventoried per PO, while item-by-item integrity, answer key, audio mapping, duplication and rights-release evidence remain for the approved QA checkpoints.
6. **No evidence proves a particular framework, provider, database or clock location is best**: none is being evaluated as a product here. No budget or personnel estimate is authorized.

## 3. Trade-offs that PO might prioritize in D05-TECH-003

| Lens | Value | Cost/risk (qualitative only) | Why no automatic selection |
|---|---|---|---|
| P-A Independent continuity evidence priority | Can surface contradictory elapsed and save claims | May introduce unknown state under outage, added complexity | Exact operational source and threshold undecided |
| P-B Device-contained evidence priority | Reduces continuous network reliance | Untrusted/missing continuity after reboot and shared device risks | No real-device risk proof |
| P-C Independent corroboration priority | External evidence of continuity could improve auditability | Connectivity and private data dependency, latency concerns | No verification of availability or information security |

## 4. Analyst disposition

**RESEARCH DOCUMENTS COMPLETE FOR PO REVIEW; TECHNICAL SELECTION NOT READY.** Recommend **D05-TECH-003=A** only as a **research shortlist priority emphasizing multiple/independent evidence and explicit unknown states**, while retaining the other two models as comparators. A is **not** a framework/provider/server-clock/architecture selection; ARCH-03 must require new scope authorization.

**Uncertainty:** no physical-device tests, user tests, content audit or code proof; signed technical thresholds/grace values are still due at the specified test-plan checkpoint. Stage05 Gate remains unassessed.
