# Requirements Traceability Matrix V0.2 — Working Draft

**State:** DRAFT; chưa phê duyệt PRD/SRS baseline; giá trị chưa có bằng chứng là điều kiện hoặc risk.

| Need/Evidence | Requirement candidates | Gate/dependency | Status |
|---|---|---|---|
| PV-001 / J-01 PDF/audio và đáp án phân mảnh | FR-002..007, NFR-001..002 | Q-content / Rights | CONDITIONAL |
| PD-009/VAL-004 học theo thời lượng | FR-001, FR-008, FR-009 | Workload/content | CANDIDATE |
| VAL-017/018 Android full Part + mock | FR-002, FR-010..012 | 2 forms; Android test | CONDITIONAL |
| VAL-020/021/022 full mock done but Reading/mỏi mắt | FR-004, FR-011, NFR-003/004/008 | Device usability study | OPEN |
| VAL-002/023 có tài liệu PDF/audio | FR-013/014 | Per-source license; mapping | UNVERIFIED |
| Vision progress KPI + ETS scoring | FR-012, NFR-007 | Equating / claim review | CONDITIONAL |
| CP-03, ETS + Google Play IP | FR-013/014/016, NFR-001/010 | Rights inventory | BLOCKER CONTENT |
| CP-04 AI quality | FR-018 (OUT) | Separate eval if revisited | OUT |
| CP-04 OPEX ~0 | NFR-006 | Cost scenario and cap | OPEN |
| CP-05 tests deferred | none baseline | optional no-code tests | NON-BLOCKER |
| VAL-005/006/007/008/009 notifications | FR-019 (OUT) | user permission/controls | OUT FOR PILOT DRAFT |
| Privacy Google Play | FR-015, NFR-005 | data retention/consent | OPEN |

**Requirement completeness is not assured:** từng dòng phải được review khi có dữ liệu nguồn và quyết định MVP cuối cùng. Chưa trace sang code, kiến trúc, UI hay automated tests.
