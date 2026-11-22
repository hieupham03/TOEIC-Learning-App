# Stage05 FAST-01/02 — Báo cáo kỹ thuật APK dùng thử V0.1

Ngày 22/11/2026 (Asia/Saigon). Nhánh `development/fasttrack-48h-preview`. Mốc mục tiêu P0 là 24/11/2026. Phạm vi theo [chỉ đạo PO V0.2](STAGE05_FASTTRACK_PO_RIGHTS_AND_EXECUTION_PRIORITY_V0.2.md), [workplan](STAGE05_FASTTRACK_48H_PREVIEW_14D_PLAY_PLAN_V0.1.md) và [issue #7](https://github.com/hieupham03/TOEIC-Learning-App/issues/7).

## Thay đổi

| Tệp | Triển khai |
|---|---|
| `android-app/app/src/main/java/vn/toeiclearning/alpha/ui/AlphaApp.kt` | Task Hub dẫn vào Listening/Reading DEMO. Lựa chọn Reading Part 5–7 giữ trong bộ nhớ khi chuyển màn hình. Chuyển câu trước/sau, quay lại đoạn văn, giải thích mẫu khi người dùng yêu cầu, xem số câu đã chọn và xóa lựa chọn có xác nhận. |
| `android-app/app/src/main/java/vn/toeiclearning/alpha/ui/ListeningDemoScreen.kt` | Mỗi Part 1–4 có một mẫu với các nút tạm dừng, dừng và phát lại. Có thể chuyển Part và xem lại lựa chọn. Lựa chọn Listening không được chấm. Vẫn dùng MediaPlayer, vòng đời và tệp WAV tự tạo của CX-04. |
| `android-app/app/src/test/java/vn/toeiclearning/alpha/domain/AlphaRulesTest.kt` | Thêm hồi quy về lựa chọn và giải thích độc lập giữa các Part. |
| `.gitignore` | Loại APK và AAB khỏi staging thông thường. Công cụ, tài sản nguồn và bằng chứng cục bộ nằm trong thư mục đã ignore. |

Liên kết kỹ thuật hiện có gồm FR-002 / AT-02 (điều hướng), FR-003 / AT-03 (audio theo nhóm), FR-004 / AT-04 (Reading), FR-009 / AT-09 (lựa chọn), FR-011 / AT-11 (khóa Full Mock) và Design V0.3/UI-G01..16. Sáu tệp đã ký khớp SHA-256 trong [manifest kiểm soát](STAGE05_ALPHA_CX00_CX03_SOURCE_AND_CONTROL_MANIFEST_V0.1.md). FR/AT là tham chiếu phạm vi kỹ thuật. Stage05 vẫn CONDITIONAL cho Development, G05-CP01..08 và các CP trước còn ACTIVE, POL01..16 OPEN và ngân sách DEFERRED.

## APK và cách cài

- APK cục bộ `android-app/.tooling/fasttrack/preview/TOEIC-offline-preview-debug.apk`. Kích thước 11.103.052 byte. Bản build nguồn `1434e9bbee1d9bc138cfc5c994f1fbbd56a8b218`.
- SHA-256 `850d4d8afcca3fb236c994f9919318ba124827627d0a9531b0fa4bbff883883f`. Có tệp `.sha256` đặt cạnh APK. `apksigner verify --verbose` exit 0, chữ ký APK v2. Package `vn.toeiclearning.alpha`, Android 8.0+ (min API 26), target 35, `0.1.0-alpha` (versionCode 1).
- Trên Windows, từ thư mục gốc repo chạy `Get-FileHash -Algorithm SHA256 android-app/.tooling/fasttrack/preview/TOEIC-offline-preview-debug.apk` và so với hash trên. Trên emulator riêng hoặc thiết bị đã được đồng ý, kiểm tra `adb devices -l`, rồi dùng `adb -s SERIAL install -r android-app/.tooling/fasttrack/preview/TOEIC-offline-preview-debug.apk`. Nếu thiết bị đã có bản cùng package nhưng khác chữ ký, dừng ở lỗi cài đặt để tránh xóa dữ liệu của bản hiện hữu.
- Mở **TOEIC Learning · Alpha**. Dùng **Mở Listening DEMO** hoặc **Mở Reading DEMO**. Xem lựa chọn trong **Tiến độ**, chọn **Xóa lựa chọn tạm** và xác nhận nếu muốn bắt đầu lại. Lựa chọn tồn tại khi điều hướng trong phiên. Đóng hẳn ứng dụng sẽ mất lựa chọn. Bản này không có tài khoản, backend, lưu bền vững hay điểm TOEIC.
- Gói APK chứa đúng bốn WAV tự tạo. Khai báo quyền của APK chỉ có quyền signature nội bộ do AndroidX tạo cho receiver. Không có Internet, quyền lưu trữ hoặc thu âm.

## Build, test và bằng chứng

Chạy từ `android-app/` với Temurin 17.0.21.1, Gradle Wrapper 8.13, Android SDK 36 và Kotlin CLI 2.2.21. Lệnh Kotlin dùng `-KotlinHome` và `-JavaHome` tới bản cài cục bộ.

| Lệnh hoặc kiểm chứng | Kết quả | Exit |
|---|---|---:|
| `python -B -X utf8 scripts/check_alpha_scope.py` | PASS, 10 kiểm tra. | 0 |
| `python -B -X utf8 scripts/check_beta_reading_ui_scope.py` | PASS, 11 kiểm tra. | 0 |
| `python -B -X utf8 scripts/check_cx04_listening_scope.py` | PASS, 9 kiểm tra, gồm hash WAV và đối chiếu với bộ tạo tệp. | 0 |
| `python -B -X utf8 scripts/crawl_one_zenlish_part3_group.py --self-test` | PASS offline. Dùng dữ liệu đã có cho lần kiểm tra này. | 0 |
| `python -B -X utf8 -m unittest discover -s tests/ingestion -v` | PASS 36/36. | 0 |
| `scripts/run_pure_kotlin_core_checks.ps1` | PASS, 25 assertions. | 0 |
| `gradlew.bat --offline --no-daemon --console=plain :app:assembleDebug :app:testDebugUnitTest --rerun` | PASS sau khi đồng nhất hai biến đường dẫn SDK. Lần đầu FAIL vì `ANDROID_HOME` và `ANDROID_SDK_ROOT` trỏ hai SDK khác nhau (exit 1). Lần chạy ổn định lại trên commit P0 thành công và giữ nguyên SHA-256 của APK bàn giao. | 0 |
| JUnit XML `TEST-vn.toeiclearning.alpha.domain.AlphaRulesTest.xml` và `TEST-vn.toeiclearning.alpha.domain.ListeningDemoTest.xml` | PASS 12/12 (5 + 7), 0 failures/errors/skips. | 0 |
| `python -B -X utf8 scripts/normalize_zenlish_batch.py` | PASS offline, 4 nhóm. | 0 |
| `python -B -X utf8 scripts/listening_manifest.py .tooling/listening-overnight/normalized_manifest.json` | HOLD, 4 MAPPED, 0 lỗi cấu trúc, 24 hold, `eligible_for_app=false`. | 2 |

## Đối chiếu Zenlish cục bộ

Kết quả từ manifest đã thu thập và probe Android API 34 `MediaExtractor` + `c2.android.mp3.decoder`. Probe yêu cầu đủ PCM qua EOS với biên độ khác 0 và thời lượng trong 150 ms so với manifest. Bốn MP3 đều 44.1 kHz stereo. Android giải mã ảnh Part 1 qua BitmapFactory. Dữ liệu thử giữ ở `android-app/.tooling/listening-overnight/`. Probe chỉ chép tạm vào emulator riêng và dọn các tệp sau khi chạy.

| Part / nhóm | Thứ tự câu và cấu trúc nguồn | Byte MP3 / thời lượng PCM | SHA-256 MP3 |
|---|---|---|---|
| 1 / `zenlish:40911` | Q1, PARTIAL, chỉ có nhãn lựa chọn, ảnh giải mã 581 × 358. | 440.034 / 23,197 s | `223b4cab3e6382f21f7b7056bb48a781f0db14a0247efb13417980f5373ce9a3` |
| 2 / `zenlish:40943` | Q7, PARTIAL, chỉ có nhãn lựa chọn. | 407.508 / 21,159 s | `ac324f03ba0d0573df50b9dda29f5bf177e750dc28a31ebb200693e81908038f` |
| 3 / `zenlish:41021` | Q32, 33, 34, FETCHED, có câu hỏi và lựa chọn. | 1.265.710 / 74,919 s | `cf77cbe460cfe87cf4a396fcb9b90194773c7bfeeb97f98e333e494fb2dcae4b` |
| 4 / `zenlish:41104` | Q71, 72, 73, FETCHED, có câu hỏi và lựa chọn. | 1.305.325 / 77,401 s | `f226785958cf1a5555725500bd890331892d681dcd497d9556042b5c36a5c5e3` |

Ảnh Q1 SHA-256 `ae739010604b7de17f64065434d3bcaec3861596731ab53ee8f3797a166cbcac` (141.122 byte). Bốn nhóm cùng phiên bản nguồn `sha256:2db58276d138f6d1374698c150fc518765a3d9cd4f84c77765a33e9f44556c14`. **PASS** xác minh mã nhóm/câu, thứ tự, liên kết trong manifest, checksum và giải mã. **NOT RUN** đối chiếu bằng người nghe giữa lời nói và nội dung câu hỏi/ảnh. **BLOCKED** dùng mẫu nguồn như học liệu đã QA vì cả 8 câu có khóa đáp án chưa xác minh và Part 1–2 thiếu dữ liệu. Bản APK để cài sử dụng nội dung synthetic. Quyết định PO về quyền học liệu là đầu vào của FAST TRACK.

## Kiểm thử emulator và quyết định

AVD `TOEIC_EUI_API34`, API 34 x86_64. Tắt Wi-Fi và dữ liệu di động, cả hai thiết lập đọc lại là `0`. Bản cài từ APK Debug đúng checksum. Kịch bản điều khiển qua ADB và UI Automator.

| Trường hợp | Kết quả |
|---|---|
| 360dp, font 1,0×. Listening Part 1–4 và điều hướng phiên. | PASS. Tạm dừng, tiếp tục, dừng khi đi xuống nền, phát lại tới hết, chuyển qua Part 2–4, giữ lựa chọn khi xem lại và Back. Lần chạy nối sang Reading có exit 1 do lỗi unpack trong script điều khiển. Bước Listening đã ghi PASS trước lỗi của script. |
| 360dp, font 1,0×. Reading, xóa và khởi động lại. | PASS, exit 0. Part 5 chuyển câu và mở giải thích mẫu, Part 6 Back về đoạn, Part 7 giữ đoạn đang đọc và câu đang xem. Nút Hủy giữ lựa chọn, xác nhận xóa cả Reading và Listening. Cưỡng bức dừng tiến trình rồi mở lại cho phiên mới. Full Mock vẫn khóa. |
| 360dp, font 1,5× và 800dp, font 1,0×. | PASS, mỗi trường hợp exit 0. Quan sát Reading Part 7 trước/sau Back và Listening chuyển Part, phát xong, truy cập lại lựa chọn. Script lần đầu ở 1,5× chỉ cuộn một lần nên dừng trước khi tới phần thân bài. Đã sửa bước cuộn và chạy lại. |
| WAV sai SHA-256 của Part 1. | PASS, exit 0. APK fault-injection chỉ thay 1 byte WAV và vẫn giữ độ dài. App báo tệp không khớp qua cả hai lượt thử, Back được. Đã cài lại APK bàn giao sau đó. |
| Tín hiệu phát ra từ loa ảo. | PASS sau tái kiểm tra, exit 0. Thu PCM qua gRPC có token trên loopback và xác định đúng 330, 440, 550, 660 Hz cho Part 1–4. Mỗi clip có 3,4–3,6 s khớp ngưỡng tần số, dải thời gian 5,6–5,8 s, không clip PCM. Lần đầu Part 1 có tín hiệu ngoài ngưỡng, bộ phân tích exit 1. Thu riêng lại Part 1 và idle, giữ kết quả đã đạt của Part 2–4. |
| Hai người dùng/hai điện thoại thật, nghe qua loa/vật lý, TalkBack, QA/ECP chính thức. | NOT RUN. Workspace chỉ có emulator. Chưa có hai thiết bị và lượt quan sát đồng thuận được ghi nhận. |

**GO cho APK DEMO kỹ thuật trên cấu hình emulator đã kiểm tra và cho bước chuẩn bị gói Play. NO-GO để tuyên bố hai người đã dùng thử hoặc đủ bằng chứng nghiệm thu hai thiết bị.** Listening của APK vẫn là tone thử nghiệm với ảnh giữ chỗ, không chấm. Lựa chọn là trạng thái RAM của phiên và có thể mất khi Activity được tái tạo hoặc khi tiến trình kết thúc. B1, Full Mock, kiểm chứng thiết bị thật và QA học liệu vẫn ở trạng thái chưa đạt điều kiện.

Bản APK, checksum và bản sao JUnit XML nằm trong `android-app/.tooling/fasttrack/preview/`. Log, ảnh, bản thu PCM, mã probe và log emulator nằm trong `android-app/.tooling/fasttrack/`. Các thư mục đó nằm ngoài Git.
