# Stage05 ARCH-01 — Evidence Gap & Verification Register V0.1

**Status:** ANALYST REVIEW; no runtime/app/device test PASS. `ARCH-01` records gaps and due gates; it does not select their technical solutions.  
**Priority labels:** P0 pilot blocking **if unmet**; P1 significant; GOV separate PO signoff.

| Gap | Priority | What is known now | What is *not* evidenced | Due checkpoint | Next evidence owner (role only) |
|---|---|---|---|---|---|
| EG-01 | P0 | A/B form inventories PO-confirmed, B1 signed | Item-by-item 2×200 structure, key/media/image audit, cross-form duplication proof | Before pilot content release | Content curator + QA-01..06 reviewer |
| EG-02 | P0 | Ordered ~45m Listening +75m Reading strict policy signed | Time drift/grace thresholds, process/network interruption outcomes tested | AC-08 test-plan signoff; then QA-08 before pilot | Later QA/technical owner |
| EG-03 | P0 | No arbitrary mock replay/pause and separate practice rules signed | Media order/latency/interruption reliability on actual form/device | QA-03 content and QA-08 system before pilot | Content/media QA + device test owner |
| EG-04 | P0 | Save pending/ACK/unknown design-copy baseline signed | Durable write acknowledgement under network loss, process death, retries and deduplication | QA-08 before pilot | Later implementation/QA owner |
| EG-05 | P0 | Isolation/deletion ≤7d/≤30d retention signed | Identity verification procedure, access-test results, exception/legal record and deletion proof | Before identity-dependent pilot use, QA-08 | Later privacy/QA owner |
| EG-06 | P0 | Practice bank must be separate from A/B; authorized-source requirement signed | Practice pool quality, pre-exposure checks and asset provenance | QA-01..06 before pilot | Content curator |
| EG-07 | P0 | Raw-only scoring and version fidelity signed | Score arithmetic, blank outcomes, invalid attempt labels, historical corrections | QA-02/07/08 before pilot | Scoring QA owner |
| EG-08 | P1 | W-02A Reading and ≥2 Android contexts required | Real long Reading, position return, zoom/text scale/TalkBack/contrast tests | QA-08 and UX accessibility before pilot | Android/UX tester |
| EG-09 | P1 | 19 UI state classes and 9 static visual samples in signed design | Dynamic state correctness with live content, 2 devices & learner comprehension; n=0 so far | G04-CP02..04 before UX acceptance | UX/Android QA |
| EG-10 | GOV | AC-08 requires numeric targets signed | Timer tolerance, save confirmation time, reconnect/recovery, responsiveness, accessibility targets | Before SOFTWARE TEST-PLAN BASELINE | PO + test-plan owner |
| EG-11 | P1 | 4wk pilot 2–5 learners, ≥2 valid paired forms & 2 practice feedback signed | Actual usage, incidents, acceptable comparisons, representativeness | During/after pilot | Pilot reviewer |
| EG-12 | P1 | Explanation shown only when vetted | Explanation coverage, provenance/version mapping, missing explanation UX actually works | QA-02/06 and build before pilot | Content curator/UX QA |
| EG-13 | GOV | Existing signed controls CP01..05, G03, G04 | Future waivers/closures or condition owners and evidence still TBD | Each control's stated checkpoint | PO and delegated reviewer |
| EG-14 | GOV | Budget-related activity expressly deferred | Costs/quotes/vendor evidence intentionally NOT requested or authorized | ONLY when PO explicitly reopens CP-04 | PO |
| EG-15 | P1 | No official ETS score claim, no inferred sponsor status | Final name/copy and source-use permission at public-distribution scope | Prior to public release | Rights/compliance reviewer |
| EG-16 | P0/P1 | Requirements and design baselines byte-identical | Actual integrated component implementation and production controls | Stage05 later approved options, implementation and verification stages | Future technical/QA owner |

## Evidence tiers and false-positive prevention

1. **SIGNED:** PO approved business requirements and design semantics. Strong evidence of **what must hold**, not **that software currently holds it**.
2. **PO-REPORTED:** two mock sets inventoried and permitted source use affirmed. Not an independent item/media/key/test audit. **Do not ask PO to re-count or re-prove** as ARCH-01 busywork.
3. **ANALYST DESK:** UI diagrams, scenario matrices, requirement tracing and external Android guidance. Not test results.
4. **ACTUAL TEST (FUTURE):** source item/media audit, unit/device/network/accessibility checks and pilot observations with reviewer, date, environment, PASS/FAIL/BLOCKED/NOT RUN status.

**No unresolved item is silently waived.** No gap in this list requires an app, vendor account, paid service, new corpus upload or budget discussion to complete ARCH-01.
