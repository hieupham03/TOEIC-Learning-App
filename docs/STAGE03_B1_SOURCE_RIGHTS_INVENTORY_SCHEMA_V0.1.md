# B1 — Mẫu kiểm kê nguồn và quyền học liệu (V0.1)

**Tình trạng:** TEMPLATE ONLY, ZERO SOURCE RECORDS VERIFIED. **Không yêu cầu upload ngay.** Không tự đưa tài liệu vào cloud khi quyền chưa rõ.

## 1. Kiểm kê ở mức bộ nguồn (mỗi hàng một nguồn)
| source_id | Tên bộ tài liệu / tổ chức | Owner / tác giả | Nguồn nhận/mua | Có bao nhiêu đề/Part | Audio? | Answer key? | Images? | Quyền số hóa | Quyền app/cloud | Quyền 2–5 học viên | Quyền thương mại/công khai | Bằng chứng/điều khoản | Hết hạn / lãnh thổ | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TBD | (chưa khai báo) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | NONE | UNKNOWN | NOT VERIFIED |

## 2. Kiểm kê từng asset khi chuẩn bị mock (mỗi hàng một asset)
| asset_id | source_id | form(A/B/practice) | part | item_or_group_id | asset_type(question/audio/image/passage/transcript/answer/explanation) | created_by | owner | license_scope | rights_proof_uri_or_record | file_hash | QA_status | release_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TBD | TBD | UNASSIGNED | TBD | TBD | TBD | UNKNOWN | UNKNOWN | UNKNOWN | NONE | NONE | NOT RUN | HOLD |

## 3. Các câu hỏi quyền tối thiểu
1. Ai sở hữu quyền đối với **từng loại asset**, kể cả giọng nói và hình ảnh trong câu?
2. Quyền chỉ học cá nhân hay có **quyền tạo bản sao số / upload lên máy chủ / phát qua app / cho người khác truy cập**?
3. Có cho phép **chỉnh sửa, cắt audio, OCR, biên soạn lời giải, tạo bản dịch**?
4. Phạm vi **thương mại, Việt Nam, nhóm thử nghiệm và thời hạn giấy phép**?
5. Có yêu cầu ghi công, giới hạn số lượt truy cập, DRM, báo cáo sử dụng, thu hồi khi hết hạn?
6. Có bị giới hạn sử dụng để **huấn luyện AI / xử lý bởi bên thứ ba** nếu sau này tính năng đó được đề xuất?

## 4. Quy tắc duyệt nguồn
- `ORIGINAL VERIFIED`: biên soạn gốc, lưu xác nhận tác giả và nguồn của audio/hình, kiểm tra không sao chép đề có bản quyền.
- `LICENSED VERIFIED`: văn bản cho phép đúng loại sử dụng và asset; trả phí không đồng nghĩa có quyền khác với hợp đồng.
- `OPEN LICENSE VERIFIED`: giấy phép được xác thực cho **từng asset**, tuân thủ ghi công và điều kiện NC/SA nếu có; không suy đoán nội dung tìm thấy trên mạng là CC.
- `PERSONAL-OWNED UNKNOWN`: sách/PDF/audio user sở hữu nhưng chưa có quyền cho app/cloud/sharing — **không đưa vào bank chia sẻ**.
- `UNKNOWN/RESTRICTED`: không dùng trong pilot/đăng tải; không làm biến mất bản ghi để né kiểm tra.

## 5. Những gì thực sự đã có
Product Owner báo cáo đang sở hữu tài liệu đủ Listening/Reading cho baseline trên laptop. **Chưa có file mẫu, danh mục thực, giấy phép hay bất kỳ kiểm định trong dự án này.** Điều này không phủ định giá trị của tài liệu đối với việc học cá nhân.
