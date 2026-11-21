# Mẫu Inventory/Quyền học liệu V0.1 — Chưa điền dữ liệu thật

**Chỉ dành cho rà soát nguồn và rights; không mặc định user đã cho phép tải tài liệu hoặc xử lý lên server.**

## A. Bảng nguồn — trạng thái hiện tại
| Source-ID | Loại nguồn | Số lượng/item | Chủ sở hữu | Bằng chứng quyền | Cá nhân local | Đưa lên cloud | Chia sẻ 2–5 người | Public/commercial | AI processing | Kết luận |
|---|---|---|---|---|---|---|---|---|---|---|
| SRC-OWN-01 | PDF/sách/audio PO sở hữu bản sao | UNKNOWN | UNKNOWN | Chưa có | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | **NOT CLEARED** |
| SRC-ORIG-01 | Câu hỏi/audio tự tạo gốc | 0 **được chứng minh** | Tác giả chưa xác định | Chưa có | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | **NOT CLEARED** |
| SRC-LIC-01 | Học liệu giấy phép mua/được cấp | 0 **được chứng minh** | UNKNOWN | Chưa có hợp đồng | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | **NOT CLEARED** |
| SRC-ETS-01 | ETS sample/official materials | Chưa xác minh | ETS | Chính sách ETS yêu cầu quyền | RESTRICTED | RESTRICTED | RESTRICTED | RESTRICTED | UNKNOWN | **NOT CLEARED** |
| SRC-CC-01 | CC / public domain khi có | 0 **được chứng minh** | Theo từng nguồn | Chưa có URL license | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | **NOT CLEARED** |

**Lưu ý:** `0 được chứng minh` chỉ nghĩa là **chưa có bằng chứng trong hồ sơ**, KHÔNG có nghĩa người dùng không sở hữu tài liệu hoặc không có nguồn hợp lệ. `UNKNOWN` tuyệt đối không được chuyển thành `AUTHORIZED` dựa trên việc file có sẵn.

## B. Trường phải điền khi kiểm kê
- ID nguồn, tác giả/chủ quyền, URL/mã hóa đơn/hợp đồng, phiên bản & ngày kiểm tra.
- Đối tượng: PDF text/scan, ảnh, audio, transcripts, đáp án, lời giải, câu hỏi, trích đoạn.
- Ngữ cảnh: đọc riêng, sao lưu nội bộ, đưa lên cloud, chia sẻ trong pilot gia đình, công bố Play Store, thương mại, biến đổi, dùng AI bên thứ ba.
- License: giới hạn người dùng/thiết bị, vùng địa lý, thời hạn, cho phép chuyển định dạng hay trích xuất, yêu cầu ghi công, quyền thu hồi.
- Chất lượng: đủ 7 Part? số form? audio ↔ question/group ↔ answer? file lỗi? độ chính xác? người kiểm tra?
- Kết quả: `AUTHORIZED` / `RESTRICTED` / `UNKNOWN` / `REJECTED`, tài liệu bằng chứng và ngày ký.

## C. Decision rule
Bất kỳ mục nào thiếu quyền cần thiết hoặc mất trace → **không đưa vào app pilot/public trong ngữ cảnh tương ứng**. Với từng nguồn, chỉ một phần các quyền có thể được cấp — không dùng một ô `có giấy phép` để suy ra tất cả.
