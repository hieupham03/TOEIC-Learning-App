# B1 — Blueprint hai Full Mock và kiểm tra chất lượng V0.1

**Status:** REQUIREMENTS SUPPORTING DRAFT, NOT ITEM GENERATION / NOT APPROVED MOCKS. **Nguồn:** ETS Examinee Handbook (paper-delivered L&R, 2025 copyright), xem link cuối.

## 1. Phân bổ câu hỏi theo Part
| Part | Mô tả | Đề A | Đề B | Tổng 2 đề | Asset cần có |
|---|---|---:|---:|---:|---|
| 1 | Photographs | 6 | 6 | 12 | Hình + audio lựa chọn + key |
| 2 | Question–Response | 25 | 25 | 50 | Audio câu hỏi/đáp lại + key |
| 3 | Conversations | 39 | 39 | 78 | 13 hội thoại × 3 câu mỗi đề + audio + key |
| 4 | Talks | 30 | 30 | 60 | 10 bài nói × 3 câu mỗi đề + audio + key |
| 5 | Incomplete Sentences | 30 | 30 | 60 | Câu hỏi/chọn đáp án + key |
| 6 | Text Completion | 16 | 16 | 32 | Đoạn văn + chỗ trống/câu hỏi + key |
| 7 | Reading Comprehension | 54 | 54 | 108 | Các bài đơn/đa đoạn + câu hỏi + key |
| **Tổng** | | **200** | **200** | **400** | Cùng metadata/rights/QA |

Trong mỗi form: Listening 100 câu / khoảng 45 phút; Reading 100 câu / 75 phút, tổng 120 phút. **Hai form độc lập chỉ là yêu cầu biên soạn; chưa có ngân hàng nội dung thật được kiểm tra.**

## 2. Manifest kiểm tra từng đề
| Field | Ý nghĩa |
|---|---|
| mock_id, version, date, author/reviewer | Nguồn gốc, lịch sử phiên bản |
| section, part, item_id, item_group_id | Đúng cấu trúc, group hội thoại/bài đọc |
| source_id, license_id, asset IDs, checksums | Quyền và tính nguyên vẹn |
| prompt, options, answer_key, rationale_status | Khả năng làm/soát câu; lời giải nếu cam kết |
| audio_ref, image_ref, passage_ref, transcript_ref | Liên kết từng câu tới tài nguyên đúng |
| difficulty_review, ambiguity_flags | Đánh giá độ khó và câu mơ hồ |
| exposure_status, overlap_report | Chặn luyện lại câu từ đề kiểm tra |
| QA reviewer, revision_log, severity | Đánh dấu lỗi và xử lý |

## 3. QC procedure trước khi dùng mock thực tế
- `QA-A RIGHTS`: kiểm tra quyền từng asset, cả âm thanh/ảnh từ bên thứ ba.
- `QA-B STRUCTURE`: đếm đúng theo Part, kiểm tra lựa chọn, thứ tự, timing, các nhóm 3 câu.
- `QA-C ACADEMIC`: đối chiếu đáp án, logic/ngữ pháp, tính tự nhiên, câu chỉ có một best answer theo tiêu chí xây dựng riêng.
- `QA-D MEDIA`: nghe thử, đồng bộ group/item, tránh audio vỡ/thiếu đoạn, xác minh transcript.
- `QA-E INDEPENDENCE`: không trùng form A/B, không đưa item mock vào bank practice trước khi đo.
- `QA-F FORM LEVEL`: đối chiếu chuyên gia theo ma trận ngữ pháp, từ vựng, Part và độ khó. **Không tự nhận tương đương thống kê.**
- `QA-G REPORT`: chỉ báo kết quả và giới hạn đánh giá rõ, không chứng nhận ETS, không sử dụng số câu đúng tự quy ra điểm TOEIC.

## 4. Exit states
- `NOT READY`: chưa đủ nguồn; hiện trạng.
- `CONTENT ASSEMBLED / RIGHTS PASS / QA PENDING`: mới có dữ liệu, chưa phát cho pilot.
- `QA REVIEWED / RELEASE DECISION PENDING`: có báo cáo kiểm tra, PO quyết định riêng.

## 5. Dữ liệu còn thiếu
Không có đề thực, không có nội dung/audio/ảnh, không có reviewer độc lập/giấy phép, không có score calibration, không có độ khó đo thực tế. Không đặt độ khó tương đương như một tuyên bố thực chứng.

**Sources:** https://www.ets.org/pdfs/toeic/toeic-listening-reading-test-examinee-handbook.pdf ; https://www.ets.org/legal/permissions/licensing.html .
