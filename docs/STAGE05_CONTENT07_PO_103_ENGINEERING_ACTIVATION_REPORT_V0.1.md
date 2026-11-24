# CONTENT-07 · Study 0.3.8 · Báo cáo kích hoạt V0.1

Ngày 24/11/2026. Nhánh `development/two-user-study-mvp`. Quyết định `D05-CONTENT07-PO-103` chấp nhận cả lô. Kỹ thuật đối chiếu từng câu với chứng cứ gốc và nhập 103/103 quyết định vào pipeline hiện có. Tất cả 103 câu vượt qua đối chiếu ID, phiên bản, câu và thứ tự lựa chọn, vị trí khóa gốc, nhóm và media áp dụng. Đợt này không có kiểm duyệt học thuật độc lập từng câu. [Biên bản PO](STAGE05_CONTENT07_PO_BATCH_ACCEPTANCE_103_V0.1.md)

## Số câu trong APK

| Part | Câu khả dụng | Khóa nguồn khớp | Duyệt trước đó | Chấp nhận lô và đối chiếu đạt | Chấm được trong APK |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 5 | 0 | 0 | 0 | 0 |
| 2 | 25 | 0 | 0 | 0 | 0 |
| 3 | 39 | 0 | 0 | 0 | 0 |
| 4 | 33 | 3 | 0 | 3 | 3 |
| 5 | 68 | 39 | 9 | 30 | 39 |
| 6 | 32 | 16 | 0 | 16 | 16 |
| 7 | 110 | 56 | 2 | 54 | 56 |
| **Tổng** | **312** | **114** | **11** | **103** | **114** |

Kiểm tra trực tiếp APK xác nhận nguyên trạng 209 câu và media cũ, gồm 11 câu đã duyệt ở đợt trước và 198 câu Zenlish vẫn chưa chấm. Không có câu bị giữ lại vì sai lệch trong lô mới. Pack gồm 159 nhóm và 0 form mock.

- **TOEIC Question Ocean** có 100 câu Reading theo phong cách TOEIC, bản nguồn `a940bb8b479ef4d06af468015d757041c3d2e457`. Đối chiếu lại năm tệp JS theo SHA-256 đã ghim bằng cách đọc literal, giữ nguyên thứ tự gốc và bản quyền MIT trong APK. [Nguồn tác giả](https://github.com/kdeppaei/toeic-question-ocean/tree/a940bb8b479ef4d06af468015d757041c3d2e457)
- Ocean có khóa gốc phân bố A/B/C/D là 69/20/11/0. App xáo thứ tự hiển thị theo ID phiên đã lưu, phiên bản và ID câu. SQLite lưu chỉ số gốc. Kết quả hiển thị chữ cái tương ứng với thứ tự của phiên đó. Mô phỏng trên 200 ID phiên, mỗi ID gồm 100 câu, cho vị trí khóa A/B/C/D lần lượt 5.106/4.927/4.918/5.049. Đây là kiểm tra phân bố, không phải hiệu chuẩn đề thi.
- **VOA Learning English / Bryan Lynn** xuất hiện dưới nhãn **Luyện nghe bổ sung**. Ba câu thuộc mục Part 4 trong mô hình dữ liệu. Đối chiếu kết quả quiz gốc và audio MP3 `1799169ef33a616cabf30bf83d614039714e738e3aabab20b3363903e07f4d10`. Audio trong APK dài 346,047 giây, 44,1 kHz mono. [Quiz VOA](https://learningenglish.voanews.com/a/6588866.html)

## Kiểm chứng

| Lệnh hoặc kiểm tra | Kết quả |
| --- | --- |
| `review_study_content.py --workspace content-07 --import-review <local-file>`, chạy lại cùng đầu vào | PASS, exit 0 cả hai lượt, SHA pack trùng |
| Rút một quyết định mẫu lô trên bản sao dữ liệu | PASS, exit 0. Chỉ câu đó mất quyền chấm, khóa nguồn vẫn còn |
| `gradlew.bat --offline --console=plain :app:assembleStudy :app:testStudyUnitTest --rerun :app:assembleDebug :app:testDebugUnitTest --rerun :app:assembleLocalPreview :app:testLocalPreviewUnitTest --rerun` | PASS, exit 0. JUnit 25/25 mỗi biến thể, 0 lỗi và 0 bỏ qua |
| `python -B -X utf8 -m unittest discover -s tests/ingestion -v` | PASS, 67/67, exit 0 |
| `check_alpha_scope.py`, `check_beta_reading_ui_scope.py`, `check_cx04_listening_scope.py` | PASS, 10/11/9 kiểm tra, exit 0 mỗi lệnh |
| `run_pure_kotlin_core_checks.ps1` | PASS, 25 kiểm tra, exit 0 |
| SHA-256 của sáu baseline đã ký theo manifest Alpha | PASS, 6/6 |
| `apksigner verify --verbose --print-certs`, `aapt2 dump badging`, kiểm kê APK và ZIP | PASS, exit 0. Cùng chứng chỉ với 0.3.7. APK không khai báo quyền Internet |
| Giải mã MP3 trên Android API 36 bằng `ProbeMedia` | PASS, exit 0. Codec MP3 của Android trả PCM với đỉnh 26.535 |
| Emulator API 36 · cài đè từ 0.3.7 khi offline | PASS, exit 0. Cùng package và chữ ký. Giữ lịch sử có chấm, dấu trang và một phiên Reading đang mở, rồi tiếp tục chấm đúng |
| Emulator API 36 · hạ bản thông thường 0.3.8 → 0.3.7 | PASS theo kỳ vọng. `adb install -r` trả exit 1 với `INSTALL_FAILED_VERSION_DOWNGRADE`. Ứng dụng giữ versionCode 12. Không ép hạ bản |
| Emulator API 36 · Ocean Part 5–7, 360 dp | PASS, exit 0 từng Part. Chấm đúng/sai trên câu thật, kiểm tra chữ cái sau xáo và thứ tự/lựa chọn sau force-stop. Part 5 kiểm tra ôn lại câu sai và lịch sử sau khởi động lại |
| Emulator API 36 · Ocean Part 7 tại 800 dp, cỡ chữ 1,5× | PASS, exit 0. Đọc đoạn văn, chọn phương án và nhận kết quả đúng |
| Emulator API 36 · VOA | PASS, exit 0. Chế độ máy bay, Wi-Fi tắt. Phát MP3 trong app, dừng khi chuyển nền, chấm đúng/sai trên câu thật. Kiểm tra bằng giải mã PCM và thao tác app, chất lượng âm thanh qua loa hai máy chưa được kiểm tra |
| Hai điện thoại thật | NOT RUN. Checklist cài đè và thử riêng cho từng máy nằm trong ZIP |

Lượt Gradle trung gian lỗi một assertion Android mock mới ở biến thể Debug. Lượt build và JUnit cuối trên cây mã nguồn đầy đủ đã qua. Lượt UI Part 7 đầu dừng khi script chưa cuộn lên tới dòng đáp án trong màn kết quả. Lượt chạy lại tìm được dòng đáp án với cùng APK. XML, log lệnh, kiểm kê và chứng cứ cục bộ lưu riêng trong `acceptance-103`.

## Bàn giao riêng

- Package `vn.toeiclearning.alpha.study`, versionName `0.3.8-study`, versionCode `12`. Android 8.0 trở lên.
- Thư mục `android-app/.tooling/two-user-study/content-07/acceptance-103/`.
- Asset dùng cho lần build này nằm ở `android-app/.tooling/two-user-study/content-07/release-assets/`. Lệnh build cần asset cục bộ này để tạo APK chứa lô mới.
- APK `TOEIC-Study-0.3.8-debug.apk`, SHA-256 `1f8205be5cbef84d93995c07bc1bd5fae6c955508cc68410ff77aeb1a8211dc7`.
- ZIP `TOEIC-Study-hai-may-0.3.8.zip`, SHA-256 `716fd51551bda74651f8cd96537783abb7d0b9d1c2d72d15a9bfed59a343ca4f`. Gồm APK, tệp checksum, hướng dẫn cập nhật và checklist hai máy.
- Pack SHA-256 `25069630ba9a8f015b24374536d670248a60635136da86206a1be9f886690e26`.

Full Mock A/B **LOCKED**, mỗi đề có 0/200 câu đủ điều kiện. Stage05 giữ CONDITIONAL PASS, các CP tiếp tục ACTIVE và ngân sách DEFERRED. Kiểm thử thiết bị thật và QA/ECP chính thức ở trạng thái NOT RUN. Google Play tiếp tục tạm hoãn.
