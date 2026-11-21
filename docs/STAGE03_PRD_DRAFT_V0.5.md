# Product Requirements Document — TOEIC Learning App — DRAFT V0.5

**Stage:** 03 Requirements · **Status:** ANALYST WORKING DRAFT — NOT APPROVED / NOT MVP BASELINE · **Date:** 2026-11-21.

**Changes:** D03-REQ-007 R1–R4 **APPROVED AS DRAFTING PRINCIPLES**; content of individual requirements remains **CANDIDATE**. D03-QA-006 QA-01..08 approved *framework*, actual testing **NOT VERIFIED**. B1 **two Full Mocks mandatory**; two sets inventoried according to PO; budget DEFERRED. CP-01..05 still active. No UI/architecture/code.

## A. Why the product exists and whom it serves

- **Problem:** Người học TOEIC Listening & Reading hiện phải chuyển qua lại giữa đề, audio, đáp án và ghi lỗi; khó tạo thói quen học trong lịch không đều. Trên Android, Reading dài gây cuộn nhiều, mỏi mắt và khó đối chiếu đoạn văn.
- **Target:** nhóm 2–5 người thân tại Việt Nam; pilot bốn tuần; smartphone Android, online-first, TOEIC Listening & Reading. Mẫu nhỏ không đại diện thị trường.
- **Goal:** có thể luyện từng Part, làm **hai Full Mock** và học từ lỗi sai trong quy trình thống nhất; nhận tín hiệu kết quả luyện tập minh bạch và ý kiến trải nghiệm. **Không** hứa tăng 100–200 điểm sau bốn tuần.
- **Baseline caution:** ~550 là mock cá nhân, ~650 là điểm TOEIC chính thức của người học khác; không cộng/trừ trực tiếp hai chuẩn.

## B. Governance baseline — already approved, not optional

| GOV | Authority | Confirmed |
|---|---|---|
| GOV-01 | Vision V1.0 | Android L&R, pilot gia đình online-first, hành trình dài hạn cá nhân hóa và học liệu hợp lệ |
| GOV-02 | D03-LOCK-001=B1 | Hai Full Mock độc lập, mỗi đề 200 câu; không tự chuyển Part-only |
| GOV-03 | D03-SOURCE-004; rights attestation | PO đã kiểm kê xong hai đề, xác nhận quyền sử dụng 3 website và các nguồn khác; QA từng item chưa được kiểm toán |
| GOV-04 | D03-QA-006 | QA-01..08 là khung kiểm định đã phê duyệt; chưa có kết quả PASS |
| GOV-05 | D03-REQ-007 | R1–R4 được phép định hướng soạn Requirements, không tự duyệt các quy tắc con |
| GOV-06 | PO | Ngân sách DEFERRED, không hỏi, không dự toán, không mua; CP-04 vẫn được ghi nhận cho checkpoint phù hợp |

## C. User jobs / journeys / measurable exits

| Journey | Job-to-be-done | Observable exit | Candidate requirements |
|---|---|---|---|
| J01 | Chọn học theo thời gian rảnh | Phiên học bắt đầu với Part hoặc thời lượng đã chọn, không bắt buộc nghe gợi ý | FR-001,002,009,014 |
| J02 | Luyện câu L/R mà không chuyển nhiều công cụ | Nội dung đúng item/group, media/passage đúng, lựa chọn được ghi | FR-002..006 |
| J03 | Làm Full Mock A/B có tính đánh giá | Đúng form/7 Part; thời gian/lệch chuẩn và trạng thái attempt minh bạch | FR-010,011,013,019 |
| J04 | Học từ lỗi và ôn lại | Có danh sách sai, key chuẩn, lời giải được kiểm duyệt nếu có | FR-006..009 |
| J05 | Theo dõi tiến bộ | Báo correct/attempted, từng Part/section, form/date; không nhận điểm ETS | FR-008,012,013 |
| J06 | Quản lý nội dung đủ chuẩn | Chỉ phát hành version đạt kiểm duyệt; lỗi được sửa/thu hồi có dấu vết | FR-015..017 |
| J07 | Khôi phục sau gián đoạn, đọc Reading dài | Đáp án đã xác nhận không âm thầm biến mất; trạng thái thời gian/đề rõ | FR-004,005,018,019 |

## D. Candidate capability boundaries — NOT MVP LOCK

| Candidate | Assessment | Rationale/dependency |
|---|---|---|
| Part 1–7 với nội dung có QA | CANDIDATE — content contingent | Giải quyết học từng phần; cần bank riêng tránh lộ mock |
| **Hai Full Mock L&R A/B** | **B1 mandatory direction; release contingent** | 2 × 200, 45m L + 75m R; inventory PO-complete, QA execution open |
| Answer key, kết quả, lịch sử lỗi | CANDIDATE high priority | Phải nhất quán với content-version và quy tắc chấm |
| Học nhanh một câu / gợi ý theo quy tắc | CANDIDATE | Không mặc định là AI, vẫn cho người học tự chọn |
| Học liệu cá nhân và quản lý nguồn có quyền | CANDIDATE — controlled | Dùng học liệu PO sở hữu/quyền sử dụng; chưa cam kết parser PDF/audio tự động |
| Lời giải được QA | CANDIDATE conditional on availability | Không có thì báo rõ, không bịa |
| Lưu/khôi phục bài và dữ liệu tách riêng | CANDIDATE quality obligation | Chưa chọn login, DB, UI hoặc đồng bộ |
| AI giải thích/sinh câu, auto PDF + audio mapping, interactive vocabulary notifications | DEFERRED IDEA | Không cam kết MVP, cần quyết định riêng nếu muốn thêm |
| iOS/offline, TOEIC Speaking/Writing, thanh toán/quảng cáo | DEFERRED IDEA | Ngoài pilot Android L&R đầu tiên |

## E. Four approved drafting principles, product-level semantics

### R1 — Full Mock integrity, flexible practice

- **Mock evaluation candidate:** 100 Listening (~45m), sau đó 100 Reading (75m), các Part theo ETS. Hiển thị cho người học quy tắc thời gian, tiếp diễn, kết thúc và việc phiên bị gián đoạn có được xem là đủ điều kiện so sánh hay không.
- **Part practice candidate:** người học có thể chọn Part, thời gian/phiên một câu; không được trình bày kết quả luyện không giới hạn như một lượt mock thi thử chuẩn.
- **Open before baseline:** người học có được chủ động tạm dừng/replay Listening trong mock? Có tự kết thúc Listening lúc audio hoàn thành hoặc mốc thời gian? Xử lý gián đoạn, thoát, mạng và timeout thế nào? Đề xuất hành vi mặc định nằm trong D03-READY-008 (chưa duyệt).

### R2 — Results without false equivalence

- **Reported fields candidate:** form ID/version, ngày/lượt, submitted vs unanswered, correct/answered by Part, Listening, Reading, total; trạng thái attempt (hoàn tất/không hoàn tất/không đủ điều kiện so sánh).
- **Score claims:** đây là bài thi luyện tập và kết quả thô; không dùng thuật toán tự suy ra điểm ETS chính thức 10–990; hai đề chưa được equate thì so sánh đúng/sai chỉ mô tả thay đổi, **không chứng minh tăng năng lực**.
- **Integrity:** ảnh hưởng của đáp án sửa sau thi phải minh bạch, không tự ghi đè kết quả lịch sử.

### R3 — Error-to-practice loop

- Đáp án đúng được QA là điều kiện để chấm; giải thích chỉ hiện khi có nội dung đã kiểm duyệt; nếu thiếu phải ghi rõ. Người học có thể xem lại câu sai và chọn học ngắn.
- Gợi ý bài luyện chỉ dựa trên dữ liệu có sẵn và quy tắc rõ (Part yếu, mục tiêu, thời gian rảnh), có hành vi mặc định khi người mới chưa có lịch sử; không bắt buộc làm theo.
- Không đưa AI runtime, sinh câu hoặc importer PDF tự động vào scope bằng cách suy diễn từ từ “cá nhân hóa”.

### R4 — Pilot trust and privacy

- Mỗi đáp án đã xác nhận phải có trạng thái rõ, không âm thầm mất qua điều kiện nền/mất mạng/khởi động lại; nếu không thể bảo đảm cần báo lỗi và quy tắc khôi phục/hủy.
- Dữ liệu người học trong nhóm gia đình phải tách; quy tắc quyền truy cập, thu hồi và xóa dữ liệu phải được xác định trước pilot theo phương án tài khoản được PO duyệt sau.
- Reading dài và nhiều đoạn, ảnh/bảng phải đầy đủ khi hiển thị và có thể tiếp cận trên điện thoại Android; phương pháp UI vẫn chưa quyết định.

## F. Pilot observations — candidate indicators, not numeric success targets

| Ref | Evidence intended | Caveat |
|---|---|---|
| PM-01 | Completion/full mock A-B, validity status | Cần phân biệt hoàn tất và lần không đủ điều kiện so sánh |
| PM-02 | Raw correct/attempted/Part and section | Hai form có thể không tương đương độ khó |
| PM-03 | Part practices per week / duration chosen | N nhỏ; chỉ tín hiệu hành vi pilot |
| PM-04 | Wrong answers reviewed and lessons revisited | Không chứng minh retention dài hạn |
| PM-05 | Unsaved answer, media/timeout, Reading readability incidents | Chưa có target threshold do PO duyệt |
| PM-06 | Feedback 2–5 learners after four weeks | Không ngoại suy thị trường |

## G. Quality gates and unresolved decisions

- **G-content:** Hai Full Mock đã PO kiểm kê; **QA-01..06 actual item/media/duplicate audit evidence not provided**. Không yêu cầu người dùng kiểm kê lại hoặc tải corpus lên ngay. Nội dung không QA không được đánh dấu ready theo đề xuất.
- **G-results:** logic chấm điểm/report cần các AT cases có known answers và invalid attempts; kết quả actual thử app chỉ có sau giai đoạn coding/testing.
- **G-mobile/privacy:** yêu cầu bảo toàn lựa chọn, data isolation, lưu trữ/xóa và readability cần target/test phù hợp giai đoạn sau. Kiến trúc/tài khoản chưa chọn.
- **G-budget:** all work DEFERRED BY PO, **không xóa CP-04**, không tạo blocking spend question ở Stage03.
- **Pending PO grouped decisions:** D03-READY-008 (R1 detailed behavior, R4 retention, pilot acceptance ranges, formal scope/baseline pathway). Đây là gói định hướng kế tiếp, **không** đồng nghĩa stage Gate APPROVAL.

## H. Exit constraints and non-authorizations

Stage03 Gate chỉ nên xem xét sau một **quyết định PO riêng** về phạm vi MVP cụ thể, quy tắc nghiệm thu cần thiết và cách theo dõi các dependency mở. PRD V0.5 không phải baseline. Không thiết kế UX/UI, architecture, code, scraper, mua hàng hoặc phát hành theo tài liệu này.

**References:** ETS L&R format/score interpretation, Android lifecycle, Google Play user data policy — xem `STAGE03_REQUIREMENTS_EVIDENCE_LEDGER_V0.5.md`.
