# VAL-013 — KẾ HOẠCH THỬ NGHIỆM SOLO (KHÔNG CODE, KHÔNG NGƯỜI HỖ TRỢ)

**Phiên bản:** V0.4 — 2026-11-20 · **Trạng thái:** PROPOSED / NOT RUN  
**Nguồn:** VAL-013 đau điểm luồng phân mảnh; VAL-014 chọn 2 nhánh; VAL-015 chọn **B: tự thực hiện một mình**.  
**Thay thế trong triển khai:** `VAL_013_LIBRARY_NO_CODE_TEST_PLAN_V0.3.md` (giữ lịch sử; mô hình B có facilitator không áp dụng trong điều kiện hiện tại).

## 1. Mục đích, phạm vi và điều chưa thể suy ra

- **Mục đích gần:** Đo mức phiền toái quan sát được khi tự sử dụng PDF/sách/audio để luyện TOEIC và hiểu những hành vi của một trải nghiệm luyện đề tích hợp mà người học đánh giá cao.
- **Không thể làm khi thử một mình:** Wizard-of-Oz có người phục vụ ở điều kiện B. Không được gọi baseline + website khác là A/B cùng nguồn, kết luận causal hay tính % giảm thao tác do app chúng ta tạo ra.
- **Tách hai track:** Listening (L) và Reading (R), không gộp các chỉ số đặc thù.
- **Không kiểm chứng:** Tự động nhập PDF/audio; ghép audio–câu, bản quyền tải lên/phát hành, tăng điểm TOEIC, lợi ích market-wide.

## 2. Quy trình A — đo baseline ngay trên tài liệu cá nhân (bắt buộc nếu thực hiện)

1. Chọn thiết bị mà người học đang sử dụng THỰC TẾ (VAL-016 sẽ xác định), duy trì điều kiện mạng, thiết bị và nguồn ổn định trong từng lượt. Chỉ dùng tài liệu được phép truy cập, không upload/lan truyền đề/audio.
2. **Listening VAL-013L:** Chọn một đoạn Listening mà nguồn audio–câu–đáp án được xác định đúng, ví dụ Part 3 (1 đoạn, 3 câu). Nếu không đủ mapping hoặc đáp án, đánh dấu BLOCKED và mô tả thiếu gì; không tự đoán.
3. **Reading VAL-013R:** Chọn 5 câu chưa làm cùng Part (ví dụ Part 5) có đáp án nguồn. Không có câu phù hợp thì ghi BLOCKED, không tự tạo đáp án để lấp trống.
4. Tự làm như bình thường. Không thay đổi quy trình để tạo ra kết quả đẹp; không mở sẵn toàn bộ nguồn nếu trước đây chưa làm thế. Không gián đoạn giữa bài để trả lời khảo sát.
5. Sau mỗi lượt, ghi lại: thiết bị, nguồn, số câu định làm/hoàn thành; thời gian bắt đầu đến câu đầu (`T_start`), thời gian tìm đúng audio (`T_audio_locate` chỉ L, **không tính thời lượng nghe**), số lần chuyển app/tab/tài liệu (`N_switch`), thời gian từ chọn xong đến thấy đáp án nguồn (`T_feedback`), lỗi nguồn, mức tiện 1–5 và mô tả chỗ bất tiện nhất.
6. Có thể tự dùng đồng hồ hay quay màn hình cục bộ nếu phù hợp; **không bắt buộc quay**. Nếu không có thời điểm quan sát chính xác, ghi `ƯỚC LƯỢNG`, không giả số liệu chính xác. Nếu quay, giữ nội bộ và bảo vệ thông tin riêng tư/bản quyền.

## 3. Quy trình B — benchmark trải nghiệm web có sẵn (tùy chọn)

1. Nếu người dùng đã có quyền truy cập một website TOEIC cho phép luyện theo luồng tích hợp, thử đúng kỹ năng/Part gần giống baseline nếu có. Không cần nêu thương hiệu hay cung cấp nội dung cho ChatGPT nếu không muốn.
2. Ghi chú thao tác nào tập trung trong một phiên, cần bao nhiêu lần rời màn hình, độ dễ nghe audio, đánh đáp án, xem lời giải; đánh giá mức thuận tiện 1–5, thích/không thích và mô tả.
3. **Không so thời gian hay điểm A với B như đối chứng**: khác nguồn câu hỏi, nội dung, độ khó, thiết bị, mức quen thuộc, có thể có chênh lệch tính năng. Chỉ dùng benchmark như tài liệu tham chiếu trải nghiệm.
4. Không có website hợp pháp đang dùng: ghi `NOT AVAILABLE`; baseline vẫn có giá trị. Không thúc ép tạo tài khoản/mua gói.

## 4. Dữ liệu và giá trị sử dụng

| Trường | Listening L | Reading R | Ghi chú |
|---|---|---|---|
| `Device / Source / Part` | Có | Có | Thiết bị sử dụng thực tế, nguồn hợp lệ |
| `T_start_s` | Có | Có | Từ quyết định làm bài tới câu hỏi đầu tiên |
| `T_audio_locate_s` | Có | N/A | Không cộng thời lượng nghe |
| `N_switch` | Có | Có | Đổi tab/ứng dụng/tài liệu liên quan để hoàn thành bài |
| `T_feedback_s` | Có | Có | Từ trả lời xong đến khi tiếp cận được đáp án/lời giải nguồn |
| `Completion` | Có | Có | Số câu hoàn thành/định làm |
| `N_source_errors` | Có | Có | Nhầm đoạn audio, đáp án, trang, câu v.v. |
| `Ease_1_5` | Có | Có | Tự đánh giá thuận tiện |
| `Timing_quality` | Có | Có | `MEASURED` / `ESTIMATED` / `UNAVAILABLE` |
| `Most_annoying_step` | Có | Có | Ví dụ và số thao tác cụ thể nếu nhớ |
| `Benchmark` | Tùy chọn | Tùy chọn | Chỉ nhận xét định tính, không chứng minh cải thiện của app |

Tham khảo phiếu `VAL_015_SOLO_TEST_LOG_V0.1.md`.

## 5. Tiêu chí diễn giải / các cổng ra quyết định

- **Sau khi có baseline:** Chỉ xác nhận **ma sát đã được quan sát** ở kỹ năng tương ứng; ví dụ mất 45 giây tìm audio, chuyển 5 tab. Không tự động kết luận giải pháp hoặc sản phẩm đã đem lại hiệu quả.
- **Nếu có benchmark:** Có thể xây dựng tiêu chí kỳ vọng cho UX tương lai, KHÔNG thiết kế màn hình hay tính năng UI trong Stage 02. Cảm nhận cá nhân là dữ liệu định tính.
- **Muốn định lượng hiệu quả giải pháp với tài liệu cá nhân:** Cần thêm phép thử đối chứng phù hợp sau này (facilitator, prototype được phê duyệt, hoặc phương án kiểm chứng khác) và sau đó còn phải xác minh ingest, bản quyền.
- **Mẫu chỉ 1 người hoặc 2–5 người:** Bằng chứng định hướng pilot, không đại diện thị trường.
- **Chưa có kết quả:** `H-003-VALUE-L/R = INCONCLUSIVE / NOT RUN`; `H-003-INGEST = DEFERRED`; `H-003-RIGHTS = UNKNOWN`.

## 6. Bước kế tiếp — VAL-016

**Một câu hỏi duy nhất:** Người dùng hiện gặp bất tiện nêu trên khi luyện PDF/audio chủ yếu **trên điện thoại Android, trên máy tính hay trên cả hai**? Phải xác định nguồn ma sát trên thiết bị thật trước khi ghi thời gian. Sau đó mời người dùng tự thực hiện một lượt baseline ngắn trên thiết bị đã xác định và gửi **chỉ số**, không cần gửi nội dung đề.

**Stage Gates:** Product Vision V1.0 APPROVED; Stage 02 IN PROGRESS/HOLD; chưa phê duyệt MVP, PRD/SRS, UX/UI, architecture, code.
