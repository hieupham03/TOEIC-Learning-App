# STUDY-DELIVERY-01 · Lô Reading và Listening chờ duyệt

24/11/2026 · `development/two-user-study-mvp` · [Issue #14](https://github.com/hieupham03/TOEIC-Learning-App/issues/14)

**READY_FOR_PO_REVIEW.** Đã lấy và đối chiếu 100 câu Reading mới, giữ ba câu VOA có khóa và audio từ CONTENT-06. Cả 103 câu có khóa nguồn khớp và đang chờ người duyệt xác nhận. Có 0 câu mới đã duyệt. APK đang bàn giao giữ **209 câu, 11 câu chấm được**.

| Part | Câu trong APK 0.3.7 | Có khóa nguồn và chấm được trong APK | Khóa nguồn bổ sung chờ duyệt |
|---|---:|---:|---:|
| 1 | 5 | 0 | 0 |
| 2 | 25 | 0 | 0 |
| 3 | 39 | 0 | 0 |
| 4 | 30 | 0 | 3 |
| 5 | 38 | 9 | 30 |
| 6 | 16 | 0 | 16 |
| 7 | 56 | 2 | 54 |
| **Tổng** | **209** | **11** | **103** |

Gói duyệt cục bộ có 312 câu, 114 khóa nguồn và 11 quyết định duyệt cũ. Mọi bản ghi trong 209 câu cũ giữ nguyên khi dựng gói duyệt. Full Mock A/B vẫn khóa, mỗi đề có 0/200 câu đủ điều kiện. Google Play tạm hoãn.

## Đối chiếu nguồn

- **HAU 2018.** Kiểm tra lại PDF thật 52 trang, SHA-256 `bfe2665201558f20c288b3ada635ebdfe2fb3cce68c3515255ae69c64e3e34f7`. Trang PDF 50 có đủ 200 cặp số câu và khóa, gồm Q101–200 Reading. PDF không chứa tệp audio. Chưa xác lập được phạm vi sử dụng cho APK, nên giữ ở mức tham chiếu và đưa 0 câu HAU vào gói duyệt. [PDF và khóa HAU](https://siteresources.blob.core.windows.net/siteresourcescontainer/hauportal/media/root/exams/support/individuals/toeic_sample-test-2018_v70_orfeas.pdf#page=50) · [Hướng dẫn nguồn](https://www.hau.gr/en-us/exams/announcements/2018/07/ets-has-announced-updates-to-the-toeic-listening-and-reading-as-of-september-2018)
- **TOEIC Question Ocean.** Lấy năm tệp ngân hàng và giấy phép gốc từ commit `a940bb8b479ef4d06af468015d757041c3d2e457`. Tác giả phát hành các bài mô phỏng Reading tự biên soạn theo MIT. Lô chọn gồm 30 câu Part 5, 16 câu Part 6 và 54 câu Part 7. Giữ ID, nhóm, đoạn văn, thứ tự bốn lựa chọn và khóa đã công bố. Mỗi dòng lưu vị trí trong tệp gốc, hash nguồn và hash câu. Giấy phép và ghi công có trong gói duyệt cục bộ. Đây là lô luyện từ một ngân hàng mô phỏng độc lập. [Phiên bản nguồn](https://github.com/kdeppaei/toeic-question-ocean/tree/a940bb8b479ef4d06af468015d757041c3d2e457) · [Giấy phép MIT](https://github.com/kdeppaei/toeic-question-ocean/blob/a940bb8b479ef4d06af468015d757041c3d2e457/LICENSE)
- **Thứ tự đáp án Reading.** Khóa theo thứ tự gốc phân bố A=69, B=20, C=11, D=0. Trang của tác giả có cơ chế xáo lựa chọn lúc luyện. Gói chờ duyệt giữ thứ tự gốc để so khớp chính xác. Phân bố này cần được lưu ý trước khi dùng lô mới để chấm. [Mã xáo lựa chọn của nguồn](https://github.com/kdeppaei/toeic-question-ocean/blob/a940bb8b479ef4d06af468015d757041c3d2e457/app.js#L2494)
- **VOA Learning English / Bryan Lynn.** Kiểm tra lại cả ba câu chờ duyệt có đúng thứ tự A–D cùng một clip gốc được dẫn từ quiz 6588866. MP3 SHA-256 `1799169ef33a616cabf30bf83d614039714e738e3aabab20b3363903e07f4d10`. Android giải mã đủ 346,047 giây thành PCM khác 0. Ghi đây là luyện nghe bổ sung. Giữ ảnh AP ngoài gói. [Bài VOA](https://learningenglish.voanews.com/a/free-google-ai-tool-aims-to-improve-job-interview-skills/6588892.html) · [Quiz](https://learningenglish.voanews.com/a/6588866.html) · [Phạm vi sử dụng](https://learningenglish.voanews.com/p/6861.html)

Các phương án QuAIL, WCE và Bow Valley được kiểm tra hữu hạn, giữ ở mức tham chiếu vì khác mục đích hoặc cấu trúc câu. Hồ sơ nguồn và SHA nằm trong `android-app/.tooling/two-user-study/content-07/source-discovery/`.

## Duyệt lô bằng trang hiện có

Mở `android-app/.tooling/two-user-study/content-07/review.html`, sau đó lọc theo Part. Trang tự hiện 103 câu đang chờ duyệt. `HUONG_DAN_DUYET_LO.md` trong cùng thư mục ghi tệp cần đối chiếu, cách thấy đúng ID/dòng và cách xuất JSON. **Đầu vào để tăng số câu chấm được là quyết định thật của người duyệt cho các ID và phiên bản đã xem.**

Hai adapter chỉ làm nhiệm vụ đọc dữ liệu nguồn. `extract_ocean_literals.cjs` dùng Acorn để đọc literal và số dòng. `prepare_ocean_reading.py` xác thực SHA-256 của tệp gốc, ghép khóa và gọi pipeline nhập/duyệt hiện có. Phần ứng viên ở workspace `content-07`. Gradle Study mặc định tiếp tục dùng ngân hàng đã bàn giao. Gói duyệt đã đối chiếu có SHA-256 `bdb34c285ac3f33fd0dce3054410677b4169e523cb006b736728445293cef32a`.

## Kiểm thử và gói cài

| Kiểm tra | Kết quả |
|---|---|
| `prepare_ocean_reading.py`, audit pack và tệp chứng cứ | PASS, exit 0. 100 Reading và 3 VOA có khóa nguồn, 0 câu mới có khóa chấm. Đối chiếu chứng cứ theo hash cho cả 103 bản ghi. |
| Chrome offline | PASS, exit 0. Lọc đúng 30/16/54 câu Reading và mở được cả ba dòng VOA với audio khớp hash. |
| Gradle offline | PASS, exit 0. Chạy JUnit Study, Debug, LocalPreview **23/23 mỗi variant**, và assemble Debug/LocalPreview. |
| Ingestion và guards | PASS, exit 0. Ingestion **67/67**, Alpha/Beta/CX-04 **10/11/9**, Kotlin smoke **25 assertions**. |
| Emulator API 36, cài đè 0.3.6 → 0.3.7 | PASS, exit 0. Giữ điểm đã chấm, dấu trang, phiên memo và lựa chọn SQLite. Chấm lại và luyện câu sai còn đúng sau force-stop. Cả hai Mock vẫn khóa. |
| Emulator API 36, phát âm thanh trong APK offline | PASS, exit 0. Part 3 Zenlish phát trong chế độ máy bay, dừng khi app xuống nền. Lựa chọn giữ nguyên sau force-stop. |
| VOA trên Android API 36 | PASS, exit 0. Giải mã MP3 gốc hoàn tất. |
| APK, chữ ký và ZIP | PASS, exit 0. APK 0.3.7 có đúng SHA và chứng chỉ debug tương thích 0.3.6. ZIP chứa đúng APK, checksum và checklist. |
| Hai điện thoại thật và QA/ECP chính thức | NOT RUN. |

Issue #14 chỉ phát hành APK mới khi có câu đã duyệt mới hoặc sửa lỗi UX cản trở việc học. Lượt này đóng gói lại APK **0.3.7** cùng checklist hai máy. Chưa có APK tăng số câu chấm. Dữ liệu nguồn và quyết định dùng nội bộ, không lên GitHub Public.

- APK `android-app/.tooling/two-user-study/content-07/TOEIC-Study-0.3.7-debug.apk` có SHA-256 `1cc7d3ef5056d97f54ae29de09208066b231549ab832c30b093a0aac8d38e587`.
- ZIP `TOEIC-Study-hai-may-0.3.7.zip` trong cùng thư mục có SHA-256 `82316cf70aaedba3edd2c1d9ae7827f2f8ffb1f963adab284acd46fff73d9627`.
