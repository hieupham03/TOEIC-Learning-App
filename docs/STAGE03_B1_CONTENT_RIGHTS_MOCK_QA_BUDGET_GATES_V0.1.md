# B1 — Điều kiện khả thi / khóa MVP (Gate Matrix V0.1)

**Status:** ANALYST PROPOSED CRITERIA; PO approved B1 decision, not thresholds. **Date:** 2026-11-21.

## 1. Phân biệt các mốc kiểm soát
- **Giai đoạn hiện tại (Stage03):** Chỉ xây dựng và rà soát yêu cầu, kiểm kê bằng chứng, trình quyết định khóa MVP khi readiness rõ ràng.
- **Gate khóa MVP tương lai:** PO chấp thuận danh mục MVP và điều kiện; **không tự động cho phép thiết kế/code**. Nếu bằng chứng chưa đủ, không trình PASS.
- **Gate trước khi dùng học liệu trong pilot/phát hành:** quyền, QA từng asset, bài thi, âm thanh, nội dung và tính an toàn phải chứng minh thực tế. Không coi việc ghi điều kiện trên giấy là pass.

## 2. Ma trận gate
| ID | Hạng mục | Điều kiện đề xuất để trình khóa B1 | Bằng chứng cần xuất trình | Hiện trạng | Người chịu quyết định |
|---|---|---|---|---|---|
| G-B1-01 | Blueprint & inventory | Hai form A/B đủ **200 câu mỗi form**, 100 L/100 R, đúng số câu ở các Part; item ID độc lập | Hai manifest đầy đủ, số đếm, asset group | RED: chưa có manifest | PO duyệt scope; reviewer nội dung QA |
| G-B1-02 | Sự độc lập của 2 form | Không trùng item giữa A/B; không sử dụng item trong ngân hàng practice trước khi đánh giá | Báo cáo trùng ID/text/audio, item-exposure policy | RED | Content QA + PO |
| G-B1-03 | Pháp lý, nguồn gốc | Phân loại từng asset và giấy phép cho **số hóa, biến đổi, host, stream, chia sẻ 2–5**, lãnh thổ và thời hạn; không có asset UNKNOWN trong nội dung dự định phát cho người học | Rights inventory, tác giả/owner, file hợp đồng/permission, credit lines | RED: chưa có bản quyền được kiểm chứng trong hồ sơ | PO + pháp lý (khi cần) |
| G-B1-04 | Nghe/đọc đúng | Mỗi item có đáp án gốc đã kiểm tra; audio đúng group, speaker, thứ tự/câu, và hình ảnh/đoạn văn đúng; tất cả lỗi trọng yếu đã biết phải xử lý trước pilot | QA log, checklist link, audit report | RED: chưa chạy | Content QA |
| G-B1-05 | Độ khó và mục tiêu điểm | Hai đề cùng cấu trúc, được chuyên gia nhận xét theo Part/độ khó; ghi rõ độ bất định so sánh; **không khẳng định psychometric equating hay điểm ETS** | Item review rubric, form-review memo, reporting language | RED: thiếu QA/độ khó | Content advisor + PO |
| G-B1-06 | Công sức và chi phí | Có bảng ước lượng có cơ sở + trần VNĐ 1 lần, trần OPEX 4 tuần, giờ công QA và contingency, giới hạn chi trả được PO ký duyệt | Cost workbook/estimate + decision sheet | AMBER/RED: có public list prices nhưng không có caps/quotes | PO |
| G-B1-07 | Trải nghiệm Android | Mô tả tiêu chí mỏi mắt/Reading dài, gián đoạn, mất tiến độ, audio và thời gian phiên thi; **kiểm thử sau khi có sản phẩm** | Requirement & acceptance plan trước scope lock; test results ở gate sau | AMBER | PO + QA |
| G-B1-08 | Phạm vi phụ thuộc | Có đủ nguồn practice độc lập để vận hành các chức năng luyện từng Part đã cam kết; không làm lộ đề đánh giá | Manifest practice + partition constraints | RED | Content lead + PO |

`RED` = **thiếu bằng chứng trong dự án**, không khẳng định ngoài đời không có học liệu. G-B1-07 không yêu cầu chứng minh trải nghiệm bằng app chưa được phát triển trước khi khóa scope; chỉ yêu cầu acceptance plan, kiểm chứng ở gate thích hợp.

## 3. QA tối thiểu — đề xuất (chưa phải ngưỡng phê duyệt)
- **100% item** trong 2 mocks có nguồn, ID, Part, đáp án và metadata liên kết; **100% audio/image/passage groups** được kiểm tra ánh xạ. 100% nghĩa là phải có kết quả kiểm tra toàn bộ, không phải cam kết không có sai sót.
- **Không còn lỗi nghiêm trọng đã biết** có thể làm câu không thể trả lời, đáp án sai, phát nhầm audio/hình/đoạn, lỗi giấy phép hoặc mất bài.
- Tổ chức **ít nhất hai vòng QA** đề xuất: kiểm tra biên soạn/kỹ thuật và rà soát độc lập bởi người đủ năng lực, tránh coi người tạo nội dung là người phê duyệt duy nhất (nếu không có người độc lập, ghi rõ hạn chế và escalated PO decision).
- Có **chính sách thay item lỗi, lưu dấu phiên bản, chặn nội dung chưa duyệt**; sample review riêng không thay cho full audit cuối.
- **Score communication:** số câu đúng, tỷ lệ đúng, breakdown theo Part và thời điểm; không dùng nhãn điểm ETS chính thức/“tăng X điểm TOEIC” nếu chưa có căn cứ equating. Hai đề có thể cho tín hiệu tiến bộ, không phải kết luận nhân quả.

## 4. Phân tách trạng thái
`PROPOSED` = tiêu chí chuyên môn trong tài liệu; `EVIDENCE PENDING` = chưa có chứng từ; `REVIEWED` = đã rà soát; `PASS` = có biên bản duyệt đúng gate; `HOLD` = thiếu bằng chứng quan trọng. Không ghi PASS chỉ vì PO chọn hướng B1.

## 5. Source references
ETS format & counts: https://www.ets.org/pdfs/toeic/toeic-listening-reading-test-examinee-handbook.pdf (p.1 print / PDF p.7). ETS psychometric equating: cùng tài liệu (p.5 print / PDF p.11). ETS licensing: https://www.ets.org/legal/permissions/licensing.html. Google Play IP: https://support.google.com/googleplay/android-developer/answer/18265346.
