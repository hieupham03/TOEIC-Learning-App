# D05-CONTENT05-PO-11 · Báo cáo kích hoạt chấm điểm V0.1

24/11/2026 · `development/two-user-study-mvp` · Study `0.3.6-study` · [Issue #13](https://github.com/hieupham03/TOEIC-Learning-App/issues/13)

**Đã kích hoạt 11/11 câu Reading trong APK Study.** Bản cài có 209 câu, 11 câu có khóa nguồn đã được PO duyệt và 198 câu Zenlish tiếp tục chưa chấm. Hai điện thoại thật chưa được thử.

## Quyết định và đối chiếu chứng cứ

Chuyển đúng một quyết định PO thành 11 bản ghi cục bộ `APPROVED`. Reviewer là vai trò Product Owner theo lời xác nhận ngày 22/11/2026, với mã quyết định `D05-CONTENT05-PO-11` trong metadata cục bộ. Không phát sinh lời giải hoặc nhận định kiểm duyệt khác. [Biên bản phê duyệt](STAGE05_CONTENT05_PO_REVIEW_APPROVAL_11_V0.1.md)

Kiểm tra lại PDF đề và đáp án Faust cùng revision, hai trang HTML EnglishClub và hash tệp trong kho chứng cứ. So từng khóa và vị trí với bản ghi nguồn đã lưu, cùng ID nhóm/câu, thứ tự A–D, hash phiên bản, nội dung câu và memo trong pack 0.3.5. Có **11 khớp, 0 lỗi**. CLI `review_study_content.py` nhập các bản ghi qua bộ kiểm tra hash và ràng buộc nguồn hiện có.

| Bộ luyện | Có khóa nguồn | PO duyệt và import | Chấm được trong APK |
|---|---:|---:|---:|
| Faust Reading 01, Part 5 | 5 | 5 | 5 |
| EnglishClub Part 5 | 4 | 4 | 4 |
| EnglishClub Part 7 | 2 | 2 | 2 |
| Zenlish Part 1–7 | 0 | 0 | 0 |
| **Tổng** | **11** | **11** | **11** |

So với APK 0.3.5, phần dữ liệu pack chỉ thêm khóa đã duyệt vào đúng 11 câu. 111 nhóm, 209 câu, media và 198 câu không có khóa giữ nguyên. Dữ liệu Study không có form mock. A và B mỗi đề còn thiếu 200/200 câu đã kiểm chứng. Google Play tiếp tục tạm hoãn.

## Build và kiểm thử

| Lệnh hoặc kiểm tra | Kết quả |
|---|---|
| Đối chiếu cục bộ và `python -B -X utf8 scripts/review_study_content.py --workspace content-04 --import-review <decisions.json>` | PASS, exit 0. 11 bản ghi được nhập, 0 bị chặn. |
| `python -B -X utf8 -m unittest discover -s tests/ingestion -v` | PASS, exit 0, 65/65. |
| `check_alpha_scope.py`, `check_beta_reading_ui_scope.py`, `check_cx04_listening_scope.py` | PASS, exit 0 mỗi lệnh, 10/11/9 mục. |
| `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/run_pure_kotlin_core_checks.ps1` | PASS, exit 0, 25 assertions. |
| `gradlew.bat --offline --no-daemon --console=plain :app:assembleStudy :app:testStudyUnitTest --rerun :app:assembleDebug :app:testDebugUnitTest --rerun :app:assembleLocalPreview :app:testLocalPreviewUnitTest --rerun` | PASS, exit 0. JUnit XML ghi Study 22/22, Debug 22/22, LocalPreview 22/22. |
| Audit APK, chứng chỉ và ZIP hai máy | PASS, exit 0. APK có chính xác 11 khóa mục tiêu, 198 câu cũ và media nguyên vẹn. Chứng chỉ debug trùng 0.3.5. ZIP chứa đúng APK, checksum và checklist, với hash APK khớp sau giải nén. |
| Bảo toàn baseline đã ký | PASS, 6/6 SHA-256 khớp manifest. Đối chiếu kỹ thuật FR-005/006/007/008/015/016/019 và AT-05/06/07/08/15/16/19. |
| Emulator API 36, `adb install -r` từ 0.3.5 lên 0.3.6 | PASS, exit 0. Giữ vị trí, lựa chọn, dấu trang và lịch sử sau force-stop. Bài Faust đã nộp ở 0.3.5 vẫn có kết quả chưa chấm. Bài Zenlish đang làm tiếp tục được. Home ghi 9 câu Part 5 và 2 câu Part 7 đã duyệt. A/B vẫn khóa. |
| Emulator API 36, chấm 11 câu thật ở chế độ máy bay | PASS, exit 0. Lựa chọn thử bám khóa nguồn và cố ý có câu sai. Faust 3 đúng/2 sai, EnglishClub Part 5 đạt 2 đúng/2 sai, EnglishClub Part 7 đạt 1 đúng/1 sai. Tổng 6 đúng/5 sai, 0 chưa chấm. Hiện đáp án đã xác minh và “Chưa có lời giải”. |
| Emulator API 36, câu sai, luyện lại và SQLite | PASS trong lượt chấm thực tế. Câu sai có nút luyện lại. Lựa chọn ở bài ôn còn sau force-stop. Nộp lại đúng đưa câu ra khỏi nhóm câu sai, giữ lần làm trước trong lịch sử và lưu số liệu đúng/sai theo Part. |
| Hai điện thoại thật và QA/ECP chính thức | NOT RUN. |

Nguồn thay đổi trong Git là `android-app/app/build.gradle.kts` để nâng Study lên versionCode 10, giữ package ID `vn.toeiclearning.alpha.study`, và báo cáo này. G05-CP01..08 vẫn ACTIVE, ngân sách DEFERRED. Bản ghi PO, PDF/HTML gốc, khóa nguồn, APK và log kiểm thử lưu cục bộ.

## Gói cài hai điện thoại

- Thư mục `android-app/.tooling/two-user-study/content-05-po-11/`.
- APK `TOEIC-Study-0.3.6-debug.apk` có SHA-256 `588898e0298c4578220d387e60deb1e4bf0922c2b9d83697beab8694b6621179`. Min SDK 26, có thư viện cho arm64-v8a, armeabi-v7a, x86 và x86_64.
- Pack SHA-256 `094e217db5dba1c4d7044828c961fae88e22df768466c71901430b27dcc5546e`.
- ZIP `TOEIC-Study-hai-may-0.3.6.zip` có SHA-256 `ca2ed2dce102f5cdde9b184aa0cbee26d13737eaa79533a8549d87c6dd97bd38`. Checklist khoảng 15 phút mỗi máy gồm cài đè, chấm offline, luyện lại câu sai, khôi phục và xác nhận hai Mock vẫn khóa.
