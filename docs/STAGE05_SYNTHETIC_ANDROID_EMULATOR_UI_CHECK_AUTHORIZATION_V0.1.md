# Stage05 — Synthetic Android Emulator UI Engineering Check V0.1

**Status: PO CHAT-AUTHORIZED, ENGINEERING-ONLY.** The Product Owner replied **"ok hãy làm đi"** after the assistant proposed **one bounded round of Android UI verification with synthetic data**, following Beta BUI-01..03 Engineering Closure. This allows *local Android Emulator UI smoke inspection* only, not formal ECP/QA, learner tests, device acceptance, a pilot or a release. This file logs the scope; it is not an independently signed formal QA decision.

**Source baseline:** Beta branch `development/beta-reading-ui`, commit `cd2fc2e97bcf6f5a1e7cd1e30098c62de0f83024`. Execute on `validation/android-ui-synthetic`. Do not rewrite/merge historical Alpha/Beta baselines as part of this check.

## Purpose

Check that the existing **synthetic-only** Android app can be launched and navigated *in a local Android Emulator*, and observe gross Reading layout, font scaling, tap targets and in-session navigation. These are engineering observations. A build/unit-test PASS never substitutes for UI observation; an emulator observation never substitutes for real-device, learner or accessibility acceptance.

## Authorized bounded tasks

**EUI-01 — Environment & baseline:** On the user's local development workstation, verify JDK/SDK/Gradle availability, source HEAD and no forbidden Android permissions. Build the existing Debug APK and run local JVM unit tests and Alpha/Beta source guards. Use only free, local tooling already available or explicitly zero-cost Android SDK packages; no paid resources or cloud device farms.

**EUI-02 — Local emulator UI smoke:**
- Prefer **two different emulator screen-width contexts**, one compact (~360–393dp) and one wider (>= 400dp), subject to locally available AVDs; note actual `wm size`, `wm density`, API, measured logical width and any setup blocker. Do **not** fabricate two contexts from one unmeasured device.
- For each, launch the current synthetic app and check: three tabs; Part 1–4 unavailable; Part 5 synthetic select + explicit sample explanation; Part 6 and Part 7 Reading passage/question transitions and return-to-passage position; Full Mock A/B disabled and clear not-QA-ready copy.
- In at least one emulator context, try ordinary font scale (1.0) and enlarged text (e.g., 1.3 or 1.5 if supported), capturing source-labelled observations of clipping, scrolling, contrast, labels and minimum tap-target intent. Use visual inspection rather than asserting accessibility PASS.
- Check wide Reading content measure *visually* after the Beta modifier fix. Do not claim the exact 720dp cap was proved without measurements.
- Any crashes, blockages, truncation or navigation regressions: capture reproducible steps and fix only **small reversible UI defects within existing BUI-01..03**; re-run internal build/unit tests. Do not broaden functionality.

**EUI-03 — Evidence & honest report:**
- Record actual commands, exit codes, local emulator/AVD/API/scale characteristics, screenshots/logcat paths and SHA-256 of generated APK if built.
- Screenshots must contain **synthetic content only**, no personal information, accounts or live credentials. Keep emulator screenshots, raw logcat and APK **local**; do not publish them to the currently public repository. A PO-controlled private storage location may be used in the future, with specific approval.
- Commit only safe source fixes and a **text-only** report `docs/STAGE05_SYNTHETIC_ANDROID_EMULATOR_UI_ENGINEERING_REPORT_V0.1.md` to this branch. Clearly distinguish **OBSERVED / PASS / FAIL / BLOCKED / NOT RUN**, do not claim formal QA/ECP/device/learner acceptance.
- When screenshots cannot be shared here, do not present their absence as verified visual evidence.

## Stop conditions / not authorized

- **No real Android phone** (user's approval is implemented with the narrower emulator-only option), no learner, external testers, personal/production content, real B1 or media.
- **No formal ECP-00..06, QA-01..08, full acceptance, pilot, performance certification, security/privacy validation, release/Play Store publishing.**
- **No new CX-04..CX-09, Listening, media, real Full Mock, account, authentication, backend/API/remote DB, persistent learner state, durable ACK, authoritative clock, ARCH03 option selection or costs.**
- **No changing any signed baseline, G05-CP01..08, pre-existing CPs, POL01..16, B1 availability or DEFERRED budget.**
- If emulator cannot be started or the system image is unavailable at zero cost, mark **BLOCKED** and report; do not silently substitute screenshots, simulator claims or run device tests.

## Acceptance of this limited work package

The work package is considered **engineering evidence complete**, **not QA PASS**, only when EUI-01..03 have truthful results and the report identifies any not-run contexts, remaining defects and proof gaps. A nonfunctional emulator is a blocker and does not count as a completed UI inspection. Stop and return for a material PO decision before any further scope or formal test.

**GitHub handoff:** `AGENTS.md` on this branch points Codex to this scope. Codes, repo credentials and local keys must not be committed.
