# TOEIC Learning Demo 0.2.1 — Cài và thử trên hai điện thoại

Mốc P0 là 24/11/2026. Dùng APK synthetic trong gói bàn giao cho hai lượt thử nội bộ có đồng thuận. Mỗi người thử ghi riêng một kết quả với mã **Máy A** hoặc **Máy B**. Listening Part 1–4 sử dụng âm thử nghiệm. Reading Part 5–7 sử dụng câu hỏi và giải thích mẫu. Lựa chọn giữ trong bộ nhớ của phiên.

## Cài APK

1. Giải nén gói vào một thư mục cục bộ. Kiểm tra SHA-256 của `TOEIC-P0-0.2.1.apk` với tệp `TOEIC-P0-0.2.1.apk.sha256`. Trên Windows dùng `Get-FileHash -Algorithm SHA256 .\TOEIC-P0-0.2.1.apk`.
2. Trên thiết bị đã đồng ý thử và cho phép USB debugging, kết nối bằng cáp và chấp nhận xác nhận máy tính trên điện thoại. Dùng Android Platform Tools.

   ```powershell
   adb devices -l
   adb -s SERIAL install -r .\TOEIC-P0-0.2.1.apk
   ```

3. Thay `SERIAL` bằng đúng thiết bị đang thử. Android tối thiểu 8.0 (API 26). Nếu cài không được vì chữ ký bản đã có hoặc chính sách thiết bị, ghi lỗi và dừng trên máy đó để giữ dữ liệu hiện hữu.
4. Mở **TOEIC Learning Demo**. Bản trong gói có package `vn.toeiclearning.alpha`, versionCode 3, versionName `0.2.1-preview`.

## Checklist 10 phút trên mỗi máy

| Bước | Kết quả mong đợi |
|---|---|
| Cài và mở app. Tắt Wi-Fi và dữ liệu di động rồi mở lại. | Trang bắt đầu hiện đầy đủ và mở được cả Reading lẫn Listening DEMO. |
| Vào Listening Part 1. Phát, tạm dừng, tiếp tục, để hết rồi phát lại. | Nghe được tone ổn định và trạng thái trên màn hình khớp thao tác. |
| Trong lúc phát, đưa app xuống nền hoặc dùng Back. Mở lại và thử một Part khác. | Audio cũ dừng. Âm của Part mới phát theo thao tác của người dùng. |
| Chọn một đáp án Listening và chuyển sang Part khác rồi quay lại trong cùng phiên. | Đáp án vừa chọn vẫn hiện. Không xuất hiện chấm đúng/sai. |
| Vào Reading Part 5, chọn một đáp án và mở giải thích mẫu. Sang câu kế, rồi quay về câu trước. | Lựa chọn và giải thích mẫu vẫn hiện ở câu đã làm. |
| Vào Reading Part 7, cuộn đoạn, sang câu hỏi, chọn đáp án và dùng Back. | Quay lại đoạn ở vùng vừa đọc. Câu đã chọn vẫn có trong phiên. |
| Tăng cỡ chữ hệ thống, thử lại một màn hình Listening và một màn hình Reading. | Đọc và cuộn tới được câu hỏi, lựa chọn và nút điều hướng. |
| Vào Tiến độ, mở Xóa lựa chọn tạm, thử Hủy rồi xác nhận. | Hủy giữ lựa chọn. Xác nhận đưa cả hai bộ đếm về 0. |
| Mở điều kiện Full Mock. | Hiện trạng thái khóa và không bắt đầu bài thi. |

Mỗi máy ghi trạng thái `PASS`, `FAIL`, `BLOCKED` hoặc `NOT RUN` cho từng bước. Ghi lỗi treo/crash, mất lựa chọn trong phiên, sai âm, hoặc nút không thao tác được ngay khi thấy. Có thể dùng [mẫu phiếu dưới đây](#phiếu-ghi-nhận).

## Phiếu ghi nhận

```text
Máy (A/B) và mã lỗi:
Model máy, Android, bản app:
Ngày thử, đồng thuận thử nội bộ (có/chưa):
Bước checklist và trạng thái:
Cách tái hiện (1, 2, 3):
Kết quả mong đợi:
Kết quả thực tế và thông báo:
Số lần gặp / số lần thử:
Điều kiện (offline/online, font mặc định/lớn, loa/tai nghe):
```

Giữ phiếu và ảnh đính kèm ở nơi trao đổi nội bộ của nhóm thử. Dùng mã Máy A/B trên báo cáo tổng hợp.
