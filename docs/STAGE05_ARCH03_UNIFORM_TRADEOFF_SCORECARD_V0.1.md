# Stage05 ARCH-03 — Uniform Comparative Scorecard and Trade-offs V0.1

**Decision state:** NO ARCHITECTURE SELECTED. This is a qualitative trade-off assessment, **not benchmark data, numeric cost or a weighted winner**.

## Same tests for all three candidates

| Criterion / invariant | Common acceptance burden | ARCH03-A Device-primary | ARCH03-B Independent-led | ARCH03-C Reconciled evidence | Trace |
|---|---|---|---|---|---|
| Clean Full Mock / reboot | Must justify time evidence and classify unprovable intervals | Reboot gap may lack independently trusted evidence | Remote observations may be absent offline / stale | Conflicting clocks require future unapproved adjudicator | EV01..03; FM01..04 |
| Listening interruption | Correct audio order, avoid arbitrary replay | Local playback claims require focus evidence | External record does not prove audio heard | Multiple records can disagree about actual hearing | EV04; FM01/05/18 |
| Durable answer ACK | No false saved message / duplicate result | Local commit and identity/durability not established | Network loss/late ACK can leave unknown | Resolution of delayed/conflicting ACK unproven | EV05/06; FM07/08/14 |
| Shared-phone privacy | No cross-learner pending/history leakage | Device session separation unverified | Authorization remains required on every context | Copy/authorization boundary coordination unproven | EV07; FM09 |
| Deletion/retention | All copies, verified request ≤7d, retention ≤30d | Device/backups/removal proof missing | External data/backups/removal proof missing | Additional copies increase audit scope | EV08; FM10/11 |
| Content readiness | 2x200 plus independent bank, QA01..06 | Local corpus/version QA still mandatory | Remote corpus/version QA still mandatory | Replica/source reconciliation cannot replace QA | EV09/11; FM06/13/16 |
| Results provenance | Raw results, historic version, one result | Local original/correction record unverified | Corroborated original/correction record unverified | Cross-source correction and duplicate handling unverified | EV10; FM12/14/17 |
| Reading/Android | Context return and accessibility on 2+ real phone contexts | UI continuity no real device evidence | External observation cannot fix Reading UX | Multiple signals cannot fix UI legibility | EV12; FM15 |
| Connectivity and availability | Online-first, honest outage status | May allow local observation; clean validity still unknown | Independent observation unavailable during outage | Pending/conflicts may grow and need resolution | EV02/05/06; FM02/07/08 |
| Operational complexity / privacy surface | Must not invent performance, price or compliance | Local state/protection/recovery burden unknown | External service/access burden unknown | Cross-boundary coordination burden unknown | EV07/08; all FM |
| Reversibility | Do not lock stack or irreversible semantics now | Local evidence may need future export/normalization | External evidence may need continuity/fallback | Cross-source correlation may be hard to unwind | G04-CP06; G03-CP06 |

## Cross-candidate verdicts

- **No demonstrated advantage:** Each candidate has at least one critical unverified integrity/ACK/privacy case and no target-device evidence. Comparative words such as “might reduce dependency” do not imply measured improvement.
- **No automatic inferiority:** A localized solution may be adequate if it later satisfies all signed obligations; independent evidence may be beneficial if outages/identity can be handled; reconciliation may be beneficial if independent provenance and conflict rules can be justified.
- **Decision reversal:** Reboot/tamper, offline/late ACK, identity switching, deletion-copy inventory, wrong-media and key revisions can change the relative preference materially. No budget or performance score is available; do not fabricate it.
- **Non-architecture dependencies:** Content QA-01..06 and usability QA-08 are mandatory regardless of responsibility placement. Specific data retention and no-replay policies are **business rules**, not optimization variables.
- **Conservative recommendation:** Do **not** select an implementation architecture solely from this scorecard. A PO may explicitly choose a provisional conceptual direction for further elaboration, but its unverified parts and change-control must remain recorded; exact tech/clock authority stays out of scope.

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
