# Stage05 ARCH-03 — Full FM01..18 Negative-case Comparison V0.1

**Status:** 18/18 signed ARCH02 falsifiers considered for all 3 conceptual options; **0/18 executed** and **zero runtime results observed**. Reuses `STAGE05_ARCH02_FAILURE_MODE_AND_EVIDENCE_MATRIX_V0.1.md` without changing acceptance or deadlines.

| FM | Adversarial scenario | EV link | ARCH03-A weakest point | ARCH03-B weakest point | ARCH03-C weakest point | Evidence checkpoint |
|---|---|---|---|---|---|---|
| FM-01 | App-switch during Listening | EV-02/04 | Local focus/playback event continuity not observed | Independent gap during app-switch may be unobserved | Conflicting source observations must not silently be clean | Android audio/QA-08 |
| FM-02 | Process reclaimed during Reading | EV-02/05 | Restore UI separate from persisted answers/timing | External events might be missing until reconnect | Partial history cannot be treated as continuous proof | Android/persistence QA-08 |
| FM-03 | Phone reboots mid-Reading | EV-01/03 | Since-boot elapsed cannot span reboot alone | Independent observations may lack outage interval | Reboot gap remains unknown absent approved authority | Timing QA-08 + PO threshold |
| FM-04 | User changes device clock | EV-01/03 | Local wall clock susceptible; no signed trusted source | Outside clock cannot be assumed authoritative | No automatic majority/first timestamp rule | Timing QA-08 + PO threshold |
| FM-05 | Incoming call steals audio focus | EV-04 | Local audible position and focus need trace | Remote playback record does not prove heard audio | No automatic clean outcome if events disagree | Audio QA-03/08 |
| FM-06 | Media missing/wrong clip | EV-09 | Pre-release local binding must show QA | Externally indexed assets still need version QA | Neither source majority replaces human key/media QA | Content QA-01..06 |
| FM-07 | Choose answer without connection | EV-05 | Local durability and learner binding not verified | No remote ACK must remain unconfirmed | Pending/unknown not a confirmed durable write | Persistence QA-08 |
| FM-08 | Write succeeds but ACK response is lost | EV-06 | Local acknowledgement status and retry provenance needed | Remote confirmation may be delayed | Contradictory/later ACK cannot double-count | Persistence QA-08 |
| FM-09 | Switch family learner mid-pending save | EV-07 | Per-learner local pending ownership needs test | Cross-user authorization/identity needed | Multi-context reconciliation must isolate both learners | Privacy QA-08 |
| FM-10 | Verified learner deletion request | EV-08 | Prove removal of device/backup copies | Prove removal of remote/backup copies | Prove scope of all in-scope copies | Privacy SOP + ≤7d audit |
| FM-11 | Retention check >30 days post pilot | EV-08 | Local copies must obey retention/exceptions | Remote copies must obey retention/exceptions | Aggregation cannot hide retained replicas | Post-pilot retention review |
| FM-12 | Answer key corrected after release | EV-10 | Original key/version and correction preserved | Remote key-history remains auditable | Cross-source score explanation cannot silently rewrite | QA-02/07 + content curator |
| FM-13 | Practice bank overlaps mock A/B | EV-11 | Local bank separation and overlap QA needed | Remote bank separation and overlap QA needed | Reconciling release paths does not prevent leakage | QA-05 before content release |
| FM-14 | Attempt submitted twice | EV-06/10 | Duplicate logical result proof missing | External dedup and late ACK proof missing | Cross-observation duplicate identity unverified | QA-07/08 |
| FM-15 | Long Reading large text + background | EV-12 | Anchor/scroll recovery on devices untested | External observation cannot prove readability | Additional sources do not guarantee anchor integrity | 2+ real Android contexts QA-08 |
| FM-16 | Unverified explanation displayed | EV-09 | QA gate for explanations must be proven | QA gate for remotely sourced explanations unproven | Conflicting QA metadata must fail closed | Content QA-02/06 |
| FM-17 | Different raw scores across forms | EV-10 | Local display must not imply equating | Independent results do not imply equating | Agreement across reports ≠ calibrated progress | Scoring QA-07 / pilot integrity |
| FM-18 | Target Android changes background rules | EV-04/12 | Local media lifecycle target/version untested | Outside claim cannot bypass platform audio limits | Correlation cannot repair OS focus limitations | Target/version review + QA-08 |

## Non-negotiable negative-case verdicts

- When future evidence is absent or contradictory, none of the three options may assume clean mock, durable saved answer, learner access, completed deletion, content QA PASS or official TOEIC-equivalent improvement.
- `FM-10/11` must honor the approved **7 calendar-day verified deletion** and ordinary **≤30-day post-pilot** policy; these are project commitments, not claimed test observations.
- `FM-03/04` cannot be called passed until a later PO decision specifies the necessary numeric tolerances and evidence authority; **this document creates none**.
- The two independently inventoried forms A/B remain mandatory. Real item/media/answer/content QA is a separate future release checkpoint; no forms are added, deleted or requested for re-inventory.
