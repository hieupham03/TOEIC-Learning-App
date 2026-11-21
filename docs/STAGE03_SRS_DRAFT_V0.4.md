# SRS — TOEIC Learning App — Draft V0.4 (Consolidated)

**Status:** **CANDIDATE REQUIREMENTS / NOT APPROVED, NOT BASELINED.** Date 2026-11-21.  
**No implementation design:** Yêu cầu hành vi và tiêu chí kiểm chứng, không chọn UI, stack, DB, API, thuật toán, thiết kế hệ thống hoặc code.  
**Terminology:** `PO-CONFIRMED` (quyết định/xác nhận), `CANDIDATE` (đề xuất), `CONDITIONAL` (phụ thuộc QA/content), `DEFERRED` (ý tưởng chưa cam kết), `TBD` (chưa chốt). *Mọi FR/NFR dưới đây đều không được phê duyệt baseline*.

## A. Business rules and assumptions

- **BR-01:** B1 bắt buộc có 2 Full Mock độc lập (A/B), mỗi đề 200 câu; 100 Listening ~45 phút và 100 Reading 75 phút, Part1 6, P2 25, P3 39, P4 30, P5 30, P6 16, P7 54. Theo ETS format; mô phỏng exam phải gọi là practice mock, không phải bài thi TOEIC được chứng nhận.
- **BR-02:** Hai bộ đề đã **được PO kiểm kê xong**; chưa kiểm tra kết quả QA nội dung từng câu và media theo hồ sơ này. Không ghi “no inventory” hoặc “not sourced”.
- **BR-03:** PO xác nhận quyền sử dụng 3 website (The TOEIC Lab, Zenlish, STUDY4) và nhiều nguồn khác; từng item/asset cần provenance để bảo trì; không tự nhận đã chạy audit quyền độc lập.
- **BR-04:** QA-01..08 là **APPROVED FRAMEWORK**, chưa PASS. Không có đủ bằng chứng QA thì form vẫn chưa được dán nhãn READY FOR PILOT.
- **BR-05:** Budget requirements/workflows **DEFERRED BY PO**; không hỏi hay đưa ra quyết định chi phí trong Stage03 hiện tại. CP-04 không được xóa.
- **BR-06:** Không cam kết convert raw performance thành ETS standardized/official scaled score hoặc tuyên bố mức tăng điểm đã kiểm chứng qua hai đề không được equate.

## B. Functional requirements candidates

| ID | Priority candidate | Behavior (technology-neutral) | Acceptance case | QA link |
|---|---|---|---|---|
| FR-001 | P1 | Người học đặt/sửa mục tiêu, trình độ tự khai và khoảng thời gian học sẵn có | AT-01 thay đổi dữ liệu đầu vào và xem lại đúng | QA-08 |
| FR-002 | P1 | Xem và chọn bài Part 1–7 chỉ khi nội dung đã đủ QA | AT-02 Part có nội dung hiển thị; item chưa QA không xuất hiện trong pilot | QA-01/02/06 |
| FR-003 | P1 | Listening theo nhóm câu và clip âm thanh tương ứng | AT-03 đối chiếu clip-group/ID và thứ tự câu; clip lỗi không được xuất bản | QA-03 |
| FR-004 | P1 | Reading, ảnh, bảng biểu, đoạn văn giữ đúng nhóm câu và đủ nội dung | AT-04 đủ bài đọc/multiple passage/asset; không mất dữ liệu khi nội dung dài | QA-04/08 |
| FR-005 | P1 | Lưu lựa chọn mỗi câu theo đúng attempt, item, form, Part | AT-05 đổi câu, quay lại, đưa app nền, không ghi nhầm/mất lựa chọn đã xác nhận | QA-08 |
| FR-006 | P1 | Chấm dựa trên answer key đã QA; không tự suy đoán answer key | AT-06 test known key, unmatched/invalid key không được chấm sai lệch | QA-02/07 |
| FR-007 | P1 | Hiện đáp án và giải thích đã được duyệt nếu có; phân biệt trường hợp không có lời giải | AT-07 key đúng; không có lời giải thì báo không có, không sinh lời giải giả | QA-02/06 |
| FR-008 | P1 | Lưu và xem lại lịch sử, câu sai, Part, metadata phiên | AT-08 cùng một người xem đúng bản ghi; hai người không nhìn thấy dữ liệu của nhau | QA-07/08 |
| FR-009 | P1 | Người học chọn Part hoặc thời gian để thực hành ngắn; có thể kết thúc sau 1 câu | AT-09 1-question session lưu được; đề xuất không bắt buộc | QA-08 |
| FR-010 | **B1 MANDATORY, QUALITY CONDITIONAL** | Có hai form Full Mock A/B, mỗi form đủ cấu trúc chính thức, chỉ đánh dấu READY khi QA đủ | AT-10 kiểm tra form manifest và status QA; không quảng cáo READY nếu còn lỗi chặn | QA-01..06 |
| FR-011 | P1; behavior TBD | Full Mock có quy tắc timer, thứ tự Listening/Reading, nộp và kết thúc; xử lý app nền/mất mạng rõ ràng | AT-11 đo 45+75, deadline, trạng thái gián đoạn theo chính sách PO duyệt | QA-08 |
| FR-012 | P1 | Kết quả hiển thị số đúng/đã trả lời của Listening, Reading, tổng và từng Part | AT-12 đối chiếu known key; chú thích “kết quả luyện tập”, không ETS-equivalent | QA-02/07 |
| FR-013 | P1 | Phân biệt mock dùng đánh giá và buổi luyện không đủ điều kiện so sánh | AT-13 mock mất tính toàn vẹn/đã lộ đề sẽ có nhãn, không gộp trend | QA-05/07/08 |
| FR-014 | P2 | Đề xuất hoạt động theo Part yếu/mục tiêu/thời gian bằng quy tắc có thể kiểm tra | AT-14 thiếu lịch sử có fallback mặc định; không bắt người học theo đề xuất | QA-07 |
| FR-015 | P1 | Có quy trình duyệt, sửa, ẩn/thu hồi nội dung đã kiểm kê | AT-15 key/media sai không phát hành; sửa có version và sự kiện ghi nhận | QA-02/03/04/06 |
| FR-016 | P1 | Khi sửa đáp án/asset đã dùng, lịch sử thống kê bị ảnh hưởng được nhận diện và xử lý | AT-16 thay đổi key sau attempt không âm thầm làm báo cáo cũ sai | QA-02/07 |
| FR-017 | P1 | Nội dung chưa QA hoặc không khả dụng hiện trạng thái rõ, không tạo dữ liệu giả | AT-17 không có Part/form READY thì hệ thống không cho làm như đề hoàn chỉnh | QA-01..06 |
| FR-018 | P1 | Phân tách dữ liệu và cho phép xử lý quyền dữ liệu cá nhân theo quy định áp dụng | AT-18 2 người không đọc/sửa được dữ liệu của nhau; deletion behavior được xác định trước pilot | QA-08 |
| FR-019 | P1 | Khi bị gián đoạn, khôi phục đáp án đã ghi và minh bạch trạng thái thời gian/attempt | AT-19 background/process death/reopen/timeout; no silent reset or duplicate submission | QA-08 |
| FR-020 | DEFERRED | Tự phân tích mọi PDF/audio, tạo item mapping tự động | Chỉ xem xét sau PoC; không cam kết pilot | — |
| FR-021 | DEFERRED | AI tạo câu hỏi/lời giải hoặc chấm trình độ tự động | Không đưa vào baseline nếu chưa quyết định riêng và QA | — |
| FR-022 | DEFERRED | Thông báo từ vựng với nhiều hành động | Chưa cam kết pilot, giữ trong vision backlog | — |
| FR-023 | DEFERRED | iOS/offline/Speaking & Writing/paid release | Chưa cam kết pilot | — |

**Priority P1/P2 is an analyst's drafting order, not PO approval of MVP content.**

## C. Non-functional requirement candidates

| ID | Candidate requirement | Proposed verification (no numeric threshold approved) | QA |
|---|---|---|---|
| NFR-001 | Content provenance/integrity: mọi item và asset dùng trong pilot có source/form/version/key/status | Kiểm kê dựa trên manifest và exception log, đối chiếu QA riêng | QA-01/02/06 |
| NFR-002 | Audio fidelity: clip đúng thứ tự và group, không phát sai câu | So khớp toàn bộ quan hệ item-group-clip; kiểm thử media khi có hệ thống | QA-03 |
| NFR-003 | Session persistence: đáp án đã xác nhận không âm thầm mất | Test nền, xoay màn, tiến trình bị hủy, mất kết nối, app relaunch | QA-08 |
| NFR-004 | Mock timing integrity: chính sách timer/gián đoạn nhất quán, không tăng thời gian không rõ lý do | Test timer, timeout, accidental exit, retry, submit once | QA-08 |
| NFR-005 | Mobile long Reading: không cắt ngữ liệu, hình/bảng và bài nhiều đoạn; dễ đọc | Kiểm thử thực tế trên Android pilot devices, Accessibility checks | QA-04/08 |
| NFR-006 | Personal data isolation, retention/deletion and consent as applicable | Test phân tách, delete request, privacy policy review trước pilot | QA-08 |
| NFR-007 | Score transparency: report raw correct/attempted, từng Part và metadata; không nhận điểm ETS | Kiểm tra labels, test score examples, mismatch warnings | QA-07 |
| NFR-008 | Content correction integrity: item withdrawal/versioning does not silently corrupt past report | Regression replay with corrected answer key; effect on history explicit | QA-02/06/07 |
| NFR-009 | Traceability: FR/NFR ↔ Vision/Journey ↔ QA ↔ acceptance test | Ma trận traceability đầy đủ và chưa có orphan critical requirement | QA-01..08 |
| NFR-010 | Reader accessibility: user text-size scaling, contrast, audio operability must be validated for practical use | Android accessibility manual/automated checks later, no UI designs now | QA-08 |
| NFR-011 | Online-first clarity: nếu mất mạng, người học biết trạng thái, không thấy kết quả giả | AT-19 network transition and pending status | QA-08 |
| NFR-012 | Public branding/trademark claims require legal review before public release | Review final display name and endorsement claims later | QA-06 |
| NFR-013 | Pilot cost control | **DEFERRED BY PO**; retain CP-04 risk, no active budgeting | — |

## D. QA-01..08 crosswalk / testing scope

| QA framework ID (APPROVED) | Requirement IDs | Acceptance tests | Evidence status |
|---|---|---|---|
| QA-01 Counts/Part distribution | FR-002/010, NFR-001 | AT-02/10 | PO inventory complete; detail QA NOT VERIFIED |
| QA-02 Answer validity | FR-006/007/015/016, NFR-001/008 | AT-06/07/15/16 | NOT VERIFIED |
| QA-03 Listening audio | FR-003/015, NFR-002 | AT-03/15 | NOT VERIFIED |
| QA-04 Reading assets | FR-004/015, NFR-005 | AT-04/15 | NOT VERIFIED |
| QA-05 Duplicate/exposure | FR-010/013 | AT-10/13 | NOT VERIFIED |
| QA-06 Source rights/provenance | FR-002/015, NFR-001/012 | AT-02/15 | PO rights affirmed; item audit NOT VERIFIED |
| QA-07 Result transparency | FR-012/013/016, NFR-007/008 | AT-12/13/16 | RULES DRAFT; test NOT RUN |
| QA-08 Mobile/session | FR-001/005/009/011/018/019, NFR-003/004/005/006/010/011 | AT-01/05/09/11/18/19 | REQUIREMENTS DRAFT; test NOT RUN |

**AT = acceptance test design, not execution.** QA framework **APPROVED**; acceptance thresholds, actual form QA results and requirement baseline **NOT APPROVED**.

## E. Open decisions to bundle as D03-REQ-007

| Bundle | Missing business rule | Analyst default (not approved) |
|---|---|---|
| R1 | Mock time/pause/playback policy | 45+75 min for comparative attempts, no user pause in evaluative mode; background does not reset timer; label interrupted/invalid attempts; Part practice is flexible |
| R2 | Result semantics across two mocks | Raw correct/attempted and Part breakdown; no 10–990 claim; trend only with valid, QA-cleared and exposure-free attempts, with comparability caution |
| R3 | Feedback and personalized learning | Key mandatory; vetted explanation when present; no invented explanation; default simple rule-based suggestion and learner choice |
| R4 | Pilot trust/privacy/reading | Persist confirmed answers; separate family learners; specify data deletion and long Reading acceptance later; no login/DB decision |

## F. Stage gates / constraints

- **Now:** D03-QA-006 approved **framework only**; mock inventory PO-confirmed; budget deferred; PRD/SRS still drafts.
- **Before future MVP lock:** PO decides R1..R4 requirement direction; content/mapping quality evidence plan agreed; baseline scope and acceptance thresholds explicit; budget deferral must be acknowledged at later appropriate gate, not silently assumed satisfied.
- **Not authorized:** architecture, wireframes/UI, coding/Codex, web extraction/bulk download, provider outreach, cost decisions or purchasing.
