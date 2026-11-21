# Stage 04 — Research-led UI Visual Design Baseline CANDIDATE V0.2

**Status:** **DRAFT REVISION TO PENDING D04-UI-007 — NOT PO APPROVED, NOT Stage04 Gate.**  
**Date:** 2026-11-21. **PO request:** improve UI aesthetics based on Speak Up repository, other learning apps and research into poor AI-generated UI.  
**Replaces in active PO evaluation only:** V0.1 visual *candidate* from V4.9. The V0.1 artifacts remain in history unchanged; there was no PO approval of D04-UI-007 and therefore no signed baseline to modify.

## 1. Design concept: CALM LEARNING / EXAM FOCUS

- A composed, mature, low-noise visual system appropriate for TOEIC Reading and two long Full Mocks on Android: content first, brand secondary, status unambiguous.
- Visual structure: `Bắt đầu` (IA-A Task Hub), `Part 7 Đoạn văn / Câu hỏi` (W-02A), `Full Mock A Listening` (W-03A), `Ôn lỗi sai Part 5` (W-04A).
- **This is a new original AI-generated illustration**, not a pixel-accurate copy of any referenced app and not a functioning prototype. The V0.2 original 31-state click-through PDF remains the interaction candidate.

## 2. Screen-by-screen intent and acceptance direction

| Screen | Hierarchy in proposed V0.2 | Semantics that must be tested later | Anti-pattern prevented |
|---|---|---|---|
| Home / Task Hub | Header > today context > two equally discoverable choices Part Practice vs Full Mock > optional short suggestion > 3 labeled nav destinations | Choosing a study route does not force recommendation; no extra functions or fake progress | Decorative hero, icon-grid soup, stacked CTA buttons, many colors |
| Reading Part 7 | Part/question context > two labeled `Đoạn văn`/`Câu hỏi` modes > large readable passage area > truthful anchor info > one next action | Return to exact passage anchor P7-177; preserve text/images/tables on actual Android; clarify when merely simulated | Tiny body text, crowded split view, endless decorative cards |
| Full Mock | Form & section > time/status > truthful durable answer ACK > policy note > question progress > continue | Valid attempt no voluntary pause/arbitrary replay; no false ACK, resume/reset on interruption; timer shown is illustrative | Gamified badges, repeating status icon, scary red if no error, fake live timer |
| Error review | Item/context > choices > verified key with text > curator-verified explanation (if exists) > follow-up action | Only show after eligible practice/mock completion; don't invent official ETS score or answer | Confetti, decorative success streaks, score claims, red-vs-green only |

## 3. Detailed visual rules (DRAFT)

- **Primary:** #0B736A. **Main text:** #0F172A. **Secondary:** #475569. **Canvas:** #F8FAF9. **Surface:** #FFFFFF. **Border:** #D9E1DE. **Status:** colors only with unambiguous text, never a rainbow theme.
- **Type:** one Vietnamese-safe sans family. Controlled size set 28 / 22 / 18 / 16 / 14sp; no random fonts or 10sp placeholder microtext for critical instructions.
- **Visual density:** one main CTA per screen (Home mode entry is a deliberate pair), groups separated primarily by spacing rather than boxed/shadowed wrappers. One gentle accent panel where useful.
- **Icons:** only core navigation, Back and meaningful statuses. Standard outline style with labels/semantic support; no icon in every card header.
- **Components:** status chip/panel, neutral selection list, primary full-width CTA, in-context task sections, muted bottom nav. Use consistent corner radius and vertical rhythm.

## 4. Continuity with controlled interaction directions

- IA-A Task Hub remains primary, IA-B comparator remains preserved in UX03 material.
- W-02A Reading context-return remains primary, W-02B accordion comparator preserved.
- W-03A honest save and mock integrity; screen copy is a demonstration, **not** proof of live persistence.
- W-04A vetted error feedback (or explicit unavailable message) after eligible practice, optional next Part choice.
- Preserve MVP PRD/SRS/Acceptance V0.6/V0.4, B1 two Full Mocks, QA-01..08 framework, CP-01..05 and G03-CP01..07. No UX baseline or Gate activated by this revision.

## 5. Candidate deliverables

- `design/STAGE04_UI_RESEARCH_LED_REDESIGN_CANDIDATE_V0.2.png` — 4-screen visual review board.
- `design/STAGE04_UI_RESEARCH_LED_REDESIGN_REVIEW_V0.2.pdf` — visual + token/gate summary.
- `docs/STAGE04_UI_AI_ANTIPATTERN_GUARDRAILS_V1.0.md` — persistent anti-pattern review criteria.
- `docs/STAGE04_UI_EXTERNAL_RESEARCH_AND_REFERENCE_LEDGER_V0.1.md` — verified/public reference ledger.
- `docs/STAGE04_UI_REDESIGN_COMPARE_V01_V02_V0.1.md` — candidate tradeoffs, not test results.
- `docs/STAGE04_D04_UI_007_REVISED_OWNER_DECISION_PACK_V0.2.md` — separate PO signoff.

**Caveats:** no real UX usability research (n=0), no real Android QA, no accessible artifact imported from Speak Up source, no mock content/media QA. Do not assert compliant implementation or approved final UI from an illustration.
