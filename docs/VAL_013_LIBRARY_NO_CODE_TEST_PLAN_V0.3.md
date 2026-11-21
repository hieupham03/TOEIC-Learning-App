# VAL-013 — KẾ HOẠCH THỬ NGHIỆM LUỒNG LUYỆN ĐỀ TÍCH HỢP, 2 NHÁNH (KHÔNG CODE)

**Phiên bản:** V0.3 · 2026-11-20 · **Trạng thái:** PROPOSED / NOT RUN  
**Nguồn quyết định:** VAL-013 mô tả khó khăn; VAL-014 chọn **Listening và Reading tách riêng**  
**Giai đoạn:** 02/11 — Validation; **không phải** UI, MVP hoặc yêu cầu kỹ thuật được duyệt

## 1. Mục đích và giả thuyết

- **H-003-VALUE-L:** Một quy trình luyện Listening thống nhất sẽ giảm thao tác chuyển nguồn, tìm audio, dò đáp án và sai ghép dữ liệu, đồng thời có giá trị sử dụng đối với người học.
- **H-003-VALUE-R:** Một quy trình luyện Reading thống nhất sẽ giảm thời gian tìm câu và đối chiếu đáp án, giảm thao tác và giúp người học sẵn sàng luyện thường xuyên hơn.

Tách **giá trị sử dụng** khỏi **khả thi tự động nhập PDF/audio (H-003-INGEST, đang chờ mẫu VAL-003)** và **quyền sao chép/chia sẻ (H-003-RIGHTS, chưa xác minh)**.

## 2. Điều kiện chuẩn bị tối thiểu

- Dùng tài liệu PDF/sách/audio người học đang có quyền truy cập; không buộc upload hoặc sao chép lên bên thứ ba. Chỉ trình chiếu/đọc trực tiếp từ bản hợp lệ, không phát tán.
- Có đúng **đáp án nguồn** và, nếu Listening, đúng audio tương ứng. Thiếu mốc ghép đề–audio: ghi BLOCKED, không đoán.
- **A (as-is):** người học tự mở đề, audio, đáp án và ghi câu trả lời như bình thường.
- **B (Wizard-of-Oz):** một người hỗ trợ chuẩn bị câu hỏi và audio tương ứng, ghi nhận lựa chọn của người học, đưa đáp án/lời giải có sẵn từ nguồn. Không gợi ý giải, không tạo AI answer, không làm thay bài.
- Nếu **không có người hỗ trợ**, chưa thể gọi là A/B Wizard-of-Oz. Có thể ghi baseline A và đánh giá luồng của web luyện đề hợp pháp như **benchmark định tính riêng**, không kết luận B vượt A từ hai bộ đề khác độ khó. Hỏi VAL-015 để quyết định.
- Chỉ đo khi người học tình nguyện; P02 là người học trực tiếp nếu tham gia, không coi lời kể của P01 là dữ liệu P02.

## 3. Nhánh Listening — VAL-013L

**Gợi ý lựa chọn có điều kiện:** Part 3, chọn **2 đoạn hội thoại chưa luyện**, độ dài audio/độ khó tương đối tương đồng, mỗi đoạn 3 câu; một đoạn cho A, một đoạn cho B. Nếu tài liệu không phù hợp, đổi sang Part khác có ghép audio rõ ràng, ghi lý do và giữ cùng Part giữa A/B. Không thay đổi số lượt nghe giữa A/B.

1. Chuẩn bị tài liệu, audio và đáp án; ghi riêng thời gian chuẩn bị B.
2. Bấm giờ từ **quyết định bắt đầu học** tới câu đầu; A tự thao tác, B do người hỗ trợ điều phối nguồn.
3. Ghi thời gian **tìm/bật đúng audio** (`T_audio_locate`), **không** tính thời lượng phát nghe thực tế là lợi ích tốc độ.
4. Ghi số lần đổi tab/app/trang, nhầm đoạn/nghe sai audio, thời gian dò đúng đáp án và mức độ thuận tiện.
5. Ghi số câu đúng để xem độ tương đương tương đối, **không** dùng làm bằng chứng app tăng điểm.

## 4. Nhánh Reading — VAL-013R

**Gợi ý lựa chọn có điều kiện:** Part 5, **5 câu chưa luyện cho A và 5 câu khác cho B**, cùng mức khó gần đúng, cùng nguồn hoặc bộ nguồn tương đương; tránh để B vô tình dễ hơn.

1. A tự mở PDF/sách, tìm đúng câu, trả lời, dò kết quả.
2. B được điều phối câu hỏi, ghi đáp án và nhận kết quả từ **đáp án nguồn**; không cần audio.
3. Ghi thời gian tìm câu đầu, chuyển tab/trang, thời gian tìm đáp án, hoàn tất, đúng/sai, tiện lợi và mong muốn dùng lại.
4. `T_audio_locate = N/A`; **không gộp** số liệu thời gian hoặc điểm của Reading với Listening.

## 5. Thiết kế quan sát, tránh kết luận sai

- So sánh **A với B trong từng Part**, cùng số lượng câu, các câu chưa từng làm; không dùng lại cùng câu giữa A/B vì dễ gây hiệu ứng ghi nhớ.
- Nếu P01 và P02 cùng tham gia, đổi thứ tự A/B giữa hai người khi khả thi để giảm hiệu ứng quen thao tác. Ghi thứ tự thực tế.
- Ghi thiết bị/môi trường, số lần phát lại audio cho L, thời lượng đề, và sự hỗ trợ thực tế của facilitator.
- Người đo không được gợi ý đáp án; B có thể thuận tiện vì có người phục vụ nên **không thể suy ra ứng dụng tự động đạt hiệu quả tương đương**.
- Nên làm hai phiên ngắn tách biệt, cho phép dừng bất cứ lúc nào. Không buộc đặt ngày hay file mẫu khi người dùng chưa sẵn sàng.

## 6. Metric và định nghĩa

| Biến | Định nghĩa | L | R |
|---|---|---:|---:|
| `T_start_s` | Giây từ quyết định học đến câu đầu tiên | Có | Có |
| `T_audio_locate_s` | Giây tìm/bật đúng đoạn nghe, **không tính playback** | Có | N/A |
| `N_switch` | Số lần đổi app/tab/tài liệu ngoài dự định | Có | Có |
| `T_feedback_s` | Giây từ khi hoàn tất chọn đáp án đến khi xem đáp án/lời giải nguồn | Có | Có |
| `Completion` | Số câu hoàn thành / số câu định làm | Có | Có |
| `N_source_error` | Số lần ghép nhầm câu/audio/đáp án hoặc sai nguồn | Có | Có |
| `Correct` | Số câu trả lời đúng (chỉ để nhận diện chênh độ khó) | Có | Có |
| `Ease` | Mức thuận tiện người học chấm 1–5 | Có | Có |
| `Reuse` | Muốn dùng lại? Lý do cụ thể | Có | Có |
| `Prep_B_min` | Phút chuẩn bị + điều phối của facilitator cho B | Có | Có |

## 7. Tiêu chí diễn giải và ngưỡng (đề xuất, chưa duyệt)

- **Tín hiệu thuận lợi cho từng nhánh:** B ít chuyển nguồn hơn, ít nhầm tài liệu hơn, nhanh tìm audio/đáp án hơn, người học đánh giá tiện hơn và muốn dùng lại. Mức giảm khoảng 30% trở lên đối với một số thời gian thao tác là **mốc thảo luận**, không phải ngưỡng phê duyệt hoặc bằng chứng thống kê.
- **Không thuận lợi:** B chỉ tốt hơn khi người hỗ trợ chuẩn bị quá nhiều, hoặc người học không thấy tiện hơn, hoặc có lỗi ghép nội dung.
- **Inconclusive:** không có người hỗ trợ/thiếu tài liệu/audio/đáp án, mẫu quá nhỏ, độ khó A/B khác nhau quá mức hoặc chưa ghi được số đo.
- **Bất kể kết quả:** không kết luận cải thiện điểm TOEIC, không chứng minh có thể tự động nhập/hiểu PDF, không xác minh được quyền xuất bản, không phê duyệt MVP.

## 8. Bước kế tiếp

**VAL-015 — hỏi một câu:** Có thể nhờ một người hỗ trợ điều phối bài làm (chuẩn bị đoạn nghe/câu hỏi, ghi đáp án, cho xem đáp án nguồn) trong các lần thử mà không chỉ người học tự thao tác hay không? Nếu không, điều chỉnh thử nghiệm cho thực tế và ghi hạn chế.

**Gate:** Product Vision V1.0 APPROVED · Phase 02 IN PROGRESS/HOLD · No UI, code, architecture, MVP/PRD/SRS approvals.
