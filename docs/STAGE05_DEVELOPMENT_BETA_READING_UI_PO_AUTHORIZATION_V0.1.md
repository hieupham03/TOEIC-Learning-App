# Stage05 — Development Beta Reading UI Authorization V0.1

**Decision origin:** Product Owner replied **"có"** in the project conversation after the 2026-11-21 Alpha CX-00..CX-03 Engineering Closure review, consenting to a **new, strictly bounded Development scope** in the immediately proposed direction: synthetic Reading UI, accessibility and responsive layout. This is a **chat-confirmed PO development authorization** recorded for implementation traceability. It is **not** a new Stage05 unconditional Gate PASS, an ECP or formal QA authorization, a release/pilot approval, or a change to any signed baseline.

**Scope status:** AUTHORIZED **for bounded internal Development only**, effective on branch `development/beta-reading-ui`. This record does not imply that CodeX has executed Beta or that Beta passed any test.

## Fixed workstream IDs — do not reuse CX-04

The signed Stage05 V6.7 backlog already assigns **CX-04 to Listening/media**; CX-04..CX-09 are not approved by this Beta authorization. Use a separate non-colliding series:

| ID | Allowed outcome | References | Required internal evidence |
|---|---|---|---|
| **BUI-01** | Improve the existing **synthetic Part 6/7 Reading** passage/question Compose layout, preserve the in-session passage scroll/anchor, and make long-text navigation understandable; no process-death recovery guarantee | Existing Alpha CX-03, FR-004 / AT-04; Design V0.3/UI-G01..16 | Source diff, deterministic state unit tests, truthful behavior notes |
| **BUI-02** | Source-level responsive UI and accessibility hardening for synthetic Reading and existing Alpha navigation: Compose spacing, font scaling-aware layout, legible labels/semantics, focus/read order review, minimum interactive targets targeted in source, restrained teal tokens | Existing Alpha CX-00/CX-03, signed Design V0.3/UI-G01..16; **no full FR/AT PASS claim** | Static/source checklist and optional local IDE Compose Preview inspection, explicitly labelled **engineering only** |
| **BUI-03** | Expand deterministic **local JVM** tests and static scope guards for BUI-01/02; fix reversible build/test issues and produce a consolidated Beta Engineering report | Internal development safeguard, **not** ECP/QA | Exit codes, Kotlin smoke, `:app:assembleDebug`, `:app:testDebugUnitTest`, source guard, changed paths, evidence gaps |

Existing CX-00..03 synthetic fixtures, disabled Part 1..4 and disabled Full Mock A/B must remain restricted. UI changes may refactor Composables within this scope, but must not introduce production state, live data or unapproved behaviors.

## Permitted verification boundary

- Kotlin/JDK local tests, Android SDK 36 + Gradle 8.13 engineering build and Gradle JVM unit tests, source-level lint/scope guards.
- **Optional** IDE Compose Preview / layout inspection using synthetic data only; preview render notes or screenshots, if taken, are *internal engineering observations*, never a QA/UI acceptance PASS.
- No real Android phone **or emulator** execution, instrumentation, learner usability or formal accessibility acceptance without separate PO permission. Targeting 48dp, TalkBack-friendly semantics, scaled text or multiple widths is not proof that they passed on a device.

## Explicitly NOT authorized

- **CX-04 Listening/media or any CX-04..CX-09 implementation**; actual media/audio, B1 content, live Full Mock, ETS scoring or content QA.
- New backend, API, authentication, remote DB, accounts, learner/production data, persistent answers, durable ACK, clock/time authority, ARCH03 A/B/C selection or ARCH04.
- ECP-00..06, EV/FM execution, QA-01..08, Android device/emulator or learner test, pilot/release activities, contracts, purchases, budget spend.
- Editing signed Vision/PRD/SRS/Acceptance/Design baseline bytes or changing business policy thresholds.

## Active controls and completion

Stage05 Gate remains **CONDITIONAL PASS for development transition only**. G05-CP01..08 and Stage02/03/04 conditions, UI guardrails, POL01..16 open decisions, B1 unreleased 2x200 inventory, QA not PASS and budget **DEFERRED** remain unchanged.

Codex may self-manage small reversible BUI-01..03 implementation decisions and run the permitted engineering checks without per-task PO approval. On completion, commit only source/documentation/test changes to the Beta branch, do **not** commit local APK/build outputs, report actual PASS/FAIL/NOT RUN and a consolidated Beta Engineering Closure. Stop before any non-BUI feature or formal testing. Next materially new authority returns to PO.

**Source control baseline:** Alpha engineering closure commit `199bc0dae751e33b2f7e1306f877f461207d2cb8`. Do not rewrite Alpha history or re-label Alpha outcomes as formal QA.
