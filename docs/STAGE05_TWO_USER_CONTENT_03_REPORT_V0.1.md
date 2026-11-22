# Báo cáo kỹ thuật CONTENT-03 V0.1

22/11/2026 · `development/two-user-study-mvp` · Study `0.3.3-study` (7)

**GO** cài thử 198 câu offline trên hai máy. **BLOCKED** chấm điểm học liệu thật do chưa có bảng khóa đúng phiên bản và quyết định duyệt. Hai đề Full Mock A/B vẫn khóa, mỗi đề thiếu 200 câu độc lập đã kiểm chứng. [Issue #11](https://github.com/hieupham03/TOEIC-Learning-App/issues/11)

## Trạng thái học liệu

| Part | Câu khả dụng | Có khóa nguồn khớp câu | Đã QA nội dung | Chấm được |
| --- | ---: | ---: | ---: | ---: |
| 1 | 5 | 0 | 0 | 0 |
| 2 | 25 | 0 | 0 | 0 |
| 3 | 39 | 0 | 0 | 0 |
| 4 | 30 | 0 | 0 | 0 |
| 5 | 29 | 0 | 0 | 0 |
| 6 | 16 | 0 | 0 | 0 |
| 7 | 54 | 0 | 0 | 0 |
| **Tổng** | **198** | **0** | **0** | **0** |

Kiểm tra Reading trước, rồi Listening trong kho cục bộ và một lượt tra cứu hữu hạn trên các nguồn đã được PO xác nhận. Không có bản xuất khóa do PO cung cấp trong workspace. Lượt lấy lại trang Zenlish dùng **2 HTTP request** gồm robots.txt và trang đề, tải **224.089 byte**. Hai snapshot có cùng **102 bản ghi nhóm và 199 câu**. Trường `answer` trong cả 199 câu là mảng lựa chọn. Mẫu kết quả trong HTML lấy về chứa các trường tổng hợp và chưa cung cấp bảng khóa từng câu. Lượt này không nộp bài trên trang nguồn. [Zenlish ETS 2022 Test 1](https://zenlishtoeic.vn/stm-quizzes/test-1-2022/)

| Mục thiếu | Trạng thái và dữ liệu cần bổ sung |
| --- | --- |
| Part 1, câu 3 · `zenlish:40926:3` | **BLOCKED**. Hai snapshot cùng trỏ đến clip có hậu tố `part-1-3-1.mp3`. Không có chứng cứ độc lập xác nhận clip tương ứng câu và ảnh. Cần MP3 gốc và bản xuất hoặc tham chiếu xác nhận phiên bản, nhóm và câu. |
| Part 5, câu 118 | **BLOCKED**. Vắng ở cả hai snapshot và chưa có bản gốc đúng đề trong các nguồn đã kiểm tra. Cần trang hoặc bản xuất gốc, mã câu/nhóm hoặc vị trí ổn định, thân câu và bốn lựa chọn theo thứ tự nguồn. |

Snapshot lưu trước có SHA-256 `2db58276d138f6d1374698c150fc518765a3d9cd4f84c77765a33e9f44556c14`. Trang tải lại có SHA-256 `42b8faf8e1bc2033aaeae2bfd679ed17986b3bf9f16ad8fed5c12067e252c85c`. Gói 198 câu có cùng `pack.json` SHA-256 với CONTENT-02 `59102737b61c3f37de01f04c98464cab9bf6bf97c79f6ef213f1a47aab13a561`.

## Bàn giao khóa và phạm vi thay đổi

Gói yêu cầu cục bộ tại `android-app/.tooling/two-user-study/content-03/key-request/` có **99 dòng Reading** ở `01-reading-key-request.json`, **99 dòng Listening** ở `02-listening-key-request.json`, cùng chi tiết hai câu thiếu ở `03-missing-items.json`. Mỗi dòng khóa có ID câu/nhóm, phiên bản, hash câu và lựa chọn theo thứ tự nguồn. Đáp án và các trường duyệt để trống. Có thể cung cấp bảng khóa gốc khớp phiên bản và trang/dòng, sau đó đối chiếu từng câu trong `content-02/review.html`.

`android-app/scripts/review_study_content.py --export-key-request` đọc gói và hàng đợi hiện tại. Xuất bị từ chối khi ID, phiên bản, hash, số câu hay thứ tự lựa chọn lệch. Trang duyệt CONTENT-02 giữ nguyên. Khi có chứng cứ, dùng chức năng xuất quyết định của trang và lệnh `--import-review ... --evidence ...` hiện có. Nhập theo trạng thái nguồn/chờ duyệt, rồi chỉ chấm sau khi người duyệt ghi nhận đối chiếu thực tế. Thay đổi nguồn ở CLI, test `android-app/tests/ingestion/test_content_02.py` và bản Study trong `android-app/app/build.gradle.kts`. Đối chiếu kỹ thuật với FR-005/006/007/008/015/016/019 và AT-05/06/07/08/15/16/19.

## Bằng chứng kiểm thử

| Kiểm tra | Trạng thái | Kết quả |
| --- | --- | --- |
| Xuất và dựng lại offline | PASS | Export tạo đúng 99/99 dòng. Dựng lại trong workspace riêng cho cùng hash gói, 198 câu chờ chứng cứ và 0 quyết định. Hash trang duyệt không đổi. |
| Gradle và JUnit | PASS | `gradlew.bat --offline --no-daemon --console=plain :app:assembleStudy :app:testStudyUnitTest --rerun :app:assembleDebug :app:testDebugUnitTest --rerun :app:assembleLocalPreview :app:testLocalPreviewUnitTest --rerun`, exit `0`. JUnit **20/20 mỗi biến thể**, 0 fail/error/skipped. |
| Python ingestion | PASS | `python -B -X utf8 -m unittest discover -s tests/ingestion -v`, exit `0`, **60/60**. Thêm ca xuất tách Reading/Listening, từ chối mẫu chưa điền, ID trùng, thiếu hoặc lệch. Mẫu fixture đã điền chứng cứ ở trạng thái `SOURCE_ONLY` được nhập và vẫn chưa chấm. |
| Scope guards và Kotlin CLI | PASS | Alpha 10/10, Beta 11/11, CX-04 9/9, Kotlin CLI 25 assertions. Các lệnh đều exit `0`. Sáu baseline trùng SHA-256 đã ký. |
| Emulator API 36, cập nhật SQLite | PASS | `adb install -r` từ 0.3.2 lên 0.3.3 giữ lịch sử Part 3 (1/39 câu đã trả lời), câu 33 đang làm, lựa chọn và dấu đánh dấu sau force-stop. Kiểm tra số câu từng Part và khóa A/B. Seed và upgrade exit `0`. |
| Emulator API 36, Reading và Listening offline | PASS | Reading nhảy câu 168, mở hai ảnh, phóng và Back ở 800dp/font 150%. Listening nhảy câu 62, mở ảnh nhóm, phát clip và xác nhận dừng khi app xuống nền. Hai lượt exit `0`. |
| Emulator API 36, chấm và thu hồi | PASS | APK fixture riêng ghi một câu sai và hiện lời giải fixture cho khóa đã duyệt. Khóa ở trạng thái `SOURCE_ONLY` vẫn chưa chấm. Sau cài đè fixture thu hồi, lịch sử giữ kết quả đã chấm và phiên mới giữ trạng thái chưa chấm. Hai lượt exit `0`. Nhật ký crash của lượt thử trống. |
| Cấu hình APK và gói cài | PASS | `apksigner verify` exit `0`. So sánh pack và 92 media trong APK cho cùng byte với 0.3.2, Debug thông thường không chứa gói Study. Kiểm tra CRC ZIP và SHA-256 của APK nhúng exit `0`. |
| Hai điện thoại thật và formal QA/ECP | NOT RUN | Gói để hai người dùng thử. Không có kết quả thử thiết bị thật trong lượt này. G05-CP01..08 vẫn ACTIVE, Google Play tạm hoãn. |

## Tệp bàn giao cục bộ

Các tệp nằm trong `android-app/.tooling/two-user-study/content-03/`.

| Tệp | Dung lượng | SHA-256 |
| --- | ---: | --- |
| `TOEIC-Study-0.3.3-debug.apk` | 59.312.838 byte | `203a6e00f737f5e012627bec3c0d13097df3f82014344252bd5b5012ab58f560` |
| `TOEIC-Study-hai-may-0.3.3.zip` | 53.632.332 byte | `ad64914dbab2e961f6e723f6bb0e0e6b3d016bf3b996b55c142b6e869922533e` |
| `TOEIC-CONTENT03-key-request.zip` | 22.224 byte | `a4eced2493e85f9761723e8e5e413eabc730ca03e4166ef524e6699ae931f0c8` |

Package Study `vn.toeiclearning.alpha.study`, versionCode 7, minSdk 26. ZIP cài thử có APK, checksum và hướng dẫn kiểm tra hai máy. Tệp nguồn, mẫu khóa, APK, ZIP, fixture và nhật ký lưu cục bộ.
