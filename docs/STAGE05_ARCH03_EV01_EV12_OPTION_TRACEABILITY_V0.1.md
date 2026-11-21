# Stage05 ARCH-03 — Full EV01..12 Architecture Candidate Traceability V0.1

**Status:** 12/12 EVIDENCE CLAIMS MAPPED TO EACH CANDIDATE; **0/12 PRODUCT BEHAVIOR VERIFIED**. This is a *desk mapping*, not runtime acceptance or selection.

| EV ID | Claim / business truth | Signed FR/NFR/AT | FM falsifier | ARCH03-A future proof concern | ARCH03-B future proof concern | ARCH03-C future proof concern | Later owner/checkpoint |
|---|---|---|---|---|---|---|---|
| EV-01 | Time survives clock change | FR-011/019; NFR-004; AT-11/19 | FM-03/04 | On-device monotonic observation needs manipulation/reboot continuity proof | External elapsed evidence needs outage/staleness/identity proof | Competing clock claims require explicit unchosen resolution rules | Timing policy + QA-08 |
| EV-02 | UI recovery vs clean attempt | FR-011/019; AT-11/19 | FM-01/02 | Restored screen ≠ clean history; need duration/audio event proof | Cross-process history availability proof missing | Correlate event continuity, do not infer validity from restored UI | Android QA-08 |
| EV-03 | Rebooted mock trustworthy | FR-011/019; NFR-004 | FM-03 | Since-boot data cannot alone account for reboot downtime | Outage and missing outside observation may remain | Source conflicts and reboot gaps cannot be adjudicated by assumption | PO tolerance + Android QA-08 |
| EV-04 | Listening audio no improper replay | FR-003/010/011; QA-03/08 | FM-01/05/18 | Local focus/interruption evidence untested | External receipts ≠ proof the learner heard each clip | Correlating focus/media observations still untested | Media QA-03 + Android QA-08 |
| EV-05 | Durably saved answer claim | FR-005/019; AT-05/19 | FM-07 | Local durable ACK not demonstrated | Independently retrievable ACK needs connectivity/provenance | Two-tier save signals not proof of persistence | Persistence QA-08 |
| EV-06 | Lost ACK / safe retry | FR-005/019; AT-05/19 | FM-08/14 | Idempotence and late responses untested | External duplicate suppression/late reply untested | Conflict of ACK records still lacks verified policy | Persistence QA-08 |
| EV-07 | Shared family device isolation | FR-018; NFR-006; AT-18 | FM-09 | On-device identity/session leakage risk | External authorization cannot be presumed | Both contexts increase potential confused-deputy risk | Privacy QA-08 |
| EV-08 | Verified deletion across copies | FR-018; BR-08; NFR-006 | FM-10/11 | Local/backups/other copies inventory unproven | Remote/replicas/logs inventory unproven | Cross-copy completion proof could be incomplete | Privacy SOP + QA-08 |
| EV-09 | Mock content ready for release | FR-010/015/017; QA-01..06 | FM-06/16 | Local format/version does not replace key/media QA | Remote catalog/version does not replace key/media QA | More copies do not establish correct answers/media | Content QA-01..06 |
| EV-10 | Historic score truth after correction | FR-008/012/013/016; QA-07 | FM-12/14/17 | Original version and correction audit unproved | Remote correction/duplicate handling unproved | Agreement of copies cannot justify silent rescore | Scoring QA-07 |
| EV-11 | Practice bank not mock exposure | FR-002/010/013; QA-05 | FM-13 | Local separation/overlap audit needed | External separation/overlap audit needed | Multiple copies need consistent isolation | Content QA-05 |
| EV-12 | Reading anchor and accessibility | FR-004; NFR-005/010; AT-04 | FM-15 | Local UI context may be restored but not tested | External context cannot fix visual readability | Multiple evidence sources cannot guarantee readable Reading | 2+ Android contexts + UX/QA-08 |

## Evidence adjudication rule

Every EV remains **EVIDENCE REQUIRED / APP NOT VERIFIED**. A candidate's documentation cannot fulfill a real-device test, content QA proof, signed policy exception or clock-authority decision. Unsupported positive states (clean mock, saved, QA-ready, deleted, official score) are disallowed; signed UX copy remains authoritative.

**Full original review:** `STAGE05_EVAL004_CLAIM_TO_EVIDENCE_ADJUDICATION_V0.1.md`; the mapping here is a derivative comparator, not a new evaluation PASS.
