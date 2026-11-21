# Stage03 Requirements Baseline — Immutable Identity Manifest V1.0

**Approval authority:** D03-BASELINE-010 / Option A / Product Owner / 2026-11-21.  
**Baseline state:** **APPROVED AND CONTROLLED**.  
**Stage03 Gate state:** PENDING Product Owner, separate decision.

## Approved file identities — bytes retained unchanged

| Canonical ID | Filename (inside `docs/`) | SHA-256 |
|---|---|---|
| `REQ-PRD-0.6` | `STAGE03_PRD_BASELINE_CANDIDATE_V0.6.md` | `0cf1981c33a7469a10c2db8a2c33e71c8e1ac12bb285fa605f0fc6d49b46ffcc` |
| `REQ-SRS-0.6` | `STAGE03_SRS_BASELINE_CANDIDATE_V0.6.md` | `5dedf4493e6ec4f970fa3f9a26267547e1a87c30649629a831b6334118f86f08` |
| `REQ-AT-0.4` | `STAGE03_ACCEPTANCE_CATALOGUE_CANDIDATE_V0.4.md` | `4f07a02edeb95ebfb2cdc3743bf3c0b8e70b256a69f957b4e50d149c3b108e8b` |

**Status on first lines of these files:** “Candidate / Pending” was written *before* this explicit approval. For these precise hashes and versions only, the **approval record supersedes that dated workflow label** without modifying a single byte. Do not treat old status text as a reason to unset the baseline. Do not edit the approved files in place to rewrite their header; issue change-controlled successor versions if modifications are approved.

**Additional reference (not approved as part of the trio):** `STAGE03_REQUIREMENTS_TRACEABILITY_V0.6.md`, `STAGE03_MVP_SCOPE_LOCK_MATRIX_V1.0.md`, `STAGE03_MOCK_AND_DATA_POLICIES_APPROVED_V1.0.md`. These provide traceability and earlier signed business authority, but were not an implicit fourth baseline-document approval in D03-BASELINE-010.

## Change control

1. Record a change request showing what baseline clause is affected, the reason, downstream impact, and whether it modifies S1/S2/S3 or B1.
2. Product Owner must approve material business changes; preserve prior SHA-256 and archived document.
3. Publish successor version only after approval, with delta and updated traceability; do not overwrite the three approved bytes.
4. Keep technical details genuinely TBD until the declared checkpoint; do not set UI, architecture, timers, tolerances or privacy mechanics here without authorized decision.

## Future checkpoints: approved specification ≠ observed quality

- **Before releasing mock/practice content to pilot:** QA-01..06 for source, exact structure, licensed provenance, answer/media/passage relationships, A/B independence, Part bank separation; 100% necessary assets, zero known critical content defects as per S3.
- **Before pilot software release:** QA-07..08 and acceptance tests for raw scoring, attempts, truthful answer-save, resume, privacy and long Reading on ≥2 Android contexts; no critical known defect.
- **Before test-plan baseline:** define numeric performance/time/network/recovery tolerances without weakening signed P01..09.
- **Before pilot accounts/data:** verify identity/deletion handling to meet approved 7-calendar-day request and ≤30-day post-pilot routine retention policies; documented lawful exceptions.
- **Budget:** DEFERRED BY PO, cannot be treated as a waiver or authorization to spend; reopen only at applicable future PO checkpoint.
- **After implementation/pilot:** success metrics PM-01..06, e.g., 2–5 pilot learners over four weeks and ≥2 valid A/B paired attempts with feedback; insufficient observations mean INCONCLUSIVE, never fabricated score gains.

**Immutable Vision SHA-256:** `d296b085543c4646952d1572b570c1659b8b63fbcf1c61a513393a4489cca56c`.
