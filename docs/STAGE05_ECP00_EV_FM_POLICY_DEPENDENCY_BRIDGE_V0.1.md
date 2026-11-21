# ECP-00 — EV/FM Policy Dependency Bridge V0.1

**Purpose:** show why ECP-00 policy is required **before certain evidence may be certified**, without pretending every FM depends on the same threshold. This is a *non-executed document crosswalk* over the approved ECP plan.

| Proposed execution stream | Primary EV/FMs | ECP-00 policy dependencies | Existing binding rule | Evidence now |
|---|---|---|---|---|
| **ECP-01 Mock/Listening** | EV01..04; FM01..05,18 | POL01..04,07..08,13 | Clean/comparable only when continuity proven; no arbitrary replay/pause | DOCUMENT ONLY / NOT RUN |
| **ECP-02 Answer ACK** | EV05..06; FM02,07,08,14 | POL05..08,09,15 | Durable ACK, truthful `đã lưu` / unknown state | DOCUMENT ONLY / NOT RUN |
| **ECP-03 Privacy/deletion** | EV07..08; FM09..11 | POL09..10,14..15 | Family isolation, ≤7-day deletion request, ≤30-day routine retention | DOCUMENT ONLY / NOT RUN |
| **ECP-04 Content/scoring** | EV09..11; FM06,12..14,16,17 | POL11..12,15 | B1 2×200, separated Part bank, vetted content and raw-score provenance | DOCUMENT ONLY / NOT RUN |
| **ECP-05 Reading/Android** | EV04,12; FM01,15,18 | POL03..04,13..15 | Controlled Design V0.3 and accessibility checks; no UI fake ACK | DOCUMENT ONLY / NOT RUN |
| **ECP-06 Fair adjudication** | EV01..12; FM01..18 | POL07..08,15..16 | Same falsifiers for A/B/C, no preference-derived win | DOCUMENT ONLY / NOT RUN |

**Mapping accounting:** the complete individual 12-EV/18-FM inventory remains in the *unchanged*, approved `STAGE05_EVIDENCE_CHECKPOINT_EV_FM_TRACEABILITY_V0.1.md`. This bridge summarizes policy dependencies; it is **not** a revised EV/FM mapping, nor a test execution plan. If a checkpoint has no real output, its result remains NOT RUN/BLOCKED as applicable, never PASS.
