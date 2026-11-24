# CONTENT-06 · Study 0.3.7 và nhập bộ đề có khóa V0.1

24/11/2026 · `development/two-user-study-mvp` · [Issue #12](https://github.com/hieupham03/TOEIC-Learning-App/issues/12)

**APK Study có 209 câu thật, 11 câu đã duyệt và chấm được.** Mục tiêu 100 câu chấm được còn thiếu 89 câu. Ba câu Listening bổ sung của VOA đã khớp khóa nguồn và sẵn sàng duyệt cục bộ. Có 0 câu mới được duyệt và 0 bộ 200 câu đủ điều kiện đưa vào APK. Full Mock A/B vẫn khóa.

## Số câu trong APK

| Part | Câu thật | Khóa nguồn khớp | Đã duyệt | Chấm được |
|---|---:|---:|---:|---:|
| 1 | 5 | 0 | 0 | 0 |
| 2 | 25 | 0 | 0 | 0 |
| 3 | 39 | 0 | 0 | 0 |
| 4 | 30 | 0 | 0 | 0 |
| 5 | 38 | 9 | 9 | 9 |
| 6 | 16 | 0 | 0 | 0 |
| 7 | 56 | 2 | 2 | 2 |
| **Tổng** | **209** | **11** | **11** | **11** |

11 khóa trong APK là các khóa Reading đã được duyệt ở CONTENT-05. Pack có 111 nhóm, trùng từng byte với 0.3.6. 198 câu Zenlish và media giữ nguyên. [Báo cáo 0.3.6](STAGE05_CONTENT05_PO_11_ENGINEERING_ACTIVATION_REPORT_V0.1.md)

## Nguồn đã kiểm tra

| Nguồn | Tệp và khả năng sử dụng đã xác minh |
|---|---|
| VOA Learning English | Bài gốc mang ID quiz 6588866. Bốn kết quả quiz công khai qua giao diện thông thường có đủ bốn lựa chọn và một khóa mỗi câu. MP3 gốc 5.538.003 byte, SHA-256 `1799169ef33a616cabf30bf83d614039714e738e3aabab20b3363903e07f4d10`. Android giải mã đủ 346,047 giây. Chuẩn bị **ba câu đầu** theo nhóm luyện bổ sung Part 4, giữ đúng thứ tự và audio gốc, dùng trong trang duyệt cục bộ. VOA cho dùng học liệu do họ sản xuất với ghi công. Ảnh ghi công AP giữ ngoài gói duyệt. Đây là bài luyện nghe bổ sung của VOA Learning English / Bryan Lynn, với 0 câu đưa vào APK. [Bài VOA](https://learningenglish.voanews.com/a/free-google-ai-tool-aims-to-improve-job-interview-skills/6588892.html) · [Quiz](https://learningenglish.voanews.com/a/6588866.html) · [Quy định sử dụng](https://learningenglish.voanews.com/p/6861.html) |
| Hellenic American Union | PDF 52 trang bản 2018 đã lấy có 200 câu, 200 khóa và script. 100 câu Reading có lựa chọn theo đúng thứ tự. Chưa có Listening audio công khai khớp bản PDF hoặc phạm vi tái sử dụng trong APK được xác lập. PDF 64 trang riêng ghi do ETS phát triển, mở được phần đầu, lượt truy xuất nội dung khóa hết thời gian. Hai PDF ở mức tham chiếu. [HAU 2018 và khóa](https://siteresources.blob.core.windows.net/siteresourcescontainer/hauportal/media/root/exams/support/individuals/toeic_sample-test-2018_v70_orfeas.pdf#page=50) · [Phạm vi truy cập ORFEAS](https://www.hau.gr/en-us/exams/support/language-schools-teachers/exam-preparation-material) · [PDF ETS 64 trang](https://siteresources.blob.core.windows.net/siteresourcescontainer/hauportal/media/root/orfeas/ets/toeic/toeic_sample-test_a4_64pg_v30.pdf) |
| ESL Lounge Part 1 | Trang thật, sáu nhóm có sáu khóa công khai, mỗi nhóm bốn lựa chọn, một ảnh và một MP3. Đã lấy đủ sáu ảnh và sáu MP3 từ liên kết của nhà xuất bản. Android giải mã đủ cả sáu clip. Điều khoản giới hạn sao chép hoặc chuyển tiếp ngoài các trường hợp được ghi, nên dùng để tham chiếu. [Bài nguồn](https://www.esl-lounge.com/student/toeic-test-practice/toeic-001-listening-part-one-1.php) · [Điều khoản](https://www.esl-lounge.com/copyright.php) |
| ELLLO và 英語のりん | ELLLO STeP 07/18 mỗi bài có sáu khóa và ba lựa chọn mỗi câu. Máy chủ nhạc trả 403 tại robots nên dừng. Bài A2 độc lập có PDF khóa và MP3 thật, vẫn ba lựa chọn. PDF 英語のりん có 26 câu, khóa và transcript, audio ở dịch vụ trả phí. 0 câu vào APK. [ELLLO STeP](https://www.elllo.org/english/STeP.htm) · [ELLLO A2](https://www.elllo.org/book/A2/A2-01-Present-Simple.html) · [PDF 26 câu](https://eigonorin.com/assets/free/toeic-mock-vol1.pdf) |
| PrepSim, Compass và 7ESL | PrepSim mở được trình làm bài và một ví dụ có khóa, chưa lấy được đề, khóa đủ bộ và audio. Compass có mục MP3 nhưng tài liệu Answer Key/Review Test dành cho giáo viên. 7ESL cho truy cập giới hạn theo đề, một lượt Reading trả 403. Các nguồn này chưa cung cấp bộ công khai có đủ tệp để nhập. [PrepSim](https://aynadhillon.com/toeic-listening-reading-mock-test) · [Compass](https://www.compasspub.com/eng/compass/level_view.asp?h_seq=2057) · [7ESL](https://7esl.com/exams/toeic/) |

Hồ sơ kiểm tra thêm gồm Exam English, Hong Kong, Taiwan, Asahi Press, HAU và các hash media lưu trong `android-app/.tooling/two-user-study/content-06/source-discovery/`. Với Faust và mẫu ETS/IIG/IIBC, dùng lại kết quả đối chiếu trước đó. [Báo cáo CONTENT-04](STAGE05_TWO_USER_MULTI_SOURCE_GRADED_REPORT_V0.1.md) · [Báo cáo CONTENT-05](STAGE05_TWO_USER_FIRST_GRADED_PRACTICE_REPORT_V0.1.md)

Trang `content-06/voa-review/review.html` dùng trình duyệt offline hiện có và hiển thị ba câu VOA đang chờ duyệt. Gói duyệt cục bộ có 212 câu, 14 khóa nguồn, 11 đã duyệt. Nhà xuất bản cung cấp bốn câu cho audio này. Chọn ba câu đầu để phù hợp kích thước nhóm luyện hiện hành. Cả ba vẫn chưa chấm và nằm ngoài APK bàn giao. Khi có quyết định thật, nhập qua CLI hiện hành trên bundle có các ID VOA.

## Nhập bộ đề và chặn mở A/B

- `review_study_content.py` dùng lại `owner/bundle.json`, `owner/sources`, `owner/media` và `owner/source-keys.json` để đối chiếu nhóm và phiên bản, thứ tự lựa chọn, đường dẫn media, ID câu và SHA-256. Trang duyệt hiện có nhận câu form và media cách ly, ghi rõ Đề A hoặc Đề B trên dòng tương ứng. Bundle chưa có khóa nguồn độc lập giữ trạng thái thiếu chứng cứ dù có bản ghi duyệt câu.
- Mỗi form kiểm tra thứ tự 1–200 và phân bổ `6/25/39/30/30/16/54`. Khóa nguồn và quyết định duyệt của từng câu phải khớp. Hồ sơ QA form hiện có cần dấu `APPROVED`, người duyệt, ngày, URL/vị trí chứng cứ, SHA-256 tệp và `formSha256` từ báo cáo kiểm tra. CLI chỉ chép hai form và media vào pack khi **cả hai** đạt và qua kiểm tra trùng với kho luyện tập. Khi một form bị thu hồi, cả cặp và media riêng của cặp rút khỏi gói. [Lệnh hiện có](../android-app/scripts/review_study_content.py)
- Android chặn trùng cả ảnh lẫn audio, phát hiện câu lặp dù đảo lựa chọn và chặn tiếp tục bài Mock chưa hoàn tất nếu phiên bản form không còn được mở. Lịch sử và lựa chọn SQLite giữ nguyên. Tại thời điểm bàn giao A và B mỗi đề có **0/200** câu đã kiểm chứng. Không có điểm ETS quy đổi.

## Kiểm thử và bàn giao

| Kiểm tra | Kết quả thực tế |
|---|---|
| Dựng pack bằng `review_study_content.py --workspace content-06` | PASS, exit 0. SHA-256 pack `094e217db5dba1c4d7044828c961fae88e22df768466c71901430b27dcc5546e`. Không có form trong APK. |
| `python -B -X utf8 -m unittest discover -s tests/ingestion -v` | PASS, exit 0, 67/67. Hai fixture 200 câu kiểm tra khóa độc lập, QA từng câu, QA cấp form, hash cũ và rút media khi thu hồi. |
| Gradle offline `:app:assembleStudy :app:testStudyUnitTest --rerun :app:assembleDebug :app:testDebugUnitTest --rerun :app:assembleLocalPreview :app:testLocalPreviewUnitTest --rerun` | PASS, exit 0. JUnit **23/23 mỗi variant**. |
| Alpha/Beta/CX-04, Kotlin và baseline | PASS, exit 0. Guards 10/11/9, Kotlin 25 assertions. Sáu SHA-256 baseline giữ nguyên. |
| Emulator API 36 cài đè 0.3.6 → 0.3.7 offline | PASS, exit 0. Kết quả cũ, dấu trang, bài memo và lựa chọn còn sau force-stop. Chấm bài memo, thống kê Part, luyện lại câu sai và khóa A/B đạt. |
| Giải mã nguồn và trang duyệt VOA | PASS, exit 0. Android giải mã 7/7 MP3 tham chiếu tới PCM khác 0. Chrome offline hiển thị ba câu chờ duyệt và đường dẫn audio cục bộ. |
| APK và ZIP | PASS, exit 0. Cùng package ID và chứng chỉ debug với 0.3.6. ZIP chứa đúng APK, SHA-256 và hướng dẫn hai máy. |
| Hai điện thoại thật và QA/ECP chính thức | NOT RUN. Google Play tạm hoãn và ngân sách DEFERRED. |

Thư mục APK `android-app/.tooling/two-user-study/content-06/`. APK `TOEIC-Study-0.3.7-debug.apk`, versionCode 11, SHA-256 `1cc7d3ef5056d97f54ae29de09208066b231549ab832c30b093a0aac8d38e587`. ZIP `TOEIC-Study-hai-may-0.3.7.zip`, SHA-256 `0669ea777d13efe4bd2f45a268edd9bd0bc81ea15fdcb955be9ee7f74a16a5af`.
