# Development Beta Scope Proposal V0.1 — PO Review Required

**Status: PROPOSAL ONLY.** This document does not amend `D05-DEV-GATE-012=A`, does not authorize CX-04+, and must not be used as a development instruction until a Product Owner approval record identifies the permitted slices and acceptance evidence.

## Recommended bounded direction

Consider a separate Beta authorization for **synthetic Reading accessibility and layout hardening only**. A candidate scope may include clearly specified CX-04+ slices for Compose layout behavior using the already-approved synthetic Part 5–7 fixtures, with no product-policy expansion.

## PO decisions required before authorization

1. Identify the exact new CX slice IDs, signed FR/AT links and Design V0.3 constraints.
2. State which internal engineering evidence is allowed (for example screenshot/render evidence) and which remains formal QA/ECP. Real-device and learner testing need separate authority.
3. Define whether large-font, contrast, TalkBack, rotation and process-death are development targets, documentary risks, or separate QA criteria.
4. Confirm that no durable progress/answer acknowledgement, account, backend/API/remote DB, clock, Full Mock/B1, media, ARCH03 choice or cost is included.

## Explicitly excluded from this proposal

- ECP or formal QA; Android real-device or learner testing.
- B1 items, real Full Mock A/B, audio/media, ETS-equivalence claims or content QA.
- Network, backend/API/remote database, authentication/account, persistent storage, durable ACK, clock authority and ARCH03 A/B/C.
- Any spend or change to the DEFERRED budget.

## Suggested evidence boundary if approved

Require local build/unit-test exit codes, source scope guard, and any specifically authorized render evidence to be recorded separately. Those results must remain engineering evidence only unless a later QA/ECP authorization says otherwise.
