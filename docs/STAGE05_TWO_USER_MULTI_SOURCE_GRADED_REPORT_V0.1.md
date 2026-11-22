# CONTENT-04 · Báo cáo kỹ thuật học liệu nhiều nguồn V0.1

22/11/2026 · `development/two-user-study-mvp` · Study `0.3.4-study`.

**GO cho kiểm tra kỹ thuật nội bộ và đối chiếu 11 câu Reading. BLOCKED cho bản chấm điểm học liệu thật.** Đã ghép 11 khóa nhà xuất bản với đúng câu, lựa chọn và hash phiên bản. Chưa có quyết định của người kiểm duyệt thực tế nên 0 câu được chấm. Full Mock A/B tiếp tục khóa.

## Học liệu thực trong APK riêng

| Part | Câu khả dụng | Có khóa nguồn khớp | Đã được kiểm duyệt | Chấm được |
|---|---:|---:|---:|---:|
| 1 | 5 | 0 | 0 | 0 |
| 2 | 25 | 0 | 0 | 0 |
| 3 | 39 | 0 | 0 | 0 |
| 4 | 30 | 0 | 0 | 0 |
| 5 | 38 | 9 | 0 | 0 |
| 6 | 16 | 0 | 0 | 0 |
| 7 | 56 | 2 | 0 | 0 |
| **Tổng** | **209** | **11** | **0** | **0** |

111 nhóm gồm 198 câu Zenlish giữ nguyên và 11 câu Reading mới gồm 5 Faust Part 5, 4 EnglishClub Part 5 và 2 EnglishClub Part 7 cùng một memo. Tất cả 11 hàng mới là `AWAITING_REVIEW`. 198 câu Zenlish thiếu khóa gốc. Zenlish Part 1 câu 3 chưa có ánh xạ MP3 đủ căn cứ và Part 5 câu 118 vắng trong snapshot, cả hai tiếp tục chưa nhập. Có **0 bộ 200 câu đủ đề, khóa và media**. Mock A thiếu 200/200 câu kiểm chứng, Mock B thiếu 200/200. Cơ chế kiểm tra trùng giữa luyện tập và hai đề và giới hạn điểm thô giữ nguyên.

## Kết quả kiểm tra trực tiếp nguồn

| Nguồn | Kết quả thực tế | Sử dụng |
|---|---|---|
| Faust Reading 01 | HTTP 200 cho cả PDF đề 30 trang và PDF khóa 2 trang cùng revision `8bbf28d3-348f-54ec-8dd0-63b5d19b52b2`. Đề đánh số 101–200. Kiểm tra cấu trúc Part 5 đủ 30 câu. PDF khóa công khai chỉ có 5 dòng cho câu 101–105. Trang còn lại yêu cầu gói trả phí. | `PARTIAL`. Ghép chính xác 5 câu với PDF khóa. [Trang đề](https://www.faustacademy.com/pruefungsmaterial/toeic-lr-reading-01) · [PDF đề](https://www.faustacademy.com/pruefungsmaterial/toeic-lr-reading-01/revisions/8bbf28d3-348f-54ec-8dd0-63b5d19b52b2/candidate.pdf) · [PDF khóa](https://www.faustacademy.com/pruefungsmaterial/toeic-lr-reading-01/revisions/8bbf28d3-348f-54ec-8dd0-63b5d19b52b2/teacher.pdf) |
| Faust Listening 01 | HTTP 200 cho PDF đề 25 trang đánh số 1–100 và PDF lời giải 2 trang cùng revision `e74d1371-f94a-58e0-b4b6-ae948137c81b`. PDF lời giải chỉ có trích đoạn script và ví dụ, 0 khóa đánh số câu thật. Đã tải và giải mã MP3 Part 1 sau redirect công khai HTTP 307. PDF mô tả hình, chưa xác minh hình gốc hoặc mốc audio theo nhóm. | `PARTIAL`. 0 câu nhập, Part 2–4 và cặp L02/R02 `NOT RUN`. [Trang đề và audio](https://www.faustacademy.com/pruefungsmaterial/toeic-lr-listening-01) · [PDF đề](https://www.faustacademy.com/pruefungsmaterial/toeic-lr-listening-01/revisions/e74d1371-f94a-58e0-b4b6-ae948137c81b/candidate.pdf) · [PDF lời giải](https://www.faustacademy.com/pruefungsmaterial/toeic-lr-listening-01/revisions/e74d1371-f94a-58e0-b4b6-ae948137c81b/teacher.pdf) |
| EnglishClub Part 5 và 7 | Đọc HTML thật. Đối chiếu thứ tự lựa chọn và đoạn ghi đáp án cho 4 câu độc lập Part 5 và 2 câu cùng memo Part 7. Part 6 công khai có 3 câu mỗi đoạn mẫu ở phần đã kiểm tra, pipeline Study yêu cầu 4. | 6 câu vào hàng đợi. [Part 5](https://www.englishclub.com/esl-exams/ets-toeic-practice-5.php) · [Part 6](https://www.englishclub.com/esl-exams/ets-toeic-practice-6.php) · [Part 7](https://www.englishclub.com/esl-exams/ets-toeic-practice-7.php) |
| ETS, IIG Việt Nam và IIBC | PDF ETS 34 trang có 60 khóa tại trang 32. Đối chiếu tập ID khớp 30 câu Listening và 30 câu Reading in trong đề. PDF tải từ IIG giống từng byte. IIBC cung cấp MP3 thật của nhóm 32–34. Nội dung, thứ tự lựa chọn và 3 khóa khớp với PDF ETS. | 60 khóa mẫu tính một lần, 3 khóa IIBC đã nằm trong số đó. Chỉ dùng đối chiếu kỹ thuật cục bộ theo điều kiện của nguồn mẫu. [ETS](https://www.ets.org/pdfs/toeic/toeic-listening-reading-sample-test.pdf) · [IIG](https://www.iigvietnam.edu.vn/vi/bai-thi/bai-thi-toeic) · [IIBC nhóm ETS 32–34](https://www.iibc-global.org/toeic/test/lr/about/format/sample03.html) |
| YBM và ALC | YBM công bố cùng bảng khóa mẫu ETS. Kiểm tra robots trên máy chủ âm thanh YBM dừng trước khi gửi yêu cầu media. Trang ALC công khai có câu hỏi, lựa chọn, khóa và bộ phát theo nhóm. Máy chủ audio ALC trả HTTP 503 cho robots, dừng sau lần thử hữu hạn. | `BLOCKED` cho audio của hai nguồn. 0 câu nhập. [YBM](https://exam.toeic.co.kr/content/TOE/sampleAnswer.php) · [ALC](https://ej.alc.co.jp/tag/TOEIC/20201109-toeic-daily-part3) |

- Corodomo, eng-test, TestTOEIC, 990English và TOEIC Training có luồng làm bài hoặc chấm trên trang. Lượt này chưa lấy được một khóa xuất công khai khớp đề tải được. Trang Part 5 đã xem của TOEIC Training có 40 câu. [Corodomo](https://corodomo.com/toeic) · [eng-test](https://www.eng-test.com/en) · [TestTOEIC](https://testtoeic.com/) · [990English](https://990english.com/) · [TOEIC Training](https://www.toeic-training.com/toeic-test/practice-test-2/?part=5)
- 7ESL trả HTTP 403 ở lượt kiểm tra web. Webloaded mở được trang và câu đầu qua GET công khai, chưa có khóa riêng ổn định. Danh mục IIBC có audio đi kèm sách, chưa tìm thấy cặp đề và khóa công khai đủ bộ. Trang Innova TOEIC chưa truy cập được. [7ESL](https://7esl.com/exams/toeic/) · [Webloaded](https://webloadedsolutions.com/tests/toeic-practice/) · [Sách IIBC](https://www.iibc-global.org/english/publication.html) · [Innova](https://www.innovapress.com/toeic)
- Lượt tải cục bộ ghi 42 yêu cầu với 13.004.161 byte phản hồi, gồm robots, redirect và các lần thử lỗi. HTML, PDF, audio, vị trí bằng chứng và khóa cụ thể lưu trong `.tooling/two-user-study/content-04/`.

### Bằng chứng tệp và audio

| Tệp | Byte | SHA-256 |
|---|---:|---|
| Faust Reading đề | 153720 | `590e4bf41bfbe7522967d6c44586b9c9e6fc8dca012d2e0d6758e63b751e9a5c` |
| Faust Reading khóa công khai | 53633 | `ec16f7ed563127ce1897fa83a20beaa9531443b51a7ccd3d6cea81da8448a817` |
| Faust Listening đề | 124634 | `0b93a5b89645d9d379dd7d448b67dd02f7c09f192a4cb7a17d9181bc44c744d8` |
| Faust Listening lời giải công khai | 52843 | `073bd676d1addaa651709129abdf2adc302e0e6ae8808434479da6762cc24912` |
| Faust Part 1 MP3 | 2588300 | `db70ffa59210a8eb02a549a620cd4580daa83e87b62396092584b358f00277fa` |
| ETS/IIG PDF mẫu | 2461549 | `8f59abfa8f5ef653624cfc7a9810caff2d1d366012179363e4a978caa9d16d4c` |
| IIBC MP3 nhóm ETS 32–34 | 1733821 | `27ca3fe27b781849bac3329274fdbd7725e922abf48175191017f3ba2950c63e` |
| EnglishClub Part 5 HTML | 16419 | `78b76fa4723023dac16ab195b70959dfcdb321ac98defaac22638d1f880112bc` |
| EnglishClub Part 7 HTML | 23681 | `5600ecd32674ed792b983c51d1854d85677bfd60400d2416a7b477081ca31bdf` |

Android 36 giải mã hết hai MP3 bằng `MediaExtractor` và `MediaCodec` tới PCM khác 0. IIBC 72,000 giây, stereo 44.100 Hz, peak 32768. Faust 215,600 giây, mono 24.000 Hz, peak 26773. Đây là kiểm tra tín hiệu giải mã. Chưa kiểm tra đầu ra loa, nghe hiểu hoặc đối chiếu các mốc từng nhóm Faust. Hai MP3 tham chiếu đều giữ ngoài APK.

## Thay đổi triển khai

- `android-app/scripts/prepare_publisher_practice.py` nhận PDF và HTML cục bộ cùng `publisher-files.json` gồm `url`, `bytes`, `sha256` cho từng tên tệp. Dùng PyMuPDF, xác thực revision hai PDF và trích câu theo thứ tự in. Kiểm tra thực tế bắt được watermark lẫn vào câu 105 khi PDF trích theo tọa độ. Đã chuyển sang thứ tự nội dung PDF và đối chiếu cả 5 mục với văn bản gốc.
- `android-app/scripts/review_study_content.py` và `android-app/scripts/study_review_page.py` dùng lại pipeline CONTENT-02. Trang duyệt có bộ lọc chỉ hiện khóa chờ duyệt và điền sẵn nguồn/vị trí. Khóa nguồn đi riêng với quyết định của người duyệt. CLI kiểm tra hash, ID, phiên bản, thứ tự lựa chọn và các trường chứng cứ. Bản ghi lệch khóa công khai giữ trạng thái chưa chấm.
- `android-app/app/src/main/java/vn/toeiclearning/alpha/study/StudyApp.kt` và `StudySession.kt` tách bài theo nhà xuất bản và phiên bản. `android-app/app/build.gradle.kts` chọn gói riêng CONTENT-04 cho variant Study và giữ package ID. `android-app/tests/ingestion/test_publisher_practice.py` bổ sung năm ca synthetic. Đối chiếu kỹ thuật FR-005/006/007/008/015/016/019 và AT-05/06/07/08/15/16/19. [SRS đã ký](STAGE03_SRS_BASELINE_CANDIDATE_V0.6.md) · [Acceptance Catalogue đã ký](STAGE03_ACCEPTANCE_CATALOGUE_CANDIDATE_V0.4.md)

## Kiểm thử và bản bàn giao

| Lệnh hoặc phép kiểm tra | Kết quả |
|---|---|
| `python -B -X utf8 scripts/prepare_publisher_practice.py` và `python -B -X utf8 scripts/review_study_content.py --workspace content-04` | PASS, exit 0. 111 nhóm, 209 câu, 11 khóa nguồn. |
| `python -B -X utf8 -m unittest discover -s tests/ingestion -v` | PASS, exit 0, 65 bài. |
| `python scripts/check_alpha_scope.py`, `python scripts/check_beta_reading_ui_scope.py`, `python scripts/check_cx04_listening_scope.py` | PASS, exit 0 từng lệnh, 10/11/9 mục. |
| `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/run_pure_kotlin_core_checks.ps1` | PASS, exit 0, 25 assertions. |
| `gradlew.bat --offline --no-daemon --console=plain :app:assembleStudy :app:testStudyUnitTest --rerun :app:assembleDebug :app:testDebugUnitTest --rerun :app:assembleLocalPreview :app:testLocalPreviewUnitTest --rerun` | PASS, exit 0. JUnit XML ghi Study 20/20, Debug 20/20, LocalPreview 20/20. |
| Audit PDF, HTML, SHA-256 và đầu ra PCM Android | PASS, exit 0. Đối chiếu được 60 ID mẫu ETS/IIG, 3 câu IIBC và 5 câu Faust. Hai MP3 giải mã đủ. |
| So sáu tài liệu với manifest baseline đã ký | PASS, 6/6 SHA-256. |
| Audit APK Study và Debug | PASS, exit 0. 198 câu cũ giữ nguyên theo ID và nội dung, tất cả hash media trong Study khớp, 0 khóa chấm, 0 form mock. Debug không chứa gói Study. |
| `apksigner verify --verbose --print-certs` và kiểm tra ZIP bàn giao | PASS, exit 0. Debug signature trùng bản Study 0.3.3. APK dùng `vn.toeiclearning.alpha.study`, versionCode 8, min API 26. ZIP có APK, checksum và hướng dẫn hai máy. |
| Chrome mở `review.html` cục bộ | PASS, exit 0. Bộ lọc có 11 câu, riêng Faust có 5, tệp PDF đọc SHA-256 đúng và mở trang giữ trạng thái chờ duyệt. |
| Android Emulator, cài đè từ Study 0.3.3 lên 0.3.4 | PASS, exit 0. Giữ lựa chọn, vị trí câu, đánh dấu và lịch sử sau force-stop. Hai Mock hiển thị khóa. |
| Android Emulator, Reading/Listening Zenlish | PASS, exit 0 từng lượt. Part 7 ảnh đúng thứ tự, phóng ảnh và Back ở 800dp/font 1.5. Part 3 có hình, phát được và dừng khi vào nền ở 360dp, offline. |
| Android Emulator, các bộ Reading mới ở 360dp | PASS, exit 0. Faust Part 5 là bài riêng 5 câu. Trả lời và kết thúc giữ trạng thái chưa chấm, chưa có lời giải. EnglishClub Part 7 có memo, hai câu theo thứ tự và Back trở về đoạn văn. |
| Android Emulator, hai APK fixture synthetic riêng | PASS, exit 0 từng lượt. Câu có khóa fixture đã duyệt được ghi sai và đưa vào ôn lại, hiển thị lời giải. Thu hồi khóa ngừng chấm phiên mới và giữ kết quả cũ trong SQLite. |
| Hai điện thoại thật, kiểm duyệt học thuật và formal QA/ECP | NOT RUN cho hai điện thoại và QA/ECP. BLOCKED cho kiểm duyệt học thuật vì chưa có quyết định của người duyệt. |

APK cục bộ `android-app/.tooling/two-user-study/content-04/TOEIC-Study-0.3.4-debug.apk`. SHA-256 `a3dee60fec64bf6b4458beafd7f83d48ed2d913d61aaf341eec5a8d49a6ad4dd`. Gói Study SHA-256 `d3813c83dd3a4ab3b7c78114783a32e9af66992fa3fa65a88a4e0d3186b5b796`. Gói cài hai máy `TOEIC-Study-hai-may-0.3.4.zip` ở cùng thư mục. Log, JUnit XML build và APK giữ cục bộ. G05-CP01..08 vẫn ACTIVE, ngân sách DEFERRED và Google Play tạm hoãn.

## Việc còn thiếu để bật chấm điểm

Người duyệt mở `android-app/.tooling/two-user-study/content-04/review.html`, lọc câu có khóa nguồn chờ duyệt và đối chiếu nhóm Faust Part 5 trước. Tệp cần chọn đã có trong cùng thư mục gồm `faust-r01-teacher.pdf`, `englishclub-p5.html` và `englishclub-p7.html`. So nội dung với `faust-r01-candidate.pdf` hoặc trang EnglishClub tương ứng. Ghi tên, ngày, quyết định thật rồi xuất JSON. Nhập từ `android-app` bằng `python scripts/review_study_content.py --workspace content-04 --import-review <decisions.json>` với `--evidence <tệp>` cho từng tệp bằng chứng nếu chưa lưu hash. Build Study sau khi báo cáo số `reviewed` thực sự tăng. Khi thiếu chứng cứ lời giải, Study hiển thị “Chưa có lời giải”.

Listening có khóa và audio khớp ở mẫu IIBC dùng để đối chiếu. Kho Study vẫn cần bộ Listening được phép đưa vào gói cục bộ, có rõ ảnh, audio theo nhóm, khóa và người duyệt. Hai bộ Mock cần 400 câu độc lập đã kiểm chứng. Bước tiếp theo về nguồn có thể dùng trọn gói đề, khóa và media từ một bộ workbook do PO có sẵn. Kết quả chấm mẫu synthetic chỉ phản ánh đường đi kỹ thuật của chức năng.
