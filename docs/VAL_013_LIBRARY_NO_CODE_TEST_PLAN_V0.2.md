# VAL-013 — KIỂM CHỨNG GIÁ TRỊ CỦA QUY TRÌNH LUYỆN ĐỀ TOEIC TÍCH HỢP (KHÔNG CODE)

**Phiên bản:** V0.2 (revised after VAL-013; chưa thực hiện)  
**Ngày:** 2026-11-20  
**Giai đoạn:** 02/11 — Market Research & Validation  
**Giả thuyết:** H-003-VALUE — trải nghiệm luyện đề thống nhất làm giảm ma sát của kho PDF/sách/audio cá nhân  
**Phê duyệt:** Proposal only; chưa duyệt ngưỡng nghiệm thu, không phát triển ứng dụng.

## 1. Vấn đề và câu hỏi kiểm chứng

Người học đã có PDF/sách/audio TOEIC, nhưng phải mở nhiều tab, chọn và bật đoạn audio thủ công, tìm câu/đáp án, ghi câu trả lời rồi dò lời giải. Người học muốn luồng tương tự những website luyện đề hiện có, **đặc biệt với tài liệu của chính mình**.

**Câu hỏi:** Khi *câu hỏi — đoạn nghe (nếu cần) — chọn đáp án — xem kết quả* được điều phối như một phiên thống nhất, người học có giảm thời gian chuẩn bị, số lần đổi tài liệu và sai sót thao tác, đồng thời muốn luyện thường xuyên hơn không?

**Ngoài phạm vi:** OCR/AI tự động chuyển đề, khả năng import file, độ tin cậy điểm mock, hiệu quả tăng điểm, giấy phép thương mại, giao diện UI cuối cùng.

## 2. Nguyên tắc chuẩn bị

- Không cần upload tài liệu lên ChatGPT hoặc website bên thứ ba; không bắt người dùng viết code hoặc thiết kế UI.
- Chọn **một kịch bản đầu tiên** (Listening hoặc Reading) rồi mới thử kịch bản còn lại, để đo được nguyên nhân.
- Dùng bộ đề có quyền truy cập hợp lệ; khi quyền sao chép/chia sẻ chưa rõ, chỉ sử dụng bản gốc tại chỗ, không sao chép/phát tán hoặc đưa nội dung lên dịch vụ khác.
- Có thể làm với P01; P02 chỉ tham gia nếu họ tự nguyện và có dữ liệu quan sát độc lập.
- Người học cần làm câu khác nhau cùng Part và có độ khó gần tương đương giữa A/B; người hỗ trợ không gợi ý đáp án.

## 3. Hai cách học cần so sánh

**A — Thực trạng (fragmented):** Người học tự mở PDF/sách, tìm đúng câu, audio (nếu Listening), ghi/chọn đáp án trên giấy hoặc ghi chú, tìm đáp án cuối tài liệu và tự đối chiếu.

**B — Mô phỏng phiên tích hợp thủ công (Wizard-of-Oz):** Một người hỗ trợ sử dụng bản gốc hợp lệ để *đưa đúng câu theo lượt, điều khiển audio tương ứng, ghi nhận lựa chọn và trả về đáp án/lời giải có sẵn* ngay trong cùng một phiên. Người học không cần tự dò và đổi tab. Người hỗ trợ làm các việc mà ứng dụng tương lai **có thể** làm, không tạo lời giải AI hoặc giả vờ đã có phần mềm.

**Giới hạn của B:** B có chi phí người hỗ trợ và không tái hiện hoàn hảo một màn hình Android; kết quả chỉ kiểm chứng tiềm năng của quy trình tích hợp. Nếu không có người hỗ trợ, dùng một website luyện đề đang có và có quyền truy cập để benchmark *các bước thao tác*, nhưng **không** dùng hai bộ đề khác nhau để so sánh điểm số/độ khó như phép thử A/B chính thức.

## 4. Thực hiện

1. Chọn một bài/Part đại diện. Với Listening, bảo đảm biết chính xác file và đoạn audio; với Reading, có đáp án để tra. Nếu thiếu thông tin này, ghi blocker, không tự bịa hoặc tự suy đoán.
2. Chọn 4–6 câu cho A và 4–6 câu khác gần tương đương cho B. Ghi số câu, thời gian của từng bước bằng đồng hồ thường. Nếu có hai người, đảo thứ tự A/B để giảm ảnh hưởng làm quen.
3. Người học làm theo A rồi B (hoặc đảo), chỉ nhận đúng đáp án/lời giải có trong nguồn. Không làm trước hay cho xem đáp án.
4. Hỏi 3 câu sau phiên: (i) cách nào ít phiền hơn; (ii) có muốn dùng lại không; (iii) điều gì vẫn còn bất tiện.
5. Ghi riêng công sức chuẩn bị cho B, ví dụ lập danh sách câu, tìm mốc audio, xác định đáp án và điều phối thủ công.

## 5. Chỉ số theo từng lần chạy

| Chỉ số | Định nghĩa | Vì sao đo |
|---|---|---|
| `T_start` | Giây từ lúc quyết định học đến khi bắt đầu câu đầu tiên | Ma sát khởi động |
| `T_audio` | Giây tìm/bật đúng đoạn nghe cho câu (Listening) | Ma sát PDF/audio |
| `N_switch` | Số lần đổi tab/app/trang/tài liệu ngoài ý muốn | Phân mảnh trải nghiệm |
| `T_feedback` | Giây từ lúc trả lời xong đến lúc thấy đáp án/lời giải | Ma sát dò đáp án |
| `Completion` | Số câu hoàn tất / số câu định làm | Khả năng hoàn tất |
| `Errors` | Số lần nhầm câu, nhầm audio hoặc đáp án | Chất lượng quy trình |
| `Ease` | Tự đánh giá thuận tiện, 1–5 | Trải nghiệm |
| `Reuse` | Có muốn dùng lại cách học này không, vì sao | Giá trị cảm nhận |
| `Prep cost` | Phút người hỗ trợ chuẩn bị/điều phối B | Chi phí vận hành mô phỏng |

*Ghi `T_audio = N/A` cho Reading. Không gộp thời gian làm bài Listening với Reading để suy ra phần mềm nhanh hơn.*

### Phiếu ghi ngắn

| Người | Part | Cách | T_start | T_audio | N_switch | T_feedback | Hoàn tất | Errors | Ease 1–5 | Reuse |
|---|---|---|---:|---:|---:|---:|---|---:|---:|---|
| P01 |  | A |  |  |  |  |  |  |  |  |
| P01 |  | B |  |  |  |  |  |  |  |  |
| P02* |  | A |  |  |  |  |  |  |  |  |
| P02* |  | B |  |  |  |  |  |  |  |  |

*P02 chỉ thêm nếu tự nguyện tham gia trực tiếp; không lấy dữ liệu từ lời kể của P01.

## 6. Cách diễn giải (ngưỡng chỉ mang tính đề xuất)

- **Tín hiệu có giá trị:** người học thích B, số lần đổi nguồn và thời gian dò audio/đáp án giảm đáng kể, ít hoặc không nhầm nguồn, muốn dùng lại. Có thể tham chiếu mức giảm ~30% như ngưỡng thảo luận, **chưa được phê duyệt**.
- **Tín hiệu yếu:** sự khác biệt nhỏ hoặc B tiện cho người học nhưng chuẩn bị thủ công quá tốn công. Khi đó ghi rõ đánh đổi, không tuyên bố giải pháp tự động khả thi.
- **Inconclusive:** chưa tiến hành, không đo được, quá ít mẫu hoặc hai điều kiện không thể so sánh.

**Không kết luận:** nền tảng Android đã thiết kế xong, đã xác minh quyền phát hành, AI có thể sinh lời giải đúng, tăng điểm, hay H-003 đã được xác thực thị trường.

## 7. Decision & Open items

- `VAL-013` pain discovery: **RECORDED, qualitative**; no-code test: **REVISED V0.2, NOT EXECUTED**.
- `H-003-VALUE`: **INCONCLUSIVE**.
- `H-003-INGEST`: **DEFERRED / PENDING SAMPLE** (VAL-003).
- `H-003-RIGHTS`: **NOT VERIFIED**.
- `VAL-010`: **DEFERRED BY PRODUCT OWNER** — không hỏi giá lúc này.
- `NEXT VAL-014`: Chọn kịch bản đầu tiên cần đo, **Listening (audio + câu hỏi + chọn đáp án)** hay **Reading (câu + chọn đáp án + lời giải)**.
- Gate: **Product Vision V1.0 APPROVED; Stage 02 IN PROGRESS/HOLD; NO CODE, NO UI/UX, NO MVP/PRD/SRS/ARCHITECTURE**.
