# TOEIC Learning App — Proposed Stage 03 Requirements Kickoff Plan V0.1

**Prepared:** 2026-11-21  
**Stage 02 Gate:** CONDITIONAL PASS — PO APPROVED, CP-01..CP-05 accepted.  
**Status:** **PROPOSAL / PENDING PO KICKOFF APPROVAL**. NOT an approved PRD, SRS, MVP, UI or architecture.

## 1. Mục tiêu giai đoạn

Chuyển Product Vision V1.0 + kết quả Evidence-First Stage 02 thành **các lựa chọn phạm vi sản phẩm, yêu cầu có thể kiểm chứng và điều kiện chất lượng**, để Product Owner duyệt từng quyết định có tác động lớn. Không thiết kế giao diện, lựa chọn stack, dựng backend hoặc lập trình.

### Khóa ranh giới

- Kênh pilot hiện tại: **Android smartphone, online-first**; 2–5 người học gia đình trong **4 tuần**. Không biến đó thành phê duyệt MVP.
- Định hướng giá trị: đánh giá năng lực, lộ trình cá nhân, bài luyện Listening/Reading, phiên học linh hoạt, phân tích lỗi/tiến bộ; **library tài liệu cá nhân là hypothesis chiến lược**.
- Hiện trạng học liệu: có PDF/sách/audio được báo cáo là sẵn có; **chưa xác minh nội dung, trích xuất hay quyền sử dụng**.
- Full Mock 200 câu / 120 phút và luyện từng Part đều là nhu cầu trải nghiệm; **chưa mặc định cả hai nằm trong MVP**. Không đánh đồng mock score tự tạo với điểm ETS.
- Ràng buộc của PO: thời gian phát triển linh hoạt, chi phí pilot thấp; chỉ lấy thông tin từ người dùng khi nguồn công khai không đủ cho quyết định quan trọng. **Không hỏi từng câu Validation kéo dài.**

## 2. Work packages (thực hiện sau khi PO duyệt kickoff)

| WP | Nội dung công việc | Kết quả bàn giao (DRAFT, chưa được PO duyệt trước) | Điều kiện kế thừa |
|---|---|---|---|
| **WP-01 — Scope & User Needs** | Tổng hợp persona/JTBD, journey cấp nghiệp vụ, problem statements, goal và non-goal; tạo traceability từ Vision và evidence | `REQUIREMENTS_INPUT_BASELINE_V0.1.md`, `USER_JOURNEYS_V0.1.md` | Vision V1.0, G02 ledger; không vẽ UI |
| **WP-02 — Product Options & MVP Decision Pack** | Chia capability thành must/should/later dựa value–risk–effort/cost; so sánh **3 phạm vi đề xuất** (tối giản / cân bằng / mở rộng) và fallback | `MVP_OPTIONS_AND_TRADEOFFS_V0.1.md`, `SCOPE_DECISION_LOG_V0.1.md` | **PO duyệt scope trước khi gọi bất kỳ option nào là MVP** |
| **WP-03 — Requirements Draft** | Viết PRD draft rồi SRS draft theo user stories, flows nghiệp vụ, tình huống lỗi, acceptance criteria; bao gồm Listening/Reading, tiến độ, nội dung, tài khoản theo scope PO chọn | `PRD_DRAFT_V0.x.md`, `SRS_DRAFT_V0.x.md`, `REQ_TRACEABILITY_MATRIX_V0.1.md` | Chỉ **dự thảo**, không tự chốt baseline SRS |
| **WP-04 — Quality, Content Rights, Cost & Risk** | Content provenance/license matrix; content supply/fallback; audio–question–answer mapping, AI uncertainty, mock scoring/score claims, privacy/security, Android long-form usability, notification permissions, chi phí vận hành | `CONTENT_RIGHTS_MATRIX_V0.1.md`, `QUALITY_AND_ACCEPTANCE_PLAN_V0.1.md`, `RISK_REGISTER_V1.x.md`, `PILOT_METRICS_V0.1.md` | CP-02..CP-05; rủi ro chưa có bằng chứng vẫn OPEN |
| **WP-05 — Requirements Gate Review** | Tổng hợp requirement coverage, conflicts, cost/risk, decision log, số unknowns high severity; đề xuất Stage03 PASS / CONDITIONAL PASS / HOLD | `STAGE03_REQUIREMENTS_GATE_REVIEW_V0.1.md` và PO signoff sheet | PO quyết định gate, **không tự khởi động UX/UI/architecture/code** |

**Trình tự khuyến nghị:** WP-01 → **PO review gói phạm vi WP-02** → WP-03 và WP-04 đồng bộ theo scope đã được PO chấp thuận → WP-05. Không chốt lịch cứng hoặc bắt người dùng tham gia kiểm thử thủ công chỉ để hoàn thành tài liệu.

## 3. Phân nhóm yêu cầu để phân tích, CHƯA phê duyệt MVP

| Capability | Mục đích | Ranh giới / giả định hiện tại |
|---|---|---|
| Source & content | Câu hỏi/đáp án/audio/transcript/lời giải nguồn hợp lệ | Fallback: nội dung có cấu trúc nhập có kiểm soát hoặc tự biên soạn; auto-PDF importer chưa được bảo đảm |
| Part Practice L&R | Phiên học linh hoạt theo Part và thời lượng | Đánh giá cần đủ 7 Part ngay trong pilot hay theo giai đoạn |
| Full Mock | Đánh giá tiến bộ qua đề có thể so sánh | Điểm nội bộ/độ chính xác khác với score tương đương TOEIC chính thức |
| Diagnostics & recommendations | Phát hiện lỗ hổng, gợi ý bài theo lịch rảnh | Bắt đầu từ rule-based cũng là một phương án; AI chưa phê duyệt |
| Error review & learning record | Hỗ trợ retrieval, spaced review và theo dõi lỗi | Lịch ôn là hypothesis implementation, không cam kết tăng điểm |
| Interactive vocabulary notification | Học ngắn, tự kiểm soát nhắc nhở | 4 hành vi mong muốn nhưng Android tối đa 3 action buttons; có quyền opt-out, chưa chốt MVP |
| Accounts/consent/data | Tài khoản pilot, quản lý thông tin học tập | Phải cân nhắc quyền riêng tư, xóa dữ liệu, chi phí vận hành; chưa chọn stack |

## 4. Quality/acceptance gates được chuyển giao

| Gate | Điều kiện đưa vào Requirements | Gate muộn nhất để kiểm chứng |
|---|---|---|
| Q-CONTENT | Nội dung có nguồn, quyền sử dụng hợp lệ cho ngữ cảnh; câu–đáp án–audio đúng | Trước xử lý/phát hành nội dung tùy quyền và trước pilot |
| Q-IMPORT | Định nghĩa input hỗ trợ, tỉ lệ lỗi cho mỗi loại PDF/audio, kiểm tra thủ công và fallback | Trước cam kết auto import vào MVP |
| Q-AI | Kiểm định lời giải/câu hỏi AI; hiển thị nguồn và có fallback non-AI; ngân sách token/OPEX | Trước bật AI cho người học |
| Q-MOCK | Không tuyên bố điểm chính thức/điểm quy đổi nếu không có căn cứ; phân biệt % đúng, điểm nội bộ và ước lượng | Trước công bố hoặc so sánh tiến bộ bằng điểm TOEIC |
| Q-UX | Độ đọc được Part 6/7, mỏi mắt/gián đoạn/mất tiến độ Full Mock Android | Trước nghiệm thu pilot/UX liên quan |
| Q-COST | Chi phí vận hành pilot 2–5 người và giới hạn OPEX | Trước chốt scope có chi phí/chạy pilot |
| Q-PRIVACY | Sự đồng ý, bảo mật tài khoản/dữ liệu học, phạm vi chia sẻ nội dung | Trước xử lý dữ liệu người dùng ngoài phạm vi xác định |

Các ngưỡng định lượng chính xác được **đề xuất trong PRD/SRS draft rồi trình PO duyệt**, không tự ghi thành đã quyết định.

## 5. Deliverable acceptance criteria cho Stage 03

1. **Traceability:** Mỗi nhóm requirement có Vision goal/JTBD/evidence, mức ưu tiên, người dùng và acceptance criteria; unknown được ghi rõ.
2. **Scope decision:** MVP với các chức năng in/out và thứ tự ưu tiên được **PO phê duyệt riêng** sau khi xem ít nhất một phương án tiết kiệm chi phí và một phương án cân bằng.
3. **Rights readiness:** Phân biệt nội dung dùng riêng cá nhân, lưu cloud, upload AI, phân phối ra public; không có mặc định “sở hữu PDF = được chia sẻ”.
4. **Feasibility boundary:** Không cam kết PDF/audio importer, AI, điểm chuẩn hoặc kênh thông báo nếu thiếu test gate, dự toán hoặc fallback.
5. **Quality readiness:** Có yêu cầu kiểm thử cho score consistency, data quality, Learning UX, privacy, security, cost và phục hồi phiên học.
6. **Owner signoff:** PO duyệt PRD/SRS baseline, Risk Register và Stage 03 Gate; chưa tự bước vào UI/architecture.

## 6. Phương pháp quyết định nhanh

- ChatGPT chủ động tổng hợp evidence hiện có, có nguồn và **phân loại official/publicated/self-report/unknown**; không hỏi lại những gì PO đã trả lời.
- Chỉ đưa ra **2 hoặc 3 gói phê duyệt quan trọng** ở các điểm WP-02, PRD/SRS baseline và Stage 03 Gate; gom các lựa chọn liên quan thay vì hỏi hàng loạt câu nhỏ.
- PO có thể `APPROVE / APPROVE WITH CHANGES / HOLD` mỗi gói; ChatGPT cập nhật decision register và giữ nguyên ranh giới phê duyệt.
- Codex chỉ được mời tham gia giai đoạn triển khai kỹ thuật sau một ủy quyền mới; **không viết code ở Stage 03**.

## 7. Quyết định PO cần đưa ra ngay

**Chỉ duyệt hoặc chỉnh sửa KẾ HOẠCH KHỞI ĐỘNG Stage 03**, không phải quyết định MVP:

- **A — APPROVE KICKOFF PLAN:** Cho phép bắt đầu WP-01 Requirements Input Baseline, sau đó trình phương án scope WP-02; các điều kiện CP-01..05 tiếp tục áp dụng.
- **B — APPROVE WITH CHANGES:** Chỉnh phạm vi/phương pháp/deliverables; chỉ bắt đầu khi đã chấp nhận bản điều chỉnh.
- **C — HOLD KICKOFF:** Stage 02 vẫn Conditional Pass, Stage 03 chưa bắt đầu.

**Important:** Hồ sơ này là bản kế hoạch đề xuất, không xác nhận bất cứ option MVP nào đã được chấp thuận.
