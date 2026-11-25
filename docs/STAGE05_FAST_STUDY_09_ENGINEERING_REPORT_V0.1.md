# FAST-STUDY-09 · Study 0.3.10

- Reading Part 6–7 lưu vị trí đoạn văn khi đổi chế độ đọc hoặc rời bài bằng Back. Dải chọn câu và dấu đã trả lời luôn hiện trong màn câu hỏi. Xem kết quả và luyện lại quay về màn đã mở bài.
- Listening giữ nút phát trong tầm tay khi cuộn, có nghe lại từ đầu và dừng lượt phát cũ khi nộp. Nhãn giọng đọc tổng hợp và nguồn vẫn hiển thị.
- Gợi ý mở bài theo Part có tỷ lệ đúng thấp hoặc ít câu đã chấm. Tiến độ tách số câu chưa chấm khỏi độ chính xác.
- Giữ 388 câu. Số chấm được giảm 190 → 189, Listening giảm 79 → 78. Tạm ngừng chấm một câu Part 2 vì phản hồi báo hủy chuyến bay cũng phù hợp với yêu cầu chỗ ngồi. Câu và khóa nguồn được giữ riêng.
- Đối chiếu 76/76 câu với phiên bản, kịch bản, khóa, lựa chọn và SHA-256. Xem 8/8 ảnh Part 1, giải mã 44/44 MP3 và sàng lọc phát âm trên sáu clip bằng nhận dạng giọng nói cục bộ. Chất lượng giọng đọc chưa qua đánh giá người nghe độc lập.
- T2 PASS với `assembleStudy` và `testStudyUnitTest --tests *StudyAttemptTest` chạy incremental. JUnit tập trung 13/13 và guard CX-04 9/9.
- Android Emulator API 36 PASS. Cài đè 0.3.9 giữ nguyên phiên, lịch sử và dấu trang trong SQLite. Đã thử cuộn/Back/force-stop, chấm và ôn Reading, phát/nghe lại/nộp offline. Câu chưa chấm tăng số đã trả lời, giữ nguyên số đã chấm và số đúng. MuMu không có thiết bị ADB kết nối.
- Full Mock A/B khóa, 0/200 câu đủ điều kiện mỗi đề. Loopy có hai cặp bài nhưng khóa gắn với chấm sau đăng nhập. Compass có tệp khóa, chưa xác nhận được cả hai đề và media hoàn chỉnh. [Loopy](https://loopyai.app/en/exams) · [Compass](https://www.compasspub.com/eng/compass/level_view.asp?h_seq=2164)
- APK cục bộ ở `android-app/.tooling/two-user-study/fast-study-09/TOEIC-Study-0.3.10-debug.apk`, versionCode 14, cùng package và chứng chỉ với 0.3.9. SHA-256 `5ae3fbdd2f4e61df532aec23e90644a3b77f3a42743176396ebf35fe3e75f346`.
