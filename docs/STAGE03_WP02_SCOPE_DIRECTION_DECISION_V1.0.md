# D03-SCOPE-DIR-001 — Quyết định định hướng WP-02 V1.0

**Ngày ghi:** 2026-11-21  
**Người quyết định:** Product Owner  
**Trạng thái:** **APPROVED — DIRECTION ONLY; NOT MVP APPROVAL**  
**Nguồn:** Product Owner tuyên bố lựa chọn **B — Balanced Family Pilot CÓ ĐIỀU KIỆN** và yêu cầu soạn gói khả thi + Requirements draft; giữ CP-01..CP-05.

## Quyết định được phê duyệt
- Chọn hướng B để tiếp tục phân tích yêu cầu của Stage 03. Hướng B kỳ vọng ứng dụng Android Listening/Reading đủ 7 Part, luyện tập linh hoạt và Full Mock nếu nguồn được xác minh, lưu lỗi sai, đề xuất theo quy tắc đơn giản, kho học liệu được quản lý có kiểm soát.
- Ghi rõ các phụ thuộc chưa vượt gate: nguồn học liệu hợp pháp, 2 Full Mock hoàn chỉnh và có cơ sở so sánh, QA audio–câu–đáp án, chi phí pilot 2–5 người, trải nghiệm Reading dài.
- Cho phép: (1) lập feasibility pack và quality gates; (2) soạn **PRD/SRS DRAFT** mang tính điều kiện, để PO xem xét.
- **Không được hiểu là**: phê duyệt feature baseline/MVP, hai bộ Full Mock, tính năng nhập PDF tự động, AI, notification nâng cao, UX/UI, kiến trúc, lựa chọn công nghệ, code, dịch vụ có phí hoặc phát hành nội dung.

## Trạng thái từng work package
| Work package | Trạng thái | Ghi chú |
|---|---|---|
| WP-01 Input Baseline | COMPLETED — analyst draft | Giữ nguyên |
| WP-02 Scope Options | **DIRECTION B SELECTED — CONDITIONAL** | Chưa phê duyệt MVP |
| WP-03 PRD/SRS | **DRAFT PREPARED FOR REVIEW** | Không baseline / không sign-off |
| WP-04 Quality/Content/Risk | **FEASIBILITY PLAN PREPARED, NOT VERIFIED** | Chưa kiểm kê tài liệu |
| WP-05 Gate Review | NOT STARTED | Chờ quyết định tiếp theo |

## Điều kiện chuyển qua quyết định khóa MVP
Trình PO một bảng chứng cứ nguồn–quyền–chất lượng cho nội dung dự định sử dụng; xác định tình trạng **400 mục kiểm tra riêng biệt cho hai đề** và kho Part practice riêng (nếu cần); xác định loại điểm có thể tuyên bố; phê duyệt giới hạn chi phí, biện pháp kiểm soát dữ liệu. Nếu nguồn không đạt, bắt buộc trình phương án điều chỉnh phạm vi B/A để PO quyết định — **không tự bỏ Full Mock**.

## Điều kiện Stage02 còn nguyên
- CP-01: Requirements only — không phải phê duyệt MVP/PRD/SRS/UI/code.
- CP-02: Không mặc định auto-import, AI, điểm ETS chính thức, thông báo nâng cao hoặc mọi module cùng thuộc MVP.
- CP-03: Phân loại quyền trước khi sử dụng/phân phối nội dung.
- CP-04: Cổng QA nguồn, audio, đáp án, điểm thi, Android, chi phí.
- CP-05: Desktop baseline Listening/Reading tùy chọn, vẫn NOT RUN; VAL-003 và VAL-010 tiếp tục DEFERRED.
