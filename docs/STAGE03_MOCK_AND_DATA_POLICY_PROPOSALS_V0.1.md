# S2 — Full Mock, Scoring, Data Policy Decisions V0.1

**Status:** DRAFT PROPOSALS, **NOT PO APPROVED**. R1–R4 drafting principles are approved; detailed rules here are new candidates. No UI, algorithm or architecture selection.

| Policy | Analyst recommended default | Alternative / refinement requiring PO selection | Why it matters / linked tests |
|---|---|---|---|
| **P01 — Exam vs practice** | Full Mock evaluated under exam-like time/integrity rules; Part/one-question practice freely paused | Allow untimed Full Mock as separate **practice mode**, but never classify it as comparable evaluation | FR-009/010/011, AT-09/10/11 |
| **P02 — Time and section** | Listening follows complete ordered audio, about 45 min; Reading 75-minute countdown; finish/timeout explicit; no silent new time | Different accommodation or timing supported only if clearly relabeled non-standard, with form-specific rules | BR-01/04, AT-11; avoid cutting an audio track solely to hit 45:00 |
| **P03 — Voluntary pause** | In comparable Full Mock, voluntary pause **not allowed**; practice can pause | If pause allowed, attempt may resume but must be labeled **non-comparable** | FR-011/013, E-01 |
| **P04 — Audio replay** | No discretionary replay/rewind of Listening in comparable Full Mock; order defined by question media | Replay in untimed practice, with non-comparable label if used in Full Mock | FR-003/011/013, E-02 |
| **P05 — Background/network outage** | Preserve acknowledged answers; timer never silently resets; if essential audio unavailable or timing compromised mark incomplete/non-comparable; no offline promise | Grace policy or resumed comparable status **TBD** and must be explicitly measured/approved, not inferred | FR-005/011/019, AT-05/11/19 |
| **P06 — Save acknowledgment** | Only declare `saved` once acknowledged as durable; before acknowledgment use pending/uncertain status, no invented success | Timing/retry target chosen after device/network study | FR-005/019, AT-05/19 |
| **P07 — Submit and timeout** | A completed form gets one finalized result; early exit/timeout classified, blank answers remain blank, no duplicate submission | Early voluntary submit may count completed if time/coverage criteria explicitly met; default: completed only when user confirms end or timed end and form is consistent | FR-011/012, AT-11/12 |
| **P08 — Scores/version/comparison** | Raw count by Part and section only; log form/content version; exposed or non-standard attempt excluded from clean trend; no ETS official-score claim | Offer a clearly labeled *informal* heuristic estimate only after separate PO approval of methodology and claim control | FR-012/013/016, AT-12/13/16 |
| **P09 — Pilot identity/privacy/deletion** | Minimal pseudonym/identifier, strictly isolated learner records; allow participant to request deletion; disclose retention and correction policies before pilot | Exact identity/auth approach and deletion schedule require product approval; below are proposed limits, not active requirements | FR-018, AT-18; Google Play requirements if accounts are created |

### Candidate privacy and retention numbers requiring signoff

- Minimize profile: optional nickname + self-reported level/goal/time; no unneeded phone contacts/location or biometric data.
- Preserve answer history during the four-week pilot only to fulfill scoring and longitudinal review; **propose 30 days after pilot as maximum routine retention** unless participants explicitly agree otherwise (not approved).
- **Propose deletion of requested personal learning data within 7 calendar days** after a validated participant request, subject to any applicable lawful retention exception; if deletion cannot be completed, explain the remaining category and reason. No deletion execution is claimed.
- Participant must be able to understand what data is collected, how to ask for deletion, and when history will be removed, before using pilot. Product requirement only; no UI screen or account architecture design.
- If account creation is introduced, account-deletion access and policy must satisfy applicable Google Play requirements before publication; do not pretend current prototype already complies.

### Strong constraints

- Treat interruptions caused by Android/background/network as an explicit attempt-integrity issue, **not** a justification to lose acknowledged answers.
- No official TOEIC 10–990 score nor claims of actual score improvement from raw A/B results; tests not statistically equated.
- A content-key correction must preserve previous recorded result context and make the correction auditable; exact recomputation/appeal process is a follow-up owner rule, **not hidden in implementation**.
- The 7-day / 30-day privacy values are **candidate numbers** for decision; changing them is an amendment, not a bug.

### Residual implementation-independent TBDs to explicitly track after policy signoff

- P05 acceptable grace and what counts as material Listening interruption; **must be defined before final AT-11 baseline**; proposed conservative route is mark affected attempt non-comparable immediately.
- P06 exact save acknowledgment/recovery timing; do not invent technical SLA in Requirements.
- P09 whether accounts exist and any required retention exceptions; product-level privacy requirements approved before pilot.

Recommended `S2-A`: approve P01–P09 candidate defaults **where fully specified**, and endorse conservative labeling for unresolved timing/network cases, while leaving technical performance numbers tracked as TBD to be validated later. An unresolved **business** rule that changes the meaning of score/comparability must be signed before MVP/PRD/SRS baseline; no silent deferrals.
