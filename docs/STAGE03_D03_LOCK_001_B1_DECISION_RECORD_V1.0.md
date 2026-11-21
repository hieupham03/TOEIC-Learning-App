# D03-LOCK-001 — Quyết định Product Owner: B1 (V1.0)

**Ngày:** 2026-11-21 · **Stage:** 03 — Requirements, IN PROGRESS  
**Decision authority:** Product Owner · **Status:** APPROVED DIRECTION, NOT MVP LOCK

## 1. Quyết định nguyên văn về ý nghĩa
Product Owner chọn **B1 — giữ HAI Full Mock TOEIC Listening & Reading là điều kiện bắt buộc** đối với đề xuất khóa MVP. Tiếp tục chuẩn bị bằng chứng về nguồn học liệu, quyền sử dụng, QA và ngân sách trước khi trình PO quyết định khóa MVP. **Chưa** duyệt MVP, PRD/SRS baseline, UI/UX, kiến trúc, code hoặc mua dịch vụ.

## 2. Điều gì được phép / không được phép
| Chủ đề | Trạng thái | Ranh giới |
|---|---|---|
| Balanced Family Pilot (B) | APPROVED FOR ANALYSIS ONLY | Hướng sản phẩm, chưa phải danh mục MVP chốt |
| B1 (2 Full Mock là hard gate) | APPROVED | Điều kiện bắt buộc để đề xuất khóa MVP / cam kết hai mock |
| Hai bộ đề độc lập | REQUIRED, NOT EVIDENCED | 2 × 200 câu; nội dung, audio, hình ảnh, đáp án có quyền và QA |
| Gói khảo sát quyền/học liệu | AUTHORIZED FOR RESEARCH/REVIEW | Không tự ý số hóa, upload, phân phối hay mua quyền |
| QA và ngân sách | PREPARE CRITERIA | PO chưa chốt ngưỡng, số tiền hay giờ nhân công |
| PRD/SRS V0.2 | DRAFT ONLY | Có thể ghi phụ lục điều kiện B1; không baseline |
| MVP scope lock | NOT APPROVED | Chờ minh chứng đạt gate + quyết định PO riêng |
| UX/UI, architecture, app/Codex code | NOT AUTHORIZED | Chưa bắt đầu |

## 3. Điều kiện triển khai B1
1. **G-SOURCE:** Nguồn kiểm kê có đủ ít nhất hai đề hoàn chỉnh độc lập, đúng blueprint Part 1–7, cùng ngân hàng luyện phù hợp nếu pilot có luyện Part; số lượng chưa xác minh.
2. **G-RIGHTS:** Từng asset (câu hỏi, đoạn văn, audio, hình ảnh, transcript, answer key, lời giải) có căn cứ quyền theo mục đích sử dụng app/cloud/nhóm học viên; sở hữu sách/PDF không đồng nghĩa có quyền phân phối.
3. **G-MOCK:** Không trùng câu giữa hai đề, tránh lộ câu thi trong tập luyện; hai đề được QA nội dung, audio–answer mapping và độ khó. Không khẳng định điểm quy đổi ETS hoặc tính tương đương thống kê.
4. **G-QA:** Có phương pháp nghiệm thu, người chịu trách nhiệm, quy trình sửa lỗi và nhật ký nguồn; chưa có kết quả kiểm tra thật.
5. **G-COST:** Có dự toán có thể kiểm tra, trần nội dung/QA/4 tuần vận hành, dự phòng phát sinh và PO chấp thuận trước mua/đăng ký.

## 4. Quy tắc nếu một gate không đạt
**Không được tự động chuyển sang B2 hay B3, hạ số mock, hoặc thay đổi KPI điểm số.** Giữ trạng thái `MVP LOCK = HOLD`, tổng hợp bằng chứng còn thiếu và trình lại PO các khả năng: hoàn thiện B1, điều chỉnh nguồn/chi phí, hoặc quyết định phạm vi mới có chữ ký của PO.

## 5. Điều kiện kế thừa CP-01–CP-05
CP-01 Requirements only; CP-02 không tự cam kết importer/AI/điểm ETS/notification/cả ba chế độ; CP-03 quyền nội dung; CP-04 QA/chi phí; CP-05 thử nghiệm baseline thủ công không bắt buộc, PDF mẫu và định giá đối thủ vẫn deferred.

## 6. Truy vết
Nguồn: quyết định PO ngày 2026-11-21 trong hội thoại sau `STAGE03_SCOPE_LOCK_DECISION_PACK_V0.1.md`. Hồ sơ nguồn `STAGE03_EVIDENCE_SOURCE_LEDGER_V0.3.md`. Bằng chứng thực tế của học liệu PO vẫn chưa kiểm kê/kiểm định. Ghi quyết định không có nghĩa đã hoàn thành các gate.
