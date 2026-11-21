# Stage05 ARCH-01 — Conflict Watchlist and Undecided Engineering Questions V0.1

**Purpose:** identify apparently competing signed requirements and distinguish them from implementation decisions. **Not an architecture blueprint or selected technical approach.**

| Watch | Signed obligations that can appear to conflict | Current interpretation — no business rule change | Future proof question | Risk / evidence gate |
|---|---|---|---|---|
| CW-01 | Strict no-pause comparable Mock vs Android app/process/network interruptions | Time and integrity must not be silently reset; interrupted attempt classification remains explicit | How can a future build make timing evidence trustworthy when Android can reclaim a background process? | AD-01/04; AT-11/19; AC-08 |
| CW-02 | Online-first vs answers preserved across unstable connectivity | Confirmed ACK must remain truthful; selection and confirmed storage are distinct | What counts as durable ACK, and how is an ambiguous retry shown without double-writing? | AD-03/04; AT-05/19 |
| CW-03 | 100% released Full Mock content QA vs two inventories PO-confirmed | Inventory is acknowledged; independent QA must still occur before pilot content release | How is the future evidence chain recorded without demanding duplicate inventory work? | AD-07/08; QA-01..06 |
| CW-04 | Practice convenience vs pre-exposure/clean evaluation of two B1 forms | Practice bank cannot leak evaluated A/B items; two mocks remain required | Which evidence demonstrates set separation and version traceability? | AD-08; QA-05 |
| CW-05 | 7-day deletion + 30-day retention vs historical learning progress | Deletion/retention duties must be met; no exception invented | What account control / lawful exception mapping is needed before pilot? | AD-05/06; AT-18 |
| CW-06 | Cross-form comparison feature vs forms may differ in difficulty | Only raw descriptive comparisons; no official converted ETS score or causal improvement claim | How are form version and noncomparable attempts displayed and excluded? | AD-09/12; AT-12/13 |
| CW-07 | UI 'Đã xác nhận lưu' state vs no tested persistence | Static UI is illustrative; it cannot certify a successful write | How will future UI prove it received actual persistence ACK? | AD-03/12; UIA-03 |
| CW-08 | Goal/learning suggestions vs first-use missing data | Optional rule recommendation, learner may override; no runtime AI | What fallback is shown without a fake 15-minute user preference? | AD-11/12; UIA-01 |
| CW-09 | Key correction vs immutable historical scoring | Revised content/key cannot silently overwrite historic attempt results | How can a future result be traceable to content/key version and correction record? | AD-09/15; AT-16 |
| CW-10 | User needs long Reading on mobile vs limited screen space | W-02A preferred as signed design, IA-B/W-02B comparisons archived; must preserve original passage and position | How will scroll/anchor restoration be evaluated at large text on 2 Android contexts? | AD-10/13; QA-08 |

## Decisions that are **not** made at ARCH-01

- Framework/platform/runtime selection; cloud/local versus hybrid storage choice; server/client timing authority; schema, endpoints and auth provider; media pipeline design or technology.
- Exact timers/grace/latency/recovery and test thresholds; those belong to approved AC-08 test-plan checkpoint.
- Real person recruitment, app POC, paid services/quotations and content scraping.
- Waiving B1, signed privacy limits, mock integrity, raw-score-only policy, or CP/QA obligations.

## Proposed order of **feasibility study** — pending D05-ARCH-002

1. First investigate **integrity and data-trust feasibility** (AD-01..06,09,12), because these create the strictest business safety gates.
2. Then investigate content QA/versioning/reuse and long Reading/mobile accessibility (AD-07/08/10/13).
3. Then study scoring explainability, pilot metrics and cross-cutting compliance (AD-11/14..16).

This is a **research-priority recommendation only**, not a technical design choice. A different research sequence is available for PO decision in `D05-ARCH-002`.
