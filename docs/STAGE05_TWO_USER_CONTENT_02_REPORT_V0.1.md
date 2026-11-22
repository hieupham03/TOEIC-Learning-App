# Báo cáo kỹ thuật CONTENT-02 V0.1

22/11/2026 · `development/two-user-study-mvp` · Study `0.3.2-study` (6)

**GO** cho gói cài thử offline với 198 câu thật. **BLOCKED** chấm điểm học liệu thật do chưa có khóa nguồn gắn được với đúng câu và phiên bản để người duyệt đối chiếu. **BLOCKED** Full Mock A/B, mỗi đề thiếu 200 câu đã kiểm chứng. [Issue #11](https://github.com/hieupham03/TOEIC-Learning-App/issues/11)

## Học liệu thực trong APK

| Part | CONTENT-01 | Câu thêm | Khả dụng | Có khóa nguồn | Đã QA nội dung | Chấm được | Có trong snapshot nhưng chưa nhập |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 5 | 0 | 5 | 0 | 0 | 0 | 1 |
| 2 | 7 | 18 | 25 | 0 | 0 | 0 | 0 |
| 3 | 18 | 21 | 39 | 0 | 0 | 0 | 0 |
| 4 | 18 | 12 | 30 | 0 | 0 | 0 | 0 |
| 5 | 12 | 17 | 29 | 0 | 0 | 0 | 0 |
| 6 | 16 | 0 | 16 | 0 | 0 | 0 | 0 |
| 7 | 25 | 29 | 54 | 0 | 0 | 0 | 0 |
| **Tổng** | **101** | **97** | **198** | **0** | **0** | **0** | **1** |

Gói có **101 nhóm, 53 MP3 và 39 ảnh**. 52 nhóm mới thêm 29 MP3 và 21 ảnh. Đối chiếu theo ID xác nhận 101 câu cũ, nội dung và media tương ứng trùng bản nguồn CONTENT-01. Parser giữ ảnh nhóm của Listening và thứ tự ảnh trong markup của 6 nhóm nhiều ảnh Part 7. Câu 3 Part 1 giữ ngoài gói vì tên clip không khớp quy tắc số câu và chưa có bằng chứng độc lập để chốt ánh xạ. Câu 118 Part 5 vắng trong snapshot 199 câu.

Batch tải **51/80 HTTP request**, đều HTTP 200, gồm 1 robots.txt và 50 tài sản. Tổng **25.563.768 byte**, phản hồi lớn nhất **1.691.471 byte**. Lần dựng lại offline giữ nguyên bộ đếm, không phát sinh request mới. `http-journal.json` lưu hạn mức đã dùng và `media-receipts.json` lưu nguồn, hash và cache theo URL. Phiên bản snapshot SHA-256 `2db58276d138f6d1374698c150fc518765a3d9cd4f84c77765a33e9f44556c14`. SHA-256 `pack.json` mới là `59102737b61c3f37de01f04c98464cab9bf6bf97c79f6ef213f1a47aab13a561`. [Snapshot Zenlish](https://zenlishtoeic.vn/stm-quizzes/test-1-2022/)

## Bằng chứng, duyệt offline và gói của PO

- Cả 199 trường `answer` của snapshot là mảng lựa chọn. Rà lại dữ liệu lưu tại chỗ và tìm theo phiên bản trong ba nguồn đã được phép. Liên kết chi tiết liên quan trong snapshot đưa ra yêu cầu đăng nhập. Các danh mục công khai đã lưu và kết quả tìm kiếm chưa cho thấy bảng khóa có thể gắn với ID, phiên bản và thứ tự lựa chọn của ngân hàng hiện tại. Kho cục bộ chưa có bảng khóa do PO xuất. Có **198 dòng `SOURCE_EVIDENCE_REQUIRED`**, 0 lời giải được duyệt. [Danh mục TOEIC Study4](https://study4.com/tests/toeic/) · [The TOEIC Lab](https://test.thetoeiclab.vn/)
- Mở `android-app/.tooling/two-user-study/content-02/review.html` bằng Edge hoặc Chrome. Có thể tìm theo Part, số câu hay ID, xem câu và lựa chọn, phát MP3, đọc đoạn văn và xem ảnh theo thứ tự. Trang hiển thị SHA-256 của câu và media. Người duyệt chọn tệp chứng cứ, nhập URL cùng nguồn, trang/dòng, đáp án, tên, ngày và lời giải có vị trí nguồn nếu có. Chọn trạng thái và xác nhận đã đối chiếu trước khi xuất JSON qua nút **Tải quyết định JSON**.
- Từ `android-app`, nhập quyết định bằng `python -B -X utf8 scripts/review_study_content.py --import-review <study-review-decisions.json> --evidence <tệp-nguồn>`. Lặp `--evidence` cho nhiều tệp. CLI kiểm tra byte chứng cứ có thật, cùng nguồn, ID, phiên bản, nội dung và thứ tự lựa chọn/media, khóa hợp lệ, ngày và người duyệt, rồi sinh `source-keys.json`, `reviews.json` cùng báo cáo coverage. `SOURCE_ONLY` giữ câu chưa chấm. `REVOKED` loại khóa khỏi phiên mới, giữ điểm trong snapshot lịch sử. `withdrawn-groups.json` là mảng ID nhóm rút khỏi danh mục; phiên và kết quả cũ vẫn đọc được.
- Gói PO là JSON tại `content-02/owner/bundle.json`, với `schema: 1`, mảng `practice` và mảng `inventories` chứa `{id, groups}` nếu có A/B. Mỗi nhóm cần `id`, `part`, `source`, `version`, `items`. Mỗi câu có `id`, `number`, `prompt`, `choices`. `version` là SHA-256 của tệp gốc tại `owner/sources/<sha256>.bin`. Mỗi tài sản `audio`, `image` hoặc phần tử trong `extraImages` có `path`, `size`, `sha256`. Khai báo `path` dạng `study_pack/media/<sha256>.<mp3|png|jpg>` và đặt tệp cùng tên trong `owner/media/`. `audioItems`, `imageItems` và `passageItems` khớp thứ tự ID câu tương ứng. Quyết định khóa có thể nạp từ `owner/reviews.json` cùng chứng cứ. Tool kiểm tra media, thứ tự, ID và trùng lặp giữa practice/A/B. Kho A/B được cách ly khỏi APK và không bật Mock. Lượt này có 0 câu do PO nhập.
- Dựng lại bằng `python -B -X utf8 scripts/extend_study_content.py` rồi `python -B -X utf8 scripts/review_study_content.py`. Cờ `--fetch` chỉ lấy media chưa có cache trong ngân sách lưu trên đĩa. CONTENT-01 được đọc từ APK đã chốt, mọi tệp sinh mới nằm ở `content-02`. Cấu hình và package riêng `vn.toeiclearning.alpha.study` giữ đường cập nhật từ 0.3.1.

## Kiểm chứng

| Kiểm tra | Trạng thái | Kết quả |
| --- | --- | --- |
| Dựng lại offline | PASS | Cả `extend_study_content.py` và `review_study_content.py` exit `0`, SHA gói không đổi, 51 HTTP request tích lũy. |
| Gradle và JUnit | PASS | `gradlew.bat --offline --no-daemon --console=plain :app:assembleStudy :app:testStudyUnitTest --rerun :app:assembleDebug :app:testDebugUnitTest --rerun :app:assembleLocalPreview :app:testLocalPreviewUnitTest --rerun`, exit `0`, JUnit **20/20 mỗi biến thể**, 0 fail/error/skipped. |
| Python ingestion | PASS | `python -B -X utf8 -m unittest discover -s tests/ingestion -v`, exit `0`, **58/58**. Có ca lệch phiên bản, thân câu và thứ tự lựa chọn/media, sai ID/nhóm, chứng cứ sai hoặc trùng, ảnh lỗi, trùng nội dung qua đề, ngân sách khi tiếp tục và thu hồi khóa. |
| Guards và Kotlin CLI | PASS | Alpha 10/10, Beta 11/11, CX-04 9/9, Kotlin 25 assertions. Tất cả exit `0`. Sáu baseline khớp SHA-256 đã ký. |
| Trang duyệt offline | PASS | Edge đọc 198 câu, ảnh và điều khiển MP3, đúng 2 ảnh câu 168. Với fixture, nút ghi từ chối thiếu file và thiếu xác nhận, xuất JSON hợp lệ khi có hai điều kiện. Exit `0`. |
| Nhập bundle và quyền chấm | PASS | Workspace fixture nhập gói owner, ghi khóa và quyết định duyệt riêng, từ chối khóa lệch phiên bản và giữ bản xuất trước đó, sau đó tái dựng khi thu hồi. Exit `0`. |
| API 34, cập nhật SQLite | PASS | `adb install -r` từ 0.3.1 sang 0.3.2. Giữ phiên Part 3 đã nộp, lựa chọn, dấu đánh dấu và vị trí câu 33 sau khi buộc dừng. Màn khóa A/B vẫn hiển thị. Test seed và upgrade exit `0`. Hộp thoại System UI ở lúc boot được xử lý trước khi chạy test app. |
| API 36, Reading | PASS | Bật chế độ máy bay, 800dp, font 150%. Nhảy tới câu 168, mở và phóng hai ảnh theo đúng thứ tự, chuyển câu hỏi, Back về đoạn văn. Lượt xác minh exit `0`. |
| API 36, Listening | PASS | Bật chế độ máy bay, nhảy tới câu 62, phát clip đi kèm ảnh nhóm và xác nhận playback dừng khi đưa app xuống nền. Lượt xác minh exit `0`. |
| API 36, chấm điểm và thu hồi | PASS | Fixture riêng chấm đúng phạm vi duyệt, ghi một câu sai và hiện lời giải có chứng cứ. Câu có nguồn nhưng chờ duyệt vẫn chưa chấm. Cài đè fixture đã thu hồi giữ kết quả cũ và ngăn chấm phiên mới. Cả hai lượt exit `0`. |
| API 36, giải mã media | PASS | `MediaCodec` giải mã **29/29 MP3 mới** ra PCM có tín hiệu, chênh thời lượng dưới 150 ms. `BitmapFactory` mở **21/21 ảnh mới**. 42 tài sản từ bản trước trùng byte đã kiểm tra trong CONTENT-01. Script exit `0`. Nghe qua loa điện thoại thật NOT RUN. |
| Khóa thật và lời giải thật | BLOCKED | 0/198 khóa nguồn, 0 đã duyệt, 0 chấm được. Hiện “Chưa có lời giải” khi thiếu nội dung hợp lệ. |
| Hai điện thoại thật, formal QA/ECP | NOT RUN | Hai máy chưa được kiểm thử với 0.3.2. CP vẫn ACTIVE, Google Play tạm hoãn. |

Các lượt API 36 đầu tiên exit `1` lúc mở activity sau cold boot. Sau khi xử lý hộp thoại Android System UI, các lượt kiểm chứng Reading, Listening và chấm điểm chạy lại trên cùng APK với kết quả ở bảng.

## Gói cài và bàn giao

Các tệp dưới đây lưu trong `android-app/.tooling/two-user-study/content-02/`.

| Tệp | Dung lượng | SHA-256 |
| --- | ---: | --- |
| `TOEIC-Study-0.3.2-debug.apk` | 59.312.838 byte | `c7ad5b9f8e31a8548ca2768fb6d524248687968f80b4df931645ede6cf79c152` |
| `TOEIC-Study-hai-may-0.3.2.zip` | 53.633.778 byte | `7c89f6a14b614bbf23f2a54de0e47c94b342912559bd9d53ebdadbfc90c004c6` |

`apksigner verify` exit `0`. ZIP đã kiểm CRC và chứa APK có pack nhúng, checksum, metadata pack, hướng dẫn cập nhật, checklist 10–15 phút và phiếu ghi lỗi. Đối chiếu 92 tài sản trong APK bằng byte và SHA-256. APK Debug thông thường không có pack Study. APK, ZIP, HTML, câu hỏi, media, chứng cứ và nhật ký giữ cục bộ.
