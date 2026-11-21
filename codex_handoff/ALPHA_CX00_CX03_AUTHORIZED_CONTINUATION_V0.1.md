# Development Alpha / Codex continuation — approval boundary V0.1

`D05-DEV-GATE-012=A` authorizes Alpha CX-00 through CX-03 and activates G05-CP01..08. This file is an addendum superseding the old **PREPARED; DO NOT EXECUTE YET** header in the preserved historical handoff. The old signed release history stays readable but cannot override latest PO authorization.

## Immediate Codex scope

1. Read `docs/PROJECT_STATE.md` first top block, signed Requirements/Design/UI-G and the new Stage05 Gate approval record.
2. Use `android-app/` Kotlin Compose scaffold, all content synthetic and visibly labelled. No real B1 materials.
3. Execute `scripts/run_pure_kotlin_core_checks.sh`, `scripts/check_alpha_scope.py`; configure Android SDK/Gradle where available and actually run `:app:assembleDebug :app:testDebugUnitTest`, log truthful output.
4. Fix reversible build/UI bugs only within CX00..03 and review app at multiple screen widths **only when expressly allowed by device/testing authority**; no real device/learner test under current grant.
5. Submit consolidated Alpha report. No CX04+ without next material PO authority.

**Unresolved:** ARCH03 A/B/C, clock/ACK authority, auth/backend/API/DB, all concrete policy and ECP/QA thresholds, two 200-item B1 forms' real per-item QA, pilot privacy verification, budget DEFERRED.
