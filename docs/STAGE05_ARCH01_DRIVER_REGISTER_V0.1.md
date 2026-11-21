# Stage05 ARCH-01 — Architecture Driver Register V0.1

**Status:** `ARCH-01 DOCUMENT ANALYSIS COMPLETE; NOT ARCHITECTURE SELECTED`.  
**Authority:** `D05-KICKOFF-001=A`, limited to document extraction and evidence review.  
**Date:** 2026-11-21. This register describes **what an eventual architecture must demonstrate**; it says nothing about **how it is implemented**.

## 1. Risk/driver priority semantics

- **P0 = pilot-blocking if unmet** under signed acceptance, not a declaration that a defect currently exists.
- **P1 = important testability/usability or release-integrity requirement**; final severity needs evidence.
- **Governance = requires PO-controlled decision or later checkpoint**, not an implementation feature.
- **Current evidence status** is either `SIGNED REQUIREMENT`, `PO-REPORTED INVENTORY`, `DOCUMENT/STATIC UX ONLY`, or `UNVERIFIED REAL-WORLD BEHAVIOR`. Any quality PASS requires test evidence, not wording in this register.

| Driver | Priority | Signed requirement or design constraint | Observable behavior/evidence to demand later | Requirements / checks | Current evidence |
|---|---|---|---|---|---|
| AD-01 Full Mock time/integrity | P0 | B1 A/B, 100 L ~45m ordered audio +100 R 75m, no discretionary pause/replay in clean attempts | Interrupted/background/timeout/duplicate result cannot silently gain time or be clean-comparable | FR-010/011/013/019; NFR-004; AT-10/11/13/19; QA-08 | Signed behavior, runtime UNVERIFIED |
| AD-02 Listening audio correctness | P0 | Correct mapped audio and order; Part practice is distinct from Full Mock | Test wrong/missing media, ordered playback, interruption classification | FR-003/010/011/015; NFR-001/002; AT-03/10/11/15; QA-03 | PO-inventoried forms; audio QA NOT RUN |
| AD-03 Durable answer acknowledgement | P0 | Save success only on durable acknowledgement; unanswered/pending/unknown states truthful | Confirmed answers survive interruption and belong to exact learner/form/item; retry not falsely acknowledged | FR-005/019; NFR-003/011; AT-05/19; QA-08 | UX copy approved; real persistence UNVERIFIED |
| AD-04 Network/process recovery | P0 | Online-first; no offline-first claim; preserve acknowledged state and time integrity | Foreground/background/process termination/connectivity loss test with explicit status | FR-005/011/019; NFR-004/011; AT-05/11/19; QA-08 | Android platform lifecycle publicly documented; app UNBUILT |
| AD-05 Family access isolation | P0 | 2–5 participants, private goals and histories; zero known critical cross-learner disclosure | Independent learner access tests and explicit account-control assumptions | FR-001/008/018; NFR-006; AT-01/08/18; QA-08 | Policy signed, mechanism NOT SELECTED |
| AD-06 Retention and verified deletion | P0 | Valid deletion ≤7 calendar days; routine retention ≤30 days after pilot subject to documented lawful exceptions | Identity verification, exception register, deletion execution and proof before pilot | FR-018; NFR-006; AT-18; QA-08 | Policy signed, technical/process evidence MISSING |
| AD-07 Content/asset provenance and release | P0 | QA-approved source, item, key, audio, passage, image, revision; unready blocked | QA-01..06 evidence manifest for released corpus, 100% essential references | FR-002/003/004/015/017; NFR-001/002; AT-02/03/04/15/17 | 2 forms inventoried PO; per-item QA NOT VERIFIED |
| AD-08 Evaluation vs practice segregation | P0 | Dedicated Part bank distinct from Full Mock A/B; no pre-exposure/inadvertent comparison | Traceable item grouping/form/version and cross-set leakage checks | FR-002/009/010/013; AT-02/09/10/13; QA-05 | Rule signed, content audit MISSING |
| AD-09 Raw scoring and immutable historical meaning | P0 | Per-Part, L/R and total correct/attempted; key-version/audit; no official TOEIC-equivalent score | Blank/invalid attempt/idempotent completion and key change tests | FR-006/008/012/013/016; NFR-007/008/012; AT-06/08/12/13/16; QA-02/07 | Requirements signed, no engine tested |
| AD-10 Reading longform integrity | P1/P0 if unusable | Part6–7 multi-passage/table/image intact; W-02A context return | At least 2 Android contexts, large text, passage ↔ question exact anchor | FR-004; NFR-005/010; AT-04; QA-04/08; UX04-I01/UIA-02 | Static UX only; real device n=0 |
| AD-11 Explainability of short learning | P1 | Part/self-selected sessions, optional rule-based suggestions; vetted explanation conditional | Missing-history fallback, user override, no fabricated explanation | FR-001/007/009/014; AT-01/07/09/14; QA-02/07/08 | Business rule signed; logic unbuilt |
| AD-12 UI status/copy truthfulness | P0 | V0.3 baseline: pending/ACK/unknown; mock invalid; QA-unready; raw result | Each UI state tied to genuine evidence, 19 state classes review | FR-005/012/013/017/019; AT-05/12/13/17/19; UI-G01..16; UIA-01/03/04/07 | Static design baseline only |
| AD-13 Android-only and platform quality | P1 | Android smartphone, online-first, ≥2 phone contexts, accessibility and UX stability | Later device/version/text scale/TalkBack tests and AC-08 numeric test thresholds | FR-004/019; NFR-005/010/011; AT-04/19; QA-08 | Device n=0; numerical targets TBD |
| AD-14 Pilot measurement and reliability | P1 | 4 weeks, 2–5 learners, ≥2 valid paired A/B, ≥2 Part-practice feedback | Capture attempt validity/form/version, incidents and inconclusive if insufficient | BR-09; PM-01..06; AC-05/07 | Approved target; pilot NOT STARTED |
| AD-15 Content correction/change control | P1 | Version corrections and historic attempts auditable, baseline changes PO-controlled | Test version transitions and signed change impact; no silent historic rescore | FR-015/016; NFR-008/012; AT-15/16; G03-CP06/G04-CP06 | No correction mechanism or test |
| AD-16 Licensing/brand and deferred budget | Governance | PO attests usage rights; no false ETS affiliation; CP-04 budget deferred | Before public launch: source-use audit & copy checks; PO reopens finances only if needed | NFR-001/012/013; QA-06; CP-04; G04-CP08 | PO attestation; per-asset/public-use evidence open; no spending |

**Clarifying distinction:** P0 marks consequences if a future product fails the signed requirement. It does not mean the current non-existent implementation has a confirmed failure.

## 2. Non-negotiable constraint checklist

- Exactly **two** independent A/B mock forms, each **6+25+39+30+30+16+54=200**; no one-mock fallback without PO change.
- Strict evaluative attempts must not silently gain time, voluntary pause or arbitrary replay. An interrupted attempt cannot be called clean-comparable without evidence.
- **Actual** durable ACK is required before any positive saved claim; stored selection and ACK state are different facts.
- Family learner segregation; deletion within 7 days of verified request, ordinary post-pilot retention at most 30 days with specified lawful exception/consent.
- AI runtime, automatic PDF/audio importer, iOS/offline-first, advanced notifications, S&W, monetization and ETS score equivalence remain OUT.
- Any technical candidate later must preserve Design Baseline V0.3, UI-G01..16 and unverified UX04/UIA obligations.
- Numeric runtime tolerances MUST be approved before a software test-plan baseline (AC-08), not invented as a past fact here.

## 3. Explicitly not answered in ARCH-01

No framework, client/server ownership, clock authority, data location, encryption technology, authentication design, DB, API, cloud vendor, media library, state machine, system diagram, deployment plan, code or evidence from app/device testing has been selected or produced. These are **later option-analysis questions** requiring explicit authorization.
