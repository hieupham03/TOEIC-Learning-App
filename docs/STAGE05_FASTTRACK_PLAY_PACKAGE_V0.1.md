# Stage05 FAST-03 — Gói chuẩn bị Google Play V0.1

Ngày 22/11/2026 (Asia/Saigon). Bản dành cho chuẩn bị **Internal/Closed Testing**, theo [workplan](STAGE05_FASTTRACK_48H_PREVIEW_14D_PLAY_PLAN_V0.1.md) và [issue #8](https://github.com/hieupham03/TOEIC-Learning-App/issues/8). Xem kết quả chạy thực tế trong [Play Submission Readiness](STAGE05_FASTTRACK_PLAY_SUBMISSION_READINESS_REPORT_V0.1.md).

## Cấu hình bản phát hành

| Mục | Giá trị |
|---|---|
| Tên ứng dụng | TOEIC Learning Demo |
| Package hiện tại | `vn.toeiclearning.alpha`. Chủ tài khoản cần kiểm tra trước khi chốt ID trong Play Console. Package đã đăng ký có tính lâu dài. |
| Version | `versionCode 2`, `versionName 0.2.0-preview`. Dùng code cao hơn mọi bản đã tải lên nếu Console đã có bản trước. |
| Android | minSdk 26, compileSdk 36, targetSdk 36. Play yêu cầu API 36+ cho app điện thoại mới và bản cập nhật từ 31/08/2026. [Target API level requirements](https://support.google.com/googleplay/android-developer/answer/11926878) |
| Runtime | Dùng vùng an toàn của hệ thống cho nội dung và thanh dưới. Compose nhận Back qua dispatcher. Bản API 36 chạy theo quy tắc edge-to-edge và Back của Android 16. [Android 16 behavior changes](https://developer.android.com/about/versions/16/behavior-changes-16) |

Chạy `gradlew.bat --offline --no-daemon --console=plain :app:bundleRelease` trong `android-app/` với JDK 17 và SDK Platform 36. AAB gốc không có chữ ký upload. Dùng `bundletool validate --bundle=<aab>` và `bundletool dump manifest --bundle=<aab> --module=base` để kiểm tra. Thư mục bàn giao cục bộ `android-app/.tooling/fasttrack/play/`. [Android App Bundle tools](https://developer.android.com/tools/bundletool)

Chủ tài khoản giữ upload key đã đăng ký hoặc tạo key khi thiết lập Play App Signing trong phạm vi được phê duyệt. Ký AAB bản sao bằng `jarsigner -keystore <keystore> -signedjar <signed.aab> <unsigned.aab> <upload-alias>` và nhập mật khẩu trực tiếp khi công cụ hỏi. Kiểm tra `jarsigner -verify -verbose -certs <signed.aab>`, đối chiếu vân tay chứng thư với upload certificate trên Console, rồi chạy lại `bundletool validate`. Bản ký kiểm thử cục bộ dùng Android debug certificate, chỉ dùng để tạo và cài APK trên emulator. [Sign your app](https://developer.android.com/studio/publish/app-signing)

## Nội dung listing nháp

- **Tên** TOEIC Learning Demo
- **Mô tả ngắn** Luyện Reading mẫu và thử Listening ngoại tuyến, không cần tài khoản.
- **Mô tả đầy đủ** TOEIC Learning Demo là bản minh họa luyện tập ngoại tuyến. Reading Part 5–7 có câu hỏi tự tạo, đoạn văn mẫu và giải thích sau khi chọn. Listening Part 1–4 minh họa cách phát âm thanh bằng các tệp thử nghiệm tự tạo và không chấm điểm. Bạn có thể chuyển câu, xem lại lựa chọn trong phiên và xóa lựa chọn trong Tiến độ. Bản này không có Full Mock khả dụng, ngân hàng đề chính thức, tài khoản hoặc điểm TOEIC.
- **Danh mục đề xuất** Education. Ngôn ngữ listing `vi`. Email hỗ trợ chưa có trong workspace.

Biểu tượng nháp `store-icon.png` (RGBA 512 × 512) và `feature-graphic.png` (RGB 1024 × 500) được lưu trong `android-app/.tooling/fasttrack/play/store/`. Ba ảnh chụp Android 16 từ APK tạo từ AAB là `phone-home.png`, `phone-reading.png` và `phone-listening.png` (RGB 1080 × 1920). Kiểm tra số ảnh và định dạng theo loại thiết bị đã chọn trong Console. [Yêu cầu về hình ảnh listing](https://support.google.com/googleplay/android-developer/answer/9866151) · [Thiết lập ứng dụng và listing](https://support.google.com/googleplay/android-developer/answer/9859152)

## Chính sách quyền riêng tư nháp

**Chính sách quyền riêng tư của TOEIC Learning Demo**

TOEIC Learning Demo hoạt động ngoại tuyến. Ứng dụng không có tài khoản, quảng cáo, SDK phân tích hoặc giao diện gửi dữ liệu qua mạng. Ứng dụng không truy cập danh bạ, vị trí, micro hay tệp cá nhân và không thu thập hoặc chia sẻ dữ liệu cá nhân.

Lựa chọn trong buổi DEMO tồn tại trong bộ nhớ của phiên trên thiết bị. Dùng **Tiến độ → Xóa lựa chọn tạm** để xóa ngay. Khi phiên kết thúc, lựa chọn không được lưu cho lần mở tiếp theo. App tắt sao lưu và loại các vùng lưu trữ ứng dụng khỏi cấu hình sao lưu và chuyển dữ liệu trên Android 12+. [Android Auto Backup](https://developer.android.com/identity/data/autobackup)

Liên hệ về quyền riêng tư qua địa chỉ hỗ trợ của nhà phát triển trên Google Play. Chủ tài khoản bổ sung tên pháp nhân/nhà phát triển và email thật vào bản công bố. App hiển thị nội dung quyền riêng tư tại tab **Cá nhân**. Khi nộp lên Play, cần URL công khai, truy cập được, không giới hạn địa lý hoặc yêu cầu đăng nhập. [Google Play User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311)

## Bản nháp các khai báo Console

| Mục | Câu trả lời cho bản kiểm thử hiện tại |
|---|---|
| App access | Mọi màn hình DEMO mở trực tiếp, không cần tài khoản hay quyền thiết bị đặc biệt. Full Mock có màn hình mô tả trạng thái khóa. |
| Ads | Không. Không có network ad SDK. |
| Data safety | Không thu thập, không chia sẻ từ app. Lựa chọn chỉ ở trong bộ nhớ. SDK runtime thuộc AndroidX và Kotlin. Xem audit bản build trong báo cáo readiness. Bản chỉ ở Internal Testing được miễn hiển thị Data safety theo hướng dẫn của Play. Chuẩn bị và kiểm tra biểu mẫu khi đưa sang Closed Testing. |
| Account deletion | Không có tạo tài khoản. Người dùng có thể xóa lựa chọn DEMO trong Tiến độ. |
| Sensitive permissions | Không có quyền Android runtime hoặc truy cập mạng. Quyền AndroidX nội bộ được bảo vệ bằng chữ ký. |
| Target audience / Content rating | Tài sản là câu chữ và âm thanh tổng hợp dùng minh họa học tập. Chủ tài khoản chọn nhóm tuổi thực tế và gửi bảng hỏi IARC. Chưa có xếp hạng do Play cấp. |
| Khai báo khác | Đối chiếu các mục Console hiển thị cho package và tài khoản này. Không có tính năng tài chính, y tế, tin tức hay quảng cáo trong APK kiểm tra. Chủ tài khoản xử lý khai báo nhà phát triển, phân phối và điều khoản ký qua Console. |

[Play App content declarations](https://support.google.com/googleplay/android-developer/answer/9859455) · [Play Data safety guide](https://support.google.com/googleplay/android-developer/answer/10787469)

## Điều kiện tài khoản

Internal Testing phù hợp cho nhóm nhỏ. Closed Testing có danh sách tester riêng. Với tài khoản cá nhân tạo sau 13/11/2023, Google yêu cầu ít nhất 12 tester đã tham gia Closed Testing liên tục đủ 14 ngày trước khi nộp đơn xin quyền Production. Chủ tài khoản cần xác minh loại tài khoản, thời điểm tạo, tình trạng xác minh và yêu cầu cụ thể trong Dashboard. Tài khoản cá nhân mới còn có bước xác minh thiết bị Android thật bằng ứng dụng Play Console. [Thiết lập các track kiểm thử](https://support.google.com/googleplay/android-developer/answer/9845334) · [Điều kiện cho tài khoản cá nhân mới](https://support.google.com/googleplay/android-developer/answer/14151465) · [Xác minh thiết bị](https://support.google.com/googleplay/android-developer/answer/14316361)
