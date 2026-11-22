# Báo cáo kỹ thuật CONTENT-01 V0.1

22/11/2026 · `development/two-user-study-mvp` · Study `0.3.1-study` (5)

**GO** cho luyện offline 101 câu thật với lưu tiến độ. **BLOCKED** chấm điểm học liệu thật do chưa có khóa nguồn gắn đúng câu và phiên bản để kiểm duyệt. **BLOCKED** Full Mock A/B, mỗi đề thiếu 200 câu đã kiểm chứng. [Issue #10](https://github.com/hieupham03/TOEIC-Learning-App/issues/10)

## Ngân hàng trong APK

| Part | Câu mới | Câu khả dụng | Có đáp án nguồn | Đã duyệt và có thể chấm | Câu có trong snapshot chưa nhập |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 4 | 5 | 0 | 0 | 1 |
| 2 | 6 | 7 | 0 | 0 | 18 |
| 3 | 15 | 18 | 0 | 0 | 21 |
| 4 | 15 | 18 | 0 | 0 | 12 |
| 5 | 9 | 12 | 0 | 0 | 17 |
| 6 | 12 | 16 | 0 | 0 | 0 |
| 7 | 23 | 25 | 0 | 0 | 29 |
| **Tổng** | **84** | **101** | **0** | **0** | **98** |

Gói có **49 nhóm, 24 MP3 và 18 ảnh**. Batch nhận đủ 40 nhóm đã chọn, gồm 84 câu, thêm 20 MP3 và 15 ảnh. Sử dụng snapshot có sẵn và gửi **40/80 HTTP request**, tổng **19.710.284 byte**, phản hồi lớn nhất **1.487.554 byte**. Không gặp CAPTCHA, 403 hoặc 429. Trong snapshot có 102 nhóm và 199 câu. Còn 53 nhóm chưa nhập, gồm 41 nhóm ngoài hạn mức batch và 12 nhóm thiếu ảnh, có cấu trúc ảnh chưa hỗ trợ hoặc tên MP3 lệch dải số câu. Snapshot thiếu một câu Part 5 so với phân bổ 200 câu.

Phiên bản snapshot Zenlish SHA-256 `2db58276d138f6d1374698c150fc518765a3d9cd4f84c77765a33e9f44556c14`. `pack.json` SHA-256 `b305684cd89ac679df59bae160ce4406ac0fe2f43c61c09be6b4986a426c1685`. Đã đối chiếu byte, SHA-256 và định dạng 42 tệp media trong APK; các MP3 có thời lượng cấu trúc từ 19,827 đến 88,816 giây. Debug thông thường không chứa gói Study. [Snapshot Zenlish](https://zenlishtoeic.vn/stm-quizzes/test-1-2022/)

## Bằng chứng đáp án và hàng đợi

- Zenlish có 199 trường `answer` dạng mảng lựa chọn trên snapshot. Không tìm thấy khóa đúng công khai gắn với từng câu của gói. Liên kết chi tiết liên quan hiển thị yêu cầu đăng nhập và không được truy cập. Hai trang công khai được lấy trả HTTP 200 và không cung cấp khóa có thể liên kết với mã nhóm, mã câu và phiên bản trong gói. Hai trang giữ trạng thái **PAGE_ONLY**. [The TOEIC Lab](https://test.thetoeiclab.vn/) · [Danh mục TOEIC Study4](https://study4.com/tests/toeic/)
- Hàng đợi cục bộ `android-app/.tooling/two-user-study/content-01/answer-review-queue.json` có 101 dòng `SOURCE_EVIDENCE_REQUIRED`. Mỗi dòng có nhóm, câu, Part, số thứ tự, URL, SHA nguồn và dấu vân tay của câu gồm stem, lựa chọn đúng thứ tự, đoạn văn và hash media. `acquisition.json` ghi receipt HTTP, nguồn và checksum từng tệp.
- Khi người kiểm duyệt có tài liệu khóa thật, đặt tệp nguồn tại `content-01/source-evidence/<sha256>.bin`. Thêm dòng vào mảng JSON `source-keys.json` với các trường từ hàng đợi `groupId`, `itemId`, `source`, `version`, `itemSha256`, cùng `label`, `evidenceUrl`, `evidenceSha256`, `locator`. `evidenceUrl` thuộc cùng nguồn của câu. `locator` định vị dòng hoặc trang trong chứng cứ. Sau khi người duyệt đối chiếu, sao chép chính xác dòng khóa sang mảng `reviews.json` và thêm `status: APPROVED`, `reviewer`. Nếu có lời giải trích từ chứng cứ đã duyệt, ghi `explanation` và `explanationLocator`; các câu còn lại hiển thị “Chưa có lời giải”.
- Chạy `python -B -X utf8 scripts/activate_study_content.py` từ `android-app` để kiểm tra và dựng lại offline. Sai ID, nhóm, nguồn, byte bằng chứng, thứ tự lựa chọn, phiên bản hoặc nội dung xét duyệt giữ câu ở chế độ không chấm. UI hiển thị riêng số câu khả dụng, có đáp án nguồn, đã duyệt. Android kiểm tra dấu vân tay lần nữa khi mở gói. Người học vẫn lưu được lựa chọn cho mọi câu khả dụng.
- Phiên SQLite giữ snapshot và kết quả tại thời điểm làm. Có thể rút nhóm khỏi phiên mới qua mảng ID `withdrawn-groups.json`. Lịch sử giữ kết quả cũ, nút luyện lại chỉ mở khi ID câu còn trong ngân hàng hiện hành.

## Kiểm chứng

| Kiểm tra | Trạng thái | Kết quả |
| --- | --- | --- |
| Dựng lại gói offline | PASS | `python -B -X utf8 scripts/activate_study_content.py` exit `0`. Manifest tái tạo trùng SHA-256. |
| Gradle và JUnit | PASS | `gradlew.bat --offline --no-daemon --console=plain :app:assembleStudy :app:testStudyUnitTest --rerun :app:assembleDebug :app:testDebugUnitTest --rerun :app:assembleLocalPreview :app:testLocalPreviewUnitTest --rerun`, exit `0`. JUnit 19/19 mỗi biến thể, 0 fail/error/skipped. |
| Ingestion và media | PASS | `python -B -X utf8 -m unittest discover -s tests/ingestion -v`, exit `0`, 51/51. Bổ sung ca chứng cứ sai nguồn, lệch phiên bản, trùng ID khóa hoặc câu, MP3 thiếu, ảnh hỏng, số câu sai nhóm và rút nhóm khỏi phiên mới. |
| Scope guards và Kotlin CLI | PASS | `check_alpha_scope.py`, `check_beta_reading_ui_scope.py`, `check_cx04_listening_scope.py` exit `0` lần lượt 10/10, 11/11, 9/9. `run_pure_kotlin_core_checks.ps1` exit `0`, 25 assertions. |
| Emulator API 36, cập nhật offline | PASS | Dùng `adb install -r` từ 0.3.0 lên 0.3.1. Giữ phiên Part 3 đã kết thúc, câu 33 đang làm và lựa chọn đã lưu sau `am force-stop`. Kiểm tra số câu từng Part và màn khóa A/B. Script xác minh exit `0`. |
| Emulator API 36, chấm điểm và rút học liệu | PASS | Fixture riêng cho kết quả 1 sai, 2 đã trả lời chưa chấm. Câu đã duyệt hiện đáp án, phản hồi sai và “Chưa có lời giải”; câu chờ duyệt và lệch phiên bản giữ không chấm. Danh sách câu sai cho luyện lại. Thay fixture bằng gói thật giữ lịch sử, ngăn bắt đầu luyện lại câu đã rút. Hai lượt cuối exit `0`. Hai lượt đầu exit `1` vì script tìm nhãn ngoài vùng hiển thị. Đã sửa thao tác cuộn của script. |
| Emulator API 36, giải mã | PASS | `MediaCodec` giải mã 24/24 MP3 ra PCM có tín hiệu. Chênh lệch thời lượng so với kiểm tra frame dưới 150 ms. `BitmapFactory` mở 18/18 ảnh. Script exit `0`. Nghe qua loa điện thoại thật NOT RUN. |
| Khóa thật, lời giải thật, Full Mock | BLOCKED | 0/101 câu có khóa nguồn, 0 câu đã duyệt, 0 lời giải hợp lệ và 0/400 câu mock đã kiểm chứng. Gói cài không chứa fixture. |
| Hai điện thoại thật, ECP/QA chính thức | NOT RUN | Lượt xác minh dùng emulator nội bộ. Sáu baseline khớp SHA-256 đã ký, các CP giữ nguyên. Google Play tiếp tục tạm hoãn. |

## APK cài riêng

`android-app/.tooling/two-user-study/content-01/TOEIC-Study-0.3.1-debug.apk` · **33.724.474 byte**.

SHA-256 `9faa247af92b3de117f35b98039ca0b407f54569f8b2d923157fa505b8963684`. `apksigner verify` exit `0`, package `vn.toeiclearning.alpha.study`, API tối thiểu 26. Dùng `adb -s SERIAL install -r TOEIC-Study-0.3.1-debug.apk` để cập nhật bản 0.3.0 cùng chữ ký. Học liệu gốc, ledger, APK, fixture APK, log và dữ liệu người học lưu cục bộ.
