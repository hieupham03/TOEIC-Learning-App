# D03-REQ-007 — OFFICIAL PRODUCT OWNER DECISION RECORD V1.0

**Date:** 2026-11-21  | **Authority:** Product Owner | **Decision:** **APPROVED — R1, R2, R3, R4 as REQUIREMENTS DRAFTING PRINCIPLES ONLY**.

## 1. Verbatim decision (consolidated)

> Tôi, Product Owner, PHÊ DUYỆT D03-REQ-007: chấp thuận cả bốn nguyên tắc R1, R2, R3, R4 làm định hướng soạn Requirements theo gói V3.8. Hãy ghi quyết định, tiếp tục hoàn thiện và rà soát PRD/SRS cùng tiêu chí nghiệm thu, sau đó trình một gói readiness trước Stage 03 Gate. Hai Full Mock đã kiểm kê, QA-01 đến QA-08 là khung đã duyệt nhưng chưa được coi là đã kiểm thử PASS, ngân sách tiếp tục DEFERRED. Chưa duyệt MVP, PRD/SRS baseline, UI, kiến trúc hay code.

## 2. Approved directions

| ID | Approved principle / boundary |
|---|---|
| R1 | Tách phiên Full Mock đánh giá có quy tắc thời gian/tính hợp lệ và luyện từng Part linh hoạt. Phải nêu rõ hành vi khi mất kết nối, app nền, thoát hoặc nộp; không âm thầm gia hạn thời gian hay mất đáp án. **Không** tự chốt ngưỡng gián đoạn, replay hoặc cách tính timer. |
| R2 | Báo số đúng/đã làm, Listening/Reading và Part, form/date/integrity; so sánh hai mock chỉ là mô tả kết quả luyện tập có cảnh báo khác biệt độ khó/lộ đề. **Không** nhận điểm ETS 10–990 hoặc tăng năng lực đã hiệu chuẩn. |
| R3 | Answer key đã QA bắt buộc; lời giải chỉ khi có bản đã kiểm duyệt, không tự bịa. Lưu lỗi sai, gợi ý quy tắc đơn giản theo mức độ/yếu điểm/thời gian, cho người học tự chọn. AI/PDF auto-import/notification nâng cao **không** được tự thêm MVP. |
| R4 | Bảo toàn đáp án đã xác nhận, kiểm soát tình trạng phiên, tách dữ liệu các thành viên, xác định chính sách riêng tư/xóa dữ liệu trước pilot, đọc Reading dài toàn vẹn trên thiết bị Android. **Không** chọn UI, login flow, storage hoặc architecture. |

## 3. Inherited constraints — unchanged

- Stage01 Product Vision V1.0 **APPROVED** and file immutable; Stage02 **CLOSED CONDITIONAL PASS**, CP-01..05 active.
- Stage03 **IN PROGRESS**; WP01 done draft, WP02 B conditionally chosen, D03-LOCK-001=B1 **two 200-item Full Mocks mandatory**; no automatic B2/B3 switch.
- PO affirms rights over named 3 websites plus further sources; 2 mock inventories **completed by PO report**; per-item/audio/key/duplicates and actual QA outcome **NOT VERIFIED**.
- D03-QA-006 **approved framework QA-01..08**, **not** testing PASS.
- D03-BUDGET-005 **DEFERRED BY PO**; no current monetary tasks, forecasts or purchase permissions. CP-04 retained for appropriate later checkpoint.

## 4. Explicit non-approvals / effect

**D03-REQ-007 is NOT:** MVP LOCK; approval of individual FR/NFR or acceptance thresholds; PRD/SRS baseline; stage-03 Gate PASS; permission for UX/UI, architecture, stack selection, development/Codex, scraping/bulk downloads, vendor contact, purchasing or deployment.

**Authorized next:** edit and review PRD/SRS drafts, clarify behavioral tests, map evidence gaps; prepare **PRE-GATE READINESS REVIEW PACK** for PO. Do not silently declare requirements accepted.

**Document evidence:** PO message in current conversation; V3.8 decision pack. **Record status:** APPROVED and CLOSED. No substitute for later baseline signoff.
