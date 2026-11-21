# Stage05 V6.7 — Preliminary Stack Decision ADR-TECH-001 (NOT an architecture selection)

**Status:** TECHNICAL DIRECTION FOR HANDOFF, REVERSIBLE; PO material gate/development authorization pending. This is not an ARCH03-A/B/C decision, a cloud/provider selection, a production architecture baseline or a clock/ACK policy decision.

## Why this app is Android-specific

Signed MVP is Android online-first (family pilot, 2–5 users), not iOS/multi-platform. Full Mock 2 × independent 200 questions, 100 L ~45 min, 100 R 75 min, strict integrity across interrupted sessions, durable ACK/UNKNOWN semantics, native Android lifecycle/audio/accessibility. The app's visual baseline favors legible long Reading and minimal chrome. Technical priority: transparency and reproducible verification over broad platform reach.

## UI-platform decision for Codex preparation

| Criterion | Android Native: Kotlin + Jetpack Compose | Flutter: Dart |
|---|---|---|
| Android-specific lifecycle / foreground audio | Access platform APIs directly; still requires correct design/testing | Supported through packages/platform channels; more bridge code for exceptional flows |
| MVP Android-only | Matches target without a secondary cross-platform build layer | Cross-platform benefit currently unused |
| Accessibility / long Reading | Compose semantics and native integrations, device QA mandatory | Flutter semantics supported, device QA mandatory |
| Review of generated app with Codex | First-party Android patterns, unidirectional state, strong typed Kotlin | Productive UI iteration but additional ecosystem/plugin choices |
| UI visual reference `speak_up_flutter` | Can reproduce design direction without copying code/assets | Existing sample shares framework, but does not bind product architecture |

**Proposed engineering default:** **Kotlin + Jetpack Compose + Material 3, AndroidX ViewModel, coroutines/Flow, unidirectional state flow**, with modularized responsibilities and immutable domain event/result models. Android Media3 is a **candidate audio dependency**, not a guarantee of uninterrupted playback. AndroidX Room is a **candidate device-side persistence component** for recoverability and verifiable transaction tests, not evidence of server ACK and not a declaration that local writes are authoritative for clean Full Mock. Avoid pinning library versions until Codex initializes against current official stable toolchain.

**Not decided:** backend/cloud vendor, remote database, authentication provider, remote API contract, synchronization conflict resolution, durable ACK authority, clock authority, anti-tamper assurance, grace and drift values, actual production trust option ARCH03-A/B/C. These each have pending evidence and approval gates. A local composable UI or mocked interface is not a complete architecture.

## Layers & interfaces (non-binding, to minimize lock-in)

- **UI**: Compose views, strongly typed immutable UI state; display `CHOSEN_LOCAL`, `PENDING`, `CONFIRMED`, `UNKNOWN`, `FAILED` only when appropriate; never turn CHOSEN_LOCAL into CONFIRMED without backing evidence.
- **Domain contracts**: learner ID, content/form/key version, attempt, item identity, event provenance; no UI coupling to repository implementation.
- **Ports**: `ContentCatalogue`, `AnswerEvidenceRepository`, `AttemptIntegrityObserver`, `AudioPlaybackControl`, `ResultsView`, `LearnerDataBoundary`; behavior contracts not provider choices.
- **Data adapters**: initially synthetic isolated fixtures and fake implementations **only if development authorized**; local/remote adapters must wait for scoped authorization and relevant policy.
- **Verification seam**: deterministic fixtures for UNKNOWN, delayed ACK, duplicate submission, reboot simulation (simulation is not proof of real reboot), incomplete content, non-comparable result.

## Official reference links (consult current pages before implementation)

- Android architecture guidance: https://developer.android.com/topic/architecture/recommendations
- Compose-first: https://developer.android.com/develop/ui/compose/first
- UI unidirectional state: https://developer.android.com/topic/architecture/ui-layer
- Android Media3: https://developer.android.com/media/media3
- Android Room: https://developer.android.com/training/data-storage/room
- Flutter platform channels (comparison): https://docs.flutter.dev/platform-integration/platform-channels

**Revisit triggers:** requirement expands to iOS, native platform media proves infeasible, new remote trust evidence changes A/B/C preference, user agrees to a security policy, licensing/dependencies change. No performance or price claim without measured source.
