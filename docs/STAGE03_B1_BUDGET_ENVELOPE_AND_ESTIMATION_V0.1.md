# B1 — Budget Envelope & Cost Evidence Plan V0.1

**Status:** ANALYST COST MODEL, NO APPROVED BUDGET, NO VENDOR SELECTED, NO PURCHASE. **Currency:** VND for PO decisions; public list prices may be USD.

## 1. Budget buckets — không bỏ qua giờ công
| Bucket | Công thức/đơn vị | Trạng thái bằng chứng | Điều kiện/owner |
|---|---|---|---|
| LIC | Phí nội dung/giấy phép, hiệu lực, số user, lãnh thổ | Không có báo giá hợp đồng cho 2 full mocks | PO chấp thuận trước mua |
| AUTHOR | Số câu gốc × giờ/câu × chi phí giờ hoặc giờ tình nguyện | Chưa có dữ liệu năng suất nội bộ | Ước lượng theo mẫu khi sẵn có |
| QA | 400 câu + bank luyện Part, media hours, số vòng review | Chưa có log QA thực | Phải tính reviewer độc lập hoặc rủi ro thiếu reviewer |
| AUDIO | Kịch bản/hội thoại, TTS/recording, quality/editing | Chưa có tổng ký tự/giờ audio | Bảng giá chỉ là tiền TTS, không gồm QC |
| IMAGE | Ảnh gốc/cấp phép và đồ họa | Chưa có inventory | Rà soát quyền riêng cho ảnh |
| CLOUD | Storage, DB, network, media streams, logs, backup, domain | Free tiers tồn tại nhưng chưa có usage/stack | Không tự chọn backend hoặc cam kết 0 đồng |
| QA-DEVICE | Android long-form, crash/data loss, thiết bị thật, người test | User từng gặp Reading dài/mỏi mắt | Lập acceptance và ước lượng giờ công |
| RELEASE | Google Play account/testing nếu dùng Play | Chính sách/bảng phí có thể kiểm tra | Tách khỏi 4-week OPEX |
| CONT | Dự phòng nội dung lỗi, phát sinh vượt free tier/rights | Chưa xác định tỷ lệ | PO phê duyệt khi có estimate |

## 2. Minh họa độ nhạy (KHÔNG là forecast)
- Hai full mock = **400 items**; nếu giả định mỗi item cần [15, 45] phút biên soạn + rà soát trực tiếp thì tổng **100–300 giờ**, CHƯA tính các clip audio/bài đọc dài/ảnh, vòng kiểm tra độc lập và bank luyện Part. Đơn giá và tốc độ thực tế chưa xác minh.
- Giả định **5 học viên × 5 phiên/tuần × 4 tuần × 15 MB/phiên = 1.5 GB** tải audio trong bốn tuần, chỉ để định cỡ sơ bộ; chưa tính API, DB, logging, backup.
- Các nhà cung cấp có free quotas riêng: Firebase (Spark/Blaze theo dịch vụ) và Cloudflare R2 Standard có 10 GB-month Standard free; không suy ra tổng chi phí vận hành là 0. Các tên dịch vụ chỉ để tham chiếu ngân sách, **không phải quyết định công nghệ**.

## 3. Những cap PHẢI do Product Owner quyết định trước khi khóa MVP / chi tiền
- `CAP_CONTENT_LICENSE_ONETIME_VND = TBD`
- `CAP_CONTENT_PRODUCTION_QA_VND_OR_HOURS = TBD`
- `CAP_PILOT_OPEX_4W_VND = TBD`
- `CAP_CONTINGENCY_VND_OR_PERCENT = TBD`
- `PURCHASE_APPROVAL_RULE = EACH PAID COMMITMENT REQUIRES EXPLICIT PO APPROVAL`

## 4. Điều kiện đủ để đề xuất signoff ngân sách
1. Có ít nhất một đường cung cấp toàn bộ nội dung B1 với quyền hợp lệ và khối lượng công việc/báo giá kiểm tra được (tự biên soạn hoặc đối tác).
2. Có danh sách asset và khối lượng practice bank tách khỏi mock; số giờ QA âm thanh/ảnh và thời gian review ghi riêng.
3. Có giả định phiên học + audio/DB/backup theo 2–5 người, 4 tuần, có sensitivity 2× và giới hạn cảnh báo chi phí khi đến giai đoạn công nghệ.
4. Có lựa chọn nếu estimate vượt trần: **trình PO quyết định lại, không tự giảm mock từ 2 xuống 1**.

## 5. Public references checked 2026-11-21
- Firebase pricing: https://firebase.google.com/pricing
- Cloudflare R2 pricing: https://developers.cloudflare.com/r2/pricing/
- ETS licensing: https://www.ets.org/legal/permissions/licensing.html
- Google Play IP and app policies: https://support.google.com/googleplay/android-developer/answer/18265346

**No code, no server/vendor choice, no payment performed.**
