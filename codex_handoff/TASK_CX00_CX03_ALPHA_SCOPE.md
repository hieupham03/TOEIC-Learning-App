# Development Alpha CX-00..CX-03 — PENDING PO SIGN-OFF

**Scope:** One bounded Codex execution authorization covering four synthetic-only UI/Reading milestones. Codex can choose minor implementation details and run local engineering build/unit tests without repeated PO approval **after** PO signs the Stage05 conditional development-only Gate/Alpha decision. This document is not execution permission.

| Task | Scope | Review evidence |
|---|---|---|
| CX-00 | Native Kotlin/Compose repository scaffold, 3-tab nav, visual tokens; synthetic states | Build logs, app preview under dev simulator only if separately in-scope; no real device claim |
| CX-01 | Part selection, only mock readiness labels/QA blockers, practice bank distinct from two Full Mock forms | Tests show NOT_QA_READY items blocked |
| CX-02 | Synthetic practice one-item/Part flow, selection and optional explanation when verified **in fixture only** | Synthetic tests for answer status and wrong explanation blocked |
| CX-03 | Long-Reading Part6/7 multi-question context navigation and return to location under synthetic passages | Pure UI tests, text-size preview, must keep Android-real proof pending |

## Hard exclusions

No production authentication/accounts, production backend/API/DB, clock or ACK authority, real TOEIC/media assets or scraped content, full mock execution, secure deletion claims, actual ECP formal QA PASS, real device or learner test, external spending. Room/Media3 may be discussed but not implemented as production truth under Alpha.

## Finish line

One consolidated Alpha review: repo diff, commands run, build+unit test results if tools available, synthetic screenshot/visual QA, FR/AT trace, deviations from UI-G01..16 and next blocked boundaries. Stop before CX-04 and ask only for the next genuinely material authorization.
