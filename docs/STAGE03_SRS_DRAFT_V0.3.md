# Software Requirements Specification (SRS) — CANDIDATE DRAFT V0.1

**Không phải SRS đã phê duyệt.** Đặc tả ở cấp hành vi và điều kiện nghiệm thu, không chọn stack/UX/architecture/data schema.  
**Status codes:** `CANDIDATE` = đề xuất; `CONDITIONAL` = phụ thuộc gate; `OUT` = không cam kết.  
**Yêu cầu chưa có ngưỡng chính thức được đánh dấu `TBD BY PO/QA`**.

## 1. Yêu cầu chức năng ứng viên
| ID | Mức | Yêu cầu ở mức hành vi | Tiêu chí nghiệm thu phác thảo |
|---|---|---|---|
| FR-001 | CANDIDATE | Người học xác định mục tiêu, trình độ tự khai báo, quỹ thời gian | Thông tin được ghi nhận/hiển thị lại chính xác, có thể cập nhật |
| FR-002 | CONDITIONAL | Truy cập các phiên luyện Part 1–7 có nội dung được phép | Chỉ Part có đủ item được QA mới hiển thị; không tạo bài rỗng |
| FR-003 | CONDITIONAL | Listening phát đúng audio cho item/group | Mỗi bài Listening dùng có ánh xạ đúng audio/group/key đã kiểm duyệt |
| FR-004 | CONDITIONAL | Xem ngữ liệu hình, bảng, văn bản nhiều đoạn đúng câu | Part 1/3/4/7 không bị mất thông tin cần trả lời |
| FR-005 | CANDIDATE | Chọn câu trả lời và xác nhận/nộp phiên | Trả lời được gắn đúng item, không ghi nhầm câu khác |
| FR-006 | CONDITIONAL | Hiển thị đáp án và giải thích khi có dữ liệu đã kiểm duyệt | Không tự bịa giải thích; nêu rõ khi chưa có giải thích |
| FR-007 | CANDIDATE | Lưu lịch sử câu đã làm, lỗi sai và Part liên quan | Người học xem lại được attempt và bản nội dung tương ứng |
| FR-008 | CANDIDATE | Chọn thời lượng hoặc Part để nhận hoạt động phù hợp | Không đề xuất hoạt động dài hơn giới hạn công bố mà không báo trước; quy tắc rõ |
| FR-009 | CANDIDATE | Có phiên học nhanh một câu trong ứng dụng | Người học có thể kết thúc sau một câu mà vẫn lưu kết quả |
| FR-010 | CONDITIONAL | Hai mock A/B (mỗi form đủ 200 item, đúng format 45+75m) | **BLOCKED:** 400 câu đúng, hợp pháp, không trùng; QA đạt và PO phê duyệt |
| FR-011 | CONDITIONAL | Full Mock phản ánh thời gian và tiến độ | Quy tắc timeout/gián đoạn/submission phải duyệt trước pilot |
| FR-012 | CONDITIONAL | Báo số câu đúng và tỷ lệ/Part cho mock | Nêu rõ là số thô/diagnostic; không tuyên bố ETS-equivalent |
| FR-013 | CANDIDATE | Người quản trị quản lý kho item được phép qua quy trình kiểm duyệt | Không công bố nếu rights/answer/audio QA fail; có version |
| FR-014 | CANDIDATE | Có thể sửa/thu hồi item sai, ghi nhận ảnh hưởng lên lịch sử | Sửa key không âm thầm làm sai thống kê cũ |
| FR-015 | CANDIDATE | Người dùng kiểm soát dữ liệu cá nhân và xóa khi áp dụng | Chính sách/luồng xóa phù hợp dữ liệu và quy định phát hành |
| FR-016 | CANDIDATE | Cảnh báo rõ những hoạt động không khả dụng do thiếu nguồn | Không giả tạo bài mock/Part chưa có nội dung |
| FR-017 | OUT | Tự đọc mọi PDF và ghép audio | Chỉ xem xét sau PoC rights/quality; không thuộc B draft |
| FR-018 | OUT | Sinh câu trả lời/lời giải AI tự động | Không thuộc B draft, cần eval riêng |
| FR-019 | OUT | Thông báo từ vựng nhiều thao tác | Nhu cầu đã ghi; hoãn phạm vi pilot |

## 2. Yêu cầu phi chức năng ứng viên
| ID | Phạm vi | Chỉ tiêu sơ bộ / gate |
|---|---|---|
| NFR-001 | Content integrity | 100% item đã phát hành có SOURCE-ID, quyền hợp lệ theo use case và key đúng; ngưỡng đề xuất chờ PO/QA |
| NFR-002 | Audio fidelity | 100% item Listening phát đúng audio/group; test sau khi có dữ liệu thực |
| NFR-003 | Session reliability | Không mất đáp án đã xác nhận khi chuyển trạng thái phổ biến; yêu cầu RTO/recovery time TBD |
| NFR-004 | Long-form Android | Đọc Part 7 trên phone không mất đoạn, hỗ trợ chữ dễ đọc; test trên ít nhất thiết bị pilot thật, tiêu chí readability TBD |
| NFR-005 | Security/privacy | Có quyền truy cập người học, phân tách data 2–5 users, hạn lưu/xóa dữ liệu, đồng ý cần thiết; kiến trúc TBD |
| NFR-006 | Operational budget | Bất kỳ khoản cloud/AI/content được dự báo theo 4 tuần và có cap do PO duyệt; TBD giá VND |
| NFR-007 | Transparency score | Không hiển thị quy đổi điểm TOEIC 990 chính thức nếu không có phương pháp đáng tin và giấy phép phù hợp |
| NFR-008 | Accessibility | Nội dung đọc lâu, chữ/contrast/đáp án dễ thao tác; acceptance từ nguồn Android và kiểm chứng người học |
| NFR-009 | Traceability | Mỗi yêu cầu liên hệ JTBD, bằng chứng, CP gate, test/case ID; bản SRS khóa sau PO duyệt |
| NFR-010 | Data correction | Khi item sai hoặc hết quyền, có phương án ẩn/xóa hoặc thay thế và xử lý báo cáo đã tính trước đó |

## 3. Ràng buộc và phụ thuộc
- ETS là nhãn hiệu và nội dung bảo hộ; **không sao chép đề ETS vì tìm thấy trực tuyến**. Chi tiết kiểm tra `STAGE03_WP04_CONTENT_MOCK_RIGHTS_COST_FEASIBILITY_V0.1.md`.
- Không coi 2 mock có cùng cấu trúc là được equate; quy đổi điểm nội bộ chỉ nếu được nghiên cứu/duyệt.
- Không cam kết AI hay auto-import trong B; không bất ngờ thêm hạ tầng hoặc đăng ký thuê bao.
- Không có cam kết offline, iOS, ads, public release ở pilot.

## 4. Kiểm thử đề xuất, chưa thực hiện
`AT-001` quyền dùng hợp lệ ⇒ mục nguồn được cấp; `AT-002` thiếu rights ⇒ chặn item; `AT-003` audio mapping lỗi ⇒ không phát hành; `AT-004` Part 7 có văn bản dài ⇒ không mất ngữ cảnh; `AT-005` save/restore mock interrupted; `AT-006` chấm đúng từ answer key; `AT-007` hiển thị raw/percent đúng nhãn; `AT-008` sửa key có audit trail; `AT-009` cap chi phí được giám sát. Các trường hợp sẽ cụ thể hóa ở Stage Testing theo phạm vi PO phê duyệt.

## 5. Open parameters trước khi SRS được baselined
- Nội dung/source count, Part coverage, mocked full forms, target device list.
- Ngưỡng tỉ lệ lỗi, target latency, accessibility acceptance, timeout/recovery semantics.
- Privacy retention, account model, ngân sách, học liệu backup và scope fallback.
- Nguồn giải thích đáp án; việc nội dung chỉ có đáp án mà thiếu giải thích có được chấp nhận trong pilot không.


---

## V0.2 REQUIREMENTS ADDENDUM — DRAFT CANDIDATES, NOT BASELINED

| ID | Status | Requirement candidate | Conditional acceptance evidence |
|---|---|---|---|
| FR-020 | CONDITIONAL | Prevent unauthorized content from entering shared pilot catalog | Each asset has source/right/use-case approval; UNKNOWN/REJECTED blocked |
| FR-021 | CONDITIONAL | Block duplicate/exposed items from comparing two mock forms | Distinct item IDs and leakage audit; if fail, do not treat scores as comparable |
| FR-022 | CONDITIONAL | Distinguish raw accuracy from official-equivalent scaled scores | No 10–990 ETS score claim unless calibration proven; labels explicitly state limits |
| FR-023 | CONDITIONAL | Support item-source version corrections and withdrawals | Changing key/audio invalidates affected statistics until reconciled |
| NFR-011 | CANDIDATE | A public product name must comply with third-party trademark policy | Reviewed brand/descriptor; no unapproved ETS/TOEIC logo or endorsement |
| NFR-012 | CANDIDATE | Enforce an approved content budget and pilot operating ceiling | Content license/authoring separate from four-week infrastructure costs |
| NFR-013 | CONDITIONAL | Full mock content and user attempt isolation | Two forms 200 items, per-Part allocations, valid timing; content QA and ownership attested |
| NFR-014 | CANDIDATE | Distinguish family internal testing from Play public release | Store release only after applicable account/closed-test requirements |

Status remains `DRAFT/NOT APPROVED`; requirements may be reworked after `D03-LOCK-001` PO decision. No implementation/stack/UI decisions.

---

## V0.3 STATUS ADDENDUM — 2026-11-21 — DRAFT, NOT BASELINED

**Current PO-reported state:** Two Full Mock sets have been inventoried. This supersedes earlier statements that no inventory was done. The analyst has **not** received/audited an item-level manifest; 400 distinct valid items, audio/key/passage mapping, QA and rights metadata are **not independently verified**.

**Budget:** All budget-related steps are explicitly **DEFERRED BY PO**, without waiving CP-04, granting spend authorization or claiming zero costs. Requirements work may progress without asking for budgets.

**B1 still mandatory:** Two full mocks must remain in the candidate scope and undergo content quality review. No automatic fallback to one mock or Part-only pilot; any change requires separate PO approval.

**Refer to:** `STAGE03_D03_SOURCE_INVENTORY_004_PO_CONFIRMATION_V1.0.md`; `STAGE03_B1_MOCK_QA_READINESS_V0.1.md`; `STAGE03_REQUIREMENTS_CHANGELOG_V0.3.md`.

**Approval:** PRD/SRS V0.3 remains WORKING DRAFT; MVP, requirements baseline, UI, architecture and code NOT APPROVED.
