# Stage05 — Two-person daily-study MVP, Google Play DEFERRED (2026-11-22)

**Latest explicit PO direction:** "hoàn thiện sản phẩm để 2 người bọn tôi có thể dùng hết tính năng, học tập mượt đã. Việc up lên google play tính sau".

**Binding priority:** **Full usable study product for two actual people first**. Pause Play Console, AAB/signing/store listing, external marketing and Production release. Work on **`development/two-user-study-mvp`**, forked from accepted Fast Track two-phone preview `ebeb7e06b66757aa2be5e92ce48be929c58be995`. The 0.2.1 two-phone PO success is retained. Treat this document as later PO work-priority instruction; do **not** silently alter the signed Stage03/04 business MVP baseline or claim formal Stage05 QA/Production PASS.

## User-visible definition of DONE

On **each of two separate Android phones**:
- **Part1–7 real study**: discover and select part, start/continue sessions with actual locally provided content packs; Part1 image, Part1–4 playable English speech, Part3/4 group clip to 3 items, Reading P5–7 passages and structured multi-item groups.
- **Answer/practice**: select/change, previous/next, skip and jump-to-question, finish with unambiguous state; reveal correct/incorrect **only when a source-backed reviewed answer key exists**; explanatory text **only if supplied/reviewed**, otherwise "Chưa có lời giải".
- **Study history**: persist selections, completed sessions, per-Part correct/attempted/accuracy, recent mistakes, review wrong answers and resumable unfinished work, stable after app process death/reboot and app upgrade. **One local learner profile per installation/device**; no syncing between the two phones, remote accounts, Cloud backend or claims of acknowledged remote writes.
- **Real study routine**: per-day study goal, simple deterministic/reproducible next-Part recommendation from weak areas and missed items, review list/bookmarks, manual clearing/reset or privacy controls.
- **Two full practice mocks A/B**: separate offline engine with item layout exactly 200 per form and 6/25/39/30/30/16/54 Part distribution, 100 Listening +100 Reading, about 45m +75m mode; sample navigation, lifecycle/pause policy, no loss of prior answers, result raw correct/200 and Part breakdown only. **Never silently unlock a deficient form**. The engine/UI can be built and tested on original synthetic end-to-end test fixtures while actual A/B release remains LOCKED until complete independent 400-item/asset QA + answer integrity + media-group checks + no overlap; no ETS-equivalent 10–990 claims. For private study, visibly distinguish personal practice scoring from official test results. No fake answer keys or invented pass.
- **Smooth daily experience**: 360dp + large text and tablet; navigation, audio interruption/seek/replay rules as appropriate for practice vs full mock, error and offline messaging, fast launch, no known P0/P1 crash/memory/answer-loss; two-person real phone exploratory check.
- No mandatory internet connection **for this separate two-user study build**. This is a scoped personal-use variant, NOT a silent change to the signed **online-first** baseline M01/M07 or formal backend ACK/time policy.

## Most important gaps at current HEAD

1. Current production-like Android build has only **4 synthetic audio tones** for Listening, 2 synthetic P5 items, 2 P6, 3 P7; authentic Part3 Q32–34 MP3 + text is in distinct LOCAL lab build only. Source content is local in `android-app/.tooling`; Part1/2 acquisition partial; all 8 known Zenlish answer keys UNVERIFIED.
2. Current app state is Compose `remember` and lost when app closes; no Room/SQLite/DataStore, no history and no offline local profiles.
3. Full Mock A/B locked; no playable, verified 200+200 forms.
4. Play readiness is separate #8 and **on hold at PO request**.

## Autonomous implementation batches, in this order — prioritize working product over docs

### STUDY-01 / prompt 1 — Persisted study sessions and results (P0)

- Preserve existing 0.2.1 demo variants and signed baselines; implement **typed generic content models and repositories** for P1–7 + local Room/SQLite for **local user settings, attempts, answer selections, bookmarks, reviewed answer provenance, history, app-close process-death recovery and migration tests**. Prefer stable AndroidX OSS packages; no paid SDK or backend.
- Implement a real usable flow: Home -> select Part -> question group (audio/photo/passage where appropriate) -> select -> navigate -> finish -> review -> history -> retry errors; detailed results raw counts only if source-backed key is `VERIFIED`.
- Use safe self-authored synthetic fixtures to build/test engine first. Do NOT block structural engineering just because the source sample answer key is unknown. Require app storage error handling, device backup/privacy truthfulness, no duplication across records, session deletion/reset confirmation and launch after process death.
- Add deterministic tests for interruption/relaunch; preserve old DEMO regression, avoid breaking existing Play AAB. No official mock readiness claims.

### STUDY-02 / prompt 2 — Real Listening+Reading P1–7 content pipeline (P0)

- Reuse local `android-app/.tooling/listening-overnight/` sample and its validated manifest/normalizer. Extend local-only *source-agnostic* import adapters for **already owner-affirmed sources** Zenlish / TheTOEICLab / Study4. No generic copyright re-research; PO declared rights handled 100%. Nonetheless preserve source hashes and correctness evidence.
- **Actively assemble a useful, bounded first batch of actual practice content across all P1–7**, not just tone. Work in **finite batches**, with manifest/answer/media checks and exact success counts; do not call a group QA-ready if its answer key is unknown. Obey site robots/access limits; do not defeat CAPTCHA, 403/429 or use credentials without explicit access approval. Avoid endless crawling. A source that only has labels may be used for **unscored listening practice**, not fake scoring.
- Bundle owner-controlled real content **only in ignored local installable two-user build variants**. Public GitHub contains import code, schema, synthetic fixtures and aggregated technical reports, not copied source HTML/audio/questions/keys or private logs. Source pack version/hash, per-Part question count, actual keys/QA state, image/media bindings and content corrections are required in private packs.
- Keep import/build reproducible and updateable offline without re-downloading all content. Test malformed assets, corrupt MP3, missing image/audio, repeated IDs, wrong passage/group, unknown answer keys and content pack upgrades. Generate actual locally installable user study APK when checks pass, with clear per-Part coverage ("X câu đã xác minh") and warnings for incomplete packs.

### STUDY-03 / prompt 3 — Full Mock A/B engine, offline safety and content completeness (P1)

- Implement mock **engine UI, offline persistence, countdown/session-state/restoration/correction handling** and separate form A/B using **synthetic 200-item fixture manifests for automated engine tests only**; never make synthetic forms available as authentic real exams.
- Input **two separate 200-item actual form inventories** supplied/assembled from PO-controlled sources, *without mixing bank practice and pre/post mock items*. Run strict checks for Part distribution, duplicate/overlap, all verified keys, audio/image/passage group mapping, source version, full timing and score reporting. If 400 real reviewed questions are not available, preserve real A/B lock and publish exact deficits rather than inventing.
- Raw score and Part breakdown for verified completed real forms only; no ETS scaled equivalent or "official" pass claim; restart/restore user attempt must not lose answers after process death. Handle device reboot/wall-clock change transparently and never call the local timer an authoritative server clock.
- Stress tests: 200 answers, repeated 45+75m state transitions simulated, interrupted playback, 1–2 device loss/resume, migration, multiple attempts, duplicate content, partial pack, cleanup.

### STUDY-04 / prompt 4 — Two-phone quality, polish, ready-to-study handoff (P1)

- Review and improve the *existing Compose visual design* within Stage04 UI-G guardrails; clean, practical reading/listening UX with bottom navigation and large accessible controls. Avoid redesign that disrupts working Android architecture.
- Run unit tests, 40+ ingestion Python tests, Gradle Debug / private Study variants / relevant guards, emulator API34/API36, font1.5, 360dp/800dp, audio completion/interrupt/error, storage/reboot/upgrade, 200-item mock engine synthetic checks.
- Produce private local ZIP/APKs for **two** independent installs; include concise installation/update procedure, local backup/export only if safely implemented and tested, per-device ~15–20-min test checklist and bug collection.
- Have the two consenting real users try it. **Only PO may report actual two-phone outcome**. Fix reproducible P0/P1 defects and report what functions/Part content are *actually* usable vs BLOCKED.
- Deliver one short `docs/STAGE05_TWO_USER_STUDY_ENGINEERING_REPORT_V0.1.md` with verified Part coverage, pack-level status, real question counts, history persistence tests, mock A/B readiness, build hashes, tests and actual two-device status, with no unverified PASS.

## No-go rules that remain binding

- **Stage05 D05-DEV-GATE-012 conditional DEVELOPMENT authority**, CPs active, POL01..16 OPEN, no formal ECP/QA PASS. The latest PO wants more engineering scope to support personal learning, but does not explicitly waive signed acceptance conditions. Do not modify signed baseline/guardrail files or claim formal online-first MVP release acceptance without a separate documented PO scope decision.
- No public Google Play submission or store-policy work until PO resumes #8. No new backend, cloud account, payment, commercial release or budget commitments. No secret/user information in the public repo. Generic copyright research is not needed: owner attestation accepted.
- Do not invent answer keys, explanations, or review approvals; do not unlock real Full Mock without two independent QA-ready 200-question forms. **Feature code can be completed and tested now; content readiness is a separate factual gate**.
- Don't force many small PO questions. If source content is unavailable, report exactly and continue with other independent work. Each prompt: IMPLEMENT -> TEST -> FIX -> REPORT -> COMMIT/PUSH; stop after finite scope, no indefinite retry.
