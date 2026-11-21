# Stage04 — UX/UI Visual Design Baseline CANDIDATE V0.1

**Status:** **CANDIDATE — PENDING PRODUCT OWNER D04-UI-007**. **NOT** final/approved visual UI, **NOT** Stage04 Gate.  
**Date:** 2026-11-21. **Decision basis:** approved D04-UI-006 = A, D04-DESIGN-005 = A, D04-IA-003 = A; approved signed Requirements PRD/SRS V0.6 and Acceptance V0.4.  
**Evidence:** static UI concept board rendered + 31-screen clickable *low-/mid-fi* UX prototype V0.2; human usability n=0; real Android device tests n=0. No live audio, running clock, save, login or scoring.

## 1. Proposed visual language — VN first, neutral academic

- **Principle:** calm, readable Android learner interface, high-contrast text, state-first rather than decoration, distinct entry paths to Practice and Full Mock. Visual theme is an *author proposal*, not a product brand decision.
- **Colors (proposed not signed):** `primary-teal #087F7C` for primary practice actions, `mock-blue #1F5FC5` for exam actions; `ink #1D2B40`, `secondary-text #64748B`, `paper #FFFFFF`, `surface #F1F5F9`, `success #117D53`, `warning #A15F00`, `error #A12634`. **Do not encode persistence/validity solely by color.** White on `#087F7C` ~4.84:1 and white on `#1F5FC5` ~6.0:1 mathematically; other combinations and actual device/font sizes still require verification.
- **Type scale proposal:** 28/24 screen heading; 18/20 section; 16 body; 14 secondary; 12 metadata (never the sole carrier of a critical policy). Use readable Vietnamese, accommodate font size scaling and paragraph wrapping. Font family for implementation **TBD**; design board font not contractual.
- **Spatial proposal:** 8dp grid, 16dp lateral safe paddings, card radius 16dp, input/control min touch target **48×48dp target** (implementation-stage QA), meaningful focus and disabled states. These are **candidate design tokens**.
- **Components proposal:** top app bar, two equal-weight entry cards, optional rule-based suggestion card, mode badge, Part selector, answer cards/radio states, audio availability label, passage/question tab preserving anchor, save-status status panel, timer/integrity banner, results breakdown, curated feedback card, family profile/data view, unavailable-content message and recover/exit actions.

## 2. UX information architecture candidate

**IA-A (primary):** `Bắt đầu` / `Tiến độ` / `Cá nhân` (three destinations). First screen presents equal visibility to **Luyện tập** and **Full Mock**; user may ignore rule-based study suggestions. Content selection must exclude quarantined/withdrawn items and preserve separate practice/mock banks. **IA-B comparator** with `Luyện tập / Thi thử / Lỗi sai / Tiến độ` remains research alternative, not discarded without PO control.

## 3. High-priority interaction candidates

**W-02A Reading Part6–7:** choose `Đoạn văn` and `Câu hỏi`; keep a semantic passage/group anchor e.g. P7-177, last reading context and question association, including text scaling, tables/images and Android Back policy; never claim actual scroll-state preservation from a static image. **W-02B expandable passage** comparator retained.

**W-03A Full Mock:** explain **2×200, 7 Parts, 100 Listening approx 45m then 100 Reading 75m**, no voluntary pause or arbitrary audio replay in comparable attempt; show timer/integrity/save state only when applicable; no false 'Đã lưu' without durable acknowledgement. A suspect/interrupt attempt is flagged **không đủ điều kiện so sánh** per approved business policy; preserve acknowledged answers; clarify submission/timeout. Illustration does not run live clock/audio.

**W-04A Feedback:** during eligible **Part practice**, show correct answer and curator-approved explanation if available; otherwise transparent absence. After Full Mock, results/error review only when policy allows; never reveal official keys mid clean attempt. Rule suggestions opt-out and learner free choice. Display raw correct/answered by Part and section, **not official ETS TOEIC scaled scores**; comparison of uncalibrated forms is limited.

## 4. Screen coverage / UX obligations

See `STAGE04_UI_SCREEN_INVENTORY_AND_STATES_CANDIDATE_V0.1.md` (all 19 IN FR / 13 NFR, AT-01..19). **Four representative illustrated screens are visual anchors, not 31 pixel-perfect approved production screen layouts**. Low-fi 31-state PDF remains the primary reference for alternative/error-state flow; each represented UI state's copy is described in the screen inventory.

## 5. Privacy + content + failures

- Family members' attempts/results must be isolated; UX communicates current identity and protected state, without choosing authentication/DB/backend.
- Approved data policy: **verified deletion request within 7 calendar days** subject to legally permitted exceptions; routine retention **no more than 30 days after four-week pilot** absent further explicit agreement. Design must surface user-appropriate disclosure and request status; this image does not prove enforcement.
- Missing/unready audio, incomplete passages, unreviewed key, withdrawn form and uncertain save require **explicit blocking / safe retry / truthful messaging**; never render unsafe content as test-ready.
- **Two Full Mock inventories completed per PO report**, but answer/media/duplicate audits QA-01..06 not yet tested. Form availability shown in generated mockup is only a **design-state simulation**.

## 6. Baseline acceptance / carry forward

Conditional approval of this **design baseline candidate**, if granted, controls visual style and UX screen/state wording as a design reference; it cannot waive remaining I01–I08 evidence gaps, real Android/device/user tests, QA-01..08, approved Requirements, Stage04 Gate or Stage05 authorization. Before actual pilot, perform accessibility, timing/media, persistence/privacy and content QA per signed conditions. All budget work deferred.

## 7. Files forming this candidate package

- `design/STAGE04_UI_VISUAL_CONCEPT_BOARD_CANDIDATE_V0.1.png`
- `design/STAGE04_UI_VISUAL_01_TASK_HUB_CANDIDATE_V0.1.png` through `...04_FEEDBACK...png`
- `design/STAGE04_UI_VISUAL_BASELINE_CANDIDATE_REVIEW_V0.1.pdf`
- `docs/STAGE04_UI_SCREEN_INVENTORY_AND_STATES_CANDIDATE_V0.1.md`
- `docs/STAGE04_UI_VISUAL_ACCESSIBILITY_AND_CONTENT_REVIEW_V0.1.md`
- Historical clickable `prototypes/STAGE04_UX04_FOCUSED_CLICKTHROUGH_PROTOTYPE_CANDIDATE_V0.2.pdf` **retained unchanged**.
