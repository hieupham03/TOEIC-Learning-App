# TOEIC Learning App — Stage 02 Gate Review V1.0

**Ngày rà soát:** 2026-11-21  
**Dự án:** TOEIC Learning App  
**Giai đoạn được đánh giá:** 02/11 — Market Research & Validation  
**Trạng thái hiện hành:** IN PROGRESS / GATE DECISION PENDING  
**Phương pháp:** Evidence-First / Secondary Research First — D-025A–B theo chỉ đạo PO, D-025C–F đã được PO phê duyệt ở phiên hiện tại  
**Product Vision:** V1.0 APPROVED (2026-11-20), bảo toàn nguyên trạng.  
**Không bắt đầu Stage 03, không duyệt MVP, PRD/SRS, UX/UI, kiến trúc, code.**

## A. Executive Gate Recommendation

**ĐỀ XUẤT: CONDITIONAL PASS — CHƯA PHẢI QUYẾT ĐỊNH CỦA PRODUCT OWNER.**

Có đủ hiểu biết về *problem*, nhóm người dùng pilot, kênh Android, định dạng TOEIC và các mô hình luyện tập đang tồn tại để lập yêu cầu sản phẩm. Chưa đủ bằng chứng về việc số hóa bộ đề PDF/audio cá nhân chính xác, quyền sử dụng học liệu, độ tin cậy điểm mock, chất lượng AI và lợi thế thị trường thật sự. Có thể quản trị các vấn đề này qua yêu cầu/kiểm thử chuyên biệt, không cần chặn Stage 03 chỉ vì thiếu thử nghiệm solo hoặc người dùng không tải được file mẫu.

### PASS / CONDITIONAL PASS / HOLD — tiêu chuẩn và tác động

| Phương án | Ý nghĩa | Điều kiện áp dụng | Đánh giá |
|---|---|---|---|
| PASS | Stage 02 đã đủ cơ sở không kèm điều kiện; PO quyết định Stage 03 | Vấn đề trọng yếu hầu hết đã được giải quyết với tài liệu nguồn thích hợp | **Chưa nên:** content/score/AI chưa xác minh |
| **CONDITIONAL PASS** | Chấp nhận đủ evidence để sang giai đoạn đặc tả, chuyển open risks thành constraints và later quality gates | PO đồng ý CP-01–CP-05, không ngầm duyệt scope/MVP | **RECOMMENDED** |
| HOLD | Giữ Stage 02, tập trung giải quyết blocking uncertainties trước khi lập requirements | PO không chấp nhận rủi ro tồn đọng hoặc insist importer/official-equivalent score ngay từ bản đầu mà chưa có nguồn | Có thể chọn, nhưng tốn thêm thời gian |

## B. Checklist Stage 02 — Evidence & Gate scorecard

| Gate ID | Tiêu chí | Bằng chứng | Mức đánh giá | Ý nghĩa |
|---|---|---|---|---|
| G02-01 | Vision và phạm vi khách hàng | Vision V1.0 approved, pilot 2–5 người, Android/online | PASS | Có tầm nhìn rõ; không suy ra toàn thị trường |
| G02-02 | Pain/JTBD được xác định | Người #1 trực tiếp báo cáo ma sát PDF/audio/đáp án, lịch thất thường; #2 gián tiếp tương tự | PASS FOR FAMILY PILOT | Không có khảo sát đại diện hoặc nhu cầu trả phí |
| G02-03 | Benchmark giải pháp hiện có | ETS format; STUDY4 full/part practice/review; PREP/Migii lộ trình | PASS | Standard flows đã có, khác biệt phải tinh hơn |
| G02-04 | Cơ sở phương pháp học | Nghiên cứu spaced practice, retrieval, feedback, học từ trên mobile | PASS WITH BOUNDARY | Không đảm bảo app sẽ nâng điểm TOEIC |
| G02-05 | Android format fit | PO từng full mock, gặp Reading dài bất tiện và mỏi mắt | CONDITIONAL | Có tín hiệu dùng được; còn vấn đề UX/long-session quality |
| G02-06 | Personal library value & ingest | Nhiều tệp PDF/sách/audio có sẵn nhưng chưa kiểm tra mẫu | OPEN | Value plausible; feasibility/provenance không được xem validated |
| G02-07 | Content rights/supply | Google Play IP policy; nguồn tài liệu chưa kiểm kê quyền | OPEN — HIGH | Không được hứa public distribution chưa có quyền |
| G02-08 | Measurement/scoring quality | ETS cần kiểm soát tính nhất quán test forms | OPEN — HIGH | Không khẳng định raw correct -> điểm TOEIC chuẩn |
| G02-09 | AI quality & cost | Chưa có PoC/chấm mẫu/OPEX chứng minh | OPEN — HIGH | AI giữ optional; chất lượng/cost gate đi sau |
| G02-10 | Validation method & deferred work | PO duyệt evidence-first; VAL-013 optional; VAL-003/010 deferred | PASS ON PROCESS | Không yêu cầu lại baseline chỉ để đủ checklist |

## C. Phân tích bằng chứng — facts vs hypotheses

### C1. Đủ vững để lập yêu cầu

- **Cấu trúc kỳ thi:** TOEIC Listening & Reading chuẩn có 2 phần, mỗi phần 100 câu; 45 + 75 phút, tổng thời gian làm bài 120 phút, 7 Part [E01].
- **Chuẩn luyện đề thông dụng:** STUDY4 công bố luyện full/part, lựa chọn thời gian, nghe, xem đáp án, tự chữa, thống kê [E02]. PREP công bố kho luyện thi và Migii công bố lộ trình theo trình độ và mục tiêu [E03–E04]. Đây là *benchmark*, không tự động là chất lượng được kiểm chứng độc lập.
- **Nền tảng khoa học:** Spacing, retrieval practice và feedback có bằng chứng học thuật giúp học và ghi nhớ trong những ngữ cảnh nghiên cứu cụ thể [E06–E07]. Không chứng minh việc thông báo từ vựng sẽ tăng điểm TOEIC.
- **Nhóm pilot:** PO tự báo cáo trực tiếp rằng workflow trên PC bị phân mảnh và mong Android vừa học từng Part vừa làm full mock; đã hoàn thành một full mock Android nhưng bị bất tiện Reading/mỏi mắt. Người #2 do PO kể lại nên chưa có xác nhận trực tiếp [U01–U03].

### C2. Tính năng kế thừa nhưng chưa nên gọi là lợi thế độc nhất

- Full Mock, Part Practice, chọn thời lượng, kiểm tra đáp án, lịch sử lỗi sai và lộ trình học đã có sản phẩm cung cấp/công bố. Không gọi chung chung là USP của dự án.
- Quizlet hỗ trợ chuyển nội dung/tệp thành *flashcards* trong điều kiện đủ quyền truy cập [E05]; **không chứng minh** nhập đề TOEIC PDF và audio chính xác. Hơn nữa, tính năng nhập của Quizlet có giới hạn tài khoản, ngôn ngữ và khu vực; danh sách được công bố tại thời điểm rà soát không có Việt Nam.
- Giả thuyết khác biệt hợp lý để đưa vào đặc tả nghiên cứu: **thư viện học liệu cá nhân hợp lệ → luyện đề thống nhất → phân tích lỗi → gợi ý học theo thời gian rảnh**, trong một trải nghiệm Android; giá trị và độ khả thi riêng phải được thử ở pilot hoặc spike có mục tiêu.

### C3. Rủi ro không thể suy luận vượt dữ liệu

- **Tài liệu cá nhân:** File sẵn trên laptop không chứng minh chất lượng, quyền dùng hoặc pipeline importer. **VAL-003 deferred**, không đánh dấu fail/pass.
- **Quyền nội dung:** Google Play cấm vi phạm copyright ngay cả khi sửa đổi nội dung; cần ma trận nguồn/giấy phép khi định nghĩa mô hình học liệu và trước phân phối [E11].
- **Mock-score:** ETS áp dụng điều chỉnh, kiểm soát độ khó để các forms có tính so sánh; mọi đề tùy ý không tự sinh ra điểm 990 tương đương [E12].
- **AI:** Chưa có đánh giá độ chính xác giải thích, chi phí, sai sót; không lấy kết quả demo AI chung làm chứng cứ chất lượng sản phẩm.
- **Thông báo:** Android hỗ trợ tối đa 3 action buttons và kiểm soát quyền; người dùng muốn 4 hành vi, phải giải quyết ở Stage 04/QA nếu đưa vào scope [E08–E10].
- **Mobile UX:** Nhu cầu full mock Android có thật với PO, đồng thời Reading dài và mỏi mắt là pain trực tiếp; đưa accessibility/usability vào điều kiện nghiệm thu sau thay vì duyệt một giao diện giả định.

## D. Risk register và các điều kiện cần để Conditional Pass

Chi tiết tại `docs/STAGE02_TO_STAGE03_OPEN_RISKS_V1.0.md`. Cần PO chấp nhận các điều kiện:

1. **CP-01 — Giới hạn ủy quyền:** Qua Stage 02 chỉ cho phép bước **phân tích yêu cầu** sau một quyết định Gate riêng; không chốt PRD/SRS/MVP/architecture/UI/code.
2. **CP-02 — Chưa ràng buộc feature speculative:** Import PDF/audio tự động, AI, kết quả quy đổi 990, tính năng thông báo và cả 3 chế độ trải nghiệm chưa được cam kết là MVP.
3. **CP-03 — Quyền nguồn:** PRD/SRS sau phải quản lý provenance/license và điều kiện tài liệu cá nhân vs chia sẻ/phát hành; không được tải lại/công khai tài liệu chưa rõ quyền.
4. **CP-04 — Quality & cost:** Tạo tiêu chí kiểm tra nội dung, AI, mock scoring, reading long-form, nguồn đề và ngân sách pilot; hoàn tất các kiểm thử tương ứng trước khi có tính năng vận hành/ship.
5. **CP-05 — Không dựng thêm nghi thức validation:** Hai baseline PC `VAL-013L/R` vẫn `NOT RUN / OPTIONAL / ON HOLD`; `VAL-003` PDF/audio và `VAL-010` giá vẫn `DEFERRED`, không xem chúng là kết quả giả hoặc blockers chung.

**Blocker thật sự đối với Gate tiếp theo:** Nếu PO đòi cam kết ngay import tự động bộ đề chưa nhìn thấy, tái phân phối tài liệu không có quyền, hoặc công bố điểm 990 tương đương ETS từ đề bất kỳ thì không thể Conditional Pass trên cơ sở bằng chứng hiện tại; cần HOLD hoặc loại claim khỏi scope.

## E. Chuyển giao tới Stage 03 — chỉ nếu Gate được phê duyệt

Đầu ra Stage 03 cần đề xuất (chưa khởi tạo, chưa phê duyệt):

- PRD/SRS có traceability: Vision → Jobs-to-be-Done → user flows → yêu cầu → acceptance criteria → kiểm thử.
- Ưu tiên MVP theo **value/risk/cost**, gồm phương án fallback học liệu structured/manual nếu importer phức tạp; tuyệt đối không mặc nhiên chốt cả ba chế độ ngay.
- Content provenance/license matrix + nguồn tài liệu tối thiểu hợp pháp cho pilot; đánh giá quyền share/cloud/AI theo từng tập dữ liệu.
- Plan thẩm định audio–question–answer mapping, accuracy, khả năng import theo từng dạng PDF, và ngưỡng lỗi (không tự tạo ngưỡng hôm nay).
- Measurement framework: đúng/sai và tiến bộ từng Part được tách khỏi ước lượng điểm TOEIC; so sánh score giữa forms chỉ nếu có validation.
- AI quality gate + OPEX guardrails + non-AI fallback; notification opt-in; mobile Reading accessibility & interruption acceptance.
- Pilot 4 tuần, 2–5 người, đánh giá mức tiện, nhu cầu, duy trì học và chất lượng kết quả; không khẳng định thị trường rộng đã chứng minh nhu cầu.

**Cấm hiểu nhầm:** Conditional Pass KHÔNG phải phê duyệt MVP, PRD, SRS, UX/UI, architecture hoặc code; đó chỉ là điều kiện cho phép **bắt đầu thu thập và viết dự thảo yêu cầu trong Stage 03** khi PO phê duyệt Gate.

## F. Quyết định & trạng thái

| ID | Nội dung | Trạng thái |
|---|---|---|
| D-025A | Evidence-first | APPROVED per PO directive |
| D-025B | VAL-013L/R optional, không chặn Gate | APPROVED per PO directive |
| D-025C | Benchmark theo sản phẩm luyện đề hiện có; khác biệt ở library + workflow | **APPROVED BY PO** |
| D-025D | Nguyên lý spaced/retrieval/feedback, không đồng nhất notification | **APPROVED BY PO** |
| D-025E | Định thời điểm quản lý rủi ro nội dung/AI/scoring | **APPROVED BY PO** |
| D-025F | Chuẩn bị và trình Gate Review, Stage 03 chỉ khi PO duyệt Gate | **APPROVED BY PO** |
| G02-GATE | PASS / CONDITIONAL PASS / HOLD | **PENDING PO DECISION** |

**Kết luận trình PO:** CONDITIONAL PASS (CP-01–CP-05). Alternatives: PASS khi PO chấp nhận độ thiếu chứng cứ như không cần điều kiện (không khuyến nghị); HOLD nếu điều kiện không chấp nhận được hoặc cần chứng minh nhập đề trước Requirements.

## G. Nguồn

Chi tiết, loại bằng chứng, giới hạn và liên kết được ghi ở `docs/STAGE02_EVIDENCE_SOURCE_LEDGER_V1.0.md`; báo cáo không tự tạo số liệu thí nghiệm, phỏng vấn hoặc báo giá.
