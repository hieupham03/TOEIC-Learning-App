# PRD — TOEIC Learning App — Draft V0.4 (Consolidated)

**Status:** **WORKING DRAFT — NOT APPROVED, NOT MVP BASELINE**  
**Stage:** 03 Requirements, WP-03/04; **date:** 2026-11-21.  
**Evidence:** Product Vision V1.0 APPROVED; Stage 02 CONDITIONAL PASS; D03-LOCK-001=B1; D03-CONTENT-002=C; PO self-reported source rights and inventory of two Full Mocks; D03-QA-006 approves QA-01..08 *as a framework*.  
**Constraints:** CP-01..05 active. All budget actions DEFERRED BY PO. No UI, architecture, tooling, scraping, code or spending authorization.

## 1. Product outcome and target

**Problem:** Người học TOEIC L&R phải chuyển giữa đề, audio, đáp án, tiến độ; việc học theo thời gian rảnh và hiểu lỗi sai chưa thống nhất. Người dùng đã có trải nghiệm Full Mock trên điện thoại và phản ánh Reading dài gây mỏi mắt.  
**User:** pilot 2–5 người thân tại Việt Nam, 4 tuần, Android smartphone online first. Người học #1 khoảng 550 từ mock, #2 khoảng 650 từ thi TOEIC chính thức, **không trực tiếp so sánh hai baseline khác chuẩn**.  
**North-star pilot:** thu được tín hiệu tiến bộ **có thể diễn giải minh bạch** qua hai Full Mock cùng cấu trúc và QA, cùng thói quen học, học từ lỗi sai và trải nghiệm; 4 tuần **không** bắt buộc tăng 100–200 điểm. Không hứa so sánh tương đương TOEIC chính thức nếu chưa có hiệu chuẩn độ khó.

## 2. Confirmed governance / non-negotiable

| ID | Quyết định và ràng buộc | Nguồn | Tác động |
|---|---|---|---|
| GV-01 | Android, L&R, online-first, 2–5 pilot, 4 tuần | Vision Approved | Phạm vi nghiên cứu pilot |
| GV-02 | Hai Full Mock độc lập, mỗi đề đủ 200 câu, là điều kiện B1 bắt buộc | D03-LOCK-001 Approved | Không tự chuyển Part-only |
| GV-03 | Hai bộ đề đã kiểm kê xong theo PO; quyền với 3 web và nhiều nguồn theo PO | D03-SOURCE-004; D03-WEB-SOURCE-003 | Không bắt PO xác nhận lặp lại; QA từng item chưa chứng minh |
| GV-04 | QA-01..08 được PO duyệt **làm khung kiểm tra** | D03-QA-006 | Mọi gate/test không được tự đánh dấu PASS |
| GV-05 | Bỏ qua bước ngân sách hiện tại | PO 2026-11-21 | DEFERRED, không xóa CP-04 |
| GV-06 | Không khóa MVP/PRD/SRS/UI/kiến trúc/code | PO 2026-11-21 | Mọi đề xuất đều DRAFT |

## 3. Jobs and user journeys (business level, no UI)

| Journey | Ý định | Bắt đầu | Hoàn thành có thể kiểm chứng |
|---|---|---|---|
| J01 | Chọn thời lượng/Part hoặc bài gợi ý | Người học có quỹ thời gian | Vào được phiên hợp lệ, biết phạm vi và thời gian dự kiến |
| J02 | Học L&R liên kết media | Chọn một bài luyện Part | Câu, audio/ảnh/đoạn đọc đúng nhóm; lựa chọn và đáp án được ghi nhận |
| J03 | Làm Full Mock A hoặc B | Đề đã đủ QA, người học chọn chế độ đánh giá | Nộp hoặc kết thúc theo quy tắc thời gian rõ ràng, có thống kê minh bạch |
| J04 | Học từ lỗi sai | Có lịch sử câu đã làm | Xem lại câu/đáp án/bằng chứng; giải thích nếu có bản đã QA; thử lại nếu cho phép |
| J05 | Theo dõi tiến độ | Có các phiên học và mock | Xem dữ liệu đúng người và đúng phiên/Part; không suy diễn điểm ETS |
| J06 | Quản lý nội dung và sửa lỗi | Nguồn đề đã kiểm kê | Item/asset được kiểm duyệt, sửa/thu hồi có dấu vết, lịch sử không bị âm thầm sửa |
| J07 | Tiếp tục sau gián đoạn | Ứng dụng bị nền, mất mạng hoặc bị đóng | Không có mất đáp án đã xác nhận; trạng thái bài thi và thời gian được giải thích |

## 4. Candidate scope organized by need (NOT MVP IN/OUT approval)

| Module | Candidate status | Target behavior / dependencies |
|---|---|---|
| M-01 Bắt đầu và mục tiêu | CANDIDATE | Trình độ tự khai, mục tiêu, thời gian học linh hoạt; không cam kết thuật toán thích nghi |
| M-02 Luyện Part 1–7 | CONDITIONAL | Chỉ nội dung có đủ audio/ảnh/answer QA; lựa chọn Part và bài học ngắn |
| M-03 Hai Full Mock L&R | **MANDATORY B1, EXECUTION CONDITIONAL** | 2×200, 7 Part, quy tắc 45+75 phút; inventory PO confirmed, QA chưa chứng minh |
| M-04 Đáp án và xem lại lỗi | CANDIDATE | Chấm đúng key, lưu attempted/error, xem giải thích đã QA nếu có; không bịa |
| M-05 Thống kê học tập và tiến bộ | CANDIDATE | Số đúng/tổng câu, Listening/Reading/Part, metadata từng form, cảnh báo giới hạn so sánh |
| M-06 Chọn phiên theo thời gian rảnh | CANDIDATE | Người dùng tự chọn; gợi ý rule-based cần dữ liệu đầu vào hợp lệ, không phải AI |
| M-07 Quản lý nguồn đề theo quyền | CONDITIONAL | Nguồn và asset có ID; có thể import/nhập thủ công **bằng luồng được phép**, không yêu cầu parser PDF đa dụng |
| M-08 Tin cậy Android & dữ liệu | CANDIDATE | Không mất câu đã xác nhận; khôi phục phiên hợp lý; Part 7 đọc được; dữ liệu người học tách biệt |
| M-09 Học nhanh 1 câu | CANDIDATE | Trong app, không đồng nghĩa thông báo tương tác |
| M-10 Kho PDF/audio tự động | DEFERRED IDEA | Không cam kết import mọi PDF / mapping tự động |
| M-11 AI generation/explanation | DEFERRED IDEA | Chỉ đánh giá riêng sau; không là nguồn giải thích không QA |
| M-12 Vocabulary notification nâng cao | DEFERRED IDEA | Nhu cầu dài hạn đã ghi; không chốt MVP |
| M-13 iOS, offline, S&W, quảng cáo, paywall | DEFERRED IDEA | Không cam kết pilot đầu tiên |

## 5. Pilot observables (targets NOT BASELINED)

| ID | Chỉ số dự kiến | Cách đọc thận trọng |
|---|---|---|
| PM-01 | Tỷ lệ hoàn thành ít nhất một Full Mock / hai Full Mock | Không khẳng định tăng điểm nếu chỉ hoàn thành |
| PM-02 | Số đúng trên tổng, Listening, Reading, từng Part, theo form ID | Chỉ số kết quả luyện tập; hai form khác độ khó nếu chưa hiệu chuẩn |
| PM-03 | Số phiên luyện Part/tuần; thời lượng chọn vs thực tế | Tín hiệu thói quen, không đại diện thị trường với N=2–5 |
| PM-04 | Tỷ lệ câu sai có phản hồi; số lần ôn lại | Học từ lỗi sai cần quan sát thêm, không suy ra retention dài hạn |
| PM-05 | Sự cố mất đáp án, timeout, mapping audio, Reading readability | Chưa có benchmark hay test kết quả thực tế |
| PM-06 | Ý kiến định tính sau 4 tuần | Tổng hợp bất tiện, đặc biệt Reading dài và quy tắc gián đoạn |

**Guardrail:** Chỉ so sánh Mock A/B như dữ liệu luyện tập có giới hạn; không công bố bằng chứng tăng năng lực đã được hiệu chuẩn hoặc chuyển đổi 10–990 ETS khi chưa đủ phương pháp. Những mock đã bị lộ trước khi thi được đánh dấu không phù hợp cho so sánh.

## 6. Quality / rights / privacy gates

- **QA-01..08:** framework APPROVED under D03-QA-006; actual execution results unknown. Tất cả nội dung dùng trong pilot cần có key, media, group/passage và provenance kiểm soát được. Cần cách xử lý dữ liệu không đạt trước khi phát hành, không phải đánh dấu pass trong tài liệu.
- **Source rights:** PO self-attested reuse rights for 3 named websites and more. Ghi provenance theo item/asset để bảo trì; không tái chất vấn quyền sở hữu đã được khai báo; không suy ra quyền vượt qua các điều kiện chuyển giao/đăng lại chưa kiểm tra.
- **Privacy:** dữ liệu luyện tập của mỗi người tách biệt; quyền sửa/xóa và chính sách lưu trữ dữ liệu được đặc tả trước pilot nếu cần tài khoản. Chưa chọn phương án tài khoản hay cơ sở dữ liệu.
- **Mobile:** hiển thị ngữ liệu dài toàn vẹn; khôi phục sau việc Android kết thúc tiến trình, app nền, mất mạng phải có quy tắc cụ thể trước Stage Testing.
- **Budget:** DEFERRED BY PO; ghi dependency CP-04 ở future gate, không đưa thành yêu cầu quyết định trong gói này.

## 7. Unresolved grouped decisions — D03-REQ-007 (NOT YET APPROVED)

1. **Mock integrity:** đề xuất chế độ đánh giá giới hạn thời gian và quy tắc thoát/gián đoạn khác với phiên luyện Part tự do.
2. **Result semantics:** số đúng và thống kê Part, so sánh hai form có cảnh báo; không tuyên bố điểm ETS 990.
3. **Feedback and learning loop:** key bắt buộc; lời giải chỉ từ nội dung đã QA; gợi ý rule-based đơn giản + người học tự chọn.
4. **Pilot reliability/data:** lưu đáp án, phân tách dữ liệu và thử nghiệm Reading dài; không chọn cụ thể account, UI, stack.

Product Owner có thể duyệt **nguyên tắc soạn yêu cầu**, yêu cầu sửa, hoặc HOLD. Không lựa chọn nào tự phê duyệt MVP hoặc baseline nếu không có quyết định riêng.

## 8. Future Stage 03 gate / handoff

Trước khi đề xuất khóa MVP và Stage 03 Gate: nhận quyết định của PO về D03-REQ-007; làm rõ những hành vi còn TBD; liên kết SRS/acceptance/QA; phân loại nội dung B1 đã PO kiểm kê, và phân biệt tiến độ QA thực tế chưa hoàn tất. Budget gate được giữ là deferred theo quyết định hiện tại, phải trình lại khi đến mốc thích hợp chứ không lén coi đã xong.

**Not allowed:** UI mockup, app architecture, vendor selection, code/Codex, site scraping, spend, official score claims.
