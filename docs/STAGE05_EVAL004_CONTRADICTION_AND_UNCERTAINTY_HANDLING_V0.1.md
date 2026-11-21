# Stage05 — Contradiction and Uncertainty Desk Classification V0.1

**Status:** analyst review vocabulary, **NOT** a runtime enumeration, persistence state machine, selected API protocol, architecture, automatic policy change or implemented UI copy.

## 1. What counts as documentary uncertainty

| Class | Example from authorized EV/FM review | Why decisive proof is absent | Conservatively supportable interpretation | Do not infer |
|---|---|---|---|---|
| `ABSENT` | No elapsed evidence after reboot (EV-03/FM-03) | Time since boot cannot establish lost interval | Mock validity unproven pending approved handling; do not silently reset clock | Clean comparable attempt |
| `CONFLICTING` | Device clock and another duration account disagree (EV-01/FM-04) | No authority or tolerated skew chosen | Flag contradiction; require future policy/verification | Highest or lowest clock must win |
| `DELAYED` | Answer ACK arrives after user retries (EV-06/FM-08) | Event order and durability not validated | Leave outcome unconfirmed until supporting evidence obtained | Retry is a new answer or first write failed |
| `AMBIGUOUS` | ACK missing though write may have succeeded (EV-06) | Response loss is not write outcome | Cannot-confirm state; avoid false success and false failure | Automatic safe retry guaranteed |
| `STALE` | Content key/version changed after an attempt (EV-10/FM-12) | Old score's context may differ from new key | Preserve original meaning and show correction transparently if later approved | Retroactive edit without audit is valid |
| `WRONG CONTEXT` | Pending answer appears after family learner switch (EV-07/FM-09) | Identity/form association not proved | Withhold other learner's information; require authorization evidence | Current device user owns pending answer |
| `INCOMPLETE COVERAGE` | Deletion reported but backups/copies unknown (EV-08/FM-10/11) | Not all in-scope copies/exception mapping evidenced | Do not certify completion; signed time bounds remain | Mark deletion completed based on one location |
| `NON-RELEASE` | Audio or answer explanation not QA-ready (EV-09/FM-06/16) | Per-item QA not performed | Block content from pilot; explain unavailable state | PO-inventoried means QA-ready |

## 2. Claim status versus user-facing status

**Desk labels are evaluator classifications**, not a UI state schema. Signed UX rules remain binding, including `đang xác nhận`, `đã xác nhận`, `chưa thể xác nhận` for answer save semantics and explicit clean / incomplete / not-comparable conditions for a Full Mock. The exact mapping in a runtime product depends on future authorized design/implementation and acceptance thresholds. Never translate a `DOCUMENT CLAIM SUPPORTED` note into a green Saved or PASS signal.

## 3. Four disambiguation rules for later review

1. **Source provenance:** First confirm same user, form, item, attempt and content version, not merely similar timestamps or labels.
2. **Temporal scope:** Distinguish missing observation, delayed observation and contradictory observation. Avoid turning `not observed` into `false` or `true`.
3. **Negative cases:** Cite an explicit FM falsifier. A qualitative claim is not defensible only because an optimistic normal-flow story sounds plausible.
4. **Approval boundary:** Business-critical grace periods, policy exceptions, clock evidence authority, identity boundaries and persistent acknowledgment rules cannot be invented in this desk pass. Refer each to its later PO-controlled checkpoint.

**Empirical observations made in this exercise:** none. The contradictions are hypothetical **review cases**.
