# Stage04 UI V0.2 — Pre-Baseline Desk Audit V0.1

**Date:** 2026-11-21. **Decision:** D04-UI-007 PENDING. **Status:** DESK REVIEW, NOT USER/ANDROID TEST PASS. 
**Evidence:** existing 4-screen AI-generated static board V0.2 + UX04 31-page linked PDF V0.2 + approved requirements + UI-G01..16.

## 1. Findings specific to the actual V0.2 illustration

| ID | Finding | Impact | Required wording/handling | Disposition |
|---|---|---|---|---|
| UIA-01 | Home shows `Hôm nay · 0/15 phút`, while study target is an illustrative preference, not known learner data. | Could imply a compulsory 15-minute goal. | If no goal, show `Chưa đặt mục tiêu` and let learner choose; sample boards must explicitly say `DỮ LIỆU MẪU`. | OPEN before final handoff |
| UIA-02 | Reading displays `Vị trí đọc đã ghi nhận` without a real persistence engine. | May imply proven scroll restoration. | Allow copy only when an actual anchor is recorded; static board must be labelled illustrative. | OPEN test UX04-I01 |
| UIA-03 | Mock displays `Đáp án đã xác nhận lưu` in a visual sample. | Misleading without durable ACK if copied directly. | Conditional state only: pending → ACK confirmed, or pending → unknown / retry. Never show success on pending/network error. | OPEN UX04-I02 |
| UIA-04 | Error review shows `Giải thích đã kiểm duyệt` beside AI-generated sample text. | Conflates illustration and item QA. | In real app, render only vetted explanation; sample should say `Lời giải mẫu · chưa QA` or omit verified badge. | OPEN content QA |
| UIA-05 | Four representative illustrations, but UI inventory has 19 classes. | Insufficient visual detail for claim that all screens are pixel-complete. | New 19-state atlas accompanies V0.2. Still NOT full fidelity or real Android. | PARTIALLY ADDRESSED |
| UIA-06 | Outline token `#D9E1DE` vs white = ~1.33:1. | Fine as decorative divider; weak if relied upon as essential input/control boundary. | Use `#64748B` or alternate ≥3:1 boundary where a control boundary conveys functionality; keep pale line decorative only. | DESIGN RULE PROPOSED |
| UIA-07 | `Listening · 35:24 còn lại` is demonstration time and mock format shows ~45m Listening + 75m Reading. | Screenshot cannot prove correct timer/audio transition. | Label time values as sample, never copy into test evidence; confirm actual clock per approved policy later. | OPEN UX04-I03/I04 |
| UIA-08 | Typography and touch targets cannot be measured reliably from AI image. | Cannot claim WCAG/Android PASS from pixels. | Design specs target scalable `sp`, ≥48dp touch and contrast; actual implementation/device test remains open. | OPEN |

## 2. Guardrail review of UI-G01..UI-G16

| Rule group | Desk evidence | Status |
|---|---|---|
| UI-G01..G05 (icons, font, palette, card, CTA) | V0.2 shows reduced decoration, one main visual accent, mostly unboxed content. Typography metrics remain unverified. | DESIGN DIRECTION OK / PARTIAL |
| UI-G06..G08 (readability, contrast, states) | Palette contrasts computed for exact solid tokens, Reading receives more space; meaningful border color needs adjustment. | PARTIAL |
| UI-G09..G12 (navigation, live state, copy, exceptions) | IA-A/labels and mock/persistence semantics mapped; 31-page UX document includes exceptions; image itself only 4 screens. | PARTIAL |
| UI-G13..G16 (no fake content, scope, originality, accessibility) | Demo labels and status claims require explicit qualification; no new feature or copyrighted asset added. | PARTIAL / BLOCKS UNCONDITIONAL SIGNOFF |

## 3. Recommendation

**CONDITIONAL REVIEW READY** as a design language/interaction specification candidate, NOT a validated complete UI. Every unverified live-state copy must be treated as conditional, not a tested property. A future Stage04 Gate review must state which UIA-/UX04-/QA checks are deliberately carried forward and who owns them. Product Owner alone decides D04-UI-007. No Stage05 architecture/code.

**External standards:** W3C WCAG 2.2 https://www.w3.org/TR/WCAG22/ ; Android accessibility https://developer.android.com/design/ui/mobile/guides/foundations/accessibility. Computed ratios use the WCAG sRGB formula on declared token pairs, not sampling the rendered AI image.
