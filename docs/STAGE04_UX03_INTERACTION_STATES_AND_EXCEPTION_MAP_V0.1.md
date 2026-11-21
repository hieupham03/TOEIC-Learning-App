# Stage 04 UX-03 — Interaction State & Exception Map V0.1

**Status:** proposal-only UX content model; not architecture, implementation state machine or QA results. UX copy examples are not signed final strings.

## State sets (conceptual/user-facing)

| Journey | States to distinguish to learner | UX invariant / forbidden transition | Related acceptance |
|---|---|---|---|
| Practice answer | unselected → selected → pending confirmation → acknowledged; failed pending visible | Unconfirmed must never display saved; retry not falsely merged | AT-05,19 |
| Mock availability | QA-cleared/available vs checking/unavailable/withdrawn | Not-ready form cannot launch as clean evaluative attempt | AT-10,15,17 |
| Mock phase | rules/consent → Listening → Reading → submit/timeout → result | No arbitrary pause or listening replay in clean mock | AT-03,10,11 |
| Mock integrity | clean/eligible → unclear → non-comparable/incomplete (as applicable) | Unknown interruption cannot be silently restored as clean | AT-11,13,19 |
| Result | complete/comparable; complete/noncomparable; incomplete; timeout; withdrawn audit | Do not imply equated ETS certification or automatic historic recalc | AT-12,13,16 |
| Practice feedback | answer accepted → key → vetted explanation or missing → learner chooses next Part | No forced recommendation, no fabricated explanation | AT-06,07,14 |
| Content relationship | passage/figure group → relevant question → return to group & last position | No dropped figures or loss of matching passage on Reading | AT-04 |
| Family data | own history / denied access / verified deletion requested / executed / exception | No cross-person exposure; 7 day/30 day policy follows baseline | AT-08,18 |

## Edge cases for PO review of UX clarity only

- **UX-E01:** User leaves during Listening: explain integrity state and acknowledged answer boundary; do not offer an unapproved pause.
- **UX-E02:** App process dies after selecting but before save acknowledgment: distinguish last durable answer vs pending; no guarantee of data that was not confirmed.
- **UX-E03:** Source question/key/audio withdrawn: suppress playable clean attempt, preserve auditable outcome history and notify when it materially affects old result; do not invent recalculation feature.
- **UX-E04:** Part7 multi-passage/embedded table: preserve matching question and last useful scroll position across return.
- **UX-E05:** User tries to inspect explanations mid-mock: provide no answers before the attempt ends.
- **UX-E06:** Raw scores A/B differ: present version/date and caveat; no claim official score gain/equivalence.
- **UX-E07:** Second family participant accesses a shared phone: user-specific data not mixed; account mechanism TBD, do not choose authentication method.
- **UX-E08:** Verified deletion request: state acknowledged/processing/completed/exception; demonstrate 7-day window and retention policy without inventing support channel.
- **UX-E09:** Practice bank item overlaps a protected Full Mock: content readiness QA issue, not a UI permission to expose the item.

## UX flow coverage versus mandatory later QA

UX-03: each P0/P1 state needs user-understandable label and path in low-fi. UX-04: prototype to verify comprehensibility/reading ease. Later: item-level QA-01..06 and Android/software QA-07..08 must be ACTUALLY RUN before pilot. These documents provide neither pass evidence nor a technical design.
