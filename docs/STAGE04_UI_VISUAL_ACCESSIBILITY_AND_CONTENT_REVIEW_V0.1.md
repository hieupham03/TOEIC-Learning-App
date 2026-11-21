# Stage04 — Visual / Accessibility / Content Review V0.1

**Type:** analyst desk review of image candidate and traceable UI specification. **Not** human/device usability testing, QA-01..08 PASS, or Stage04 Gate.

## Visual review summary

- **Pass at document level:** Four key visual concepts presented, touchpoint-to-baseline traceability is documented, candidate IA and Reading/Mock/Feedback patterns are consistent with D04-UI-006 direction. White on candidate `#087F7C` contrast estimate **4.84:1**; white on `#1F5FC5` **6.0:1** by standard sRGB calculation. These calculations do NOT certify whole-screen WCAG compliance.
- **Open/high:** Image-generation typography and sample English question text are **illustrative**, not signed copy, source TOEIC test content or UI design tokens. Exact final strings require copyedit; screenshot depicts a MOCKED success state, not real confirmed persistence. Font scaling, dark mode policy, color-blind semantics, touch hitboxes, clipping, Android TalkBack/focus order and large-screen behavior need later validation.
- **Open/high:** Reading contextual restoration on real devices (I01), ACK/retry/unknown durability (I02), interrupted/mock integrity meaning (I03/I04), actual raw-score comprehension (I07), privacy SOP/enforcement (I08). No evidence that mock timing/audio or question logic functions.
- **Open/medium:** IA-B discoverability and W-02B text/passage alternative, not user-compared (I05/I06).
- **Open/medium:** Image concept uses internal learning theme/name, not a confirmed public brand/trademark approval; marketing/public-release naming remains separately governed.

## Contrast and sizing proposals

- Candidate body `#1D2B40` on white, strong; secondary `#64748B` on white ~4.76:1. Avoid pale gray for important conditions and do not use green/red without text/symbol confirmation.
- Target minimum 48×48dp controls, support text scaling, meaningful loading/disabled/alert semantics, accessible alternate text for informative image and text equivalents for audio-reliant cues. *Targets to verify*, not already achieved.
- No real user participants (`n=0`), real Android devices (`n=0`), or pilot data. Existing two viewport *illustrations* are not physical device tests.

## QA prerequisites after design authorization

1. Text/copy audit all screens in VN, long/translated content in EN; score disclaimer and no unauthorized ETS brand claims.
2. Focus/large-text/table image and device density reviews for W-02A, plus IA-B/W-02B short comparator if uncertainty persists.
3. Physical Android feedback for Reading and warning comprehension; short voluntary walkthrough rather than a 120-min mock.
4. All real QA-01..08 content+software checks at release-appropriate checkpoint; do not close I01..I08 based on screenshots.
5. Preserve immutable Stage03 signed baseline and defer all budget matters until PO expressly reopens them.
