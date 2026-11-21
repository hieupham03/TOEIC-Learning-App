# D05-ARCH-006 — Separate PO Decision: Candidate Architecture Direction V0.1

**Status:** **PENDING PRODUCT OWNER**. Prior approval `D05-ARCH03-005=A` grants only option comparison, **NOT** selection, architecture baseline, technology selection, Stage05 Gate, code/POC or spending.

## What PO can decide now

The following are **mutually exclusive choices at a conceptual evidence-responsibility level**, not framework/provider/database/clock decisions. All carry the same signed FR/NFR/QA/CP requirements and unverified evidence gaps. For any A/B/C, PO would authorize only *provisional direction to be refined under a separate controlled decision*, not feasibility PASS.

| Choice | PO decision effect if explicitly approved | Principle of uncertainty | Still expressly NOT authorized |
|---|---|---|---|
| **A — PROVISIONALLY SELECT ARCH03-A** | Prefer device-primary evidence-boundary hypothesis for future option refinement | Reboot/clock/data/identity and deletion proof missing | No stack, authority, backend/API/DB, tests/POC, code/spend, Gate |
| **B — PROVISIONALLY SELECT ARCH03-B** | Prefer independent-observation-led hypothesis for future refinement | Online outages/late ACK/privacy proof missing | Same exclusions |
| **C — PROVISIONALLY SELECT ARCH03-C** | Prefer evidence-convergence hypothesis for future refinement | Arbitration, correlation, complexity and source protection unproved | Same exclusions; no implied time/clock authority |
| **D — DEFER CONCEPTUAL SELECTION (ANALYST RECOMMENDATION)** | Keep A/B/C **UNCHOSEN**, retain exact comparison and ask PO later about a separately scoped evidence-planning checkpoint | Evidence remains 0 observed app proof; no falsifier was executed | No automatic next study, testing, architecture or Gate |
| **E — AMEND / HOLD** | Request a single grouped correction or preserve all studies without a selection | Re-review only named issue | No automatic technical authority |

### Why D is recommended now

This desk comparison has not verified any execution: **real Android devices 0, real learners 0, app test 0, content QA PASS 0, ARCH03 options 0 chosen**. While A/B/C are distinguishable hypotheses, the known unknowns materially affect their suitability; assigning a winner based on policy compliance tables alone could conceal false confidence. **D preserves progress** (finished option catalogue and full EV/FM trace), and places the burden of proof at proper future checkpoints; it does **not** ask PO to redo source inventory or reopen budget.

### What a future decision to select A/B/C must retain

1. **Selection is provisional conceptual direction**, not adoption of any framework, backend, API, DB, target Android version, service topology, clock authority or budget.
2. All FM01..18 and EV01..12 evidence obligations persist; only real evidence can close them. Numeric timing tolerances require explicit PO policy approval.
3. Full Mock B1 two 200-item sets, separate Part bank, signed integrity/ACK/privacy/deletion/raw-score policies, official Requirements/Design baselines remain fixed.
4. **Stage05 Gate**, ARCH-04 and all implementation or test actions require separate explicit PO approval; no implied next step.

### Suggested complete replies (examples, not current approvals)

- **A:** “Tôi, Product Owner, chọn D05-ARCH-006=A, tạm chọn **ARCH03-A ở cấp hướng phân bổ trách nhiệm bằng chứng** cho bước nghiên cứu tiếp, giữ nguyên mọi khoảng trống và CP. Chưa chọn công nghệ, clock authority, kiến trúc triển khai hay code/POC.”
- **B:** “Tôi chọn D05-ARCH-006=B, tạm chọn ARCH03-B trên giấy với các điều kiện tương tự.”
- **C:** “Tôi chọn D05-ARCH-006=C, tạm chọn ARCH03-C trên giấy với các điều kiện tương tự.”
- **D:** “Tôi chọn D05-ARCH-006=D, chưa chọn bất kỳ phương án kiến trúc nào; giữ V5.9 làm bộ so sánh, chỉ cho phép chuẩn bị một gói đề xuất checkpoint bằng chứng riêng, không mở ARCH-04 hoặc code.”
- **E:** “Tôi chọn D05-ARCH-006=E, HOLD/AMEND; giữ mọi phương án chưa chọn, chưa triển khai bước tiếp theo.”

## Bất biến và giới hạn thẩm quyền

- D03-SCOPE-009/B1: **hai Full Mock A/B độc lập, mỗi đề 200 câu** (100 Listening ~45 phút theo audio và 100 Reading 75 phút); Part practice có ngân hàng riêng. Hai đề **đã được PO xác nhận kiểm kê**, chưa QA từng câu/audio/đáp án/trùng lặp; không yêu cầu kiểm kê lại.
- Không cho phép tạm dừng tự nguyện hoặc replay tùy ý trong lượt Full Mock được xem là *clean/comparable*. Không có bằng chứng liên tục thì **không** gán clean/comparable. Không tự đặt ngưỡng grace/clock skew.
- Trạng thái **đã lưu** chỉ khi có bằng chứng ACK bền vững, đúng learner/form/attempt/item; thiếu ACK = **chưa thể xác nhận**, không phải mặc định thành công hay thất bại.
- Gia đình 2–5 người: cách ly dữ liệu người học; xóa theo yêu cầu hợp lệ trong **7 ngày lịch**, thời hạn lưu thông thường **không quá 30 ngày sau pilot** nếu không có ngoại lệ hợp pháp/đồng ý đã được ghi nhận.
- Kết quả chỉ là số đúng/đã làm theo Part/L/R/form/version; không khẳng định điểm ETS chính thức hoặc tăng năng lực thực nghiệm; giữ lịch sử sửa đáp án có truy vết.
- Baseline chính thức **không thay đổi**: PRD V0.6, SRS V0.6, Acceptance V0.4, Design Specification V0.3, UI-G01..16. 19 FR IN + 13 NFR có kiểm soát; tính năng FR020..023 OUT.
- **CP-01..05, G03-CP01..07, G04-CP01..08 ACTIVE**; QA-01..08 **chỉ là framework APPROVED, chưa có kiểm thử PASS**; UX04-I01..08 và UIA-01..08 còn mở.
- **ALL BUDGET WORK DEFERRED BY PO**. Không chi tiêu, nhận báo giá, chọn nhà cung cấp trả phí, cào nội dung, dùng corpus thực, thử Android/người học, viết code/POC; không mở Stage05 Gate.
- ARCH-03 là **các giả thuyết bố trí trách nhiệm để so sánh trên giấy**, *không phải* thiết kế hệ thống đã được thông qua; chưa chốt framework, backend, API, database, cloud, chủ thể quyết định giờ, kiến trúc hoặc giao thức.


**Default:** Decision PENDING, all ARCH03 candidates **UNCHOSEN**, Stage05 **IN PROGRESS**.
