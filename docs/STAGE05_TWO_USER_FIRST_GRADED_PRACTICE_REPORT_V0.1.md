# CONTENT-05 · Báo cáo bộ luyện chấm điểm đầu tiên V0.1

22/11/2026 · `development/two-user-study-mvp` · Study `0.3.5-study` · [Issue #13](https://github.com/hieupham03/TOEIC-Learning-App/issues/13)

**WAITING_FOR_HUMAN_REVIEW.** Cả 11 khóa Reading đã xác định được từ tài liệu nguồn và có sẵn trong trang duyệt. Chưa nhận được quyết định của người kiểm duyệt. APK giữ 209 câu luyện và có 0 câu thật chấm được. Bản 0.3.5 sửa việc bài đang làm có thể giữ khóa đã thu hồi sau cập nhật. Hai thiết bị thật chưa được thử.

## Số câu trong APK cục bộ

| Part | Câu thực | Có khóa nguồn | Người duyệt xác nhận | Chấm được |
|---|---:|---:|---:|---:|
| 1 | 5 | 0 | 0 | 0 |
| 2 | 25 | 0 | 0 | 0 |
| 3 | 39 | 0 | 0 | 0 |
| 4 | 30 | 0 | 0 | 0 |
| 5 | 38 | 9 | 0 | 0 |
| 6 | 16 | 0 | 0 | 0 |
| 7 | 56 | 2 | 0 | 0 |
| **Tổng** | **209** | **11** | **0** | **0** |

Gói có 111 nhóm và trùng SHA-256 của pack 0.3.4. Hàng đợi có 5 câu Faust Part 5, 4 câu EnglishClub Part 5 và 2 câu EnglishClub Part 7 đang `AWAITING_REVIEW`. 198 câu Zenlish vẫn thiếu khóa gốc. Kho luyện tiếp tục tách theo nhà xuất bản và phiên bản. Có **0 bộ 200 câu có đủ khóa, audio và ảnh đã kiểm chứng**. Full Mock A và B vẫn khóa, mỗi đề thiếu 200/200 câu đã kiểm chứng.

## Duyệt 11 đáp án

Mở `android-app/.tooling/two-user-study/content-04/review.html` trong Chrome hoặc Edge. Trang mặc định lọc 11 câu có khóa chờ duyệt. Câu hỏi, thứ tự lựa chọn, khóa công bố, vị trí, URL và SHA-256 đã điền. Khi chọn tệp, trang đối chiếu hash với câu đang xem.

| Tìm theo mã | Đối chiếu trước khi duyệt |
|---|---|
| `faust-r01` | Câu 101–105, trang PDF 2 của `faust-r01-candidate.pdf` và khóa trang PDF 1 của `faust-r01-teacher.pdf`. |
| `englishclub-p5` | Câu, bốn lựa chọn và đoạn đáp án ở Example 1–4 trong `englishclub-p5.html`. |
| `englishclub-p7:memo` | Memo, thứ tự hai câu, bốn lựa chọn mỗi câu và đoạn đáp án trong `englishclub-p7.html`. |

Người duyệt đối chiếu từng câu, nhập tên thật và ngày, chọn trạng thái đã duyệt khi khớp rồi xuất JSON. Giữ tệp trong môi trường cục bộ. Nhập từ `android-app` bằng `python -B -X utf8 scripts/review_study_content.py --workspace content-04 --import-review <decisions.json>`. Thêm `--evidence <tệp>` nếu có tệp bằng chứng mới. CLI kiểm tra lại ID, thứ tự lựa chọn, phiên bản, vị trí và hash trước khi ghi khóa có thể chấm. Sau khi dựng APK từ pack mới, bắt đầu bài mới để áp dụng khóa vừa duyệt. Luồng chấm, kết quả, câu sai và ôn lại trên học liệu thật đang chờ đầu vào này.

## Mẫu ETS và nguồn mới

- **ETS/IIG, `OFFICIAL_SAMPLE`, tham chiếu cục bộ.** Hai PDF giống từng byte, SHA-256 `8f59abfa8f5ef653624cfc7a9810caff2d1d366012179363e4a978caa9d16d4c`. Đối chiếu 60 ID bằng lựa chọn in trong đề hoặc script với nhãn trên trang PDF 32. Số câu Part 1–7 lần lượt là 2/4/12/12/5/4/21. Lưu chỉ mục ID, Part, trang đề/lựa chọn/khóa vào hồ sơ cục bộ, tách khỏi hàng duyệt của các nhà xuất bản độc lập. Điều kiện của ETS cho phép giữ bản nguyên vẹn để tham chiếu cá nhân. Chưa có quyền chuyển nội dung PDF sang APK, nên có 0 câu ETS trong Study. [PDF ETS](https://www.ets.org/pdfs/toeic/toeic-listening-reading-sample-test.pdf) · [IIG](https://www.iigvietnam.edu.vn/vi/bai-thi/bai-thi-toeic) · [Điều kiện ETS](https://www.ets.org/legal/terms.html) · [Điều kiện sao chép TOEIC](https://www.ets.org/legal/permissions/licensing.html)
- **IIBC nhóm 32–34, `OFFICIAL_SAMPLE`, tham chiếu cục bộ.** Ba câu, thứ tự lựa chọn và khóa khớp ETS. Trang gốc gắn đúng một MP3 với nhóm 32–34. Nhóm này không có hình, hình trên cùng trang thuộc nhóm 41–43. Hash MP3 đã kiểm tra lại là `27ca3fe27b781849bac3329274fdbd7725e922abf48175191017f3ba2950c63e`. Android API 36 giải mã hết 72 giây thành PCM stereo 44.100 Hz, peak 32768, exit 0. Nhóm IIBC thuộc cùng mẫu ETS và giữ ngoài APK. [IIBC Part 3](https://www.iibc-global.org/toeic/test/lr/about/format/sample03.html) · [MP3 gốc](https://www.iibc-global.org/hubfs/library/common_migration/orjp/library/toeic_data/toeic/about/tests/media/Part3No32_34.mp3)
- **Hellenic American Union 2018, `PARTIAL`.** PDF 52 trang, 3.277.710 byte, SHA-256 `bfe2665201558f20c288b3ada635ebdfe2fb3cce68c3515255ae69c64e3e34f7`. Xác nhận đề có 200 câu và trang PDF 50 có 200 khóa theo phân bổ 6/25/39/30/30/16/54. Đối chiếu thứ tự A–D của 100 câu Reading. Có sáu ảnh Part 1 và các hình trong Listening. PDF có script, 0 tệp audio đi kèm. Nhà xuất bản hướng dẫn qua ORFEAS có đăng nhập. Chưa tìm thấy MP3 công khai đúng phiên bản hoặc quyền đưa PDF này vào APK. Tạm giữ toàn bộ tài liệu làm tham chiếu. [PDF và khóa](https://siteresources.blob.core.windows.net/siteresourcescontainer/hauportal/media/root/exams/support/individuals/toeic_sample-test-2018_v70_orfeas.pdf#page=50) · [Thông báo HAU](https://www.hau.gr/en-us/exams/announcements/2018/07/ets-has-announced-updates-to-the-toeic-listening-and-reading-as-of-september-2018) · [Tài liệu qua ORFEAS](https://www.hau.gr/en-us/exams/support/language-schools-teachers/exam-preparation-material)
- **Grivas 2019 và Pass the TOEIC Test.** Hai PDF mẫu Grivas mở được, dài 35 và 9 trang, có 0 đề đầy đủ và 0 bảng 200 khóa. Mục bốn CD dẫn đến đăng ký email/PIN. Trang khóa và audio của Pass the TOEIC Test yêu cầu đăng nhập kèm mã sách. Cả hai nguồn có 0 câu và 0 audio đủ điều kiện nhập. [PDF học viên](https://www.grivas.gr/assets/files/toeic2019/TOEIC_2019_NEW_ST.pdf) · [PDF companion](https://www.grivas.gr/assets/files/toeic2019/TOEIC_2019_COMPANION_NEW.pdf) · [Audio Grivas](https://www.grivas.gr/en/free-multimedia-material/toeic-exams-revised-format/) · [Answer key](https://www.pass-the-toeic-test.com/answer-key.php) · [Audio program](https://www.pass-the-toeic-test.com/audio-program.php)

## Thay đổi phần mềm

- `study_review_page.py` dùng lại trang duyệt hiện có, mở bộ lọc hàng có khóa, ghi nhãn nguồn/hash/vị trí và hiện phản hồi khớp tệp cho từng câu. Trạng thái khởi tạo là `SOURCE_ONLY`.
- `StudyModels.kt`, `StudyApp.kt` và `StudyStore.kt` xác thực lại khóa theo gói hiện hành khi tiếp tục bài luyện. Khóa đã thu hồi hoặc thuộc câu đã đổi không thể tạo điểm mới từ snapshot cũ. Lưu thay đổi khóa cùng snapshot trong SQLite, giữ lựa chọn, vị trí và lịch sử đã hoàn thành. Bài đã mất khóa không tự lấy lại khóa khi pack quay về bản cũ.
- `StudySession.kt` hiển thị trạng thái chấm ngay trước câu. `app/build.gradle.kts` nâng Study lên versionCode 9 và giữ package ID `vn.toeiclearning.alpha.study`. `StudyAttemptTest.kt` thêm hai ca hồi quy cho cập nhật, mất bằng chứng và rollback. Đối chiếu kỹ thuật FR-005/006/007/008/015/016/019 và AT-05/06/07/08/15/16/19. [SRS đã ký](STAGE03_SRS_BASELINE_CANDIDATE_V0.6.md) · [Acceptance Catalogue](STAGE03_ACCEPTANCE_CATALOGUE_CANDIDATE_V0.4.md)

## Kiểm thử và bàn giao

| Lệnh hoặc kiểm tra | Kết quả |
|---|---|
| `python -B -X utf8 scripts/review_study_content.py --workspace content-04` | PASS, exit 0. 209 câu, 11 khóa nguồn, 0 đã duyệt. |
| `python -B -X utf8 -m unittest discover -s tests/ingestion -v` | PASS, exit 0, 65/65, gồm sai nhãn, đổi thứ tự lựa chọn, thiếu audio và lệch phiên bản nguồn. |
| `check_alpha_scope.py`, `check_beta_reading_ui_scope.py`, `check_cx04_listening_scope.py` | PASS, exit 0 mỗi lệnh, 10/11/9 mục. |
| `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/run_pure_kotlin_core_checks.ps1` | PASS, exit 0, 25 assertions. |
| `gradlew.bat --offline --no-daemon --console=plain :app:assembleStudy :app:testStudyUnitTest --rerun :app:assembleDebug :app:testDebugUnitTest --rerun :app:assembleLocalPreview :app:testLocalPreviewUnitTest --rerun` | PASS, exit 0. JUnit XML Study 22/22, Debug 22/22 và LocalPreview 22/22. |
| So 6 SHA-256 với manifest baseline đã ký | PASS, 6/6. |
| Trang duyệt Chrome cục bộ | PASS, exit 0. 11 hàng mặc định, 5 hàng Faust, chọn PDF hash khớp, chuyển sang hai hàng EnglishClub Part 7 báo khác tệp. Mở trang không tạo quyết định. |
| Đối chiếu PDF/script ETS và nhóm IIBC | PASS, exit 0. 60/60 mục có dãy lựa chọn khớp loại câu và khóa có trong dãy. 3/3 mục IIBC khớp cả nội dung và khóa. |
| Kiểm tra APK, chữ ký và ZIP | PASS, exit 0. Pack, 209 câu, 11 khóa nguồn và hash media giữ nguyên. APK Study có cùng chứng chỉ debug với 0.3.4, không có mẫu ETS/IIBC hoặc form mock. ZIP kiểm tra giải nén đạt. |
| Emulator API 36, cập nhật 0.3.4 → 0.3.5 | PASS, exit 0. Cài đè giữ bài đang làm, lựa chọn, dấu trang và lịch sử. Khôi phục sau force-stop. A/B đều hiển thị khóa. |
| Emulator API 36, APK Study với 209 câu | PASS, exit 0 từng lượt. Faust và EnglishClub có bài riêng, câu có khóa nguồn vẫn chưa chấm. Memo EnglishClub và Back đạt ở 360dp. Ảnh Zenlish Part 7 đúng thứ tự, phóng ảnh và Back đạt ở 800dp/font 1.5. Part 3 có hình, phát và dừng khi app xuống nền ở 360dp và chế độ máy bay. |
| Emulator API 36, hồi quy thu hồi và rollback với fixture synthetic | PASS, exit 0 từng lượt. Bài đã hoàn thành giữ điểm sai, lời giải và mục ôn. Sau khi thu hồi, bài đang làm giữ lựa chọn qua force-stop và khóa rút khỏi snapshot SQLite. Đổi lại pack trước vẫn không chấm bài đó. Bài mới với khóa fixture hợp lệ chấm đúng. |
| Hai điện thoại thật và QA/ECP chính thức | NOT RUN. Bản cập nhật và checklist đã chuẩn bị để thử nội bộ. |

APK cục bộ `android-app/.tooling/two-user-study/content-05/TOEIC-Study-0.3.5-debug.apk`. SHA-256 `809a42110b89270f87b5d08d10bd5b6c138bb162ff58aadf04b65490b8dbc971`. SHA-256 pack `d3813c83dd3a4ab3b7c78114783a32e9af66992fa3fa65a88a4e0d3186b5b796`.

Gói `TOEIC-Study-hai-may-0.3.5.zip` ở cùng thư mục chứa APK, checksum, hướng dẫn duyệt và checklist khoảng 15 phút mỗi máy. Toàn bộ tệp gốc, dữ liệu quyết định, ảnh, log và APK giữ cục bộ. Google Play tạm hoãn. G05-CP01..08 vẫn ACTIVE, ngân sách DEFERRED.
