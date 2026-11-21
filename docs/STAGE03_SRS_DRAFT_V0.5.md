# Software Requirements Specification — TOEIC Learning App — DRAFT V0.5

**Status:** REQUIREMENTS CANDIDATES — **NOT APPROVED / NOT BASELINED**. Date 2026-11-21.  **No UI, architecture, infrastructure, schema/API or code design.**

## 1. Semantic conventions and decisions

- `APPROVED PRINCIPLE`: R1–R4 in D03-REQ-007, QA-01..08 framework in D03-QA-006, B1 two Full Mock forms mandatory. **Individual FR/NFR and thresholds below are not automatically approved.**
- `PO-REPORTED`: two Full Mock inventories completed; rights to STUDY4, Zenlish, The TOEIC Lab and further sources affirmed; no independent item/asset audit performed.
- `DEFERRED BY PO`: all budget work; CP-04 remains tracked, no monetary/effort decisions made.
- `TBD`: behavior requires later PO selection, not a license to invent an answer in coding.

## 2. Business rules — candidate language testable at boundary

| ID | Requirement / status |
|---|---|
| BR-01 | Two separate full mock forms A/B, **each 200 questions**: P1=6, P2=25, P3=39, P4=30, P5=30, P6=16, P7=54; 100 Listening (~45 minutes) and 100 Reading (75 minutes). **B1 approved** as requirement direction. |
| BR-02 | PO inventory of both forms recorded complete, not a verified QA PASS. Content-only QA before pilot; app behavior tests after implementation. |
| BR-03 | Each content item/group/answer/asset is attributable to a source/form/version; rights affirmation does not substitute for QA evidence. |
| BR-04 | Timed mock evaluation vs flexible practice are distinct; an invalid/interrupted/previously exposed attempt must not appear as a clean comparable assessment. Detailed timer/replay/exit rules **TBD**. |
| BR-05 | Raw correct/attempted and Part/section totals only as default. Official ETS scaled 10–990 score and scientifically comparable cross-form growth are **NOT CLAIMED**. |
| BR-06 | Answer key mandatory; vetted explanations optional where available, never fabricated. User may ignore rule-based recommendations and select own practice. |
| BR-07 | Confirmed answers must not silently disappear or be attributed to another learner after interruptions. Exact account, conflict and deletion policy **TBD before pilot**. |
| BR-08 | QA-01..QA-08 approved review framework, tests not run. Budget DEFERRED, no cost gate to be silently marked PASS. |

## 3. Functional requirements — scoped candidates, stable identifiers

| ID | Candidate priority | SHALL behavior (implementation-neutral) | Test ID | QA |
|---|---|---|---|---|
| FR-001 | P1 | Người học có thể cung cấp/sửa mức tự khai, mục tiêu và thời lượng học mong muốn, và thấy dữ liệu nào đang được dùng để gợi ý. | AT-01 | QA-08 |
| FR-002 | P1 | Người học có thể chọn luyện Part 1–7 trên nội dung hợp lệ; nội dung chưa đủ QA không được gắn trạng thái READY. | AT-02 | QA-01/06 |
| FR-003 | P1 | Mỗi câu hoặc nhóm Listening tham chiếu đúng clip/audio, thứ tự và ngữ cảnh; nếu thiếu/khớp sai phải được từ chối phát hành trong tập đang xét. | AT-03 | QA-03 |
| FR-004 | P1 | Ngữ liệu Reading, hình ảnh, bảng biểu, nhiều đoạn và nhóm câu phải còn nguyên nội dung, quan hệ và thứ tự. | AT-04 | QA-04/08 |
| FR-005 | P1 | Khi người học xác nhận/chuyển câu, hệ thống ghi đúng lựa chọn vào đúng learner–form–attempt–Part–item, không lẫn đáp án. | AT-05 | QA-08 |
| FR-006 | P1 | Chấm dựa trên key đã QA; key thiếu/mơ hồ/khác version không được tự suy đoán. | AT-06 | QA-02/07 |
| FR-007 | P1 | Chữa lỗi chỉ hiển thị key và lời giải đã QA nếu có; nếu không có phải hiển thị trạng thái rõ. | AT-07 | QA-02/06 |
| FR-008 | P1 | Người học xem lịch sử câu sai và phiên làm đúng dữ liệu của chính mình; lịch sử gắn form/Part/date/version. | AT-08 | QA-07/08 |
| FR-009 | P1 | Người học có thể chọn luyện từng Part hoặc phiên học ngắn kết thúc sau một câu, độc lập quy tắc strict full mock. | AT-09 | QA-08 |
| FR-010 | **B1 mandatory; content QA conditional** | Có hai form Full Mock A/B đáp ứng cấu trúc BR-01; chỉ công bố làm đề sẵn sàng pilot khi QA content đạt tiêu chí áp dụng. | AT-10 | QA-01..06 |
| FR-011 | P1; details TBD | Phiên mock có quy tắc thời gian, chuyển section, kết thúc, nộp; khi bị gián đoạn/thoát không âm thầm gia hạn hay biến attempt thành hoàn tất sạch. | AT-11 | QA-08 |
| FR-012 | P1 | Báo attempted/correct/unanswered, total L/R/Part, thời gian/form/version và attempt integrity, không gắn điểm ETS chính thức. | AT-12 | QA-07 |
| FR-013 | P1 | Tách attempt hợp lệ cho chuỗi theo dõi và attempt bị lộ đề/được hỗ trợ/tạm dừng trái quy tắc; cảnh báo rằng biến đổi raw giữa hai form không đồng nghĩa tương đương năng lực. | AT-13 | QA-05/07 |
| FR-014 | P2 | Có thể đề xuất bài luyện theo Part yếu, thời gian rảnh/mục tiêu dựa trên quy tắc kiểm chứng được; khi thiếu lịch sử có fallback, và không khóa lựa chọn của người học. | AT-14 | QA-07/08 |
| FR-015 | P1 | Có trạng thái nội dung, version, lịch sử duyệt/chỉnh/ẩn; media/key/passage sai không được tự chuyển sang READY. | AT-15 | QA-02/03/04/06 |
| FR-016 | P1 | Việc sửa key/media ảnh hưởng tới lịch sử phải được phát hiện và giải thích, không tự cập nhật thống kê cũ mà không lưu dấu vết/version. | AT-16 | QA-02/07 |
| FR-017 | P1 | Chỉ cho phép khởi tạo phiên hoàn chỉnh từ nội dung còn khả dụng và đủ chuẩn; giải thích rõ khi nguồn tạm lỗi/không có. | AT-17 | QA-01..06 |
| FR-018 | P1 | Dữ liệu mỗi người học phải tách; có nguyên tắc xử lý truy cập/chỉnh/xóa dữ liệu theo chính sách được duyệt trước pilot. | AT-18 | QA-08 |
| FR-019 | P1 | Khi background/process stop/relaunch/network loss, người học biết trạng thái lưu và thời gian/attempt; tránh mất lựa chọn đã xác nhận, nộp trùng hoặc tạo false-comparable attempt. | AT-19 | QA-08 |
| FR-020..023 | DEFERRED | Auto PDF/audio parser; AI runtime/generation; advanced notification actions; iOS/offline/S&W/monetization. Chưa cam kết pilot, chỉ theo dõi backlog. | N/A | N/A |

**Priorities are analyst ordering, not MVP-in/out approval.** Quan hệ form/answer/version ở đây là khái niệm nghiệp vụ, không lựa chọn cấu trúc dữ liệu.

## 4. Non-functional requirements — candidate, threshold status

| ID | Candidate quality criterion | Verification & status |
|---|---|---|
| NFR-001 | Item, group, audio, image, passage và key có provenance, version và trạng thái QA | Source-to-content spot/full audit sau; mức phủ đề xuất 100% content released, **threshold chưa PO chốt** |
| NFR-002 | Audio đúng quan hệ với item/group; không phát clip khác câu | So khớp asset map và kiểm thử playback sau; **NOT VERIFIED** |
| NFR-003 | Không mất đáp án **đã xác nhận**, kể cả khi app nền, bị hủy tiến trình hoặc reconnect | AT-05/19 and device test later; recovery-time/availability **TBD** |
| NFR-004 | Time policy consistent, no silent reset, no duplicate submit | AT-11/19; exact grace/tolerance **TBD** |
| NFR-005 | Ngữ liệu Reading dài, nhiều đoạn/bảng không bị mất hoặc đổi thứ tự; đọc được trên target Android | Device + accessibility tests later; target device list and size thresholds **TBD** |
| NFR-006 | Không cho người học A xem/sửa dữ liệu B; privacy + data retention/deletion rule explicit before pilot | AT-18; account-dependent Google Play requirements to assess at publication |
| NFR-007 | Results transparent as raw practice statistics, correct Part/section/attempt labels | AT-12/13 and copy review; no artificial ETS scaled claim |
| NFR-008 | Item/key correction auditability, report reproducibility and traceable result history | AT-16; correction policy **TBD** |
| NFR-009 | Critical FR/NFR traceable to approved Vision, journeys, QA/AT and owner decision | Traceability audit before Gate; any orphan critical requirement must be reconciled |
| NFR-010 | Basic mobile accessibility: text resizing/readability, contrast, large reading sources; functional controls identifiable | Android test later; quantitative standards/targets not approved |
| NFR-011 | Online-first sessions show network/pending state accurately; no fabricated score/result | AT-19; offline behavior not promised |
| NFR-012 | External publication does not imply ETS endorsement; product naming/trademark review pre-release | Legal copy review later |
| NFR-013 | Pilot cost/OPEX quality control | **DEFERRED BY PO**, retain CP-04 with future trigger; no budget task at this review |

## 5. QA approved framework / actual testing separation

| QA | Design trace | Current evidence |
|---|---|---|
| QA-01 mock counts and Part totals | BR-01, FR-010; AT-10 | PO inventory completed; item-level count not independently verified |
| QA-02 keys | FR-006/007/015/016; AT-06/07/15/16 | Actual QA NOT VERIFIED |
| QA-03 audio | FR-003/015; AT-03/15 | Actual QA NOT VERIFIED |
| QA-04 passages & assets | FR-004/015; AT-04/15 | Actual QA NOT VERIFIED |
| QA-05 cross-form duplicates/exposure | FR-010/013; AT-10/13 | Actual QA NOT VERIFIED |
| QA-06 provenance and rights | FR-015; AT-15 | Rights PO-AFFIRMED; per-item audit NOT VERIFIED |
| QA-07 scores & reporting | FR-012/013/016; AT-12/13/16 | Reporting behavior DRAFT; software test not run |
| QA-08 interruptions, family data, Reading | FR-005/011/018/019; AT-05/11/18/19 | Behavioral specs DRAFT; software test not run |

## 6. Critical edge cases and unresolved policy decisions

| Edge | Candidate behavior for later owner signoff | Status |
|---|---|---|
| Timed mock: foreground → background → return | Time must not silently reset; if event breaks integrity, label invalid/non-comparable; retained answered items visible | **Threshold/event policy TBD** |
| Process killed just after answer confirmed | On next legitimate session access, confirmed answer still attributable to correct item, no ghost double submission | Target test later |
| Network loss before vs after answer acknowledged | Clearly disclose pending/saved status; cannot claim confirmation if not durable | Handling & UI wording TBD, no offline mode commitment |
| Listening replay / section timing | Strict evaluation distinct from flexible Part practice; allow/forbid replay only as later PO policy | **TBD** |
| 1 / 2 Full Mock partially finished | Separate incomplete/invalid vs completed; do not include invalid in honest trend | Candidate |
| Correct answer changes after attempt | Preserve version and distinguish old/new scoring, never silent re-score | Candidate |
| Long Reading P7 with multiple paragraphs/tables | Complete passage and answer group remains accessible at common Android text sizes | Device/threshold TBD |
| Two family learners | History, errors, goal and deletion of one learner cannot expose or destroy other's records | Retention/access model TBD |

## 7. Source and references

ETS 200-question test and 45/75-minute sections, Android lifecycle, Play account deletion if applicable: see `STAGE03_REQUIREMENTS_EVIDENCE_LEDGER_V0.5.md`. No code, UI or architecture implied by behavioral language.
