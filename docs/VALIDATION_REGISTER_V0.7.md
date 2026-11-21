# VALIDATION REGISTER V0.7 — TOEIC Learning App

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
| VAL-006 | Chế độ xuất hiện thông báo từ vựng | Người dùng chọn **kiểm chứng phương án ít gây phiền và hiệu quả nhất**; không chọn theo lịch/thường trực/mỗi lần bật màn hình | Quyết định chiến lược kiểm chứng; **không** là phê duyệt phương án kỹ thuật | RECORDED — EVALUATION PLAN REQUIRED |

## 2. Validation Register — Hypothesis & Evidence

| ID | Giả thuyết | Bằng chứng hiện có | Cần kiểm chứng | Trạng thái |
|---|---|---|---|---|
| H-001 | Người học cần cá nhân hóa sâu hơn và thao tác đơn giản hơn | VAL-001 | Benchmark có thang đo, phản hồi pilot #2+ | INCONCLUSIVE |
| H-002 | Học nhanh 1 từ / 1 câu giúp người dùng dễ bắt đầu | VAL-001, VAL-004 | Quan sát số thao tác, thời gian tới bài đầu tiên, sử dụng lặp | INCONCLUSIVE |
| H-003 | Thư viện TOEIC cá nhân đem lại giá trị | Có PDF/sách/audio, VAL-001/002 | Kiểm kê, đề mẫu, khả năng tách/gắn audio, quyền | INCONCLUSIVE; VAL-003 DEFERRED |
| H-004 | AI tạo đáp án/lời giải và câu hỏi nguyên bản đạt chất lượng với chi phí thấp | Ý tưởng Discovery | Gold set, kiểm duyệt chuyên môn, tính đúng, quyền, chi phí | NOT TESTED |
| H-005 | Full Mock Test phù hợp để so sánh tiến bộ qua nhiều lần | Định hướng Product Vision | Đề tương đương, độ khó, quy đổi điểm, tránh nhớ đề | NOT TESTED |
| H-006 | Thông báo từ vựng giúp tăng cơ hội tiếp xúc/học mà không gây phiền | VAL-004, VAL-005, VAL-006; Android hỗ trợ thông báo | So sánh hình thức thông báo, mức nhớ từ và gây phiền, opt-in/opt-out, thử trên thiết bị | INCONCLUSIVE |
| H-007 | Đề xuất bài theo thời gian rảnh giúp tăng tần suất học | VAL-004 | Thử nghiệm luồng chọn thời lượng và hoàn tất bài phù hợp | INCONCLUSIVE |
| H-008 | Pilot 2–5 người có thể vận hành gần như miễn phí | Ràng buộc ngân sách PD-020 | Ước tính API/host/audio/free tier | NOT TESTED |

**Lưu ý về ID:** H-006 tại phiên bản V0.3 là giả thuyết về chi phí, nay chuẩn hóa thành **H-008** để tránh trùng với H-006 đã dùng trong phiên trao đổi VAL-004/005. Không thay đổi nội dung giả thuyết cũ.

## 3. Android Notification — Feasibility (Desk Research Only)

**Nhu cầu xác nhận:** Người dùng muốn nhìn thấy từ vựng TOEIC từ hệ thống thông báo mà không cần mở app, đồng thời ưu tiên hiệu quả học tập **và** ít gây phiền. Việc hiển thị ở màn hình khóa phụ thuộc cài đặt Android và quyền riêng tư của người dùng.

**VAL-006 (2026-11-20):** Người dùng chọn hướng **thử nghiệm rồi quyết định**. Chưa chọn chế độ theo lịch, một thông báo thường trực, kết hợp, hay kích hoạt mỗi lần bật màn hình. Không mặc định việc bật màn hình là một trigger notification được hệ điều hành bảo đảm.

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

**Nguồn tham khảo (Android Developers):**
- https://developer.android.com/develop/ui/compose/notifications/create-notification?hl=en
- https://developer.android.com/training/monitoring-device-state/doze-standby
- https://developer.android.com/develop/background-work/services/alarms
- https://developer.android.com/develop/ui/compose/notifications/channels
- https://developer.android.com/develop/ui/compose/notifications/notification-permission
- https://support.google.com/googleplay/android-developer/answer/9969861?hl=en

## 4. Quyết định, mở và rủi ro

### Decision Log
- **VAL-D006 (APPROVED VALIDATION STRATEGY):** So sánh các cách hiển thị thông báo theo tiêu chí **ít gây phiền, giúp nhớ từ/học thật, dễ kiểm soát**; không khóa bất cứ chế độ kỹ thuật nào vào MVP. Ưu tiên thử nghiệm tự nguyện, cho phép dừng, không ép nhận thông báo.
- **VAL-D005:** Product Owner chọn **Notification** làm nơi hiển thị nhanh từ vựng; đây là lựa chọn trải nghiệm cần kiểm chứng, **không khóa chức năng MVP, UI hay cơ chế kỹ thuật**.
- **VAL-D004:** Có 2 tình huống học: (a) tiếp xúc từ mới trong khoảnh khắc ngắn, (b) chủ động nêu thời lượng rảnh và nhận đề xuất bài.
- **VAL-D003:** Hoãn kiểm định file mẫu do chưa thể upload; không tự đánh giá nội dung đã phù hợp.

### Open Questions
- **OQ-N01 (RESOLVED BY VAL-006):** Chưa chọn cơ chế xuất hiện; sẽ so sánh phương án thay vì chốt theo trực giác.
- OQ-N02 (NEXT): Thế nào là **gây phiền không chấp nhận được** (âm thanh/rung, thời điểm, số lượt nhắc, độ dai của thông báo)?
- OQ-N03: Nội dung notification: từ mới, từ ôn, nghĩa, ví dụ, cách phát âm hay bài hỏi nhanh?
- OQ-N04: Tiêu chí thử nghiệm (bắt đầu học, nhớ từ, khó chịu, tỷ lệ tắt thông báo).
- OQ-N05: Hiện thị đúng trên những phiên bản Android và thiết bị khác nhau; độ tin cậy khi Doze/tiết kiệm pin.
- OQ-C01: Content inventory, cấu trúc, chất lượng, audio mapping, bản quyền — chờ tài liệu mẫu.

### Risks
- **R-N01:** Quá nhiều thông báo khiến người dùng tắt quyền hoặc gỡ app.
- **R-N02:** Doze/khóa màn hình/bộ tiết kiệm pin khiến thời gian/hiển thị không như kỳ vọng.
- **R-N03:** Hiểu nhầm thông báo định kỳ có thể tự đổi từ ở mỗi lần sáng màn hình.
- **R-N04:** Quyền thông báo bị từ chối, app vẫn phải học được bình thường.

## 5. Kế hoạch kiểm chứng đề xuất — CHƯA triển khai, không viết code

**Mục tiêu:** Xem thông báo có giúp người dùng tiếp xúc, nhớ từ và tự nguyện tiếp tục sử dụng mà không làm họ khó chịu hay không; không lấy số thông báo đã gửi làm thước đo thành công.

| Phương án thử nghiệm | Cách giả lập ban đầu (không code sản phẩm) | Điểm cần đo |
|---|---|---|
| A — Theo lịch, ít lần | Gửi 1–2 thẻ từ vựng/ngày vào khung giờ người tham gia tự nguyện chọn, dùng công cụ nhắc/tin nhắn sẵn có | Số lần xem, nhớ từ sau ~24 giờ, mức gây phiền |
| B — Một từ có sẵn để xem khi rảnh | Để một thẻ từ dễ truy cập (ví dụ ghi chú ghim) làm **proxy cho mô hình thường trực**, không giả vờ đã thử notification thật | Số lần chủ động xem, tỷ lệ nhớ, chủ động dùng tiếp |
| C — Kết hợp | Chỉ thử sau A/B nếu giá trị kỳ vọng rõ, đồng thời tránh nội dung trùng | Lợi ích bổ sung so với mức gây phiền tăng thêm |

- Tập hợp ít nhất người dùng 01 và 02 nếu họ đồng ý; thử các phương án trong khoảng thời gian ngắn tương đương, cho phép tắt/bỏ cuộc bất kỳ lúc nào. Thời lượng và ngưỡng đạt cần được Product Owner duyệt trước khi tiến hành.
- Đo dự kiến: lượt **đã nhìn thấy** (không chỉ đã gửi), số từ nhớ sau khoảng 24 giờ, cảm nhận gây phiền (thang 1–5), số lần bỏ qua/tắt, và mức sẵn sàng tiếp tục. Các chỉ số và ngưỡng nghiệm thu vẫn là **đề xuất**.
- Các bản giả lập không chứng minh Android hiển thị ổn định; kiểm tra trên máy thật, quyền, lock-screen và Doze phải thực hiện sau khi có quyền làm feasibility test.
- Không đề nghị `exact alarm`, foreground service hoặc screen-on trigger khi không có nhu cầu kỹ thuật hợp lệ và chưa đánh giá tác động.
- Nếu không đo được hiệu quả ghi nhớ và mức phiền một cách đáng tin, đánh dấu **INCONCLUSIVE**, không tự phê duyệt MVP.

## 6. Gate & Next Question

- **Vision V1.0:** APPROVED.
- **Phase 02:** IN PROGRESS, HOLD — no sign-off to Requirements.
- **MVP/PRD/SRS/Architecture/Code:** NOT AUTHORIZED.
- **NEXT QUESTION:** Đối với thông báo học từ, kiểu làm phiền nào bạn **không chấp nhận** (âm thanh/rung, chen vào lúc bận/ngủ, lặp quá nhiều, thông báo nằm mãi trong khay)? Cần ràng buộc trải nghiệm trước khi thiết kế thử nghiệm.
- **VAL-006 status:** CHOICE OF EVALUATION APPROVED; hiệu quả học & mức gây phiền chưa kiểm chứng; MVP NOT LOCKED.
