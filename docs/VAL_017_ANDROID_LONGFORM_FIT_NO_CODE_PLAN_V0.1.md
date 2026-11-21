# VAL-017 — Android Full-Practice Fit (No-code Validation) V0.1

- **Updated:** 2026-11-21
- **Status:** PROPOSED / NOT RUN — chỉ là kế hoạch định tính, không thay thế thực nghiệm H-003 hoặc quyết định MVP
- **Owner:** Product Owner; solo, không có facilitator; không tải PDF/audio và không lập trình
- **Inputs:** VAL-016 (hiện tự luyện chủ yếu trên PC), VAL-017 (mong dùng Android thay PC cho đề đầy đủ)

## 1. Mục đích và ranh giới

Kiểm chứng liệu học viên muốn/và cảm thấy đủ thuận tiện để hoàn thành **Listening và Reading trên smartphone Android**, trong đó trải nghiệm dài và phức tạp hơn học 1 từ/câu. Khác với VAL-013L/R là đo **baseline PC**, thử nghiệm này đánh giá **mobile suitability**. Không đối chiếu điểm số giữa hai nguồn đề khác nhau, không kết luận sản phẩm tương lai đã khả thi.

## 2. Các giả thuyết cần đo

- **H-PLATFORM-01:** Người học thấy điện thoại đủ phù hợp để hoàn thành phiên luyện TOEIC dài với ít thao tác không cần thiết.
- **R-P01:** Part 6/7 có văn bản dài/nhiều đoạn, cuộn và đọc trên phone có thể gây mệt/nhầm.
- **R-P02:** Listening Part 3/4 cần vừa nghe vừa theo dõi câu hỏi và lựa chọn, dễ phân tán khi trên phone.
- **R-P03:** Phiên dài có thể bị gián đoạn (cuộc gọi, tin nhắn, khóa màn hình, mất mạng/pin), ảnh hưởng khả năng hoàn thành.

## 3. Quy trình thử không code — chưa bắt đầu

1. **Chờ VAL-018:** Làm rõ “đầy đủ” là mock liên tục ~120 phút, đủ Part chia phiên, hoặc cả hai. Không ép người học làm 120 phút nếu không cần.
2. **Chọn nguồn hợp pháp đã có trên Android**, ví dụ một ứng dụng TOEIC có nội dung tích hợp Listening/Reading; không cần dùng PDF cá nhân, không chốt đối thủ/công nghệ. Ghi tên app và nguồn chỉ để lập hồ sơ.
3. **Phiên L ngắn kiểm chứng khả năng sử dụng:** Thử một bài Part 3/4, ghi mức khó nghe–đọc–chọn, số lần nhầm câu, số chuyển màn hình và ý định dùng tiếp.
4. **Phiên R ngắn kiểm chứng đọc dài:** Thử bài Part 6 hoặc 7 có văn bản dài, ghi mức dễ đọc/cuộn/thao tác, mỏi mắt và ý định dùng tiếp.
5. **Phiên dài tự nguyện:** Chỉ sau khi hiểu yêu cầu VAL-018 và phiên ngắn đủ thuận tiện mới đề xuất thử 30–45 phút hoặc full 120 phút nếu thực sự mong muốn; tuyệt đối không gắn ngưỡng hoàn thành khi chưa thống nhất.
6. Ghi quan sát/đo thực tế ngay sau phiên, phân biệt ước lượng và số đo. Nếu không có ứng dụng phù hợp thì `NOT AVAILABLE`, không giả định đã test.

## 4. Phiếu đo tối thiểu (L và R ghi riêng)

| Field | Nội dung |
|---|---|
| device_context | Android phone, kích thước máy nếu biết; tay cầm/tai nghe; môi trường (ở nhà/di chuyển) |
| content_reference | Tên app/bộ đề, Part, số câu, thời lượng thực tế; không cần chép nội dung bản quyền |
| start_latency | Thời gian từ muốn bắt đầu tới câu đầu tiên (giây/phút) |
| task_completions | Số câu hoàn tất, có bỏ cuộc và vì sao |
| switching_errors | Số lần chuyển ngữ cảnh gây khó, sai câu/audio/đáp án |
| audio_legibility_L | Khả năng vừa nghe vừa theo dõi câu hỏi (chỉ Listening), 1–5 |
| text_legibility_R | Dễ đọc văn bản dài/multi-passage và cuộn (chỉ Reading), 1–5 |
| comfort / fatigue | Mức dễ chịu, mỏi mắt/tay, 1–5 (nêu rõ thang) |
| interruptions | Cuộc gọi/thông báo/khóa màn hình/kết nối/pin và cách ảnh hưởng |
| reuse_intent | Có muốn làm thêm bài dài trên điện thoại không; lý do |

## 5. Giới hạn suy luận & dấu hiệu quyết định

- Một người tự thử, khác đề/app với PC baseline => **bằng chứng định hướng**, không có phép A/B nhân quả hoặc % cải thiện chính thức.
- Nếu cả L và R chấp nhận được với phiên ngắn, mới cân nhắc đánh giá phiên dài. **Không** suy ra người học chắc chắn hoàn thành 120 phút.
- Nếu phiên dài gây khó chịu nghiêm trọng, cần xem xét lại mức ưu tiên *full mock liên tục trên Android* tại Stage Gate; Product Vision hiện chưa được thay đổi.
- Việc nhập đề PDF/audio/giải thích và quyền nội dung là một câu hỏi **khác** (H-003-INGEST / H-003-RIGHTS), không được chứng minh bởi việc dùng app sẵn có.
- Ngưỡng định lượng chấp nhận được phải được Product Owner phê duyệt sau khi xác định kiểu phiên học.

## 6. External desk references

- ETS TOEIC L&R format: https://www.ets.org/toeic/about/listening-reading.html (200 câu / ~120 phút).
- Android state interruptions: https://developer.android.com/guide/components/activities/activity-lifecycle.html
- Android accessibility legibility and touch targets: https://developer.android.com/guide/topics/ui/accessibility/apps
- Android TOEIC product benchmark listings: https://play.google.com/store/apps/details?id=org.iibc.global.toeic.officialapp ; https://play.google.com/store/apps/details?id=com.englishtest . Chỉ là bằng chứng tính năng được công bố, không phải trải nghiệm thực tế của người dùng.

## 7. Gates

- Product Vision V1.0 APPROVED, unchanged.
- Stage 02 IN PROGRESS/HOLD. No MVP/PRD/SRS/UI/architecture/code authorized.
- NEXT VAL-018: hỏi cách người học hiểu “luyện đề đầy đủ” trên Android.
