# Stage05 V6.7 — Architecture choices versus evidence responsibilities

**Status:** CONTROLLED ANALYST RECOMMENDATION; NO ARCH03-A/B/C WINNER, no chosen clock/ACK authority, no real testing.

## Distinct decisions that must not be conflated

| Decision | Proposed disposition now | Can Codex begin bounded UI work? |
|---|---|---|
| Android client UI toolkit | Kotlin/Compose recommended as reversible engineering default | Yes, after signed development authorization |
| State/event/domain layering | Separate UI from evidence/identity/content ports (reversible) | Yes, after signed development authorization |
| ARCH03-A Device primary | Unselected, no verified reboot or tamper trust | Yes; UI fixture does not choose A |
| ARCH03-B Independent-led | Unselected, no verified outage / late ACK proof | Yes; UI fixture does not choose B |
| ARCH03-C Reconciled evidence | Unselected, no independent provenance or arbitrator proof | Yes; UI fixture does not choose C |
| Timestamp / clock authority | OPEN, no default source/threshold | UI can label 'unknown'; cannot declare clean mock |
| Durable ACK and learner ownership authority | OPEN, no provider; signed P05–P08 reviewer rules only | UI can model uncertainty; cannot claim remote durability |
| Backend/remote API/database/auth provider | OPEN | UI and read-only synthetic practice shell only |
| Data-retention enforcement | Business rule signed, implementation unverified | Do not claim working deletion |

## Conservative behavior across all candidates

1. Mock losing critical time/audio continuity ⇒ `INCOMPLETE` or `NON_COMPARABLE` when integrity cannot be established; never silently clean, reset, pause or replay.
2. ACK missing, duplicate/conflicting or arriving late ⇒ preserve UNKNOWN until suitable evidence; source precedence is NOT assumed.
3. Don't present fake TOEIC forms or unvetted keys as QA-READY; B1 2×200 required before pilot, inventory has been affirmed by PO but not QA-checked.
4. No personal learner data, real test accounts, collected audio, vendor credentials or live service calls in the first Codex slice.
5. Every implementation/test result must identify whether synthetic, local, device real, server, QA reviewed, and what claim it can prove.

## Evidence gates before potentially consequential work

- Development UI shell may use synthetic data ONLY, with explicit PO authorization for the bounded coding step.
- Real answer durability, clock integrity, authentication or privacy cross-user logic require a scoped policy and test plan approval based on the 9-field evidence contract in the signed `STAGE05_MINIMUM_EVIDENCE_AND_READINESS_GATE_V0.1.md`.
- Full Mock pilot availability requires QA of all essential A/B items, media and answer keys, plus actual device/integrity/privacy verification and PO pilot/release approval.

**Not a hidden architecture design**: these are review boundaries and ports for future reversible work; no diagrammatic placement of trust authority or mandatory cloud components is decided here.
