# Content Gate cho 7 Part và 2 Full Mock V0.1 — Chưa đạt

**Status:** NOT VERIFIED / NOT READY FOR MVP COMMITMENT.

## Inventory yêu cầu
- TOEIC L&R: 7 Parts, 100 Listening + 100 Reading câu cho mỗi form, 120 phút làm bài.
- Form A: 200 mục riêng biệt; Form B: 200 mục riêng biệt; tổng 400 mục không trùng qua hai form; các nhóm Part 3/4/6/7 phải giữ đúng cấu trúc.
- Có nguồn quyền độc lập cho text, image, audio, key, explanations nếu khác chủ sở hữu; tham chiếu 100% câu và audio.
- Nếu có thêm Part practice, cần nguồn khác ngoài mock forms, hoặc phải ghi rủi ro người học nhớ đề khiến kết quả so sánh không còn đáng tin.

## Quality checklist
- [ ] Inventory 7 Parts được rà soát, mỗi item có SOURCE-ID và quyền dùng theo ngữ cảnh.
- [ ] Mỗi form đủ 200 câu (6+25+39+30+30+16+54), đúng nhóm bài.
- [ ] Mỗi câu có 1 đáp án chuẩn dựa trên nguồn và kiểm tra chéo; câu mơ hồ loại bỏ.
- [ ] Mỗi câu Listening ghép đúng audio/group; không phát thừa/thiếu/sai track.
- [ ] Part 1/3/4/7 hình, bảng, văn bản đủ bản quyền và khả năng đọc.
- [ ] Forms A/B không trùng mục kiểm tra; cơ sở so sánh độ khó được trình bày **trung thực về giới hạn**.
- [ ] Tách training bank khỏi evaluation bank để giảm test leakage.
- [ ] Không công bố scale ETS/990 nếu chưa có đánh giá tương đương có thể bảo vệ.
- [ ] Chế độ xem điểm phản ánh chính xác `raw_correct`/`percentage`/`internal diagnostic`; không ám chỉ official ETS.
- [ ] Có người chịu trách nhiệm duyệt việc sửa đáp án và ảnh hưởng tới lịch sử điểm.
- [ ] Chạy kiểm thử đầy đủ trên Android ở giai đoạn Testing trước pilot: 120 phút, audio, Reading dài, interruption, recovery.

## Chỉ số báo cáo bắt buộc ở review tiếp theo
| Metric | Giá trị hiện tại | Mức cần trước cam kết |
|---|---|---|
| Rights-cleared count Part 1..7 | UNKNOWN | Đủ định mức Part theo scope PO duyệt |
| Rights-cleared Mock A count | UNKNOWN | 200/200 |
| Rights-cleared Mock B count | UNKNOWN | 200/200 |
| Q/A mapping verified | UNKNOWN | 100% item dự kiến dùng |
| Listening audio matched | UNKNOWN | 100% item Listening dự kiến dùng |
| Level of mock comparability | UNKNOWN | Được mô tả rõ, phù hợp claim sản phẩm |
| Content acquisition cost | UNKNOWN | Bên dưới ngân sách PO cho phép |

## Gate action
- Nếu đạt: trình PO khóa danh sách yêu cầu và phê duyệt MVP riêng.
- Nếu chưa đạt: cung cấp 3 phương án B1/B2/B3 (B có mock; B thu gọn Part practice; A pre-pilot) và bản tradeoff, PO ra quyết định. Không tự chọn.
