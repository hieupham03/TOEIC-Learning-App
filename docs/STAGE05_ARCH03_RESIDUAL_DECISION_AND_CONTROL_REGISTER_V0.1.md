# Stage05 ARCH-03 — Residual Authority, Assumption and Dependency Register V0.1

**Scope:** records what each future PO decision would need to choose, and what is *not* authorized now.

| ID | Unchosen decision / assumption | Why ARCH03 cannot decide it | Future prerequisite or veto | Control anchor |
|---|---|---|---|---|
| U-01 | Time authority and clock-skew/grace | Multiple elapsed accounts need evidence across reboot/outage | PO numeric timing policy + FM01..04 proof | BR02/04; QA08; EV01..03 |
| U-02 | Listening progression/interruption implementation | Background/focus varies by target | Target Android applicability + FM01/05/18 | QA03/08; UI baseline |
| U-03 | Durable ACK source | UI restoration not durable write proof | FM07/08/14 plus identity/form binding | FR005/019; G04-CP07 |
| U-04 | Local vs external responsibilities | Option catalogue not a chosen topology | Separate architecture PO selection and evidence | D05-ARCH03-005 boundary |
| U-05 | Account/learner identity boundary | Shared device 2–5 people and data rights need authorization test | Privacy SOP, negative FM09 | BR08; QA08 |
| U-06 | Data location, copies, backups, deletion | Must prove ≤7d deletion / ≤30d post-pilot retention | Copy/exception inventory + FM10/11 | NFR006; G04-CP07 |
| U-07 | Content storage, publishing and revision mechanism | PO inventory does not replace key/media QA | FM06/12/13/16 + QA01..06 | FR015..017; B1 |
| U-08 | Scoring historical correction rules | Fixed provenance cannot be silently rewritten | FM12/14/17 + separate correction policy if needed | FR012/013/016; QA07 |
| U-09 | Android target and device scope | Platform requirements and OEMs vary | PO-controlled target/version + 2 actual Android contexts | NFR005/010; G04-CP03 |
| U-10 | Performance thresholds | No real measurements or signed numeric bounds | PO-approved test-plan targets prior to execution | NFR004; AC08 |
| U-11 | Framework, DB, API, backend, vendor | User expressly withheld selection authority | Separate PO authorization; no implementation here | D05-ARCH03-005 |
| U-12 | Real tests, device walkthrough, any paid action | Expressly prohibited this turn | Distinct PO decision + cost control if ever needed | CP04; G04-CP08 |

## Research-only evidence classes

| Category | Available now | Never infer |
|---|---|---|
| Signed policy and baseline | Requirements and Design Spec official versions | Software was tested |
| Public Android/OWASP/Play docs | General technical constraints | App compatibility or compliance validated |
| PO content inventory/rights attestation | Two Full Mocks inventoried; source-use affirmed | Every item/media/key audited |
| EV/FMs | 12 desk adjudications + 18 negative scenario definitions | 12/18 runtime test passes |
| Conceptual A/B/C options | Three possible evidence boundaries with tradeoffs | One chosen, benchmarked or feasible |

## Handoff without reopening previous decisions

- Future reviewers do not request budgets, vendor quotes, re-inventory of the two Full Mocks or repeated content-rights attestations. They shall schedule **actual QA checks** at the already specified future checkpoints.
- A later architecture selection must explicitly record assumptions and fail conditions, without changing BR01..10 or Design Baseline. If it requires a business-policy change, submit a controlled PO change request first.
- Keep all CP families active, and do not infer Stage05 Gate readiness or new ARCH-04 authority from this comparison.

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
