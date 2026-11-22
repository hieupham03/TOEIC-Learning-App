# AGENTS.md — Fast-track 48-hour Android internal preview / 14-day Play test-track readiness

## Current PO directive, 2026-11-22

The PO demands a **small 2-person internal trial build by 2026-11-24** and a **Google Play-track-ready package by 2026-12-06**, with larger autonomous Codex prompts and fewer microapprovals. **Active working branch: development/fasttrack-48h-preview.**

Binding engineering workplan: docs/STAGE05_FASTTRACK_48H_PREVIEW_14D_PLAY_PLAN_V0.1.md. Codex handoff: codex_handoff/FASTTRACK_48H_AND_14D_EXECUTION_V0.1.md. **READ BOTH BEFORE CODING**. Code source base: a0253b5e899b643ecc261323b603db3cca1073fc, including safe crawler and offline ingestion tools. Work through FAST-01 → FAST-04, with 48-hour preview tasks first.

This is permission to advance *reversible engineering* for an offline bounded internal demonstration and Play packaging preparation. It is NOT a waiver of signed baseline/CP, permission to label actual content QA-ready, public distribution, paid procurement, production authentication or formal pilot. The user wants speed and quality, not fabricated green status.

## Priorities

**FAST-01 + FAST-02 = urgent:** usable responsive Android offline demo, safe session interactions, truthful Listening/Reading synthetic practice labels, real debug APK and unit/emulator checks, concise exact evidence, P0/P1 bug fixes. Original WAV tones allowed; real user-sourced Zenlish MP3 and questions still stored in ignored .tooling with unverified answer keys. No shipping or exposing those as verified. If a material gate blocks real content, mark BLOCKED and use safe fixtures; do not silently change QA status. Any app-private preview selection storage must be checked, local-only, clearable and never represented as authoritative remote ACK. **Two real-device / two-person observation needs explicit consent and a recorded scoped authorization; do not claim formal QA pilot.**

**FAST-03 + FAST-04 = next:** current Google Play new mobile apps target API 36+; existing app targetSdk 35 needs upgrade. Test API36 UI/lifecycle, prepare safe local AAB/signing checklist, Privacy/Data safety/store assets drafts based on real SDKs, run all tests and report. No use of Play Console credentials or upload without explicit PO account approval. Newly registered personal Play accounts may require 12 continuously opted-in closed testers/14 days and production-access approval, so do not promise public Production in two weeks.

## STOP conditions / non-negotiable control

Maintain signed Vision/PRD/SRS/Acceptance/Design/UI-G bytes; Stage05 still CONDITIONAL PASS for Development transition; G05-CP01..08 and prior CPs active, POL01..16 open, 2 independent 200-question Full Mock A/B B1 content NOT QA-approved, budget DEFERRED. Do not unlock Full Mock, invent answers, claim official ETS score or comparable result, create backend/auth/cloud/official durable answer ACK/clock, embed unaudited media, stage actual ECP/QA/pilot, publish/release, spend money, broaden ingestion, or implement unrelated CX-05..09 as production behavior without separate material PO decision.

Public GitHub repo: commit only safe source, synthetic tests, reports and allowed metadata; keep APK/AAB, keystore, scraped questions/audio/images, raw logs and actual personal data LOCAL in ignored directories. If tools/testers/permissions unavailable, record NOT_RUN or BLOCKED instead of guessing. Fix small reversible technical errors autonomously; do not ask approval for every task; finish one slice completely before starting the next.
