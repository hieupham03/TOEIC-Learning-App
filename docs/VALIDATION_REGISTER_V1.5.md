# VALIDATION REGISTER V1.5 — TOEIC Learning App

- **Ngày cập nhật:** 2026-11-20
- **Giai đoạn:** 02/11 — Market Research & Validation (IN PROGRESS)
- **Product Vision:** V1.0 APPROVED, không thay đổi
- **Phase 02 Gate:** HOLD — cần bằng chứng thực tế trước khi duyệt Requirements
- **Code / UX / architecture:** NOT AUTHORIZED
- **Latest observation:** VAL-014 Product Owner chọn **C: kiểm chứng cả Listening và Reading, tách hai nhánh thử độc lập** (`VAL-013L`, `VAL-013R`); kế hoạch no-code nâng V0.3. **NEXT:** VAL-015 kiểm tra có người hỗ trợ điều phối mô phỏng Wizard-of-Oz hay không. **Cả hai nhánh chưa chạy; H-003-VALUE INCONCLUSIVE.**
- **Nguồn bằng chứng:** Người dùng pilot #1 tự báo cáo (bao gồm VAL-009, quyết định hoãn VAL-010, lời kể lại người học #2 tại VAL-011 và khó khăn luyện đề tại VAL-013), tài liệu chính thức Android Developers/Google Play; chưa chạy thử notification hoặc xem tài liệu TOEIC mẫu; VAL-013 mới mô tả vấn đề, chưa có thử nghiệm hành vi.

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
| VAL-010 | Trải nghiệm chi phí và giới hạn dịch vụ của các app TOEIC khác | Product Owner chọn **tạm thời bỏ qua** việc cung cấp tên app/giá từng trả/cân nhắc; không có thêm bằng chứng trải nghiệm cá nhân. Đối chiếu sơ bộ từ trang chính thức đã được ghi riêng tại mục Market Snapshot. | Quyết định tạm hoãn thu thập bằng chứng; không phải phủ nhận nhu cầu hay xác nhận giá thị trường cao | **DEFERRED BY PRODUCT OWNER — NOT VALIDATED** |
| VAL-011 | Đối chiếu vấn đề của người học pilot #2 | Product Owner trả lời người #2 “cũng như tôi thôi”: có các khó khăn tương tự người #1 ở mức tổng quát; chưa xác nhận từng vấn đề hoặc thứ tự ưu tiên, đặc biệt nhu cầu thư viện tài liệu cá nhân | Báo cáo gián tiếp từ Product Owner, KHÔNG phải phỏng vấn trực tiếp / quan sát hành vi người #2 | **RECORDED — SECOND-HAND EVIDENCE; NEEDS INDEPENDENT CONFIRMATION** |
| VAL-012 | Chọn ưu tiên kiểm chứng đầu tiên | Product Owner chọn **C — giá trị tận dụng thư viện TOEIC cá nhân**, thay vì A microlearning hay B lộ trình theo thời lượng | Quyết định ưu tiên kiểm chứng; không phải kết quả thử nghiệm hoặc phê duyệt MVP | **PRIORITIZED — EXPERIMENT NOT RUN** |
| VAL-013 | Vấn đề ưu tiên khi dùng đề cá nhân | Product Owner chọn **E — mọi bước đều bất tiện**: mở đề, chuyển qua nhiều tab/ứng dụng để nghe audio và chọn đáp án, rồi dò đáp án/lời giải. Muốn trải nghiệm làm bài tích hợp **tương tự website luyện đề phổ biến**, trên bộ tài liệu mình đã có; không yêu cầu phát minh cách làm bài mới. | Phản hồi định tính trực tiếp từ pilot #1; chưa quan sát thao tác, chưa có dữ liệu thời gian hoặc file mẫu; không chứng minh sự khả thi nhập đề | **PAIN POINT CONFIRMED BY OWNER — H-003-VALUE INCONCLUSIVE; TEST PLAN REVISED, NOT RUN** |

| VAL-014 | Phạm vi thử nghiệm no-code cho luồng luyện đề cá nhân | Product Owner chọn **C: cả Listening và Reading nhưng tách riêng**; không gộp số liệu hai kỹ năng; không yêu cầu upload file | Quyết định thiết kế phép thử, không phải dữ liệu đo, phê duyệt tính năng hay kết luận hiệu quả | **PLAN SCOPE CONFIRMED — VAL-013L / VAL-013R NOT RUN** |

## 2. Validation Register — Hypothesis & Evidence

| ID | Giả thuyết | Bằng chứng hiện có | Cần kiểm chứng | Trạng thái |
|---|---|---|---|---|
| H-001 | Người học cần cá nhân hóa sâu hơn và thao tác đơn giản hơn | VAL-001 | Benchmark có thang đo, phản hồi pilot #2+ | INCONCLUSIVE |
| H-002 | Học nhanh 1 từ / 1 câu giúp người dùng dễ bắt đầu | VAL-001, VAL-004 | Quan sát số thao tác, thời gian tới bài đầu tiên, sử dụng lặp | INCONCLUSIVE |
| H-003 | Thư viện TOEIC cá nhân đem lại giá trị | Có PDF/sách/audio, VAL-001/002/013/014 | Đo riêng `H-003-VALUE-L` (Listening) và `H-003-VALUE-R` (Reading) bằng A/B mô phỏng no-code; kiểm kê/đề mẫu/audio/đáp án/quyền sau | INCONCLUSIVE; BOTH TESTS NOT RUN; VAL-003 DEFERRED |
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


---

## VAL-010 UPDATE (2026-11-20) — PRICE EXPERIENCE DEFERRED, MARKET SNAPSHOT ONLY

**Quyết định VAL-D010 — DEFERRED:** Product Owner chọn **tạm thời bỏ qua** câu hỏi về những app TOEIC đã dùng và mức giá/giới hạn cụ thể từng trải nghiệm. Không hỏi lại ở các bước ngay tiếp theo. Việc này **không hủy bỏ** mong muốn chi phí dễ tiếp cận và **không khẳng định** các app đối thủ đều quá đắt.

### Đối chiếu dữ liệu công khai (desk research; không trải nghiệm trực tiếp)

| Đối thủ | Bằng chứng từ nhà cung cấp | Giới hạn kết luận |
|---|---|---|
| STUDY4 | Trang khóa học TOEIC niêm yết khóa Complete TOEIC **1.050.000đ (giá ưu đãi)** và giá gốc **1.800.000đ** khi tra cứu | Giá khóa học, không phải phí subscription tương đương; khuyến mãi thay đổi |
| PREP | Trang luyện đề TOEIC công bố **25 đề cơ bản** và gói PRO mở khóa kho đề/tính năng khác | Chưa xác định trải nghiệm thực tế, giá PRO tại cùng mốc |
| Migii TOEIC | Trang sản phẩm mô tả lộ trình TOEIC và khả năng nâng cấp Premium | Không khẳng định giá chính xác hoặc giới hạn theo thị trường VN tại thời điểm này |

**Nguồn chính thức (truy cập ngày 2026-11-20):**
- https://study4.com/courses/online/toeic/
- https://prepedu.com/vi/toeic/test-practice
- https://migii.net/vi/toeic

**Đánh giá:** Có mô hình miễn phí, khóa học trả phí, Premium ở nhiều nền tảng, nhưng **chưa đủ bằng chứng về khả năng chi trả, tính tương đương của các gói, sự hài lòng, hoặc mức giá thị trường bị cho là quá cao**. H-001 (giá trị khác biệt) vẫn **INCONCLUSIVE**. Chiến lược monetization của app chưa phê duyệt.

### Cập nhật giả thuyết/đầu việc

- **H-PRICE-01 (INCONCLUSIVE / DATA COLLECTION DEFERRED):** Giá là rào cản đáng kể với người học Việt. Nguồn: phản hồi 1 người; chưa có dữ liệu về mức sẵn lòng trả, lựa chọn giữa gói và tính năng, hoặc đánh giá gói cạnh tranh. Sẽ xem xét lại vào thời điểm quyết định chiến lược thương mại, **chỉ khi Product Owner muốn**.
- **VAL-003:** kiểm định PDF/audio vẫn DEFERRED do chưa thể upload; không gán thất bại kỹ thuật.
- **H-006/H-009:** thông báo tùy chỉnh mới chỉ được ghi nhận về nhu cầu; hiệu quả học và mức độ gây phiền chưa thử nghiệm.
- **NEXT — VAL-011:** Thu thêm bằng chứng từ **người học #2 (~650 TOEIC chính thức, mục tiêu 750–850)**: khó khăn khi học, kỳ vọng app, và khả năng bắt đầu phiên học ngắn. Không suy đoán hai người có cùng nhu cầu. Nếu chưa trao đổi với người #2, ghi NOT COLLECTED và chuẩn bị 3–5 câu phỏng vấn ngắn, không ép người dùng cung cấp ngay.
- **Stage gate:** Product Vision V1.0 APPROVED; Phase 02 IN PROGRESS / HOLD; **NO MVP APPROVAL, NO UX/UI, NO ARCHITECTURE, NO CODE**.
- **Canonical register:** `docs/VALIDATION_REGISTER_V1.1.md`; các bản V0.3–V1.0 lưu lịch sử.

---

## VAL-011 UPDATE (2026-11-20) — SECOND PILOT LEARNER, INDIRECT REPORT

**Nguồn:** Product Owner trả lời về người học #2: “Cũng như tôi thôi.” Đây là thông tin do Product Owner truyền đạt, **chưa có lời kể trực tiếp, phỏng vấn hay quan sát** của người học #2.

**Kết luận ghi nhận:**
- Có tín hiệu người học #2 (~650 TOEIC chính thức, mục tiêu 750–850) gặp các trở ngại học TOEIC tương tự người #1 (~550 mock, mục tiêu 650–750).
- Có thể tạm xem **khó tìm lộ trình phù hợp, học không đều, thiếu cá nhân hóa và học nhanh chưa thuận tiện** là các vấn đề chia sẻ theo báo cáo của Product Owner. Chưa biết mức độ hoặc thứ tự ưu tiên của từng vấn đề.
- Không suy ra người #2 sở hữu kho PDF/audio hoặc chắc chắn gặp khó khăn riêng về nhập tài liệu.
- Một lời kể gián tiếp **không được tính là bằng chứng độc lập thứ hai**, và không cho phép kết luận nhu cầu toàn thị trường đã VALIDATED.

**Validation Register changes:**
- `VAL-011 = RECORDED / SECOND-HAND EVIDENCE / DIRECT CONFIRMATION PENDING`.
- `H-001 = INCONCLUSIVE`; đã có tín hiệu phù hợp của hai người trong nhóm pilot, nhưng cần hỏi trực tiếp và quan sát hành vi.
- `H-002`, `H-003`, `H-007 = INCONCLUSIVE`, chờ ưu tiên bài kiểm chứng có thể thực hiện **không cần code và không cần file PDF**.
- `VAL-003 = DEFERRED` (chưa thể upload mẫu PDF/audio); `VAL-010 = DEFERRED BY PRODUCT OWNER` (giá đối thủ).

**NEXT — VAL-012: chọn một giả thuyết kiểm chứng đầu tiên (không code):**
1. `A`: Một từ / một câu TOEIC trong khoảng 30–60 giây, tối thiểu thao tác.
2. `B`: Người học nhập thời gian rảnh và được đề xuất một bài ngắn phù hợp.
3. `C`: Đo mức ưu tiên của kho tài liệu cá nhân bằng mô phỏng tình huống, **không khẳng định xử lý file**.
Quyết định ưu tiên thử nghiệm **không đồng nghĩa phê duyệt MVP**. Khi phù hợp, xác minh trực tiếp với người học #2 bằng vài câu hỏi ngắn, không bắt người dùng kể lại lần nữa ngay lúc này.

**Stage Gate:** Product Vision V1.0 APPROVED; Phase 02 Market Research & Validation IN PROGRESS / HOLD; Requirements/MVP/UX/UI/architecture/code NOT AUTHORIZED.


---

## VAL-012 UPDATE (2026-11-20) — ƯU TIÊN KIỂM CHỨNG GIÁ TRỊ THƯ VIỆN ĐỀ CÁ NHÂN

**Product Owner selection:** C — kiểm chứng **giá trị sử dụng** của `Personal TOEIC Library` trước các hướng microlearning nhanh và bài theo thời lượng. Product Vision V1.0 giữ nguyên APPROVED; giai đoạn 02 vẫn IN PROGRESS / HOLD.

### Tách bạch các giả thuyết, không đánh đồng ưu tiên với bằng chứng

| ID | Giả thuyết / câu hỏi | Bằng chứng hiện có | Kết quả hiện tại | Cần làm |
|---|---|---|---|---|
| H-003-VALUE | Một kho câu hỏi từ tài liệu người học đã có, được lập chỉ mục và truy cập thuận tiện, làm giảm ma sát bắt đầu và hoàn thành bài luyện | Người dùng có PDF/sách/audio và thấy việc ôn bằng nguồn sẵn có bất tiện; VAL-012 chọn ưu tiên thử | **INCONCLUSIVE; experiment selected, not run** | So sánh quy trình sử dụng PDF gốc với bản chỉ mục thủ công (no-code) |
| H-003-INGEST | Có thể tự động trích xuất chính xác câu, đáp án, hình, transcript, mốc audio từ tài liệu nhiều loại | Có tài liệu đa dạng, chưa có file mẫu | **PENDING EVIDENCE / VAL-003 DEFERRED** | Kiểm định tài liệu thực khi Product Owner có thể cung cấp |
| H-003-RIGHTS | Có thể dùng nội dung cho pilot và phân phối công khai với quyền tương ứng | Chưa có giấy phép/chứng cứ cụ thể | **UNKNOWN — LICENSING BLOCKER FOR PUBLIC DISTRIBUTION** | Kiểm kê tác giả, điều kiện sử dụng, phạm vi sao chép/chia sẻ |

### Đề xuất VAL-013 — thử nghiệm hành vi không cần code, không cần tải file

**Tên:** Manual Library Convenience Test / Wizard-of-Oz thủ công.

**Mục tiêu:** Kiểm tra việc người học dùng tài liệu *đã được lập chỉ mục theo Part, trang, câu, đáp án và vị trí audio* có thuận tiện hơn cách tự mở PDF/sách/audio hiện tại hay không. Chưa đánh giá tự động nhập file và chưa chứng minh tăng điểm TOEIC.

**Đối tượng:** người học #1 và (nếu tự nguyện) người học #2. Không biến thông tin do người #1 kể lại thành quan sát trực tiếp của #2.

**Chuẩn bị (không gửi file lên ChatGPT):**
1. Chọn **1 bộ đề mà từng người có quyền sử dụng phù hợp** và chọn một nhóm câu có đáp án (ưu tiên một Part Reading, nơi không bị nhiễu bởi thao tác audio; audio thử riêng sau). Không sao chép/tái phân phối nội dung sang bên không có quyền truy cập.
2. Soạn *chỉ mục riêng* khoảng 10–12 câu: `mã nguồn/tập`, `Part`, `trang/câu`, `trang đáp án`, `vị trí audio (nếu có)`, `độ khó ước lượng (nếu biết)`. Có thể dùng giấy ghi chú/ứng dụng ghi chú sẵn có. Không cần nhập nội dung câu hỏi có bản quyền vào dịch vụ ngoài.
3. Hai điều kiện: **A — hiện trạng:** tự mở PDF/sách và tìm câu/lời giải; **B — hỗ trợ thủ công:** sử dụng chỉ mục đã chuẩn bị để đến câu/đáp án. Mỗi điều kiện dùng 5 câu **khác nhau nhưng cùng Part/độ khó gần tương đương**; không tái sử dụng cùng câu.
4. Đổi thứ tự A/B giữa hai người nếu có thể để giảm tác động do quen thao tác. Cho phép tự học như thường ngày, không hỗ trợ trực tiếp khác nhau giữa hai điều kiện.
5. Dùng đồng hồ điện thoại để ghi mốc và phản hồi trong một bảng nhỏ. Ghi cả **thời gian tạo chỉ mục** (chi phí chuẩn bị), không chỉ thời gian học.

**Chỉ số đề xuất:**
- `T_start`: từ lúc quyết định học đến khi **nhìn thấy câu đầu tiên** (giây).
- `T_feedback`: từ khi trả lời đến khi **mở được đáp án/lời giải** (giây).
- `Completion`: số câu hoàn thành / 5 trong cùng một khoảng thời gian; ghi số lần bỏ dở vì thao tác.
- `Steps`: số thao tác chuyển màn hình/tìm trang đáng kể, đếm tương đối nhất quán.
- `Ease`: độ thuận tiện tự đánh giá 1–5 sau mỗi điều kiện; `Would use again`: Có/Không/Tùy điều kiện.
- `Prep cost`: phút chuẩn bị chỉ mục / 10 câu; ghi cả lỗi chỉ mục, đáp án không khớp, audio không ghép được (nếu thử).

**Ngưỡng quyết định sơ bộ (đề xuất để Product Owner duyệt trước khi thực hiện; không phải ngưỡng đã phê duyệt):**
- **Tín hiệu tích cực** nếu cả hai người (khi có hai người tham gia) thích B, `T_start` hoặc `T_feedback` của B giảm khoảng **30% trở lên**, và không phát sinh lỗi đối chiếu đáp án; đồng thời công sức chuẩn bị được đánh giá có thể chấp nhận. Đây chỉ là tín hiệu định tính/pilot, không kết luận thị trường.
- **Cần điều chỉnh** nếu lợi ích thời gian nhỏ, hoặc chỉ số thuận tiện tăng nhưng chuẩn bị quá tốn thời gian; xem xét ưu tiên tự động hóa nhập liệu trong Feasibility sau.
- **Inconclusive** nếu chưa thực hiện, chỉ có một vài quan sát quá ít, hoặc hai điều kiện không tương đồng; không được ghi `VALIDATED` chỉ từ mong muốn.

**Rủi ro diễn giải:** Bản chỉ mục thủ công không tương đương một app có trải nghiệm hoàn chỉnh; phép thử chỉ đo *giá trị của việc tổ chức nguồn tài liệu*, không đo độ chính xác OCR, matching audio, chất lượng AI, retention 4 tuần hay tác động tăng điểm TOEIC. Người dùng đã nói không thể upload file ở thời điểm hiện tại: **không hỏi lại file lúc này**.

**Chi tiết thao tác, phiếu ghi dữ liệu, cách kết luận:** `docs/VAL_013_LIBRARY_NO_CODE_TEST_PLAN_V0.1.md`.

### Gate & Next Question

- **VAL-012:** PRIORITY SELECTED; experiment NOT RUN; H-003-VALUE INCONCLUSIVE.
- **VAL-003:** DEFERRED (sample upload unavailable) — không được gán `FAILED`.
- **VAL-010:** DEFERRED BY PRODUCT OWNER — không thúc ép dữ liệu giá ở bước liền sau.
- **NEXT VAL-013:** Hỏi người dùng **bước thao tác nào phiền nhất khi dùng PDF/sách/audio hiện có** để xác định chính xác ma sát cần đo trước (tìm câu, mở audio đúng đoạn, dò đáp án, hay lưu lại lỗi sai). Một câu hỏi, không chuyển sang thiết kế UI hay code.
- **Product Vision:** V1.0 APPROVED, không đổi. **Phase 02:** IN PROGRESS/HOLD. **MVP/PRD/SRS/UX/UI/architecture/code:** NOT AUTHORIZED.


---

## VAL-013 UPDATE (2026-11-20) — MA SÁT CHÍNH LÀ QUY TRÌNH LUYỆN ĐỀ RỜI RẠC

**User evidence (direct, pilot #1):** “Tất cả, cần quy trình thống nhất”; phải mở đề, dò đáp án, chuyển nhiều tab để vừa nghe audio vừa chọn đáp án. Người dùng nói trải nghiệm luyện như các website luyện đề hiện có là đủ; điểm đau nằm ở **khả năng dùng chính kho đề hiện có theo luồng này**. Đây là mô tả nhu cầu, **không** phải bằng chứng rằng mọi website hiện có đều làm được, rằng nội dung có quyền để upload, hay rằng hệ thống đã có khả năng trích xuất PDF/audio.

**PAIN-004 refined:**
- `PAIN-004A`: Phải mở nhiều nguồn/tab để tìm và làm câu hỏi.
- `PAIN-004B`: Audio không được ghép thuận tiện với câu hỏi Listening.
- `PAIN-004C`: Chọn/lưu đáp án và dò đáp án/lời giải còn rời rạc.
- `PAIN-004D`: Lưu lỗi sai/ôn lại khó thao tác. Đây là vấn đề đã ghi nhận trước đó, chưa đo độc lập ở VAL-013.
- `PAIN-004E`: Có tài liệu nhưng khó biến thành bộ đề dùng được trong trải nghiệm luyện thi tiêu chuẩn.

**H-003 split, status unchanged:**
- `H-003-VALUE`: Nếu quy trình luyện đề được tổ chức thành một phiên liền mạch (đề + audio + đáp án + kết quả), người học giảm chuyển đổi ngữ cảnh, bắt đầu/hoàn tất nhanh hơn và muốn tiếp tục dùng. **INCONCLUSIVE** — chỉ mới có báo cáo định tính.
- `H-003-INGEST`: Tự động chuyển PDF/sách/audio sang dữ liệu câu hỏi có cấu trúc. **PENDING SAMPLE / VAL-003 DEFERRED**.
- `H-003-RIGHTS`: Có quyền số hóa, lưu trữ, chia sẻ và khai thác từng nguồn theo phạm vi sử dụng. **NOT VERIFIED**.

**VAL-013 TEST PLAN v0.2:** `docs/VAL_013_LIBRARY_NO_CODE_TEST_PLAN_V0.2.md` thay thế bản nháp V0.1 về mục tiêu và phép đo (bản cũ giữ lịch sử). So sánh (A) luồng tài liệu rời rạc hiện tại với (B) một **mô phỏng thủ công/Wizard-of-Oz** nơi người hỗ trợ đưa đúng câu, bật đúng audio, ghi đáp án và cung cấp kết quả trong một luồng, không cần app/copy đề lên dịch vụ khác. Nếu không có người hỗ trợ, có thể dùng ví dụ luyện đề hợp pháp đang công khai để *đối chiếu quy trình thao tác*, nhưng **không** so thời gian làm câu hay khả năng nghe hiểu giữa hai kho đề khác nhau như thí nghiệm tương đương.

**Primary measurements:** thời gian vào câu đầu (`T_start`), thời gian tìm/bật audio đúng câu (`T_audio`), số lần chuyển tab/tài liệu (`N_switch`), thời gian từ trả lời đến xem kết quả/giải thích (`T_feedback`), hoàn thành phiên, lỗi đối chiếu, độ thuận tiện 1–5, mong muốn dùng lại; **ghi riêng chi phí chuẩn bị thủ công của người hỗ trợ**. Tách Listening và Reading khi đọc kết quả. Tất cả ngưỡng chỉ là đề xuất, **chưa được owner phê duyệt**.

**Không được kết luận từ dữ liệu hiện tại:** tự động nhập tài liệu thành công, có quyền dùng thương mại, audio mapping chính xác, AI giải thích đúng, MVP phải có chức năng nào, hoặc điểm TOEIC tăng.

**VAL-014 — NEXT VALIDATION QUESTION:** Trong lần thử đầu tiên nên mô phỏng **Listening (PDF + audio + chọn đáp án)** hay **Reading (câu hỏi + chọn đáp án + lời giải)**? Hỏi người dùng **một câu trọng tâm** để chọn tình huống đo trước; không hỏi lại về giá đối thủ hoặc việc tải tài liệu lúc này.

**Gate:** Product Vision V1.0 APPROVED; Stage 02 IN PROGRESS / HOLD; **NO MVP, PRD/SRS, UX/UI, ARCHITECTURE OR CODE**.


## 8. Market Validation 14 — 2026-11-20 (current)

**Owner decision VAL-D014 — APPROVED VALIDATION SCOPE (NOT PRODUCT SCOPE):** Chọn **C — cả Listening và Reading, thử nghiệm TÁCH RIÊNG**. Hai nhánh:

- **VAL-013L / H-003-VALUE-L — Listening:** cách A = người học tự điều phối PDF/sách + audio + chọn/ghi đáp án + dò; cách B = người hỗ trợ điều phối cùng quy trình bằng tài liệu hợp lệ, KHÔNG code. Đo `T_start`, `T_audio_locate` (không tính thời lượng nghe), `N_switch`, `T_feedback`, sai ghép audio/câu, hoàn tất, tiện lợi, ý định dùng lại, thời gian chuẩn bị.
- **VAL-013R / H-003-VALUE-R — Reading:** A = tự mở PDF/sách, chọn/ghi đáp án, dò; B = người hỗ trợ điều phối thủ công. Đo tương tự, trừ `T_audio_locate = N/A`; bổ sung thời gian tìm câu/đáp án.

**Quy tắc so sánh:** chỉ so A vs B **trong cùng kỹ năng và cùng Part**, với câu *chưa làm* khác nhau nhưng gần tương đương; có thể đổi thứ tự giữa người tham gia. Không so điểm L với R, không tổng hợp thời gian hoặc độ chính xác hai Part thành một kết luận. Ghi số thao tác, thời gian và mức tiện thực tế của từng phiên; ghi tách chi phí chuẩn bị/điều phối B và khả năng sai khác độ khó.

**Proposed example, not locked:** Listening Part 3 mỗi điều kiện 1 đoạn hội thoại / 3 câu, nếu có audio được ghép đúng; Reading Part 5 khoảng 5 câu/điều kiện. Có thể thay nếu tài liệu hiện có không phù hợp; không đoán audio hoặc tạo đáp án mới.

**Evidence status:** Đây là lựa chọn của Product Owner về cách kiểm chứng; chưa có hành vi quan sát, số liệu, phép thử, kết quả lợi ích hoặc feasibility tự động nhập file. `H-003-VALUE-L` và `H-003-VALUE-R`: **NOT TESTED / INCONCLUSIVE**. `H-003-INGEST`: **DEFERRED** bởi VAL-003. `H-003-RIGHTS`: **UNKNOWN**.

**Artifacts:** `docs/VAL_013_LIBRARY_NO_CODE_TEST_PLAN_V0.3.md` (active); `docs/VAL_014_TWO_TRACK_TEST_LOG_V0.1.md` (blank capture sheet). `VAL_013_LIBRARY_NO_CODE_TEST_PLAN_V0.2.md` retained as history.

**NEXT — VAL-015:** Khảo sát **điều kiện thực hiện thử nghiệm**, cụ thể có người hỗ trợ điều phối độc lập (người đọc câu, phát đúng audio và dò đáp án) hay không. Nếu không, điều chỉnh phương án mô phỏng minh bạch, không giả định Wizard-of-Oz đã diễn ra. Chỉ hỏi một câu này, không yêu cầu upload PDF/audio.

**Stage Gate unchanged:** Product Vision V1.0 **APPROVED**. Stage 02 **IN PROGRESS — HOLD**. VAL-010 price comparison **DEFERRED BY PRODUCT OWNER**. Chưa thông qua PRD/SRS/MVP, UX/UI, kiến trúc hoặc lập trình.
