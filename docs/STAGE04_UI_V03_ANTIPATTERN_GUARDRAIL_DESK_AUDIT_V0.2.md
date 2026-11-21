# Stage04 — UI-G01..16 Anti-Pattern Audit for V0.3 (Desk Only)

**Status:** Analyst visual and token audit only; no device/learner PASS, no certified WCAG conformance.

| Control | V0.3 design evidence | Desk disposition / later work |
|---|---|---|
| UI-G01 meaningful icons | Nine concept screens use chiefly back, radio and a restrained play sign | **Desk aligned**; confirm icon semantics on device |
| UI-G02 single font | All nine exact screen renders use **Inter** normal/semibold/bold | **Desk aligned**; Android platform fallback/vi glyphs later |
| UI-G03 restrained colors | Primary deep teal and neutrals; amber only for warnings, blue for score disclaimer | **Desk aligned**; verify full render contrast |
| UI-G04 no card soup | Card only for audio, selected answer, structured info and alerts | **Desk aligned**; watch repeated white panels |
| UI-G05 CTA hierarchy | One main action per view, except an outline alternate for save-unknown | **Desk aligned**; device text scaling later |
| UI-G06 exam focus | Full Mock excludes streak/mascot/replay controls and sets transparent integrity warning | **Desk aligned**; actual timer/audio future QA |
| UI-G07 spacing & typography | 390dp logical canvas, 20dp margins, consistent heading/CTA positions | **Desk aligned** at sample canvas; not verified 360/412dp |
| UI-G08 contrast & text | Semantic tokens; ink on white and white on teal strong | **Partial**; detailed rendered text and boundaries require device audit |
| UI-G09 truthful affordances | Semantic text labels alongside radio/save/CTA | **Desk aligned**; static buttons don't work |
| UI-G10 no Mock policy violation | No pause/replay in mock, no early key disclosure, no reset claim | **Desk aligned**, runtime untested |
| UI-G11 Reading context | W-02A retained from earlier approved UX direction | **Partial**, visual Reading anchor not revalidated in V0.3 |
| UI-G12 component states | Pending/ACK/unknown & interrupted/noncomparable distinct screens | **Desk aligned**, persistence untested |
| UI-G13 no phantom real content | Bottom `MẪU THIẾT KẾ`; mock counts + data explicitly demo | **Desk aligned**, do not present screenshots as actual behavior |
| UI-G14 locked MVP | No out-of-scope AI/iOS/auto-import features | **Desk aligned** |
| UI-G15 independent design | Screens are generated original vector/raster compositions, not traced other app artwork | **Desk aligned** |
| UI-G16 accessibility | 48dp target specified, one font, status includes words | **OPEN** device TalkBack, target measurements, large text, contrast and field testing |

**Decision recommendation:** Suitable for PO design-spec candidate review **with test conditions**, not for unconditional UI quality or Stage04 Gate PASS. `UIA-01..08` and `UX04-I01..08` remain tracked to actual confirmation/testing, not automatically CLOSED by better pictures.
