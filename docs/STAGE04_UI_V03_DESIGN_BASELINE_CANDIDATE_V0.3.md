# Stage04 — UX/UI Design Baseline CANDIDATE V0.3

**Status:** **SUBMITTED FOR PO SIGNOFF D04-UI-008 — NOT YET BASELINED** · **Date:** 2026-11-21.

## 1. Scope and intent

Produce a content-first, consistent Android TOEIC Listening & Reading design language. Apply approved business journeys and Full Mock integrity policies without adding scope. Priority directions: **IA-A Task Hub**, **W-02A Reading passage/question context return**, **W-03A truthful timing/save/integrity state**, and **W-04A eligible post-practice feedback**. IA-B/W-02B kept as non-default comparators; no claim usability superiority.

This candidate comprises **(a)** existing UX interaction direction and State Atlas V0.1, **(b)** calm visual direction V0.2, **(c)** the **nine newly rendered V0.3 state examples** with explicit demo labeling, **(d)** source-of-truth component/copy rules and UI-G01..16. Earlier V0.2 AI concept board is an *inspiration/evidence artifact*, **not authoritative for sample goals, durable save, QA-vetted content, or live timers**; the V0.3 state/copy rules override such wording where they conflict.

## 2. Visual system proposed for controlled baseline

| Token / rule | Candidate V0.3 | Requirement |
|---|---|---|
| Font | One Vietnamese-safe sans: Inter (visual examples); Android family choice remains implementation review | no display/script fonts, only regular/semibold/bold |
| Primary | `#0B736A` | use for one main CTA and selected state; white text on primary |
| Ink | `#0F172A` | content and headings |
| Secondary text | `#475569` | metadata, 4.5:1 text contrast target |
| Background / surface | `#F8FAF9` / `#FFFFFF` | content reading on white, space over decorative cards |
| Neutral outline | `#C4D0CB` | decorative outline only; meaningful interactive boundaries must be clearly recognizable and verified for 3:1 where applicable |
| Muted teal | `#EDF4F1` | mild contextual status, not a rainbow background |
| Warning | `#8C4C10` on `#FFF4E5` | must include clear words, not color alone |
| Error | `#B42318` on `#FEF0ED` | failure/error semantically labelled |
| Spacing | 8dp rhythm; 20dp content margin; ~12–15dp meaningful panel radius | no nested cards for every line |
| Body / heading | 16sp body target, 20–24sp headings, 13–14sp secondary | text scaling to be tested on real Android |
| Touch targets | target ≥48×48dp | currently design intent only; no device PASS |

## 3. Core screen/state contracts

1. **Part practice Listening** provides audio and answer choice, clearly labelled *not Full Mock*. Optional replay in Part practice must not be carried into evaluative Mock.
2. **Save pending**: `Đang xác nhận lưu` (do not show success). **Save ACK**: `Đã xác nhận lưu` only upon durable persistence confirmation. **Save unknown**: `Chưa thể xác nhận lưu`, explicit retry/check route. Three states have separate visual screen examples.
3. **Mock interruption**: preserve acknowledged selections, do not silently reset time; integrity uncertain → mark noncomparable. Separate noncomparable screen explains result limitations and allowed next steps. Any ability to resume must follow previously signed S2 policies, not be inferred from visual CTA.
4. **Raw results** show correct/attempted, Listening/Reading and (where available) per Part. Never label as ETS 10–990 equivalent; sample values visibly marked illustration.
5. **Privacy** isolates family learner context; verified deletion within 7 calendar days; routine pilot retention ≤30 days after pilot except allowed exceptions. Copy is a requirement proposal to be implemented later, not deletion proof.
6. **QA-unready** content may not launch; do not show `đã kiểm duyệt` for explanations or materials lacking actual audit evidence.
7. **Reading** W-02A remains the UX choice, with return-to-passage semantics contingent on tested state persistence; existing V0.2 Reading image is only inspirational.

## 4. Delivered visual evidence

`design/STAGE04_UI_V03_01_LISTENING_PRACTICE.png` through `...09_CONTENT_NOT_QA_READY.png` (nine distinct 780×1688 raster renderings representing 390×844 logical mock phone canvases); combined PDF `design/STAGE04_UI_V03_NINE_CRITICAL_SCREENS_VISUAL_REVIEW_CANDIDATE.pdf` (10 pages: cover + nine screenshots) and `design/STAGE04_UI_V03_NINE_CRITICAL_SCREENS_CONTACT_SHEET.png`. Combined with previous four high-level visual concepts, **13 visual examples** exist, with some state overlap; **19/19 UI state classes** have underlying schematic inventory in the preserved UI State Atlas. **Do not claim 19 pixel-final screens**.

## 5. Baseline sign-off boundary

Approval of `D04-UI-008=A` would designate **this specification, its nine visual examples, the 19-state semantic inventory, and existing UI-G guardrails** as controlled *design-language, screen-state and copy* baseline with recorded conditions. It **must not** be interpreted as real Android/learner usability PASS or implementation-ready pixel assets. Additional design changes require review; typography/accessibility on actual devices and all UX04 issues still require verification. **Stage04 Gate requires a separate PO decision. No Stage05 architecture/app code authorization.**
