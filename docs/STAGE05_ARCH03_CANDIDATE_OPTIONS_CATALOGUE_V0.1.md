# Stage05 ARCH-03 — Architecture Candidate Options Catalogue V0.1

**Status:** ANALYST HYPOTHESES — **ALL UNSELECTED** · **Authority:** D05-ARCH03-005=A · **Mode:** DOCUMENT-ONLY.

## 1. Same agreed product, three possible evidence boundaries

Every candidate must satisfy the same signed 2×200 Full Mock scope, strict clean-attempt rules, truthful ACK, learner separation, controlled content and results, without changing PRD/SRS/UX baselines. **No runtime, repository, API, schema, cloud provider, clock authority or app architecture is proposed as a binding choice.**

| Candidate | Basis of future evidence | Distinct failure pressure | Status |
|---|---|---|---|
| **ARCH03-A** | Device-primary evidence boundary | Reboot, sửa thời gian, đổi người học, mất thiết bị, xóa tất cả bản sao và xác nhận bền vững đều chưa được chứng minh | **UNSELECTED / UNVERIFIED** |
| **ARCH03-B** | Independent-observation-led boundary | Mất mạng, trễ phản hồi, độ chính xác của người học/phiên bản và sự phụ thuộc vào quan sát ngoài đều có thể để lại khoảng không chứng cứ | **UNSELECTED / UNVERIFIED** |
| **ARCH03-C** | Multi-evidence reconciliation boundary | Thêm nghĩa vụ đồng bộ, phân quyền, provenance, trùng thông điệp và phân xử nguồn tin | **UNSELECTED / UNVERIFIED** |

## 2. Individual option dossiers

### ARCH03-A — Device-primary evidence boundary

- **Giả thuyết chịu trách nhiệm bằng chứng:** Bằng chứng tại thiết bị là đầu mối quan sát chính; kết quả chỉ được xác nhận khi các nghĩa vụ về tính bền vững, thời gian, định danh và provenance được chứng minh. Bằng chứng độc lập, nếu có, không tự được giả định là bắt buộc.
- **Tiềm năng:** Khả năng tiếp tục ghi nhận hoạt động khi mất mạng ngắn mà không phụ thuộc mỗi tương tác vào quan sát từ bên ngoài.
- **Rủi ro chưa giải quyết:** Reboot, sửa thời gian, đổi người học, mất thiết bị, xóa tất cả bản sao và xác nhận bền vững đều chưa được chứng minh; local presence không đồng nghĩa trusted time.
- **Hành vi bảo thủ khi thiếu chứng cứ:** Nếu không chứng minh được tính toàn vẹn sau reboot/mất ACK, trạng thái lượt thi/đáp án phải unknown/non-comparable theo policy; không tự áp dụng grace.
- **Tương tác với mô hình ARCH-02:** T-A, S-A, P-A chỉ là những model có nét tương đồng; **không được coi là gói đã ghép hoặc bắt buộc**.
- **Bằng chứng không thể thiếu:** FM-01..05 (thời gian/audio), FM-07/08/14 (ACK), FM-09..11 (privacy), FM-12/17 (kết quả), FM-06/13/16 (QA nội dung), FM-15/18 (Android).
- **Không được kết luận:** phù hợp ngân sách, dễ triển khai, hoạt động qua reboot, an toàn dữ liệu, chính xác hơn hoặc nên chọn ngay; chưa có thực nghiệm/chi phí.

### ARCH03-B — Independent-observation-led boundary

- **Giả thuyết chịu trách nhiệm bằng chứng:** Đề xuất xác minh một số sự kiện có bằng chứng từ bên ngoài thiết bị trước khi có thể nâng trạng thái tương ứng lên xác nhận; cơ chế và mức thẩm quyền chưa quyết định.
- **Tiềm năng:** Có khả năng tạo một kênh tham chiếu khác so với thiết bị, hữu ích khi có nghi ngờ thời gian hoặc nguồn gốc bằng chứng.
- **Rủi ro chưa giải quyết:** Mất mạng, trễ phản hồi, độ chính xác của người học/phiên bản và sự phụ thuộc vào quan sát ngoài đều có thể để lại khoảng không chứng cứ; privacy tăng nghĩa vụ kiểm soát.
- **Hành vi bảo thủ khi thiếu chứng cứ:** Nếu mất kết nối/late ACK, không tự thất bại và không tự thành công; phải phân loại chưa xác nhận và tránh tạo hai kết quả.
- **Tương tác với mô hình ARCH-02:** T-B, S-B, P-B chỉ là challengers khái niệm; **không chọn server, DB, API hoặc nguồn giờ**.
- **Bằng chứng không thể thiếu:** FM-01..05 (thời gian/audio), FM-07/08/14 (ACK), FM-09..11 (privacy), FM-12/17 (kết quả), FM-06/13/16 (QA nội dung), FM-15/18 (Android).
- **Không được kết luận:** phù hợp ngân sách, dễ triển khai, hoạt động qua reboot, an toàn dữ liệu, chính xác hơn hoặc nên chọn ngay; chưa có thực nghiệm/chi phí.

### ARCH03-C — Multi-evidence reconciliation boundary

- **Giả thuyết chịu trách nhiệm bằng chứng:** Đề xuất xem xét nhiều tập bằng chứng theo từng claim và mô tả xung đột/thiếu hụt tách biệt; thẩm quyền, tương quan và quy tắc xử lý bất đồng chưa được chốt.
- **Tiềm năng:** Có thể thể hiện rõ các trạng thái bất định và nguồn mâu thuẫn để tránh silent success, nếu sau này chứng minh được giá trị bổ sung.
- **Rủi ro chưa giải quyết:** Thêm nghĩa vụ đồng bộ, phân quyền, provenance, trùng thông điệp và phân xử nguồn tin; hai tín hiệu cùng sai hoặc cùng phụ thuộc không tạo ra xác nhận độc lập.
- **Hành vi bảo thủ khi thiếu chứng cứ:** Khi tín hiệu mâu thuẫn, không lấy đa số hoặc thứ tự đến làm authority mặc định; tình trạng clean/comparable và ACK phải chờ bằng chứng hoặc policy duyệt.
- **Tương tác với mô hình ARCH-02:** T-C/S-C/P-C thuộc nhóm nghiên cứu tương đồng, **không phải kiến trúc đã được chấp thuận**.
- **Bằng chứng không thể thiếu:** FM-01..05 (thời gian/audio), FM-07/08/14 (ACK), FM-09..11 (privacy), FM-12/17 (kết quả), FM-06/13/16 (QA nội dung), FM-15/18 (Android).
- **Không được kết luận:** phù hợp ngân sách, dễ triển khai, hoạt động qua reboot, an toàn dữ liệu, chính xác hơn hoặc nên chọn ngay; chưa có thực nghiệm/chi phí.

## 3. Cross-cutting capabilities are not candidates automatically selected

| Domain | Binding need | Permitted paper questions | Forbidden assertion |
|---|---|---|---|
| Timing | BR-02/04, strict validity | Which evidence may survive process death/reboot and what is unknowable? | Device/remote/hybrid clock authoritative |
| Listening | Correct media, no arbitrary replay | How could playback interruption be documented without learner advantage? | Background playback will be reliable |
| ACK | Durable confirmation only | How to distinguish selection/pending/durable ACK and retries? | UI selection implies write committed |
| Privacy | Each learner separate, deletion 7d/retention 30d | Which copies, identities and exceptions require evidence? | Account architecture or deletion completion |
| Content | QA of both 200-item Full Mocks, separate Part bank | Which provenance/revision dependencies must be visible? | Two inventoried sets are QA-ready |
| Raw results | Correct/answered/version/attempt validity | How to preserve historical meaning across correction? | ETS-equivalent official score |
| Android UX | Long Reading, focus, honest states | Which 2+ real device contexts later falsify a claim? | Static PDF = usability PASS |

## 4. Evidence Reconciliation First means *evaluate truth*, not mandate option C

The PO-approved order of reasoning cannot be promoted into selection of **ARCH03-C**. One adequately corroborated observation under a different option might meet a specific requirement; two weak or correlated signals under C might not. Future decision must evaluate each claimant against the same falsifiers and policy, rather than favor the candidate whose name sounds closest to the research direction.

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
