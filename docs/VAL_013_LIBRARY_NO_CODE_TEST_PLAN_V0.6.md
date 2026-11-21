# VAL-013 — SOLO BASELINE CHO THƯ VIỆN ĐỀ TOEIC CÁ NHÂN (KHÔNG CODE)

**Phiên bản:** V0.6 — 2026-11-21  
**Trạng thái:** PLANNED / NOT RUN  
**Nguồn:** VAL-012 ưu tiên H-003; VAL-013 quy trình rời rạc; VAL-014 hai kỹ năng tách riêng; VAL-015 tự thực hiện; VAL-016 PC/laptop; VAL-022 quay về ưu tiên thư viện sau đánh giá mobile.

## Mục tiêu
Xác định mức bất tiện **thực tế** khi tự luyện TOEIC bằng PDF/sách/audio trên PC/laptop; phân tách Listening và Reading. **Không kiểm chứng** trình nhập đề tự động, tính hợp pháp chia sẻ nội dung, giá trị trên Android hoặc tăng điểm TOEIC.

## Bước 0 — Readiness, không cần tải file lên (VAL-023)
- Xác nhận tài liệu mà người học có thể mở cục bộ trên laptop: bộ câu hỏi, đáp án nguồn; Listening phải có audio đúng đoạn/đúng câu. Nếu thiếu mapping thì ghi `BLOCKED`; không đoán đáp án/ghép audio.
- Không yêu cầu liệt kê tên sách, upload, chụp màn hình hoặc chuyển nội dung có bản quyền.
- Nếu chỉ có một nhánh sẵn, có thể đo nhánh ấy trước; nhánh còn lại giữ `NOT RUN/BLOCKED`, không tự coi đã hoàn thành toàn bộ VAL-013.

## Nhánh L — Listening baseline solo
1. Khi thuận tiện, chọn **1 đoạn Part 3 / 3 câu** (hoặc nhóm câu tương đương có audio + đáp án khớp).
2. Mở đúng PDF/sách, audio và nơi ghi đáp án như cách bạn vốn làm, **không cố tình chuẩn bị trước để giảm thao tác**.
3. Sau bài, ghi `T_start` (đến câu đầu), `T_audio_locate` (tìm đúng audio, không gồm thời lượng nghe), `N_switch` (đổi tab/ứng dụng/tài liệu), `T_feedback` (đến lúc thấy đáp án), số câu hoàn thành, số lỗi nguồn, `Ease_1_5`, thao tác bất tiện nhất, chất lượng thời gian measured/estimated.

## Nhánh R — Reading baseline solo
1. Chọn **5 câu Part 5** cùng nguồn có đáp án, lý tưởng câu chưa làm.
2. Làm bằng PDF/sách đúng quy trình cũ rồi ghi `T_start`, `N_switch`, `T_feedback`, số câu hoàn thành, lỗi tra đáp án, `Ease_1_5`, bất tiện nhất, thời gian measured/estimated. Không yêu cầu audio.

## Benchmark web TOEIC (tùy chọn)
Nếu đã có quyền dùng web luyện đề tích hợp, trải nghiệm trên **cùng laptop/PC** và ghi nhận những bước dễ hơn hoặc không dễ hơn. Đây chỉ là **đối chiếu định tính**, không phải thử nghiệm A/B tương đương; không tính % cải thiện từ hai bộ đề/nguồn khác nhau.

## Diễn giải & giới hạn
- Test hiện **NOT RUN**. Không điền số liệu giả hoặc coi câu trả lời phỏng vấn là log đo.
- Một hai phiên nhỏ giúp tìm điểm nghẽn cho người dùng pilot, không chứng minh lợi thế cạnh tranh, tiến bộ điểm số hay fit thị trường.
- `H-003-VALUE-L/R = INCONCLUSIVE`; `H-003-INGEST = DEFERRED`; `H-003-RIGHTS = UNKNOWN`.
- Nếu sau này muốn xác định **lợi ích nhân quả** từ luồng tích hợp với kho đề cá nhân, cần kế hoạch so sánh có kiểm soát và công cụ được phê duyệt; **không triển khai trong Phase 02 này**.

## Câu hỏi kế tiếp — VAL-023
**Ngay trên laptop, tài liệu bạn có đã đủ câu hỏi–đáp án và audio khớp để tự đo cả Listening và Reading chưa?** A. Cả hai; B. Chỉ Reading; C. Chỉ Listening; D. Chưa rõ/chưa có đủ. Không cần gửi tài liệu.

**Stage Gates:** Product Vision V1.0 APPROVED; Stage 02 IN PROGRESS/HOLD; Stage 03 NOT STARTED; no MVP/PRD/SRS/UX/UI/architecture/code sign-off.
