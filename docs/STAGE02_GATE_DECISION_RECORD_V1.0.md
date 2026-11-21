# TOEIC Learning App — Stage 02 Gate Decision Record V1.0

**Decision ID:** G02-DEC-001  
**Decision date:** 2026-11-21 (Asia/Bangkok)  
**Decision authority:** Product Owner (người dùng)  
**Review reference:** `STAGE02_GATE_REVIEW_V1.0.md`  
**Gate decision:** **APPROVED — CONDITIONAL PASS**  
**Scope:** Hoàn tất Stage 02 Market Research & Validation **với điều kiện chuyển giao**.  
**Stage 03 state:** **NOT STARTED — KICKOFF PLAN PENDING PO APPROVAL**.

## 1. Nguyên văn quyết định (Product Owner)

> Tôi, với vai trò Product Owner, PHÊ DUYỆT Stage 02 Gate = CONDITIONAL PASS, chấp thuận CP-01 đến CP-05 theo Gate Review V1.0. Hãy ghi quyết định Gate vào hồ sơ và trình kế hoạch mở Stage 03 Requirements cho tôi xem. Chưa tự chốt MVP, kiến trúc, UI hay viết code.

Decision binding: PASS có điều kiện, **không** phải unconditional PASS, không được gộp với quyết định cho phép triển khai tính năng.

## 2. Các điều kiện chính thức đã được CHẤP NHẬN (chưa được đánh dấu đã hoàn tất)

| ID | Điều kiện được duyệt | Acceptance | Execution state |
|---|---|---|---|
| CP-01 | Ủy quyền tới Stage 03 chỉ giới hạn **phân tích yêu cầu**; không ngầm chốt MVP, PRD/SRS, UI, công nghệ hay code | ACCEPTED | OPEN — áp dụng xuyên Stage 03 |
| CP-02 | Không cam kết tự động import PDF/audio, AI, điểm TOEIC quy đổi, notification nâng cao và đủ ba trải nghiệm trong MVP khi chưa đủ bằng chứng | ACCEPTED | OPEN — scope decisions pending |
| CP-03 | Phải phân loại provenance/license và các quyền xử lý/lưu/chia sẻ/công khai nội dung, không phát hành nguồn chưa có quyền | ACCEPTED | OPEN — content rights unresolved |
| CP-04 | Định nghĩa quality/cost gates cho dữ liệu câu hỏi–audio–đáp án, AI, điểm mock, trải nghiệm Reading dài, nguồn đề và OPEX | ACCEPTED | OPEN — verification and thresholds pending |
| CP-05 | Không yêu cầu thử nghiệm thủ công chỉ để qua gate; VAL-013L/R NOT RUN/OPTIONAL, VAL-003 và VAL-010 DEFERRED, không coi là kết quả kiểm chứng | ACCEPTED | ONGOING — evidence hygiene enforced |

**Nguyên tắc:** ACCEPTED ≠ VERIFIED/CLOSED. Điều kiện rủi ro phải được xử lý tại các điểm kiểm soát tương ứng; không lùi quyết định Stage 02 vì chưa thực hiện những phép thử đã được chấp thuận hoãn.

## 3. Rủi ro chuyển giao

R01–R10 tại `STAGE02_TO_STAGE03_OPEN_RISKS_V1.1.md` được **CARRIED FORWARD / OPEN**, chưa tự đóng; đặc biệt quyền học liệu, ingest PDF/audio, AI, tính so sánh điểm mock, trải nghiệm Full Mock Android và nguồn học liệu hợp pháp. Không nâng độ tin cậy bằng chứng chỉ vì Gate đã PASS.

## 4. Trạng thái sau quyết định

| Stage/Gate | Trạng thái |
|---|---|
| Stage 01 — Product Discovery | COMPLETE; Product Vision V1.0 APPROVED |
| Stage 02 — Market Research & Validation | **CLOSED — CONDITIONAL PASS APPROVED** |
| Stage 03 — Requirements | **NOT STARTED; kế hoạch kickoff V0.1 đang chờ PO duyệt** |
| Stage 04 — UX/UI | NOT STARTED |
| Architecture, implementation, QA, release | NOT AUTHORIZED |
| MVP scope, PRD, SRS | NOT APPROVED |

## 5. Next action

Trình `STAGE03_REQUIREMENTS_KICKOFF_PLAN_V0.1.md` để Product Owner duyệt phương pháp, deliverables, decision points và cách xử lý CP-01–CP-05. **Không bắt đầu soạn PRD/SRS hoặc chốt MVP cho tới khi PO duyệt kickoff plan.**

**References:** `PRODUCT_VISION_V1.0.md` (immutable approved vision), `STAGE02_GATE_REVIEW_V1.0.md` (historical recommendation), `STAGE02_EVIDENCE_SOURCE_LEDGER_V1.0.md` (sources), `VALIDATION_REGISTER_V2.8.md` (latest register).
