# Stage 04 UX-01 — Experience Risks & State Inventory V0.1

**Status:** ANALYST REVIEW DRAFT, not a UI spec.  
Severity reflects analyst prioritization and does not invent actual user test findings.

| ID | Priority | Situation | Unsafe UX failure to prevent | UX-02/03 treatment to compare | Normative trace |
|---|---|---|---|---|---|
| UX-R01 | P0 | Long mock begins | Person does not understand no-pause/no-replay or A/B context | Pre-start clarity without overload | P01..04; FR-010/011 |
| UX-R02 | P0 | Background/process termination | Display resumes mock as valid with reset clock | Invalidation/recovery message with honest time | P05..07; FR-011/019 |
| UX-R03 | P0 | Answer network pending | ‘Saved’ shown before durable confirmation | Saved vs pending vs failed wording | FR-005/019 |
| UX-R04 | P0 | Lost/mismatched Listening audio | Person is trapped in invalid mock or gets wrong item | Unavailable/incident state without false completion | FR-003/015/017 |
| UX-R05 | P0 | Invalid A/B comparison | Result suggests official TOEIC gain | Raw counts, form caveat, valid/non-comparable label | FR-012/013; NFR-007/012 |
| UX-R06 | P0 | Family learner context changes | Another person's history becomes visible | Explicit private context with security-owner dependency | FR-018; NFR-006 |
| UX-R07 | P1 | Long Part 7 | Exhausting scroll and losing passage references | Context-preserving reading alternatives | FR-004; NFR-005/010 |
| UX-R08 | P1 | Small display / large fonts | Passage or table cut, answer touch target tiny | Legibility/accessibility heuristics, two phone contexts | AT-04; QA-08 |
| UX-R09 | P1 | Retry/duplicate submit | Two scorecards for one attempt | Single-finalization and visible in-progress state | FR-011/019 |
| UX-R10 | P1 | Missing verified explanation | Unvetted interpretation presented as fact | Clear 'chưa có giải thích được kiểm duyệt' copy | FR-007 |
| UX-R11 | P1 | QA-rejected form | Unavailable mock falsely looks selectable | State differentiating unavailable/withdrawn | FR-017 |
| UX-R12 | P1 | Content corrected later | Historic attempt score overwritten unnoticed | Version/history correction notice | FR-016 |
| UX-R13 | P1 | First-time learner | No data makes suggestion look authoritative | Explainable first-use fallback and opt-out | FR-014 |
| UX-R14 | P1 | Deletion request | User unsure whether deletion confirmed / exempted | Policy language and status, identity method TBD | FR-018; P09 |
| UX-R15 | P2 | Learner returns from practice | Loses context or accidental mock start | Clear mode label and resumable correct state | FR-002/009 |
| UX-R16 | P2 | More content needed | UI implies auto-PDF importer or AI capability | Restrained copy consistent with OUT MVP | FR-020..023 OUT |

## State semantics to preserve

- **Mock:** `ELIGIBLE_TO_START`, `UNAVAILABLE_CONTENT`, `NOT_STARTED`, `IN_PROGRESS_CLEAN`, `INTERRUPTED_UNCERTAIN`, `INCOMPLETE`, `NON_COMPARABLE`, `SUBMITTED_COMPARABLE`, `TIMED_OUT`; these are **conceptual UX states**, not a prescribed backend state machine. Exact merge/labeling decisions require UX-02 review.
- **Answer:** `SELECTED_UNCONFIRMED`, `PENDING_ACK`, `CONFIRMED_SAVED`, `FAILED_UNSAVED`. Never call the first two durable.
- **Media:** `READY`, `LOADING`, `MISSING_OR_WRONG`, `RETRYABLE_NETWORK`, `BLOCKED_CONTENT`.
- **Content/result:** `QA_READY`, `UNAVAILABLE`, `WITHDRAWN`, `REVISION_AFFECTS_HISTORY`; no assumption that a re-grade feature is in MVP.
- **Privacy:** `OWN_RECORDS`, `UNAUTHORIZED`, `VERIFIED_REQUEST_PENDING`, `DELETION_EXECUTED`, `LAWFUL_EXCEPTION` with user-facing copy only after separate operational policy sign-off.

## UX-01 risk disposition

P0/P1 states listed as **coverage obligations**, not observed defects. UX-02 can decide preferred interaction principles, UX-03 can create screen-level flows after review, UX-04 prototype can conduct usability checks. **No code or architecture decisions.**
