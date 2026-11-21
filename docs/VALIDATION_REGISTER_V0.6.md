# VALIDATION REGISTER V0.6 — TOEIC Learning App

- **Ngày cập nhật:** 2026-11-20
- **Giai đoạn:** 02/11 — Market Research & Validation (IN PROGRESS)
- **Product Vision:** V1.0 APPROVED, không thay đổi
- **Phase 02 Gate:** HOLD — cần bằng chứng thực tế trước khi duyệt Requirements
- **Code / UX / architecture:** NOT AUTHORIZED
- **Nguồn bằng chứng:** Người dùng pilot #1 tự báo cáo, tài liệu chính thức Android Developers/Google Play; chưa chạy thử notification hoặc xem tài liệu TOEIC mẫu.

## 1. Validation Log

| ID | Nội dung | Dữ liệu thu thập được | Phân loại | Trạng thái |
|---|---|---|---|---|
| VAL-001 | Trải nghiệm các app TOEIC hiện có | Người dùng thấy cá nhân hóa hạn chế, nhiều thao tác, phí cao; khó ôn tài liệu sẵn có | Nhu cầu định tính một người; chưa đại diện thị trường | RECORDED — NOT MARKET VALIDATED |
| VAL-002 | Kho tài liệu TOEIC | Có kết hợp PDF/sách/audio nhiều loại | Tự báo cáo; chưa kiểm kê/chứng minh quyền | RECORDED — NOT FEASIBILITY VALIDATED |
| VAL-003 | Kiểm định một bộ đề mẫu | Người dùng hiện không thể tải bộ đề lên | Thiếu dữ liệu đầu vào, không phải kết quả thất bại | DEFERRED / PENDING EVIDENCE |
| VAL-004 | Thời điểm học cực nhanh | Người dùng có thời gian rảnh bất kỳ; mong thấy từ mới không cần mở app và khi rảnh khai báo thời lượng để được gợi ý bài | Nhu cầu cá nhân đã được ghi nhận | RECORDED — NOT USABILITY TESTED |
| VAL-005 | Vị trí hiển thị từ vựng | Người dùng chọn **thông báo Android** (không chọn widget/home hay màn hình khóa tùy chỉnh) | Lựa chọn trải nghiệm của một người | RECORDED — ANDROID FEASIBILITY PARTIAL |

## 2. Validation Register — Hypothesis & Evidence

| ID | Giả thuyết | Bằng chứng hiện có | Cần kiểm chứng | Trạng thái |
|---|---|---|---|---|
| H-001 | Người học cần cá nhân hóa sâu hơn và thao tác đơn giản hơn | VAL-001 | Benchmark có thang đo, phản hồi pilot #2+ | INCONCLUSIVE |
| H-002 | Học nhanh 1 từ / 1 câu giúp người dùng dễ bắt đầu | VAL-001, VAL-004 | Quan sát số thao tác, thời gian tới bài đầu tiên, sử dụng lặp | INCONCLUSIVE |
| H-003 | Thư viện TOEIC cá nhân đem lại giá trị | Có PDF/sách/audio, VAL-001/002 | Kiểm kê, đề mẫu, khả năng tách/gắn audio, quyền | INCONCLUSIVE; VAL-003 DEFERRED |
| H-004 | AI tạo đáp án/lời giải và câu hỏi nguyên bản đạt chất lượng với chi phí thấp | Ý tưởng Discovery | Gold set, kiểm duyệt chuyên môn, tính đúng, quyền, chi phí | NOT TESTED |
| H-005 | Full Mock Test phù hợp để so sánh tiến bộ qua nhiều lần | Định hướng Product Vision | Đề tương đương, độ khó, quy đổi điểm, tránh nhớ đề | NOT TESTED |
| H-006 | Thông báo từ vựng giúp tăng cơ hội tiếp xúc/học mà không gây phiền | VAL-004, VAL-005; Android hỗ trợ thông báo | Sự đồng ý, tần suất, tỷ lệ xem/nhớ, mức gây phiền, thử trên thiết bị | INCONCLUSIVE |
| H-007 | Đề xuất bài theo thời gian rảnh giúp tăng tần suất học | VAL-004 | Thử nghiệm luồng chọn thời lượng và hoàn tất bài phù hợp | INCONCLUSIVE |
| H-008 | Pilot 2–5 người có thể vận hành gần như miễn phí | Ràng buộc ngân sách PD-020 | Ước tính API/host/audio/free tier | NOT TESTED |

**Lưu ý về ID:** H-006 tại phiên bản V0.3 là giả thuyết về chi phí, nay chuẩn hóa thành **H-008** để tránh trùng với H-006 đã dùng trong phiên trao đổi VAL-004/005. Không thay đổi nội dung giả thuyết cũ.

## 3. Android Notification — Feasibility (Desk Research Only)

**Nhu cầu xác nhận:** Người dùng muốn nhìn thấy từ vựng TOEIC từ hệ thống thông báo mà không cần mở app; mục tiêu hiển thị gọn, ít thao tác. Việc hiển thị ở màn hình khóa phụ thuộc cài đặt Android và quyền riêng tư của người dùng.

| Khía cạnh | Bằng chứng / giới hạn | Kết luận |
|---|---|---|
| Nội dung thông báo | Android cho phép title/body; nội dung hiển thị phụ thuộc trạng thái mở rộng/cài đặt | Feasible in principle |
| Quyền thông báo | Android 13+ có runtime `POST_NOTIFICATIONS` cho non-exempt notifications | Permission needed |
| Notification channel | Android 8.0+ yêu cầu tạo channel | Platform requirement |
| Lock-screen visibility | Android hỗ trợ PUBLIC/PRIVATE/SECRET; người dùng có quyền cấu hình | Not guaranteed |
| Gửi đúng giờ | Doze/App Standby và OEM có thể trì hoãn công việc nền | Must test |
| Mỗi lần bật/mở màn hình nhận từ mới | Khác với thông báo định kỳ; chưa kiểm chứng khả năng/độ ổn định/quyền | NOT VALIDATED |
| Google Play | Thông báo phải phù hợp tính năng cốt lõi, không giả hệ thống, không dùng làm quảng cáo gây phiền | Policy check necessary |
| Không gây phiền | Tần suất, tạm dừng, giờ yên tĩnh, tùy chọn opt-in | UX hypothesis |

**Nguồn tham khảo:**
- https://developer.android.com/develop/ui/compose/notifications/create-notification?hl=en
- https://developer.android.com/training/monitoring-device-state/doze-standby
- https://developer.android.com/develop/background-work/background-tasks/persistent
- https://support.google.com/googleplay/android-developer/answer/9969861?hl=en

## 4. Quyết định, mở và rủi ro

### Decision Log
- **VAL-D005:** Product Owner chọn **Notification** làm nơi hiển thị nhanh từ vựng; đây là lựa chọn trải nghiệm cần kiểm chứng, **không khóa chức năng MVP, UI hay cơ chế kỹ thuật**.
- **VAL-D004:** Có 2 tình huống học: (a) tiếp xúc từ mới trong khoảnh khắc ngắn, (b) chủ động nêu thời lượng rảnh và nhận đề xuất bài.
- **VAL-D003:** Hoãn kiểm định file mẫu do chưa thể upload; không tự đánh giá nội dung đã phù hợp.

### Open Questions
- **OQ-N01 (NEXT):** Người dùng muốn **thông báo xuất hiện theo lịch** hay muốn **một từ xuất hiện mỗi khi bật điện thoại**? Đây là hai trải nghiệm khác nhau.
- OQ-N02: Tần suất, giờ yên tĩnh, quyền kiểm soát và tắt thông báo.
- OQ-N03: Nội dung notification: từ mới, từ ôn, nghĩa, ví dụ, cách phát âm hay bài hỏi nhanh?
- OQ-N04: Tiêu chí thử nghiệm (bắt đầu học, nhớ từ, khó chịu, tỷ lệ tắt thông báo).
- OQ-N05: Hiện thị đúng trên những phiên bản Android và thiết bị khác nhau; độ tin cậy khi Doze/tiết kiệm pin.
- OQ-C01: Content inventory, cấu trúc, chất lượng, audio mapping, bản quyền — chờ tài liệu mẫu.

### Risks
- **R-N01:** Quá nhiều thông báo khiến người dùng tắt quyền hoặc gỡ app.
- **R-N02:** Doze/khóa màn hình/bộ tiết kiệm pin khiến thời gian/hiển thị không như kỳ vọng.
- **R-N03:** Hiểu nhầm thông báo định kỳ có thể tự đổi từ ở mỗi lần sáng màn hình.
- **R-N04:** Quyền thông báo bị từ chối, app vẫn phải học được bình thường.

## 5. Quy trình thử nghiệm đề xuất — chưa thiết kế/viết code

1. Phỏng vấn cả 2 người pilot về mong muốn/khó chịu khi nhận thông báo.
2. Thử nghiệm mock-up bằng tin nhắn/tờ thẻ mẫu và khảo sát một tuần; tránh viết code khi chưa cần.
3. Đo tự báo cáo: có đọc hay bỏ qua, có nhớ nội dung sau một khoảng thời gian, có muốn tăng/giảm thông báo.
4. Khi đến Feasibility/Requirements, kiểm tra trên thiết bị Android thực tế: quyền, hiển thị, lịch, trạng thái pin, cài đặt khóa màn hình.
5. Không quyết định MVP cho đến khi so sánh mức giá trị với nỗ lực/rủi ro.

## 6. Gate & Next Question

- **Vision V1.0:** APPROVED.
- **Phase 02:** IN PROGRESS, HOLD — no sign-off to Requirements.
- **MVP/PRD/SRS/Architecture/Code:** NOT AUTHORIZED.
- **NEXT QUESTION:** Bạn muốn nhận thông báo từ vựng **theo lịch trong ngày** hay mong **mỗi khi bật điện thoại lên có một từ mới**? Lựa chọn chưa đủ rõ ở VAL-005.
