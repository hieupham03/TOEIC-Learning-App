# Stage05 FAST-04 — Đánh giá sẵn sàng nộp Google Play V0.1

Ngày 22/11/2026 (Asia/Saigon). Nhánh `development/fasttrack-48h-preview`. Mục tiêu 06/12/2026 là gói phục vụ Internal/Closed Testing. Hồ sơ kèm [APK P0](STAGE05_FASTTRACK_48H_ENGINEERING_REPORT_V0.1.md), [gói Play](STAGE05_FASTTRACK_PLAY_PACKAGE_V0.1.md) và [issue #8](https://github.com/hieupham03/TOEIC-Learning-App/issues/8).

## Thay đổi và phạm vi

| Tệp | Công việc |
|---|---|
| `android-app/app/build.gradle.kts` | Target API 36 và phiên bản `2 / 0.2.0-preview`. Package `vn.toeiclearning.alpha`, min API 26. |
| `android-app/app/src/main/java/vn/toeiclearning/alpha/MainActivity.kt` và `ui/AlphaApp.kt` | Edge-to-edge, vùng nội dung an toàn, dùng điều hướng Back của Compose, thông tin quyền riêng tư và đường dẫn tới Tiến độ. |
| `android-app/app/src/main/AndroidManifest.xml`, `res/xml/data_extraction_rules.xml`, `res/drawable/ic_launcher_preview.xml`, `res/values/strings.xml` | Khai báo callback Back, quy tắc không sao lưu/chuyển vùng dữ liệu, tên và biểu tượng DEMO. |

Các kiểm tra kỹ thuật liên quan FR-003/AT-03, FR-004/AT-04, FR-009/AT-09 và Design V0.3. FR-018/AT-18 và FR-019/AT-19 vẫn còn các điều kiện tài khoản, lưu chính thức, gián đoạn và dữ liệu người học của MVP. Gói DEMO chỉ có lựa chọn trong bộ nhớ của phiên. Stage05 vẫn CONDITIONAL cho Development. G05-CP01..08 và các CP trước ACTIVE, POL01..16 OPEN, B1 và Full Mock khóa, QA chính thức NOT RUN và ngân sách DEFERRED.

## Kiểm chứng build và gói

| Lệnh hoặc kiểm chứng | Kết quả |
|---|---|
| `gradlew.bat --offline --no-daemon --console=plain :app:assembleDebug :app:testDebugUnitTest --rerun :app:testReleaseUnitTest --rerun :app:lintRelease :app:bundleRelease` | PASS, exit 0 sau cập nhật manifest. Lần thử offline đầu thiếu `com.android.tools.lint:lint-gradle:31.13.2` (exit 1). Lần chạy online tải dependency chính thức và tạo AAB thành công (exit 0). |
| `gradlew.bat --offline --no-daemon --console=plain :app:extractReleaseVersionControlInfo --rerun :app:bundleRelease` | PASS, exit 0 trên commit nguồn `4cb7919c124b93f483a151a8c1d75c20edb702c6`. |
| JUnit XML `app/build/test-results/testDebugUnitTest/` và `testReleaseUnitTest/` | PASS, mỗi biến thể 12 test (5 Alpha + 7 Listening), 0 failures/errors/skips. |
| Lint release | PASS, 0 errors, 3 warnings về thuộc tính Back từ API 33, phiên bản Compose BOM mới hơn và thuộc tính backup dành cho Android cũ. `allowBackup=false` vẫn áp dụng cho Android cũ. |
| `python -B -X utf8 scripts/check_alpha_scope.py`, `check_beta_reading_ui_scope.py`, `check_cx04_listening_scope.py` | PASS lần lượt 10/11/9 kiểm tra, exit 0. |
| `python -B -X utf8 -m unittest discover -s tests/ingestion -v` và self-test crawler offline | PASS 36/36, self-test PASS, exit 0. |
| `scripts/run_pure_kotlin_core_checks.ps1` với JDK 17 và Kotlin CLI 2.2.21 | PASS 25 assertions, exit 0. |
| `bundletool 1.18.3 validate`, `dump manifest`, `jarsigner -verify`, `bundletool build-apks --mode=universal`, `zipalign -c -P 16 4` | PASS, exit 0. Kiểm chứng gói gốc, gói ký với Android debug certificate cho test local, manifest và APK universal trích từ gói thử. |

Các tệp dưới đây và checksum đi kèm nằm trong `android-app/.tooling/fasttrack/play/`.

| Tệp | Dung lượng / SHA-256 |
|---|---|
| `TOEIC-Learning-Demo-0.2.0-unsigned.aab` | 6.609.085 byte, `10baddfbf06551197753c0c0e1cb4aa012c6068f9e08882490b301e3d80851fa` |
| `TOEIC-Learning-Demo-0.2.0-local-test.aab` | 6.621.558 byte, `7ea859068a7d8ec6555e821fd80dd2d405b4239f5f0c7e3b38a4a63a3162dd2c` |
| `TOEIC-Learning-Demo-0.2.0-local-test.apk` | 7.711.226 byte, `7a0d4a7a38f35a083180f076b588798c63859648fe47591fdffc2b99946ff969` |

## Manifest, dữ liệu và bảo mật

- Package, min/target SDK và version đối chiếu theo manifest trong AAB. Quyền duy nhất của ứng dụng là quyền receiver nội bộ do AndroidX sinh, mức `signature`. Activity launcher được export. Provider AndroidX Startup nội bộ, receiver ProfileInstaller được bảo vệ bởi `android.permission.DUMP`. Bản release không debuggable.
- Audit code, manifest đã hợp nhất và `:app:dependencies --configuration releaseRuntimeClasspath` không thấy kết nối mạng, tài khoản, SDK quảng cáo/analytics hay dữ liệu người học ghi bền vững. Có đọc WAV từ assets và giữ lựa chọn DEMO trong RAM. Cấu hình Android 12+ loại vùng dữ liệu app khỏi cloud backup và device transfer. Kiểm chứng khôi phục qua OEM và thiết bị thật chưa chạy.
- AAB có đúng bốn WAV tự tạo khớp checksum CX-04. Học liệu Zenlish và đáp án nguồn giữ ở kho local riêng. APK có nhãn DEMO, Listening không chấm, Full Mock bị khóa. Bốn ABI đóng gói `libandroidx.graphics.path.so` với mọi đoạn ELF `PT_LOAD` căn 16 KB. `BundleConfig` khai báo `PAGE_ALIGNMENT_16K`. [Hướng dẫn Android về 16 KB](https://developer.android.com/guide/practices/page-sizes)

## Runtime, lỗi và bằng chứng

Android Emulator 37.2.13.0, AVD `TOEIC_FASTTRACK_API36`, Android 16 Google APIs x86_64 r7. Lần cold boot mất khoảng 211 giây, vượt thời gian chờ 150 giây ban đầu. Một thông báo ANR thuộc `com.android.systemui` che app đã được xác định qua window dump và ảnh cục bộ. Sau khi chọn **Wait**, tiếp tục kiểm tra trên cùng AVD. Trang, ảnh và log thô lưu cục bộ.

| Trường hợp trên Android 16 | Kết quả |
|---|---|
| Cài Debug v1 target 35, mở app, nâng lên Debug v2 target 36 và mở lại | PASS, exit 0. `dumpsys package` xác nhận chuyển versionCode 1 → 2. |
| Cài APK universal từ AAB cuối | PASS. `apksigner verify` và `adb install -r` exit 0. APK release được ký bằng Android debug certificate để kiểm tra cục bộ. |
| 360dp / font 1,0× / điều hướng cử chỉ | PASS. Nút Reading, Listening và Tiến độ đo đạt ít nhất 48 × 48dp. Nội dung nằm dưới thanh trạng thái, thanh dưới nằm trên vùng điều hướng. Vuốt Back trong Part 7 về đoạn văn và vuốt tiếp về picker. |
| Wi-Fi và dữ liệu di động tắt | PASS. Cả hai giá trị hệ thống là `0`. Listening phát đến hết và dừng khi đưa app xuống nền. Mở được quyền riêng tư và Tiến độ. |
| 800dp / font 1,5× theo kích thước ngang | PASS. Part 6 đọc được câu hỏi và quay lại đoạn văn qua nút. Kịch bản trên APK cuối exit 0. |
| `adb logcat -b crash -d` và `adb logcat -b events -d -s am_anr` | PASS trong phiên emulator, cả hai lệnh exit 0, 0 dòng trùng package ứng dụng. ANR hệ thống lúc cold boot được ghi riêng như trên. |

Ba ảnh thực của APK cuối và hai ảnh listing nháp nằm tại `android-app/.tooling/fasttrack/play/store/`. Ảnh màn hình có định dạng RGB 1080 × 1920. Lint HTML, XML JUnit, manifest đã giải mã và log kỹ thuật nằm trong `android-app/app/build/` hoặc `android-app/.tooling/fasttrack/`. Cả sáu baseline/guardrail có checksum khớp manifest kiểm soát. Không có nhị phân, khóa ký, ảnh, dữ liệu học liệu nguồn hoặc log thô trong commit FAST TRACK.

## Quyết định

- **GO cho bàn giao AAB kỹ thuật và APK thử cục bộ**. Hai biến thể build/test đạt và APK từ AAB cuối chạy được trên AVD đã nêu.
- **BLOCKED / NO-GO nộp Play** cho tới khi chủ tài khoản xác nhận package/track và cung cấp quy trình ký bằng upload key của họ, email hỗ trợ và URL privacy policy công khai. Các khai báo App content, nhãn Data safety, độ tuổi, IARC và điều kiện tài khoản phải được kiểm tra trên Console. [Play App content](https://support.google.com/googleplay/android-developer/answer/9859455) · [Play User Data](https://support.google.com/googleplay/android-developer/answer/10144311)
- **BLOCKED Production**. Chưa có xác minh tài khoản, kiểm thử Closed theo tài khoản, chấp thuận Play hay QA chính thức. Tài khoản cá nhân tạo sau 13/11/2023 phải có ít nhất 12 tester opt-in Closed Testing liên tục 14 ngày trước khi xin quyền Production. Mốc 06/12 được dùng cho chuẩn bị gói thử nghiệm. [Play testing requirements](https://support.google.com/googleplay/android-developer/answer/14151465)
- **NOT RUN** Console upload/review, Play Pre-launch Report, thiết bị thật, TalkBack đầy đủ, QA/ECP chính thức và runtime trang nhớ 16 KB. AVD Android 16 này báo `getconf PAGE_SIZE = 4096`. P0 đã kiểm tra API 34, vòng chạy APK release P1 chỉ dùng API 36.
