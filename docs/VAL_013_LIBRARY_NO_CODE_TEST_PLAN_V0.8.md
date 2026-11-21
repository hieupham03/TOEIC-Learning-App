# VAL-013 — KẾ HOẠCH ĐO BASELINE SOLO TRÊN PC/LAPTOP (KHÔNG CODE)

**Phiên bản:** V0.8 — 2026-11-21  
**Trạng thái:** **READY TO RUN / NOT RUN — BATCH REPORT CHOSEN (VAL-024)**  
**Nguồn:** VAL-012/013 (ưu tiên và vấn đề); VAL-014 (L/R riêng); VAL-015 (solo); VAL-016 (PC); VAL-022 (quay về H-003); VAL-023 (đủ cả câu hỏi–đáp án–audio); **VAL-024 (cả hai phiên, gửi kết quả cùng lần)**.

## Mục tiêu & giới hạn
Đo các bất tiện có thể quan sát được khi **một người tự luyện bằng PDF/sách/audio của chính mình trên laptop**. Thử nghiệm không xác nhận khả thi nhập PDF/audio tự động, giấy phép phát hành hay giá trị của ứng dụng Android tương lai; không yêu cầu upload hay code.

## Quyết định VAL-024 — thứ tự tùy ý, báo cáo một lần
- Chạy **cả VAL-013L và VAL-013R** trên laptop, theo thứ tự tùy bạn và khi có thời gian; không đặt hạn hoàn thành.
- Tách từng phiên, dùng các câu chưa làm nếu có thể và ghi ngày/điều kiện mỗi phiên. Không cộng số đo Listening và Reading; có thể làm khác ngày.
- **Gửi kết quả trong một tin nhắn duy nhất sau cả hai**. Nếu bất khả thi ở một nhánh, ghi trạng thái `NOT RUN`, `PARTIAL` hoặc `BLOCKED` và lý do, không điền số liệu giả.
- Phiếu chính: `docs/VAL_024_DESKTOP_BASELINE_BATCH_LOG_V0.4.md`.

## Chuẩn bị (trước khi bấm giờ)
1. Xác nhận có bộ tài liệu Reading và Listening hợp lệ để dùng cho việc học cá nhân, audio tương ứng cho Listening, đáp án nguồn. Việc có file là do Product Owner tự báo cáo, chưa được bên ngoài kiểm định.
2. Dùng laptop, ứng dụng đọc tài liệu và audio như khi học bình thường. Chọn **bộ nguồn/Part**, nhưng không tìm sẵn vị trí cụ thể của câu hỏi, audio, đáp án để giữ được hành vi tìm kiếm thực tế.
3. Mở ghi chú hoặc dùng giấy và đồng hồ bấm giờ; nếu việc bấm giờ làm ảnh hưởng học, có thể ghi ước lượng, nhưng phải đánh dấu `ESTIMATED`.
4. Chọn câu chưa làm nếu có thể. Việc đã quen câu hỏi phải ghi lại; không ép độ khó hoàn toàn tương đương vì đây là đo baseline, không phải thử nghiệm đối chứng.

## Buổi 1 — `VAL-013L` Listening
- Nhiệm vụ: **Part 3: một đoạn audio + 3 câu** (hoặc nhóm tương đương có đúng audio/đáp án).
- Bắt đầu từ lúc **quyết định mở bài** trên laptop; tìm tài liệu như bình thường.
- Đo: `T_start_s` tới lúc câu đầu hiện ra; `T_audio_locate_s` thời gian tìm đúng file/track/đoạn audio, **không** gồm thời gian nghe; `N_switch` số lần chuyển tab, cửa sổ app hoặc tài liệu; `T_feedback_s` từ sau khi trả lời câu cuối đến khi xem được đáp án/lời giải; `N_source_errors` ghép nhầm file/trang/câu/audio.
- Ghi thêm: số câu hoàn thành, `Ease_1_5`, trở ngại rõ nhất, công cụ sử dụng, measured/estimated. Không yêu cầu audio autoplay hoặc các thao tác giả định của app tương lai.

## Buổi 2 — `VAL-013R` Reading
- Nhiệm vụ: **Part 5: 5 câu** chưa làm (nếu có), có đáp án.
- Tương tự buổi 1 nhưng **không có `T_audio_locate_s`**; theo dõi cách tìm câu, đánh dấu đáp án, chuyển tài liệu và dò đáp án.
- Ghi riêng log của Reading, không cộng thời gian với Listening. Có thể cùng ngày hoặc ngày khác; phải ghi thời điểm và điều kiện.

## Định nghĩa phép đo
- `T_start_s`: từ khi quyết định bắt đầu học đến lúc có thể nhìn và bắt đầu trả lời câu đầu tiên.
- `T_audio_locate_s`: thời gian chỉ dành cho thao tác **tìm đúng audio**; không tính nghe bài; có thể nằm trong `T_start_s`, **không cộng hai chỉ số để tính tổng thời gian**.
- `N_switch`: số lần đổi tab/cửa sổ/ứng dụng hoặc đổi giữa file tài liệu/audio/đáp án; không tính scroll trong cùng trang.
- `T_feedback_s`: từ lúc đã chốt đáp án cuối tới khi thấy được đáp án chuẩn; nếu không có lời giải, đánh dấu `chỉ có đáp án`.
- `N_source_errors`: số lần mở/ghép sai câu, đáp án, track hoặc tài liệu; ghi 0 nếu không xảy ra, không để trống rồi suy ra 0.
- `Ease_1_5`: 1 = rất bất tiện, 5 = rất thuận tiện.
- `status`: `NOT RUN`, `COMPLETED`, `PARTIAL`, `BLOCKED`.
- `measurement_quality`: `MEASURED`, `ESTIMATED`, `UNAVAILABLE`, áp dụng riêng theo số liệu nếu khác nhau.

## Tiêu chí đánh giá sau thử nghiệm (chưa phải ngưỡng nghiệm thu)
1. Nếu hai phiên đều thực hiện được, mô tả **những thao tác gây ma sát nhất** ở từng kỹ năng.
2. Không bịa tiêu chuẩn giảm 30% hay ROI; chưa có giải pháp tích hợp thật để so sánh.
3. Nếu bất tiện nhỏ hơn dự đoán, cập nhật giả thuyết theo hướng giảm ưu tiên; không tìm cách chứng minh ý tưởng bằng mọi giá.
4. Nếu chỉ một nhánh chạy, nhánh kia vẫn `NOT RUN`, không coi toàn bộ nghiên cứu hoàn thành.
5. Bước kế tiếp tùy kết quả: đối chiếu định tính với một web luyện đề tích hợp hợp pháp hoặc hoàn thiện kế hoạch kiểm chứng giải pháp mà **không cần thiết kế UI/code**.

**Tài liệu ghi nhận:** `docs/VAL_024_DESKTOP_BASELINE_BATCH_LOG_V0.4.md`. Không gửi nội dung đề hay audio; không cần gửi cho tới khi có kết quả cả hai nhánh (hoặc ghi rõ lý do nhánh chưa xong).

**Stage Gates:** Product Vision V1.0 APPROVED; Stage 02 IN PROGRESS/HOLD; Stage 03 NOT STARTED; MVP/PRD/SRS/UX/UI/architecture/code NOT AUTHORIZED. `VAL-003` và `VAL-010` DEFERRED.
