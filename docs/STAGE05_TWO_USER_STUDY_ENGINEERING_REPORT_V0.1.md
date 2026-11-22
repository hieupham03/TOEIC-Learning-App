# Báo cáo kỹ thuật Two-User Study V0.1

22/11/2026 · `development/two-user-study-mvp` · STUDY-01..04 · Issue #9

## Bản học tập riêng

Ứng dụng Study `vn.toeiclearning.alpha.study` phiên bản `0.3.0-study` (4), Android API 26 trở lên. Bản này có thư viện cục bộ cho cả bảy Part và chạy offline. Mỗi lần cài có một hồ sơ riêng. Android backup bị tắt cho bản Study.

- Chọn hoặc đổi đáp án, về câu trước, chuyển câu, nhảy đến câu và kết thúc theo xác nhận. Listening có điều khiển phát, tạm dừng và phát lại. Reading có màn đoạn văn riêng, ảnh có thể phóng to và khôi phục vị trí đọc khi quay lại.
- SQLite lưu câu hiện tại, lựa chọn, vị trí đọc, lịch sử, câu đánh dấu và câu sai có khóa đã kiểm chứng. Ghi phiên theo giao dịch có kiểm tra revision. Phiên đang làm và phiên đã kết thúc giữ snapshot học liệu và khóa tại thời điểm bắt đầu. Gói thay thế sử dụng APK Study cùng package và chữ ký. Màn tiến độ hiển thị 100 phiên gần nhất và dùng toàn bộ phiên luyện để tổng hợp số câu.
- Học theo Part, mở lịch sử và luyện lại từ mục ôn tập. Thống kê đúng/sai chỉ tính câu đã trả lời có khóa đã kiểm chứng. Gợi ý ưu tiên Part có tỷ lệ sai cao nhất trên số câu đã chấm, sau đó ưu tiên Part đã luyện ít nhất. Mục tiêu mặc định là 10 câu/ngày. Người học có thể đặt từ 1 đến 200 và xác nhận trước khi xóa dữ liệu.
- Luồng riêng cho thiết bị cục bộ. Signed baseline, ngân sách DEFERRED, các CP đang ACTIVE và trạng thái QA chính thức giữ theo hồ sơ phê duyệt dự án.

## Học liệu thật trong gói đầu

| Part | Câu khả dụng | Khóa đã kiểm chứng | Tệp đi kèm |
| --- | ---: | ---: | --- |
| 1 | 1 | 0 | MP3, ảnh |
| 2 | 1 | 0 | MP3 |
| 3 | 3 | 0 | MP3 theo nhóm |
| 4 | 3 | 0 | MP3 theo nhóm |
| 5 | 3 | 0 | Văn bản |
| 6 | 4 | 0 | Văn bản, ảnh đoạn văn |
| 7 | 2 | 0 | Văn bản, ảnh đoạn văn |
| **Tổng** | **17** | **0** | **4 MP3, 3 ảnh** |

Gói gồm 9 nhóm từ snapshot và dữ liệu Zenlish đã lưu. Batch đọc robots và tải hai ảnh Reading trong **3 HTTP request, 189.438 byte**. Chạy lại `python -B -X utf8 scripts/prepare_study_pack.py` từ `android-app` dùng cache cục bộ và tái tạo `pack.json` cùng SHA-256 `c80d8726f502e24d0e3eb0dfe47dbb4dd1342d9f8ed8cf6f66b30dae98bd3e3d`. Phiên bản nguồn là `2db58276d138f6d1374698c150fc518765a3d9cd4f84c77765a33e9f44556c14`. Kiểm tra đủ 17 câu và bảy tài sản có dung lượng, SHA-256 trùng manifest. APK Debug thông thường không chứa gói Study.

Toàn bộ 17 câu hiện ở trạng thái **CHƯA QA**. Có thể trả lời, lưu và ôn lại theo dấu đánh dấu. Kết quả ghi số câu đã làm và trạng thái chưa chấm. Cả gói hiện có 0 lời giải đã kiểm chứng. Part 1–4 dùng nhãn lựa chọn theo cấu trúc câu nghe của nguồn. Tài sản gốc và báo cáo kỹ thuật chi tiết từng tệp nằm trong thư mục `.tooling` cục bộ.

## Full Mock A/B

Hai bộ synthetic 200 câu dùng riêng trong test engine. Hai form thật phải có tổng 400 câu độc lập, đủ 6/25/39/30/30/16/54 câu theo Part, đủ khóa và media đã kiểm chứng, có bằng chứng review trong manifest, và qua kiểm tra trùng gói và trùng form. **Đề A thiếu 200/200, đề B thiếu 200/200**. UI đã hiển thị khóa của cả hai form. Kiểm tra trùng tự động dựa vào ID, nội dung chuẩn hóa và dấu vân tay media; rà soát trùng tương đương về ngữ nghĩa còn phụ thuộc kiểm duyệt học liệu.

Engine có làm bài, đồng hồ cục bộ 45 phút Listening và 75 phút Reading, chuyển câu, lưu câu trả lời, nộp bài và kết quả số câu đúng theo Part. Listening đánh dấu lần phát trước khi mở audio. Phiên có gián đoạn phát hoặc thay đổi mốc khởi động giữ câu đã lưu và hiển thị trạng thái gián đoạn. Kiểm thử thời gian bằng mốc giả lập, gồm điểm chuyển pha và đổi đồng hồ thiết bị. Tính giờ dựa vào mốc đơn điệu Android. [SystemClock](https://developer.android.com/reference/android/os/SystemClock) · [BOOT_COUNT](https://developer.android.com/reference/android/provider/Settings.Global#BOOT_COUNT)

## Đối chiếu phạm vi kỹ thuật

| Gói | Hồ sơ đối chiếu | Kết quả triển khai |
| --- | --- | --- |
| STUDY-01 | FR-001..009, FR-014/018/019 · AT-01..09/14/18/19 | Model Part 1–7, Study Compose, SQLite, bài đang làm, lịch sử, thống kê, ôn tập và xóa có xác nhận |
| STUDY-02 | FR-002..007/015/016 · AT-02..07/15/16 | Công cụ đóng gói cục bộ, kiểm tra manifest, khóa, media và snapshot phiên |
| STUDY-03 | FR-010..013/017/019 · AT-10..13/17/19 | Engine tính giờ và kiểm tra điều kiện hai form, hai bộ synthetic 200 câu cho test |
| STUDY-04 | UI-G01..16 · AT-03/04/05/19 | Soát bố cục Compose, trạng thái ảnh/media, nâng cấp nội bộ và gói cài cho hai máy |

Các liên kết FR/AT ghi mục đối chiếu engineering. Kết quả dưới đây dùng cho build nội bộ theo workplan. Trạng thái formal ECP/QA là **NOT RUN**.

- Màn hình, model, SQLite và engine trong `android-app/app/src/main/java/vn/toeiclearning/alpha/study/`. `MainActivity.kt` dẫn bản Study vào UI riêng và `ui/ListeningDemoScreen.kt` chia sẻ bộ điều khiển phát.
- Biến thể cục bộ ở `android-app/app/build.gradle.kts` và `android-app/app/src/study/AndroidManifest.xml`. Test Kotlin ở `android-app/app/src/test/java/vn/toeiclearning/alpha/study/`.
- Công cụ và test nhập liệu ở `android-app/scripts/prepare_study_pack.py` và `android-app/tests/ingestion/test_study_pack.py`.

[Workplan STUDY-01..04](STAGE05_TWO_USER_FULL_STUDY_PRIORITY_AND_WORKPLAN_V0.1.md) · [SRS](STAGE03_SRS_BASELINE_CANDIDATE_V0.6.md) · [Danh mục AT](STAGE03_ACCEPTANCE_CATALOGUE_CANDIDATE_V0.4.md) · [Design Baseline V0.3](STAGE04_UI_V03_DESIGN_BASELINE_CANDIDATE_V0.3.md) · [Issue #9](https://github.com/hieupham03/TOEIC-Learning-App/issues/9)

## Kết quả kiểm tra

| Kiểm tra | Trạng thái | Bằng chứng |
| --- | --- | --- |
| Gradle Debug, LocalPreview, Study | PASS | `gradlew.bat --offline --no-daemon --console=plain :app:assembleStudy :app:testStudyUnitTest --rerun :app:assembleDebug :app:testDebugUnitTest --rerun :app:assembleLocalPreview :app:testLocalPreviewUnitTest --rerun`, exit `0`. JUnit XML 18/18 mỗi biến thể; 0 fail, 0 error, 0 skipped. |
| Ingestion | PASS | `python -B -X utf8 -m unittest discover -s tests/ingestion -v`, exit `0`, 44/44. Kiểm tra gồm asset hỏng/thiếu, ràng buộc nhóm/khóa, lặp ID và tái tạo pack. |
| Guards | PASS | `check_alpha_scope.py`, `check_beta_reading_ui_scope.py`, `check_cx04_listening_scope.py`, lần lượt 10/10, 11/11, 9/9, và crawler Part 3 `--self-test`, từng lệnh exit `0`. Sáu tài liệu baseline trùng SHA-256 đã ghi. |
| Kotlin CLI | PASS | `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/run_pure_kotlin_core_checks.ps1 -KotlinHome <compiler> -JavaHome <JDK17>`, exit `0`, 25 assertions. Gradle JUnit gồm 6 test mới trực tiếp về Study và Full Mock. |
| API 34, Part 3 offline | PASS | Phát/tạm dừng MP3, chọn/đánh dấu, buộc dừng tiến trình, mở lại câu 33 giữ lựa chọn, kết thúc chưa chấm, mở lịch sử và luyện lại dấu đánh dấu. Ca đầu phát hiện màn kết quả giữ vị trí cuộn cũ. Đã sửa và chạy lại. |
| API 34, lưu và nâng cấp | PASS | Cold restart cùng AVD giữ tiến độ, lựa chọn và câu hiện tại. `adb install -r` bản 4 đè bản 3 giữ cùng dữ liệu SQLite schema v1. Cài đè gói đủ media sau gói thử thiếu media giữ lại lựa chọn. Các ca xác minh lại exit `0`. |
| API 34, lỗi thiếu audio | PASS | Gói thử bỏ MP3 P3 vô hiệu hóa bắt đầu P3 mới, giữ phiên và câu trả lời đang làm, báo thiếu tệp khi phát trong phiên cũ; khôi phục APK đủ tệp và mở lại vẫn giữ đáp án. Hai ca kiểm chứng lại exit `0`. |
| API 34, cài đặt và Full Mock | PASS | Lưu mục tiêu 15, hủy xóa giữ bài, xác nhận xóa khôi phục mặc định và dọn lịch sử, màn khóa hiển thị thiếu 200 cho mỗi form. Exit `0`. |
| API 34, Reading 360dp, font 1.0 | PASS | Part 6 có ảnh và phóng to, chuyển đến câu 132, Back về đoạn văn; mở được ảnh Part 7. Exit `0`. |
| API 36, cài mới và Reading | PASS | Lần cài mới khởi đầu với hồ sơ trống. Kiểm tra khi bật chế độ máy bay ở 360dp và 800dp với font 1.5. Part 6 mở ảnh, phóng to, chuyển câu và quay lại đoạn văn; mở được ảnh Part 7 ở 800dp. Cả ba lượt exit `0`. |
| API 36, Part 1/4/5 offline | PASS | Part 1 mở ảnh và phát; Part 4 duy trì cùng audio khi chuyển câu trong nhóm; Part 5 lưu lựa chọn và hiện kết quả chưa chấm. Exit `0`. |
| API 36, giải mã và vòng đời audio | PASS | Bốn MP3 khớp byte trong APK, khớp SHA-256 và giải mã thành PCM có tín hiệu. Với Part 2, UI chuyển sang đã phát xong, phát lại, dừng khi vào nền và dừng theo thao tác. Hai lượt exit `0`. Nghe qua loa trên hai điện thoại **NOT RUN**. |
| API 36, SQLite hỏng | PASS | Đổi header SQLite trong AVD. UI báo lỗi đọc dữ liệu, SHA-256 tệp hỏng trước và sau khi mở app giống nhau. Phục hồi tệp ban đầu và mở lại Study thành công. Lượt xác minh truyền dữ liệu nhị phân qua ADB exit `0`. |
| Full Mock A/B | PASS engine · BLOCKED nội dung thật | Test engine gồm hai form 200 câu, chuyển pha, gián đoạn và khóa pack thiếu/trùng. Lượt thi thật 120 phút và phát audio của đề thật **NOT RUN**. |
| Hai điện thoại thật | NOT RUN | 0/2 thiết bị thử Study. ADB chỉ có emulator. Kết quả hai máy của preview 0.2.1 thuộc bản trước. |

API 34 gặp hộp thoại System UI trong lúc cold boot. Dùng cùng AVD sau khi System UI ổn định để kiểm tra lại dữ liệu. Ca font 1.5 ở API 34 bị timeout lúc khởi chạy activity, exit `1`. Cùng cấu hình 360dp/font 1.5 đã chạy trên API 36. Ca đầu kiểm tra tệp SQLite hỏng exit `1` khi đối chiếu byte. Kết quả PASS sử dụng script kiểm tra byte tại cả thời điểm chèn lỗi và sau khi mở app. Script offline đổi sang chế độ máy bay sau khi lệnh tắt dịch vụ dữ liệu trả mã 20 trên API 36.

## Gói cài riêng và quyết định

| Tệp lưu trong `android-app/.tooling/two-user-study/` | SHA-256 |
| --- | --- |
| `TOEIC-Study-0.3.0-debug.apk` | `a19bc94a53994d26d67d96a43566af51325b6fe2cf41f620ac83d314aa8151d1` |
| `TOEIC-Study-hai-may-0.3.0.zip` | `1ce49f83c6f18a2303bcade2a3a463132539fa018c9c742961ec9fe8d743b8f7` |

`apksigner verify` exit `0`. ZIP chứa APK, checksum, hướng dẫn cài/cập nhật, checklist cho từng điện thoại và phiếu ghi lỗi. Nhật ký, JUnit XML, APK, ZIP và học liệu gốc nằm cục bộ.

**GO** bàn giao cài thử riêng và luyện offline 17 câu chưa chấm. **NO-GO** xác nhận đạt mục tiêu dùng hằng ngày trên hai điện thoại và mở Full Mock thật. Cần chạy checklist trên hai máy có đồng ý, mở rộng số câu thực theo Part, xác minh khóa/lời giải và cung cấp hai form đã kiểm chứng để xác nhận các phần còn thiếu.
