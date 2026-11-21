# VALIDATION REGISTER V1.0 — TOEIC Learning App

- **Ngày cập nhật:** 2026-11-20
- **Giai đoạn:** 02/11 — Market Research & Validation (IN PROGRESS)
- **Product Vision:** V1.0 APPROVED, không thay đổi
- **Phase 02 Gate:** HOLD — cần bằng chứng thực tế trước khi duyệt Requirements
- **Code / UX / architecture:** NOT AUTHORIZED
- **Nguồn bằng chứng:** Người dùng pilot #1 tự báo cáo (bao gồm VAL-009), tài liệu chính thức Android Developers/Google Play; chưa chạy thử notification hoặc xem tài liệu TOEIC mẫu.

## 1. Validation Log

| ID | Nội dung | Dữ liệu thu thập được | Phân loại | Trạng thái |
|---|---|---|---|---|
| VAL-001 | Trải nghiệm các app TOEIC hiện có | Người dùng thấy cá nhân hóa hạn chế, nhiều thao tác, phí cao; khó ôn tài liệu sẵn có | Nhu cầu định tính một người; chưa đại diện thị trường | RECORDED — NOT MARKET VALIDATED |
| VAL-002 | Kho tài liệu TOEIC | Có kết hợp PDF/sách/audio nhiều loại | Tự báo cáo; chưa kiểm kê/chứng minh quyền | RECORDED — NOT FEASIBILITY VALIDATED |
| VAL-003 | Kiểm định một bộ đề mẫu | Người dùng hiện không thể tải bộ đề lên | Thiếu dữ liệu đầu vào, không phải kết quả thất bại | DEFERRED / PENDING EVIDENCE |
| VAL-004 | Thời điểm học cực nhanh | Người dùng có thời gian rảnh bất kỳ; mong thấy từ mới không cần mở app và khi rảnh khai báo thời lượng để được gợi ý bài | Nhu cầu cá nhân đã được ghi nhận | RECORDED — NOT USABILITY TESTED |
| VAL-005 | Vị trí hiển thị từ vựng | Người dùng chọn **thông báo Android** (không chọn widget/home hay màn hình khóa tùy chỉnh) | Lựa chọn trải nghiệm của một người | RECORDED — ANDROID FEASIBILITY PARTIAL |
| VAL-006 | Chế độ xuất hiện thông báo từ vựng | Người dùng chọn **kiểm chứng phương án ít gây phiền và hiệu quả nhất**; không chọn theo lịch/thường trực/mỗi lần bật màn hình | Quyết định chiến lược kiểm chứng; **không** là phê duyệt phương án kỹ thuật | RECORDED — EVALUATION PLAN REQUIRED |
| VAL-007 | Tương tác ngay trên thông báo | Muốn **Đã nhớ → từ khác**, **Ẩn từ**, **Tắt tất cả thông báo từ vựng**, **Nhắc sau X phút**; đã làm rõ phạm vi tắt tại VAL-008 | Nhu cầu thực tế từ một người pilot; chưa phải UX/MVP/implementation sign-off | RECORDED — FEASIBILITY PARTIAL / USABILITY NOT TESTED |
| VAL-008 | Phân biệt ẩn từ và tắt kênh học từ | **Ẩn từ này** chỉ ảnh hưởng từ đang xem; **Tắt tất cả** dừng mọi thông báo từ vựng cho tới khi người dùng bật lại; là hai lựa chọn tách biệt | Quyết định về ý nghĩa hành vi; KHÔNG phải phê duyệt nút UI hay logic ôn tập | RECORDED — INTENT CONFIRMED / IMPLEMENTATION OPEN |
| VAL-009 | Quyền chọn mức âm/rung khi có thông báo | Người dùng yêu cầu **tự chọn im lặng, rung hoặc âm thanh**; chưa chọn chế độ mặc định, giờ yên tĩnh, nhịp gửi | Trải nghiệm đã xác nhận; chưa thử mức gây phiền, chưa phê duyệt UI/MVP | RECORDED — USER CONTROL CONFIRMED / EFFECTIVENESS INCONCLUSIVE |

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
- OQ-N02 (PARTIALLY RESOLVED BY VAL-009): Người dùng được quyền chọn **im lặng/rung/âm thanh**. Mặc định, giờ yên tĩnh, tần suất và ngưỡng gây phiền còn OPEN.
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
- **Historical prompt after VAL-008 (answered at VAL-009):** thông báo mặc định im lặng/rung/âm thanh; VAL-009 đã quyết định người dùng tự chọn, mặc định còn để mở.
- **VAL-006 status:** CHOICE OF EVALUATION APPROVED; hiệu quả học & mức gây phiền chưa kiểm chứng; MVP NOT LOCKED.


## 7. Validation 07 — Notification Actions (2026-11-20)

**Nguồn:** Product Owner phản hồi trực tiếp về trải nghiệm mong muốn: trên thông báo có các lựa chọn (1) đã nhớ từ, hiển thị từ khác; (2) tắt không hiện nữa; (3) hiện lại sau một khoảng phút lựa chọn. Đây là yêu cầu về hành vi và quyền kiểm soát, **không chốt MVP/UI/công nghệ**.

| ID | Yêu cầu/giả thuyết | Đã xác nhận | Chưa xác minh |
|---|---|---|---|
| VAL-007A | `Đã nhớ` để nhận từ khác | Mong muốn có thao tác trên thông báo | Từ đã nhớ sẽ được ôn lại hay đánh dấu thành thạo? Thời điểm chuyển từ? |
| VAL-007B | `Tắt, không hiện nữa` | Cần một cách từ chối hiển thị | **Chỉ từ hiện tại**, toàn bộ thông báo từ vựng, hay cả hai? |
| VAL-007C | `Hiện sau X phút` | Mong muốn trì hoãn linh hoạt | Hoãn chính từ hiện tại hay tất cả; các mốc thời gian; độ tin cậy scheduler |
| VAL-007D | Thao tác không cần mở ứng dụng | Giảm số bước học | Thử trên các phiên bản Android và thiết bị pilot; giao diện hệ điều hành có thể thay đổi |

**Android feasibility desk research:** Android notification có thể chứa tới ba action buttons; nhận action qua pending intent/receiver, không nhất thiết mở app. Từ Android 13, thông báo thông thường cần quyền `POST_NOTIFICATIONS`. Các lệnh 'nhắc sau X phút' phụ thuộc cơ chế lên lịch có thể bị Doze/battery saver trì hoãn; không cam kết thời điểm chính xác tuyệt đối cho notification học từ. Các action cụ thể và trạng thái học phải được kiểm chứng trước khi đặc tả.

**Sources (official):**
- https://developer.android.com/develop/ui/compose/notifications/create-notification
- https://developer.android.com/reference/android/app/Notification.Builder
- https://developer.android.com/develop/background-work/services/alarms
- https://developer.android.com/develop/ui/compose/notifications/notification-permission

**Risks/validation:**
- `Đã nhớ` tự báo cáo không đồng nghĩa đã thuộc từ bền vững; cần đo nhớ sau 24 giờ hoặc thời gian phù hợp trong thử nghiệm.
- Bấm `Tắt` với ý nghĩa mơ hồ có thể vô tình chặn toàn bộ notification, gây mất kiểm soát.
- Khi hệ thống chưa cấp quyền/đang chế độ tiết kiệm pin, không thể bảo đảm hiển thị đúng hẹn.
- Tối đa 3 action có thể khiến nhãn, nội dung thu gọn không hiển thị đồng nhất trên mọi thiết bị.

**Status:** Interaction concept RECORDED; technical feasibility PARTIAL; user value/effectiveness INCONCLUSIVE; MVP NOT APPROVED. VAL-003 vẫn DEFERRED cho tới khi có file đề.

**NEXT QUESTION:** Từ lựa chọn `Tắt không hiện nữa`, người dùng muốn (A) chỉ bỏ từ hiện tại, (B) tắt mọi thông báo học từ cho đến khi tự bật lại, hay (C) cần cả hai lựa chọn tách biệt? Chỉ hỏi điểm này trước khi thiết lập thử nghiệm chi tiết.


## 8. Validation 08 — Separate "Hide Word" and "Disable All Vocabulary Notifications" (2026-11-20)

**Evidence / decision (VAL-D008, confirmed by Product Owner):** Người dùng chọn cả hai hành vi tách biệt. Đây là quyết định về **ngữ nghĩa hành động**, không phải phê duyệt số lượng/nội dung nút giao diện hay phạm vi MVP.

| Behavior ID | Hành vi mong muốn đã xác nhận | Không được tự suy diễn | Trạng thái |
|---|---|---|---|
| N-A01 | `Đã nhớ` ghi nhận phản hồi và yêu cầu chuyển sang từ khác | Không đánh dấu từ đã thuộc vĩnh viễn; thời điểm ôn lại chưa chốt | EXPERIENCE CONFIRMED, LOGIC OPEN |
| N-A02 | `Ẩn từ này` loại từ đang hiển thị ra khỏi nội dung notification trước mắt; thông báo với từ khác vẫn có thể đến | Không tự tắt tất cả notification; chưa chốt ẩn từ vô thời hạn hay chỉ tạm thời | INTENT CONFIRMED, DURATION OPEN |
| N-A03 | `Tắt tất cả` dừng **tất cả thông báo học từ vựng** cho đến khi người dùng tự bật lại | Không tự suy diễn là tắt thông báo khác trong app hay tắt bằng một nút system-setting không thể đảo ngược | INTENT CONFIRMED, UX OPEN |
| N-A04 | `Nhắc lại sau X phút` cho người học hoãn lời nhắc | Chưa chốt hoãn từ đang xem hay cả loạt thông báo, các khoảng thời gian và độ chính xác | INTENT CONFIRMED, SCHEDULING OPEN |

**Android feasibility constraint (official documentation):** Một notification mở rộng hỗ trợ tối đa **ba action buttons**, trong khi hiện có **bốn hành vi**. Không hứa bốn nút cùng hiển thị; nhóm giải pháp cần nghiên cứu ở giai đoạn UX/feasibility có thể gồm thao tác trong app/settings hoặc gộp luồng có chủ đích, nhưng chưa chọn cách nào. Người dùng có thể thay đổi quyền, âm/rung/importance qua Notification Channels; hiển thị thực tế phụ thuộc máy, Android version, quyền và trạng thái nền.

**Nguồn chính thức:**
- https://developer.android.com/develop/ui/compose/notifications/create-notification (tối đa 3 notification actions)
- https://developer.android.com/develop/ui/compose/notifications/channels (người dùng điều khiển notification channel)
- https://developer.android.com/training/monitoring-device-state/doze-standby (thời điểm nhắc có thể bị trì hoãn)

**Rủi ro cập nhật:**
- **R-N05:** `Ẩn từ này` và `Tắt tất cả` dễ bị hiểu nhầm/bấm nhầm; đánh giá phân biệt nhãn và kiểm soát khôi phục.
- **R-N06:** Bốn chức năng vượt số lượng action trực tiếp tối đa (3) của notification mở rộng; cần thử usability trên Android thật trước khi yêu cầu UX/UI.
- **R-N07:** `Đã nhớ` không bảo đảm ghi nhớ bền vững; cần thử nhớ lại, không loại vĩnh viễn khỏi lịch ôn dựa trên một lần chạm.

**Validation experiment bổ sung (chưa triển khai):** Cho người dùng pilot phân biệt hai tình huống `không muốn thấy lại từ X` và `không muốn nhận thông báo từ vựng nữa`, quan sát họ có chọn đúng hành động và biết cách bật lại không. Thu thập mức gây phiền, tỷ lệ bấm nhầm và phản hồi về sự tự chủ.

**Open questions còn lại, không hỏi dồn:**
1. **NEXT (VAL-009):** Mặc định thông báo nên im lặng, rung nhẹ hay có âm thanh? Đây là một đầu vào cho thử nghiệm mức gây phiền.
2. Khi nào một từ đã ẩn có thể được đưa trở lại để ôn (nếu có)?
3. Các mốc `X phút` và nội dung nào được nhắc lại?
4. Từ vựng có phù hợp để hiện trên thiết bị/màn hình khóa theo thiết lập riêng tư của người học không?
5. Đặt tiêu chí nghiệm thu thử nghiệm, đo khả năng ghi nhớ, việc sử dụng tự nguyện và tần suất tắt.

**Gate:** Product Vision V1.0 APPROVED; Stage 02 IN PROGRESS/HOLD; **no MVP approval, no UI architecture or code**. VAL-003 content sample remains DEFERRED.


## 9. Validation 09 — Tùy chọn âm thanh / rung / im lặng (2026-11-20)

**Nguồn bằng chứng:** Product Owner chọn phương án D: **người học tự tùy chỉnh âm thanh, rung hoặc im lặng** cho thông báo từ vựng. Chưa có thử nghiệm hành vi trên thiết bị hoặc với người học #2.

### Quyết định VAL-D009

- **CONFIRMED EXPERIENCE INTENT:** Cho phép người học chọn giữa **im lặng / rung / âm thanh**; không ép tất cả dùng chung một mức độ làm phiền.
- **NOT DECIDED:** Chế độ mặc định, khung giờ yên tĩnh, tần suất tối đa, thời điểm xin quyền, cơ chế thay đổi tùy chọn, UX màn hình cài đặt, các channel kỹ thuật.
- Giữ nguyên VAL-D008: `Ẩn từ này` khác `Tắt tất cả thông báo học từ vựng`; cả hai khác với việc bật/tắt âm thanh.
- Đây là **quyết định về nhu cầu người dùng**, không phải phê duyệt chức năng MVP hoặc kiến trúc.

### Đánh giá khả thi Android (desk research, chưa thử máy)

| Khía cạnh | Căn cứ chính thức / rủi ro | Kết luận |
|---|---|---|
| User control | Android 8.0+ dùng notification channels; người dùng có thể điều chỉnh importance/âm thanh/rung của kênh | FEASIBLE IN PRINCIPLE |
| Quyền ứng dụng | Android 13+ yêu cầu `POST_NOTIFICATIONS` cho thông báo thường | PHẢI CÓ QUYỀN |
| Khả năng app thay đổi thuộc tính channel | Sau khi channel được tạo, app không được tự thay đổi hành vi âm thanh/hiển thị của channel; chỉ người dùng thay đổi ở system settings | CẦN ĐÁNH GIÁ LUỒNG THAY ĐỔI TÙY CHỌN, KHÔNG HỨA CÔNG TẮC ỨNG DỤNG SẼ LUÔN GHI ĐÈ CÀI ĐẶT HỆ THỐNG |
| Chế độ hệ thống | DND, tùy biến nhà sản xuất/Android và cài đặt riêng tư có thể điều chỉnh việc rung/phát âm | PHẢI KIỂM THỬ TRÊN THIẾT BỊ |
| Giá trị người học | Thêm quyền tùy chỉnh có thể giảm cảm giác bị làm phiền nhưng chưa đo được | H-006 INCONCLUSIVE |

**Nguồn chính thức:**
- https://developer.android.com/develop/ui/compose/notifications/channels
- https://developer.android.com/develop/ui/compose/notifications/notification-permission
- https://developer.android.com/design/ui/mobile/guides/home-screen/notifications

### Giả thuyết / kế hoạch kiểm chứng (chưa thực hiện)

- **H-006 (INCONCLUSIVE):** Có tùy chọn âm/rung/im lặng và quyền ẩn/tắt sẽ làm thông báo học từ **dễ chấp nhận hơn**, nhưng hiệu quả học và mức phiền chưa xác định.
- **H-009 (NEW — NOT TESTED):** Khi có quyền chọn mức thông báo, người học sẽ duy trì việc sử dụng nhiều hơn so với một chế độ cố định; phải kiểm chứng bằng hành vi thực tế, không suy luận từ lựa chọn khảo sát.
- **Phương án thử nghiệm, chưa duyệt:** Bắt đầu im lặng như một **điểm xuất phát thử nghiệm** (không chốt mặc định sản phẩm), người tham gia được chủ động đổi rung/âm thanh; so sánh số lần xem, tỷ lệ tắt/ẩn/hoãn, mức gây phiền 1–5, nhớ từ sau khoảng 24 giờ, mong muốn tiếp tục. Thử nghiệm thủ công không chứng minh khả thi Android; cần kỹ thuật test thiết bị ở giai đoạn phù hợp.
- **R-N08:** Hứa có tùy chỉnh trong app nhưng bị giới hạn bởi cài đặt Notification Channel của Android; cần kiểm chứng và hướng dẫn rõ khi người dùng cần mở system settings.

### Open Questions — không chặn việc chuyển sang giả thuyết khác

- OQ-N02A: Mặc định âm thanh/rung/im lặng là gì? Đánh giá qua thử nghiệm, **chưa quyết định**.
- OQ-N02B: Giờ yên tĩnh và tần suất thế nào để không gây phiền?
- OQ-N02C: Cách chỉnh tùy chọn và hành vi khi Android system settings xung đột với lựa chọn trong app?
- OQ-N02D: Mức nhớ từ và tỷ lệ tắt/ẩn/hoãn có cải thiện khi có tùy chỉnh?

### Phase 02 Gate và bước tiếp theo

- **Product Vision V1.0:** APPROVED, không đổi.
- **Phase 02:** IN PROGRESS / HOLD. **MVP, PRD/SRS, UX/UI, architecture, code: NOT AUTHORIZED.**
- **VAL-003:** Đánh giá PDF/audio mẫu DEFERRED do chưa thể tải file, không yêu cầu tải lại vào lúc này.
- **NEXT VALIDATION PRIORITY — VAL-010:** Quay lại Market/Price Validation; hỏi Product Owner 1–3 ứng dụng TOEIC họ từng dùng/cân nhắc, gói giá (nếu nhớ), và nỗi đau cụ thể. Bằng chứng cá nhân chưa đủ kết luận thị trường hiện có giá cao. Song song lên kế hoạch benchmark giá và trải nghiệm từ nguồn công khai/hands-on.
