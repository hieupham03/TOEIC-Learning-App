# Stage04 — Semantic Color Contrast Token Audit V0.1

**Method:** WCAG relative luminance/sRGB contrast on *declared hex tokens*, not on generative-rendered pixel samples. **NOT an Android accessibility PASS.**

| Pair (foreground / background) | Calculated contrast | Candidate disposition |
|---|---:|---|
| #FFFFFF on #0B736A (primary button) | 5.71:1 | Suitable for normal-size text at >=4.5:1 |
| #0F172A on #FFFFFF (main text) | 17.85:1 | Suitable |
| #475569 on #FFFFFF (secondary text) | 7.58:1 | Suitable |
| #0B736A on #EDF4F1 (muted emphasis) | 5.12:1 | Suitable |
| #475569 on #EDF4F1 (secondary muted) | 6.79:1 | Suitable |
| #B45309 on #F8FAF9 (warning text) | 4.79:1 | Suitable for normal text as a color pair |
| #B42318 on #F8FAF9 (error text) | 6.27:1 | Suitable for normal text as a color pair |
| #FFFFFF on #116B63 (confirmed status) | 6.35:1 | Suitable |
| #D9E1DE vs #FFFFFF (decorative thin line) | 1.33:1 | **NOT suitable as only meaningful control boundary** |

**Design action:** keep pale line for incidental separators only. For input boundaries carrying meaning, propose stronger `#64748B` plus programmatically defined focus and visible state (must test adjacency). Status must always include text, not color only. Android recommends at least 48dp target and scalable sp font; actual app measurements pending.

**Sources:** https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html ; https://developer.android.com/design/ui/mobile/guides/foundations/accessibility .
