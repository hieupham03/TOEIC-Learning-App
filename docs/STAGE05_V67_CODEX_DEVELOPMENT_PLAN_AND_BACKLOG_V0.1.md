# Stage05 V6.7 — Codex Development Handoff Backlog (not execution permission)

**Status:** PREPARED FOR CODEX, NOT STARTED. Scope follows official FR-001..FR-019, 13 NFR, signed BR-01..BR-10, AT-01..AT-19 and approved design V0.3.

## Incremental vertical slices and permissions

| Task | Priority | Target | FR / AT | Done evidence required | Current authority |
|---|---|---|---|---|---|
| CX-00 | P0 | Repo/toolchain skeleton + Compose navigation/theme + synthetic three-tab shell | FR001, FR002, FR017 / AT01, AT02, AT17 | Gradle build in Codex environment, unit/previews if available; screenshots labelled synthetic; no real data | **PENDING PO ALPHA AUTHORIZATION** |
| CX-01 | P0 | Content availability/QA-state placeholders; practice Part selection, read-only fixtures | FR002, FR015, FR017 / AT02, AT15, AT17 | Block unready content; no B1 exposure, no fake QA-ready | PENDING PO ALPHA AUTHORIZATION |
| CX-02 | P0 | One Part practice vertical slice: selection, choices, deterministic result under synthetic verified-key fixture | FR005–009 / AT05–09 | Unit tests, provenance labels; does not imply durable production ACK | Future authorization |
| CX-03 | P0 | Reading Part6/7 long passage, context return / large font | FR004, FR019 / AT04, AT19 | 2+ Android contexts before usability PASS; no actual PASS without tests | Future authorization |
| CX-04 | P0 | Listening Part sequence and media playback contract | FR003, FR011 / AT03, AT11 | audio mapping proof; signed playback policy for clean full mock | Future authorization |
| CX-05 | P0 | Answer state + learner/attempt/version binding & unknown ACK states | FR005, FR018, FR019 / AT05, AT18, AT19 | prove no false confirmed/double result with signed evidence; no backend chosen | Future authorization |
| CX-06 | P0 | Full Mock A/B 200Q orchestration, Listening (~45) / Reading 75; integrity states | FR010–013, FR019 / AT10–13,19 | evidence-based timing authority & FM checks; content QA first for any real B1 publication | Future authorization |
| CX-07 | P1 | Raw results, history, error review, key revisions, rule-based suggestions | FR006–008, FR012–016 / AT06–08,12–16 | no ETS conversion; historical key/version provenance | Future authorization |
| CX-08 | P0 | Privacy/account isolation, deletion/retention, integration & QA gates | FR018–019 / AT18–19 | actual signed data-copy inventory, privacy QA, deletion evidence | Future authorization |
| CX-09 | P1 | Pilot readiness on real Android/learners 2–5, 4 weeks | BR09, AC & QA01..08 | separately approved data/device/learner tests, no silent PASS | Future authorization |

## Definition of Ready

Read signed baselines, map FR/AT and UI state, identify synthetic vs real data, declare allowed dependencies, known policy blockers, negative tests, and expected output. No task may silently change 2×200 B1, privacy/deletion or scoring policy.

## Definition of Done per Codex task

- Compile/test **only if actually run**; report commands and truthful results; do not fabricate emulator/device tests.
- Source files, changeset and tests trace to requirement IDs; no synthetic fixture marked QA approved.
- UI-G01..16: no icon clutter, one font family, restrained teal palette, accessibility labels/status.
- Negative states included: missing content, missing/late ACK, unfinished/mock invalid, absent vetted explanation.
- No credentials/tokens/vendor keys or copied real site content in repo; all data family boundaries preserved as future obligations.

## First safe boundary

If PO authorizes **Alpha CX-00..CX-03**, Codex MAY scaffold and build the synthetic UI/Part practice/Reading slices in sequence, using synthetic data and engineering unit tests only, but MUST NOT implement actual durable ACK, timer, mock result, remote backend, authentication, production DB schema, scoring with real B1 content, or access a device. Version selection occurs in coding environment and is reported, not invented in advance.
