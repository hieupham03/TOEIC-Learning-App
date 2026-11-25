# FAST-STUDY-08 · Study 0.3.9

Ngày 25/11/2026. Nhánh `development/two-user-study-mvp`. PO xác nhận đã hoàn tất lượt kiểm tra điện thoại trước và chuyển các vòng phát triển sang kiểm thử tự động.

## Kết quả trong APK

| Part | Tổng câu | Câu mới có khóa | Chấm được |
| --- | ---: | ---: | ---: |
| 1 | 13 | 8 | 8 |
| 2 | 45 | 20 | 20 |
| 3 | 63 | 24 | 24 |
| 4 | 57 | 24 | 27 |
| 5 | 68 | 0 | 39 |
| 6 | 32 | 0 | 16 |
| 7 | 110 | 0 | 56 |
| **Tổng** | **388** | **76** | **190** |

- Thêm 76 câu mô phỏng Listening của TOEIC Question Ocean từ bản ghim `a940bb8b479ef4d06af468015d757041c3d2e457`. Tám câu Part 1 có ảnh tạo riêng được tác giả ghi nguồn, Part 2 có câu nói và ba phản hồi, Part 3–4 có tám nhóm ba câu mỗi Part. Bỏ hai câu Part 2 có nhiễu dễ hiểu theo hai cách và một nhóm Part 3 có lời đáp thiếu chính xác so với kịch bản. [Nguồn ghim và MIT](https://github.com/kdeppaei/toeic-question-ocean/tree/a940bb8b479ef4d06af468015d757041c3d2e457) · [Nguồn ảnh Part 1](https://github.com/kdeppaei/toeic-question-ocean/blob/a940bb8b479ef4d06af468015d757041c3d2e457/assets/part1/ATTRIBUTION.md)
- Tạo 44 MP3 từ kịch bản của tác giả bằng hai giọng Windows cục bộ, tổng 18 phút 29 giây. App ghi **Giọng đọc tổng hợp**. Part 1–2 nghe các lựa chọn, cân bằng vị trí khóa trong chính bản thu và giữ đúng thứ tự chữ cái khi làm. Part 3–4 đọc đoạn nghe cùng ba câu hỏi, app xáo phương án văn bản theo phiên. 76 khóa mới dành cho luyện tập sau đối chiếu kỹ thuật. Chúng chưa qua kiểm duyệt học thuật độc lập.
- Luyện có chấm điểm là trang mặc định, chia bài tối đa 15 câu tại ranh giới nhóm. 198 câu Zenlish nằm trong mục **Luyện chưa chấm** riêng. APK giữ nguyên 312 câu và media của bản 0.3.8. Reading giữ chuyển đổi đoạn văn và câu hỏi. Màn kết quả đưa đáp án lên trước, người học có thể mở lại đoạn văn khi cần.

## Kiểm thử

| Kiểm tra | Kết quả |
| --- | --- |
| `prepare_ocean_listening.py` và kiểm kê hai APK | PASS, exit 0. Khớp khóa, ID, chỉ số lựa chọn, 44 MP3 và 8 JPEG. Lượt đầu bị chặn do trùng số câu giữa các Part trong cùng bản nguồn. Đã đánh số duy nhất toàn lô và kiểm tra lại |
| Gradle ngoại tuyến `:app:assembleStudy`, `:app:assembleDebug`, `:app:assembleLocalPreview` và JUnit tương ứng | PASS, exit 0. JUnit 28/28 mỗi biến thể |
| `python -B -X utf8 -m unittest discover -s tests/ingestion -v` | PASS, 70/70, exit 0 |
| Guards Alpha, Beta Reading, CX-04 và Kotlin smoke | PASS, 10/11/9 guard và 25 assertion, exit 0 |
| `apksigner` và `aapt2 dump badging` | PASS. Package và chứng chỉ ký trùng với 0.3.8. APK không khai báo quyền Internet |
| Bộ giải mã MP3 Android API 36 | PASS, 44/44 clip trong APK cho PCM biên độ khác 0, exit 0 |
| MuMu Android 15, ADB `127.0.0.1:16384` | Cài 0.3.8 PASS. ADB mất kết nối khi chuyển offline và vẫn offline sau lần khởi động, kết nối lại. Chuyển vòng tự động sang Android Emulator API 36 |
| Android Emulator API 36 · cài đè 0.3.8 → 0.3.9 | PASS, exit 0. Giữ lịch sử có điểm, dấu trang và phiên Part 7 đang làm, tiếp tục chấm đúng sau nâng cấp |
| Android Emulator API 36 · Listening Part 1–4 | PASS, exit 0 cho từng Part. Phát offline và kiểm tra cả đúng/sai cùng chữ cái đáp án. Part 2 khôi phục lựa chọn sau force-stop, Part 4 dừng khi app ra nền |
| Android Emulator API 36 · Reading Part 5–7 | PASS, exit 0 cho từng Part. Chấm đúng/sai và mở đáp án ở cả ba Part. Part 5 ôn câu sai và giữ lịch sử, Part 6–7 giữ câu đang làm và lựa chọn sau force-stop |
| Android Emulator API 36 · Zenlish và Full Mock | PASS, exit 0. Nộp thử Zenlish, lưu câu đã chọn ở mức chưa chấm. A/B vẫn báo thiếu 200/200 câu mỗi đề |
| Android Emulator API 36 · Reading ở 800 dp, cỡ chữ 1,5× | PASS, exit 0. Chấm bài và mở lại đoạn văn trong kết quả. Hai lỗi script ở lượt Zenlish và kiểm tra chữ lớn được sửa và chạy lại với cùng APK |

## Full Mock A/B và gói bàn giao

Full Mock A/B vẫn **LOCKED**, mỗi đề có 0/200 câu đạt đủ điều kiện. Ngay cả trước bước loại trùng và kiểm duyệt, Ocean còn tối đa 66 câu Part 3 và 54 câu Part 4 ngoài bộ đã đưa vào app. Hai form cần lần lượt 78 và 60 câu, còn thiếu ít nhất 12 và 6. 小R頻道 có một danh mục Listening 100 câu theo cấu trúc, kèm MP3 mẫu truy cập được. Quyền dùng lại câu và audio chưa xác định. Mẫu miễn phí của ETS chỉ dùng đối chiếu cấu trúc. [小R Listening](https://littler5071.github.io/toeic/) · [Mẫu ETS](https://www.ets.org/toeic/test-takers/prepare.html)

- APK Study `vn.toeiclearning.alpha.study`, versionName `0.3.9-study`, versionCode `13`.
- Tệp cục bộ `android-app/.tooling/two-user-study/fast-study-08/TOEIC-Study-0.3.9-debug.apk`.
- SHA-256 APK `f8cb723fb794e247d2750cc0daf3a5b802a98a77d5b6acb43f98ca236b67611a`.
- SHA-256 content pack `dbcf178c444dbe38e75ba9fc11e73a864e07202e1ca49b45c29f0655cb0fc625`. Bản build này đọc asset cục bộ trong `content-08/release-assets/`.

Stage05 giữ CONDITIONAL PASS và các CP tiếp tục ACTIVE. QA/ECP chính thức và Google Play vẫn tạm hoãn.
