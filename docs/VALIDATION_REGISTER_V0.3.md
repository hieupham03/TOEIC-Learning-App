# VALIDATION REGISTER V0.3 — TOEIC Learning App

- **Ngày cập nhật:** 2026-11-20
- **Giai đoạn:** 02/11 — Market Research & Validation (IN PROGRESS)
- **Product Vision:** V1.0 APPROVED (không sửa đổi)
- **Phase 02 Gate:** HOLD — chưa phê duyệt chuyển Requirements
- **Code:** NOT AUTHORIZED
- **Nguồn bằng chứng:** Phản hồi định tính của Product Owner qua VAL-001 và VAL-002; chưa xem tài liệu mẫu hoặc tiến hành thử nghiệm kỹ thuật.

## I. Validation Log

| ID | Chủ đề | Quan sát / dữ kiện | Mức độ bằng chứng | Trạng thái |
|---|---|---|---|---|
| VAL-001 | Trải nghiệm app hiện có | Người dùng cảm nhận cá nhân hóa chưa đủ, nhiều thao tác, giá cao và không tiện mở máy để học 1 từ / 1 câu rồi thoát | Người tham gia pilot #1, tự báo cáo; chưa đối chiếu sản phẩm/giá | RECORDED — NOT MARKET-VALIDATED |
| VAL-002 | Kho tài liệu | Người dùng xác nhận có kết hợp PDF, sách và audio TOEIC nhiều loại | Người tham gia pilot #1, tự báo cáo; chưa kiểm kê/xem file | RECORDED — INVENTORY PENDING |

## II. Giả thuyết / đánh giá hiện tại

| ID | Giả thuyết | Bằng chứng có sẵn | Bằng chứng còn thiếu | Status |
|---|---|---|---|---|
| H-001 | Người học Việt cần cá nhân hóa sâu hơn, thao tác đơn giản hơn và giá dễ tiếp cận | Phản hồi VAL-001 của người sáng lập | Benchmark đối thủ và người học khác | INCONCLUSIVE |
| H-002 | Học nhanh 1 từ / 1 câu giúp giảm rào cản bắt đầu | Mong muốn cụ thể từ VAL-001 | Thử nghiệm luồng, số thao tác, khả năng quay lại học | INCONCLUSIVE |
| H-003 | Thư viện tài liệu cá nhân đem lại giá trị | Có PDF/sách/audio (VAL-002), khó dùng lại tiện lợi (VAL-001) | Mẫu tài liệu thật, đánh giá chuyển đổi, quyền | INCONCLUSIVE |
| H-004 | AI có thể sinh lời giải đúng và nội dung nguyên bản với chi phí thấp | Ý tưởng đã ghi nhận tại Discovery | Bộ kiểm chuẩn, kiểm duyệt, kiểm tra quyền và chi phí | NOT TESTED |
| H-005 | Full Mock Test có thể so sánh qua nhiều lần để đo tiến bộ | Mục tiêu đo lường đã chốt | Cấu trúc, độ khó, đáp án, nguồn và chuẩn so sánh điểm | NOT TESTED |
| H-006 | Có thể vận hành pilot gần miễn phí | Ràng buộc ngân sách đã chốt | Ước tính tài nguyên, storage/audio/API, hạn mức | NOT TESTED |

## III. Đánh giá sẵn sàng kho nội dung

**Kết luận hiện tại: Có nguồn tài liệu thô, chưa đủ bằng chứng về khả năng chuyển đổi hoặc quyền sử dụng.**

| Thành phần | Khả năng về nguyên tắc | Chưa kiểm chứng |
|---|---|---|
| PDF có text chọn/copy | Có thể bóc tách text và cấu trúc câu hỏi | Có thực sự tồn tại trong kho? chất lượng và thứ tự? |
| PDF scan | Có thể cần nhận dạng ký tự và rà soát bố cục | Độ chính xác, chất lượng scan, công sức sửa |
| Sách in | Có thể cần số hóa theo quyền cho phép | Quyền sao chép/số hóa và chi phí |
| Audio Listening | Có thể gắn clip với câu / nhóm câu | File nguồn, thời lượng, mapping, transcript |
| Đáp án / giải thích | Có thể liên kết từng câu | Độ đầy đủ/chính xác, phiên bản, căn cứ nguồn |
| Full Mock Test | Có thể lắp ghép khi có bộ đề hoàn chỉnh, đủ tin cậy | Độ bao phủ, tính tương đương, nguồn hợp pháp |

**Không suy diễn:** Chưa biết PDF text hay scan chiếm tỷ trọng nào; chưa biết số lượng đề, độ phủ Part 1–7 hoặc có transcript và đáp án chi tiết hay không.

## IV. Nguyên tắc phân quyền nội dung

- **Sử dụng tài liệu cá nhân:** tùy giấy phép/ngoại lệ áp dụng; việc sở hữu PDF/sách không tự động cho phép upload lên hệ thống cho nhiều người.
- **Phân phối cho nhóm người dùng:** cần đánh giá quyền sao chép, chia sẻ, lưu trữ server và cung cấp truy cập.
- **Phát hành thương mại:** cần quyền phù hợp với app công khai có quảng cáo/mở khóa, bao gồm quyền sử dụng phái sinh/chỉnh sửa nếu có.
- **AI xử lý/tạo nội dung:** riêng rẽ kiểm tra điều kiện cung cấp tài liệu cho bên dịch vụ AI, quyền sử dụng dữ liệu đầu vào và kết quả đầu ra.
- Tài liệu **unknown rights** không được mặc định đưa vào kho công khai; ghi provenance/điều kiện sử dụng theo từng nguồn.

## V. Bài kiểm chứng tiếp theo — một bộ đề đại diện, KHÔNG CODE

**Mục tiêu:** kiểm kê/đọc thử một bộ tài liệu representative mà người dùng có quyền cung cấp để phân tích; xác định loại file, sự hiện diện của câu hỏi/đáp án/audio/transcript và độ khớp; kiểm tra tình trạng quyền.

**Dữ liệu cần có (nếu sẵn):** 1 PDF đề, file đáp án, 1–2 audio tương ứng; nếu là sách giấy, có thể dùng mục lục hoặc vài trang ví dụ theo phạm vi được phép chia sẻ để đánh giá cấu trúc. Không cần gửi toàn bộ kho.

**Kết quả mong muốn:** Content Inventory mẫu, Content Quality Check, Rights Status, danh sách lỗi và kết luận GO / REWORK / NOT USABLE cho từng nội dung và **chưa** kết luận toàn bộ kho.

**Acceptance criteria của bước kiểm kê mẫu:**
1. Ghi rõ nguồn xuất xứ và quyền được biết/chưa biết; không tự xác nhận bản quyền.
2. Xác định text/scan/mixed và tính đầy đủ của các thành phần.
3. Lập mapping thử cho một nhóm câu Listening và một nhóm Reading nếu tài liệu có đủ.
4. Nhận diện trường hợp không thể tự động chuyển đổi đáng tin cậy.
5. Chưa tạo code hoặc triển khai hệ thống.

## VI. Next Question

**Bạn có thể cung cấp một bộ đề TOEIC đại diện (PDF và nếu có thì file đáp án/audio tương ứng) để kiểm tra cấu trúc và mức độ đầy đủ của tài liệu không?** Nếu chưa tiện gửi, có thể mô tả tên bộ đề và các file thành phần để tiếp tục kiểm kê sơ bộ.

## VII. Gate Status

- Product Vision V1.0: APPROVED.
- Discovery: COMPLETE.
- Validation: IN PROGRESS, evidence incomplete.
- MVP/PRD/SRS/Architecture/Tech stack/Code: NOT APPROVED.
