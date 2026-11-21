# Stage 02 → Stage 03 — Open Risks & Approved Gate Conditions V1.1

**Date:** 2026-11-21  
**Stage 02 Gate:** APPROVED — CONDITIONAL PASS (G02-DEC-001).  
**CP-01..CP-05:** PO ACCEPTED; **underlying risk items are still OPEN**.  
**Stage 03:** NOT STARTED; kickoff plan pending.  
**Supersedes V1.0 header (which said draft/pending PO gate); preserves risk details and thresholds without silently closing any risk.**

| ID | Rủi ro chưa giải quyết | Mức độ | Gate muộn nhất cần giải quyết | Điều kiện/đầu ra kiểm chứng |
|---|---|---|---|---|
| R01 | Quyền học liệu PDF/sách/audio cá nhân, crawl và giấy phép thương mại | CRITICAL | Trước nhập lên dịch vụ chung / chia sẻ / phát hành | Ma trận provenance, license, quyền xử lý AI, phân phối; chỉ dùng học liệu có quyền hợp lệ trong mỗi ngữ cảnh. Tài liệu chưa rõ quyền không được phát hành. |
| R02 | Nhập PDF/audio: tách Part/câu, chọn lựa, map audio/transcript và đáp án không chính xác | HIGH | Trước cam kết nhập tự động thuộc MVP hoặc release | Có mẫu đại diện và spike đánh giá accuracy; nêu tập định dạng hỗ trợ và các trường hợp phải review thủ công; fallback hợp lệ bằng nội dung có cấu trúc/biên soạn. |
| R03 | AI giải thích hoặc tạo câu sai, tốn chi phí vượt OPEX pilot | HIGH | Trước cho nội dung AI tới người học | Bộ câu kiểm thử chuẩn, đối chiếu chuyên môn/nhân sự; kiểm soát confidence & sửa sai; giới hạn ngân sách, có thể tắt AI. |
| R04 | So sánh điểm mock không đáng tin, giả mạo tương đương ETS | HIGH | Trước báo cáo tiến bộ bằng điểm TOEIC quy đổi | Định nghĩa rõ scores: số câu đúng, tỷ lệ chính xác, điểm nội bộ hoặc ước lượng đã kiểm định; không gắn nhãn 'official' nếu không được phép. |
| R05 | Reading dài trên màn hình nhỏ gây mỏi mắt; quá trình thi dài gián đoạn | MEDIUM-HIGH | Trước khóa UX acceptance và trước pilot | Thiết lập tiêu chí dễ đọc, phục hồi phiên, thao tác, audio; kiểm thử thực tế có mục tiêu sau prototype thay vì buộc full mock 120 phút ngay. |
| R06 | Thị trường đã có Part Practice, full test, study plan; khác biệt chưa chứng minh | HIGH | Khi chốt PRD/MVP và đánh giá pilot | Value proposition: thư viện tài liệu hợp lệ + quy trình thống nhất + lịch học linh hoạt; pilot đo use/retention/value chứ không khẳng định PMF qua 2–5 người. |
| R07 | Nội dung hợp pháp và số lượng đề chưa rõ đủ cho 4 tuần | HIGH | Khi cam kết phạm vi MVP / trước pilot | Chốt nguồn học liệu tối thiểu; nêu nguồn thay thế nếu PDF personal chưa thể nhập. |
| R08 | Quyền thông báo, hành động và độ chính xác lịch hoãn trên Android | MEDIUM | Khi đặc tả tính năng thông báo / trước release | Thông báo opt-in, có tắt/ẩn, kiểm tra giới hạn 3 action và quyền Android; không cam kết nhắc đúng từng phút. |
| R09 | Giá, willingness to pay, mô hình ads/premium chưa có dữ liệu | MEDIUM, DEFERRED BY PO | Trước kế hoạch thương mại hóa, không chặn Requirements/pilot | Giữ monetization chưa quyết định; chỉ lập ngân sách pilot OPEX/chi phí định mức. |
| R10 | Dữ liệu pilot nhỏ và người học #2 chưa được phỏng vấn độc lập | MEDIUM | Đánh giá pilot và trước tuyên bố nhu cầu thị trường | Phân biệt beta trong gia đình với kết luận PMF; lấy phản hồi pilot trực tiếp khi có sản phẩm dùng thử. |

## Các điều kiện PO đã CHẤP THUẬN cho Conditional Pass

- **CP-01 — Charter Stage 03:** Stage 03 chỉ được phép **xác định yêu cầu, options, kế hoạch thử nghiệm/quality gate**, không mặc nhiên duyệt bất kỳ MVP hay công nghệ nào.
- **CP-02 — Scope boundaries:** Chưa cam kết AI, import PDF/audio tự động, quy đổi điểm ETS/990, thông báo nâng cao hoặc cả ba trải nghiệm đều thuộc MVP. Mọi claim cần ghi confidence và fallback.
- **CP-03 — Content rights rule:** Mọi yêu cầu ingest/hiển thị/chia sẻ nguồn đều phải có kiểm tra quyền phù hợp; không tái xuất bản tệp chưa xác minh.
- **CP-04 — Quality controls:** PRD/SRS phải có yêu cầu đo chất lượng nội dung, độ tin cậy lời giải/score, UX Reading dài, nguồn học liệu và OPEX. Các cổng quality này được nghiệm thu trước pilot/release tương ứng.
- **CP-05 — Evidence hygiene:** VAL-003 và VAL-010 vẫn deferred; VAL-013L/R optional/not run. Không tự tuyên bố chúng đã được xác thực và không dùng việc chưa chạy để kéo dài Stage 02.

**Ý nghĩa:** Các điều kiện này không phải yêu cầu triển khai ngay, mà là giới hạn để nghiên cứu giai đoạn sau không dựa trên giả định chưa có bằng chứng. PO đã chấp thuận CP-01–CP-05 tại G02-DEC-001. Giải quyết/đo lường các rủi ro theo gate muộn nhất ở bảng trên; không được coi là đã xác minh.
