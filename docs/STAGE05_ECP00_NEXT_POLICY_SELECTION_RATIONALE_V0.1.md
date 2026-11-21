# Why POL-07/POL-08 is the First Concrete ECP-00 Policy Candidate — Selection Rationale V0.1

**Status:** PROPOSAL TO PO — not a signed policy rule.  
**Permitted under:** D05-ECP00-008=A: prepare a separately controlled concrete policy decision pack.  
**Cannot be interpreted as:** executing ECP-00..06, selecting a system, implementing an adjudicator, ranking data stores/clock sources, running QA or changing product requirements.

## Why this is the smallest useful policy slice

- `POL-07` asks when two pieces of evidence genuinely corroborate one another, rather than repeating the same hidden source. `POL-08` asks how reviewers should classify contradictory/late evidence, without selecting a clock, ACK authority, weighting algorithm or trusted service.
- Both apply identically to ARCH03-A, ARCH03-B and ARCH03-C, and to timing, ACK, privacy and content claims. They reduce the risk that future documents misstate **multiple logs** as *independent proof* or a **restored screen** as *confirmed continuity*.
- The approved ECP-00 review protocol already demands provenance and inconclusive handling in general; this next decision would formalize a **more concrete per-claim admissibility test** and distinguish *independence demonstrated*, *correlated*, *unknown dependency*, and *contradictory* evidence. It would **not** repeat or modify Full Mock business policy.
- POL-01/02/05 (time and durable-ACK authorities, numeric limits) lack runnable app facts. They should **not be decided now by convenience**; do not fabricate clocks, response delays or storage options to fill them.

## What a PO decision CAN choose at this stage

A future choice can approve a **documentary admissibility policy** that a reviewer must apply when a real, separately authorized evidence set arrives. In particular it can rule out treating copies as independent proof or tallying votes among dependent indicators. This does not assert a source is trustworthy, pick one signal as truth, or certify any future test result.

## What must still be deferred

Every POL-01..16 retains an unresolved implementation/authority/evidence portion until a separate scoped decision. The next PO option A, if selected, would mean **POL-07/POL-08 REVIEW CRITERIA DOCUMENT APPROVED; substantive authority and validation OPEN**, not `CLOSED`. This is a partial, non-executable decision only. No architecture is to be inferred from its name *evidence reconciliation*.

## Decision sequence proposed (not authorized as execution)

1. **D05-POL-009:** approve, amend or hold the POL-07/POL-08 documentary admissibility rules.
2. **Only after PO says so:** prepare separate POL-03/04/06 *uncertain interruption and late ACK* policy wording, or POL-01/02/05 evidence-authority and quantification proposal with actual rationale (not values presumed).
3. **Only with later explicit PO approvals:** determine scoped device/content/privacy QA authorizations, including test data, participants, owners, source-provenance safeguards, and spending restrictions.

**Now:** D05-POL-009 PENDING; ECP-00 reviewed at protocol level; no test run, no technical choice, no extra budget.
