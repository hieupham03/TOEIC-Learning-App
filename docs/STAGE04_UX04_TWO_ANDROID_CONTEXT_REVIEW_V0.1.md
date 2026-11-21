# Stage 04 — Two Android Contexts, Illustrative Layout Review V0.1

**Important terminology:** This is a **desk inspection of two paper/prototype viewports**, **not physical Android device usability testing**. G03-CP03 still requires real device contexts before pilot.

| Review context | Proxy in clickable PDF | What could be inspected | What remains unknown |
|---|---|---|---|
| **C1 — Compact phone** | Main PDF canvas ≈390×840 pt as illustration of ≈360×780dp use; base text sizing | Card ordering, visible Practice/Full Mock entry, warning text fitting, passage/answer tabs in compact form | Real dp scaling, device cutouts, IME, TalkBack, real font enlargement, tap targets, runtime scroll |
| **C2 — Larger Android, larger text** | LARGEPASS + LARGEQ pages ≈440×955 pt simulating ≈412×915dp | Passage, table, question, anchor concept with longer line wrapping and larger typography | True adaptive layouts, text scaling on Android, system bars, screen-reader focus, physical readability |

## Inspection notes

- Both illustrative views maintain a recognizable **passage → question → return-to-passage** route; link navigation works at PDF level.
- On compact prototype, Reading passage and question are each shown as a complete view rather than forcing a permanent two-column split; this reduces *illustrated* crowding, not proven reading comfort.
- On larger prototype, text and associated table remain described without being clipped in inspected screenshots; actual partial/longer content overflow remains **OPEN**.
- Need to confirm **real scrolling, zoom, landscape, text enlargement, focus order, Android back behavior, real keyboard and TalkBack** later. No screen-reader or two-device test has been conducted.

**Status:** Desk layout review complete; actual Android usability/QA-08 NOT EXECUTED/PASS.
