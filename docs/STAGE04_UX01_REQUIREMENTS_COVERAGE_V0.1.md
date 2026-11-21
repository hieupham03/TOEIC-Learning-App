# Stage 04 UX-01 — Journey ↔ Requirements Coverage V0.1

**Status:** ANALYST INVENTORY, NOT UX APPROVAL. Authority: signed SRS V0.6 and Acceptance V0.4, no changes.  
**Rule:** Mapping an item to a planned UX touchpoint is NOT a validated interaction flow, implemented feature or QA PASS.

## A. IN MVP functional requirements: explicit 19/19 mapped

| FR | Core UX touchpoint or boundary | Journey(s) | AT | UX-specific state/risk |
|---|---|---|---|---|
| FR-001 | Participant goal, self-reported level and time preferences | J01,J02 | AT-01 | Empty/updated preferences; family isolation |
| FR-002 | Choose QA-ready Part practice, not exposed A/B test bank | J02,J03 | AT-02 | Empty/withdrawn practice pool |
| FR-003 | Correct Listening group and appropriate play controls by mode | J03,J04 | AT-03 | Missing audio, forbidden mock replay |
| FR-004 | Complete Reading multi-passage/context and question relation | J03,J04 | AT-04 | Long scroll; clipped illustration/table |
| FR-005 | Answer selection + truthful durable save status | J03,J04,J05 | AT-05,19 | Pending/uncertain; return to item |
| FR-006 | Key-validated grading, not silent missing key | J06 | AT-06,12 | Score unavailable pending content correction |
| FR-007 | Verified key; explanation when curator-approved; absence disclosed | J06 | AT-07 | No verified explanation |
| FR-008 | Own attempts/error history | J06,J08 | AT-08 | Empty history, wrong participant |
| FR-009 | One-question and Part session without pretending official mock | J02,J03 | AT-09 | Early end / no suggestion |
| FR-010 | Mock A/B start eligibility, two 200-item forms | J04,J09 | AT-10 | One form not QA-ready; never auto-remove B1 |
| FR-011 | Mock time, ordered audio, submission, timeout, integrity | J04,J05 | AT-11,19 | Background/network/audio integrity |
| FR-012 | Raw L/R + Part, counts, attempt state and form/version | J06 | AT-12 | Empty/partial result, misleading conversion |
| FR-013 | Non-comparable/mocked exposure disclaimer | J04,J06 | AT-13 | Comparative chart of invalid attempts |
| FR-014 | Optional rule-based suggestion with why/override | J02,J07 | AT-14 | New learner/no history |
| FR-015 | Learner-facing readiness and correction warning; non-UI curation tracked separately | J03,J09 | AT-15 | Wrong media/key, source withdrawn |
| FR-016 | Historic result revision transparency; scoring correction workflow TBD | J06,J09 | AT-16 | Result version changed |
| FR-017 | Unavailable Full Mock not falsely startable | J04,J09 | AT-17 | Missing form/media, retry later |
| FR-018 | Private learner context, account/data request (method TBD) | J01,J08 | AT-18 | Unauthorized view, delete pending/exceptions |
| FR-019 | Lifecycle/network recovery status; no double finish | J04,J05 | AT-05,19 | Confirmed vs unconfirmed answer; OS kill |

**FR-020..023:** OUT of MVP by signed baseline; **deliberately not assigned to Stage04 UI** (auto file importer, AI runtime, advanced notification interactions, offline/iOS/monetization).

## B. NFR-001..013: explicit 13/13 mapped (some non-UI controls)

| NFR | UX coverage vs non-UI owner | Associated J/AT | Verification due |
|---|---|---|---|
| NFR-001 | Learner must not see unverified form as ready; **NON-UI** per-asset legal/media/key QA owner | J04,J09 / AT-10,15 | Before pilot content release |
| NFR-002 | Failure text/state for wrong/missing audio; **NON-UI** content-media QA owner | J03,J09 / AT-03 | Before content release |
| NFR-003 | Saved/pending truthfulness; **NON-UI** durability test owner | J05 / AT-05,19 | Before pilot application release |
| NFR-004 | Mock timing/integrity and single result; **NON-UI** timer execution owner | J04,J05 / AT-11 | Test-plan and pre-pilot |
| NFR-005 | Full Reading/passage and 2 phone-context review | J03,J04 / AT-04 | Prototype review and later Android QA |
| NFR-006 | Private history and deletion-language; **NON-UI** deletion & security controls | J08 / AT-18 | Before pilot |
| NFR-007 | Raw-scoring disclaimer and validity label | J06 / AT-12,13 | Prototype and pre-pilot QA |
| NFR-008 | Historic score revisions visible; **NON-UI** audit policy owner | J06,J09 / AT-16 | Before version correction enabled |
| NFR-009 | **NON-UI** traceability evidence register | All journeys / AT-01..19 | Controlled Requirements baseline; carry forward |
| NFR-010 | Visual/reading accessibility, text scaling and focus affordances | J03,J04 / AT-04 | Prototype, test plan, pre-pilot |
| NFR-011 | Accurate online save/retry state; **NON-UI** connection persistence owner | J05 / AT-19 | Before pilot |
| NFR-012 | Name/copy cannot mislead about ETS official status | J04,J06 / AT-12,13 | UX copy and public-release compliance |
| NFR-013 | **NON-UI** budget deferred by PO; no cost screens/process required | None | Only after explicit PO reopening |

## C. Critical AT coverage

| Acceptance family | Relevant journey | Future UX check |
|---|---|---|
| AT-01..02 | J01–J03 | Goal/time entry and Part selection |
| AT-03..05 | J03–J05 | Correct media/passage/answer state |
| AT-06..09 | J02,J06 | Grading, reviewed explanation, errors, micro session |
| AT-10..13 | J04–J06,J09 | Two-form integrity, validity, transparent totals/comparison |
| AT-14..17 | J07,J09,J06 | Suggestion override, content correction and unavailability |
| AT-18..19 | J05,J08 | Learner privacy, lifecycle/network recovery |

## D. Coverage status and owner

- **19/19 IN FR mapped** at *inventory level*; FR-020..023 explicitly excluded.
- **13/13 NFR mapped** to UX or a named non-UI verification obligation.
- **19/19 AT represented** by a journey family (not tested).
- **NO user flow/wireframe approved. NO actual QA-01..08 PASS.** UX-02 PO choice pending; UX-03/UX-04 design not begun.
