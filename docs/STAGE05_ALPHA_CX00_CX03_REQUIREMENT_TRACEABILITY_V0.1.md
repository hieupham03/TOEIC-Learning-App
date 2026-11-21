# Development Alpha CX-00–CX-03 — Requirement/Acceptance Trace V0.1

**Evidence status:** `SOURCE CREATED / CORE JVM CHECKED`; **Android build NOT RUN**, **device UX NOT RUN**, **formal QA NOT RUN**. Existing signed FR/AT identifiers are tracing targets, not PASS statements.

| Task | Source paths | Signed FR/AT intentions | Engineering checks observed | Still open |
|---|---|---|---|---|
| CX-00 | `android-app/app/src/main/java/**/ui/AlphaApp.kt`, `AlphaTheme.kt`, Gradle and manifest | FR-001/002/017; AT-01/02/17 | Three IA-A text-labelled tabs, calm theme, no INTERNET permission; 10 static scope guards | Android build, UI on real phone, accessibility and visual QA |
| CX-01 | `android-app/app/src/main/java/**/domain/SyntheticCatalogue.kt`, PartPicker/MockBlockedScreen | FR-002/015/017; AT-02/15/17 | Part1–4 blocked; mock A/B blocked; demo-only Part5–7; unit assertions pass | Actual two B1 forms unshipped, item-by-item QA not performed |
| CX-02 | `domain/AlphaModels.kt`, PracticeScreen, QuestionPanel | FR-005..009; AT-05..09 | Selection temporary; no sample feedback until explicit choice/reveal; 22 pure Kotlin assertions | No real persistence/ACK, official content or production scoring |
| CX-03 | ReadingScreen, ReadingContext, demo text | FR-004/019; AT-04/19 | Part6/7 long original passage; linked question ID; in-screen scroll index/offset; pure Kotlin assertions | Android Back/rotation/process-death, large-font TalkBack/device contexts NOT RUN |

## Rule mapping

- UI-G01..16: no needless icons/gradients, single sans family, restrained teal, semantics and 48dp interactive targets targeted, demo labels and mock blocked.
- P05/P06/P07/P08 documentary review policy remains active for claims; no durable ACK or authoritative time source has been implemented.
- UX04-I01..08 / UIA-01..08 and all signed Stage02/03/04/05 conditions remain open.
