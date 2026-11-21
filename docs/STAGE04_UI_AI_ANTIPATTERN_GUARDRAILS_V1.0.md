# TOEIC Learning App — Persistent UI Quality Guardrails & AI Anti-Pattern Prevention V1.0

**Status:** **ACTIVE PROJECT REVIEW RULES** per explicit PO request to research, record and avoid AI-generated UI visual mistakes. This is a **design review checklist**, not a PO-approved new PRD/SRS requirement nor a signed UI baseline.  
**Applies:** All Stage04 candidate images, screen designs, prototypes, future UI implementation reviews and prompt briefs until superseded by PO.  
**North star:** `Calm Learning / Exam Focus` — coherent, content-first, credible on Android, human-readable Vietnamese, no decoration competing with learning.

## 1. Mandatory anti-pattern checks

| ID | Failure mode to prevent | Review gate / measurable proxy |
|---|---|---|
| UI-G01 | Icon overload | Every icon must represent a recognizable action/status and have text or accessibility label. No decorative icon on every card/header. Preferred target **0–3 meaningful icons within main content** of a standard screen, excluding persistent nav/necessary system controls; **project heuristic, not universal UX law**. |
| UI-G02 | Font soup | Choose **one font family** suitable for Vietnamese/English throughout UI. Controlled weights regular/medium/bold. No arbitrary display/script or tiny ornate captions. |
| UI-G03 | Color soup / rainbow cards | One brand accent family (deep teal) + ink/neutral surfaces; status colors only for semantics; avoid purple gradients, random blue/green/orange features and hue-based navigation. |
| UI-G04 | Box soup | Use cards only for semantic grouping, not a box around every sentence. Prefer whitespace/divider for lightweight subgroups; one elevation tier at most. |
| UI-G05 | CTA overload | One clearly emphasized primary task CTA per screen/decision context; secondary text/outline actions lower emphasis. Home two equal-weight *mode choices* allowed under signed U1-A. |
| UI-G06 | Overdesigned exam screen | No streak/mascot/confetti, promotional banner or non-task decoration during mock; show timing, sequence, save integrity and next action where relevant. |
| UI-G07 | Bad hierarchy/spacing | Adopt 4/8dp rhythm, 16–20dp horizontal content margins, consistent title baseline and 3–5 text roles. Check alignments and long-text wraps; don't compress reading text for aesthetics. |
| UI-G08 | Weak contrast / tiny text | Design tokens must **calculate** >=4.5:1 for ordinary text, >=3:1 for large text. Target content text 16sp, critical alerts >=14sp and never status color-only. Actual Android accessibility testing still required. |
| UI-G09 | Decorative or mislabeled interaction | Icons with clear text; no fake buttons, random arrows, illegible glyphs or misleading fake interactive states. UI screenshot is NOT functional evidence. |
| UI-G10 | Violating Full Mock policy | No unsolicited pause/replay for valid mock; no correct-answer reveal before eligible end; do not silently reset timer or announce save without acknowledged persistence. |
| UI-G11 | Context loss / cognitive strain | W-02A retains passage anchor and question relationship; avoid giant floating controls, excessive scrolling/nested tabs, truncated tables, images or answer labels. |
| UI-G12 | Inconsistent component states | Check default/selected/disabled/loading/saved/pending/unknown/failed/invalid/offline/content-unready; show plain-language recovery action. |
| UI-G13 | AI-generated phantom content | Do not invent official ETS scores, real user data or actual test readiness; label sample questions/elapsed time/mock statuses as illustration. |
| UI-G14 | Unsupported new scope | No AI runtime, auto PDF/audio importer, advanced notifications, gamification/social, Speaking/Writing, monetization or iOS added by design without controlled scope change. |
| UI-G15 | Copying another app | Do not trace proprietary screenshots or reuse logos, mascot, artwork, original questions or code from references; adapt only general interaction principles. |
| UI-G16 | Accessibility theater | Target >=48x48dp touch zones, readable scaling, semantics and TalkBack path; mark static visual review as `NOT TESTED ON DEVICE` until real test evidence exists. |

## 2. Proposed design system tokens V0.2 (DRAFT)

| Semantic token | Proposed value | Use |
|---|---|---|
| brand.primary | `#0B736A` | One foreground accent and main button; white text contrast ~5.71:1 |
| brand.ink | `#0F172A` | Main text, ~17.85:1 on white |
| text.secondary | `#475569` | Secondary, ~7.58:1 on white |
| canvas | `#F8FAF9` | Main background |
| surface | `#FFFFFF` | Reading/content and true semantic panels |
| surface.muted | `#EDF4F1` | Single muted suggestion/status band |
| outline | `#D9E1DE` | Dividers/neutral borders only |
| status.good | `#116B63` + text | Saved/confirmed/valid; **not** score correctness alone |
| status.warn | `#B45309` + text | Save pending/interruption warning |
| status.bad | `#B42318` + text | Confirmed error/invalid/unavailable |

**Color source:** project recommendation, not a cloned brand. Computed WCAG sRGB formula for listed *solid tokens*; screen mockup pixels may differ. Avoid multiple full-screen saturated colors. Do not express status by red/green alone.

**Typography:** one Vietnamese-safe sans-serif **Roboto or equivalent (font family choice remains candidate)**; 28sp screen hero, 22sp page heading, 18sp section, 16sp body/action, 14sp metadata. Use regular/medium/bold only; line-height ~1.45 for reading passages and 1.3–1.4 for ordinary labels, verify paragraph flow.

**Shape / space:** one main corner radius scale (12–14dp), small 8dp chips if needed; 8dp base spacing with 4dp micro-offset; text left-aligned; no ornamental shadows on stacked cards. >=48dp tappable area (Android recommendation); adequate physical safe insets and text scaling to be tested.

**Icon system:** one coherent outline family; back, home, progress, account and essential statuses only. Persistent bottom nav retains exactly the *approved IA-A directions* `Bắt đầu | Tiến độ | Cá nhân` with both labels and icons, but **not** an extra icon on every content row.

## 3. Exact review procedure for every subsequent AI/UI iteration

1. State scope and baseline refs in image prompt; prohibit out-of-scope screens/features.
2. Start from user task hierarchy with monochrome wireframe / content list before styling.
3. Apply one font and semantic token palette before rendering; no added decorative icons or mascot.
4. Count displayed action hierarchies, nav destinations and status labels. Confirm no ambiguity in Mock/Part Practice distinction.
5. Visually inspect 360dp and 412dp-equivalent proportions; any clipping, garbled Vietnamese/English, duplicated labels, incorrect mock time or contradictory statuses is an OPEN defect.
6. Validate token contrast computationally; treat generated image values as approximate, not verified implementation colors.
7. Trace screen/state to FR/NFR, signed mock policies and UX04 I01..I08; don't claim PASS without test.
8. Mark every image `DESIGN CANDIDATE — NOT APPROVED`. Only PO may approve final design baseline or Stage04 Gate.

## 4. Prompt guardrail (reuse as written design briefing, not executable code)

> Design a calm, functional Android TOEIC Listening & Reading learning interface. Prioritize reading legibility and user tasks. Use a single Vietnamese-safe sans-serif, a restrained deep-teal/ink/white palette, generous whitespace and a consistent 8dp rhythm. Show equal paths to Part Practice and Full Mock. Use no mascots, confetti, gratuitous icons, rainbow cards, decorative gradients or fake result claims. Never reveal answers during a valid Full Mock; save-state copy must distinguish pending, confirmed and unknown. Provide clear words with any meaningful icons. Deliver as proposed candidate, never assume approval or real application behavior.

## 5. References and evidence boundary

See `STAGE04_UI_EXTERNAL_RESEARCH_AND_REFERENCE_LEDGER_V0.1.md`. NN/g's AI-prototyping research supports a clutter/hierarchy risk; the **numerical style limits above are our project-level guardrails**, not universal research findings. Accessibility values follow WCAG/Android reference pages. No real-device or real-learner usability PASS claimed.
