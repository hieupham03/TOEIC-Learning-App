# Stage 04 — UX-02 Consolidated Journey Interaction Options V0.1

**Status: ANALYST PROPOSAL; D04-UX-002 PENDING PO.**  
**Scope:** choose UX direction/interaction principles only. **No screen, information architecture, visual style, wireframe, prototype or code approved by this document.**

## 1. Immutable constraints in every option

- Android online-first, 2–5 family participants for four weeks; Part 1–7 practice **and two mandatory B1 Full Mock forms** remain in every option. No mock removal/fewer parts.
- Mock ≠ practice. Clean mock has no user pause/no discretionary Listening replay; ~45min ordered Listening, 75min Reading; truthful interrupted/non-comparable labels; no false confirmed answer save.
- Raw/Part/L&R score and conservative cross-form caveat; no ETS official score conversion; vetted explanations only; no AI runtime or automatic PDF importer.
- Family privacy, 7-day verified deletion, ≤30 days after pilot regular retention with exceptions, accessibility and long-Reading completeness; execution/identity method TBD.
- QA-01..08 tests not PASS; budget DEFERRED, no scope creep.

## 2. Four decisions bundled into one PO review

### U1 — How learners enter a session (high-level emphasis)

| Option | Interaction concept | Advantage | Cost/risk | Analyst opinion |
|---|---|---|---|---|
| **U1-A — Two equal routes** | Make ‘luyện nhanh/luyện Part’ and ‘thi thử đầy đủ’ conceptually distinct from start; goal/time as optional guidance | Supports irregular-time and evaluative journeys without misleading either | Two choices must be explained in compact wording | **RECOMMENDED** |
| U1-B — Practice-first | Prioritize quick practice; mock is secondary but clearly discoverable | Reduces daily-start friction | May bury core B1 full mock experience | Alternative |
| U1-C — Mock-first | Lead with Full Mock A/B readiness and assessment | Makes score-tracking focus obvious | Makes short casual practice feel hard to access | Alternative |

### U2 — How to maintain reading context on a phone (no chosen layout yet)

| Option | Interaction concept | Advantage | Cost/risk | Analyst opinion |
|---|---|---|---|---|
| **U2-A — Passage context return** | Learner can return to exact relevant passage/figure, preserving reading position and question association through navigation | Lowers context loss in long Part6/7; compatible with compact phones and font scaling | Needs careful back/scroll behavior tests; not yet a wireframe | **RECOMMENDED for prototype comparison** |
| U2-B — Continuous passage–items | Passage and grouped questions in one linear reading sequence | Simple mental model | Long scrolling and lost references can remain painful | Alternative |
| U2-C — Persistent side-by-side | Passage and question always visible together | Easier visual cross-reference on wide devices | Very constrained compact-phone space; not safe as sole phone strategy | Conditional alternative, not default |

### U3 — How mock status is communicated (no changes to official exam rules)

| Option | Interaction concept | Advantage | Cost/risk | Analyst opinion |
|---|---|---|---|---|
| **U3-A — Contextual integrity status** | Explain no-pause/no-replay before start; show concise timing/phase/save-state while active; clearly call out uncertainty, invalidity or timeout at change points | Balances low distraction with honest attempts; exposes uncertainty early | Must avoid hiding critical unsaved state | **RECOMMENDED** |
| U3-B — Always-expanded audit details | Display full policy/time/save/validity explanation throughout attempt | Maximum visibility | Distracts from Listening/Reading and crowds small phone | Alternative |
| U3-C — Minimal status, details on demand | Almost all status hidden behind info action | Screen stays clean | High risk of misleading user about unsaved or non-comparable attempts | Not recommended for P0 errors |

### U4 — How practice leads to useful next action (never reveal answers during clean mock)

| Option | Interaction concept | Advantage | Cost/risk | Analyst opinion |
|---|---|---|---|---|
| **U4-A — Practice feedback then learner choice** | After practice item/session: verified key, vetted explanation if any, wrong-answer history, optional ‘practice this Part next’; mock feedback only AFTER submit/finish | Creates a short error-to-learning loop, honors user choice and score integrity | Must separate feedback timing by mode and indicate missing explanation | **RECOMMENDED** |
| U4-B — Batch feedback only after practice session | Present errors and suggested Part after chosen practice session | Fewer stops while practicing | Weak for one-item sessions; longer delay to learn from mistakes | Alternative |
| U4-C — Recommendation-first | Default to prescribed next activity before seeing results | Strong continuity | Feels forced, conflicts with learner override if unskippable | Only valid with explicit skip |

## 3. One recommended bundle — **U1-A + U2-A + U3-A + U4-A**

- Appropriate for **both** a long evaluative experience and irregular short practice without silently changing signed requirements.
- U2-A is an **interaction hypothesis** to validate later, not a chosen page architecture or implemented passage split. If desktop-style split does not work on compact Android, the experience still must expose full text and its referenced items.
- U3-A surfaces uncertainty truthfully, does not introduce pause/replay rights or guarantee recovery of an integrity-compromised attempt.
- U4-A never leaks answer or correction into an ongoing clean mock; approved answer review and content version rules remain intact.

## 4. Validation and escalation plan after PO choice (not executed yet)

| What would be tested after authorization | Evidence plan / success interpretation | Requirement link |
|---|---|---|
| Route clarity from first interaction | Desk check + later prototype walkthrough distinguishes short practice and full mock | AT-02/09/10 |
| Reading context return on compact phones | Low-fi comparison of passage reference preservation, larger text, no clipped images on >=2 Android size contexts | AT-04; AC-06; QA-08 |
| Mock rule understanding | Prototype walkthrough: user can identify no-pause/replay and integrity status before/after interruptions | AT-11/13/19 |
| Saved-state comprehension | Show saved/pending/error variants; no false success, recovery guidance | AT-05/19 |
| Mistake learning flow | Verified key and optional explanation; opt-out of recommendation; no mock early reveal | AT-07/08/14 |
| Privacy and corrective content states | Two learner contexts; no exposure, deletion info and withdrawn-form language | AT-15..18 |

**No quantitative usability PASS claimed.** UX02 does not approve a mockup or change PRD/SRS baseline. If any chosen route requires changing S1/S2/S3, open Product Owner change control under G03-CP06 before execution.
