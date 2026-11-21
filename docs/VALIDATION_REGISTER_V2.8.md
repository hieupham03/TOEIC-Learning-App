<!-- Canonical version V2.8; prior V2.7 preserved in original file -->
# Gate Update — Validation Register V2.8 (2026-11-21)

**DECISION G02-DEC-001:** PO approved **CONDITIONAL PASS** for Stage 02 and accepted **CP-01–CP-05** from Gate Review V1.0. Stage 02 CLOSED WITH CONDITIONS; Stage 03 **NOT STARTED, kickoff plan V0.1 awaiting separate PO approval**. This approval does **not** validate untested assumptions or authorize MVP/PRD/SRS/UX/UI/architecture/code.

- **D-025A..F:** APPROVED (A/B by working-mode directive, C–F by explicit PO decision).
- **VAL-013L/R:** NOT RUN / OPTIONAL / ON HOLD. No longer blocks stage transition.
- **VAL-003:** DEFERRED — sample PDF/audio still uninspected. **VAL-010:** DEFERRED — pricing research/user-specific experience not reopened.
- **H-003 (library integration, importer), scoring equivalence, AI quality, licensing, cost, mobile UX** stay OPEN/INCONCLUSIVE. Retain source classifications and risk ledger.
- **Authoritative gate record:** `STAGE02_GATE_DECISION_RECORD_V1.0.md`. **Stage03 proposed plan:** `STAGE03_REQUIREMENTS_KICKOFF_PLAN_V0.1.md`.

---

# VALIDATION REGISTER V2.7 — TOEIC Learning App

**Ngày:** 2026-11-21  
**NEW: VAL-026 / STAGE 02 GATE REVIEW PREPARED (NOT APPROVED):** Product Owner **APPROVED D-025C/D/E/F**. D-025A/B đã được chấp thuận bằng chỉ đạo trước đó. Đã hoàn thành Gate Review bằng evidence-first; khuyến nghị **CONDITIONAL PASS** theo CP-01–CP-05, nhưng Product Owner **CHƯA** lựa chọn PASS / CONDITIONAL PASS / HOLD. Stage 02 vẫn **IN PROGRESS / GATE DECISION PENDING**, Stage 03 **NOT STARTED**. Phần này thay thế trạng thái D-025C–F “chờ duyệt” ghi trong tài liệu V2.6 bên dưới (là lịch sử).

**EVIDENCE:** ETS format, STUDY4 practice flows, PREP/Migii study plans, Quizlet import-to-flashcards giới hạn điều kiện, spaced/retrieval/feedback academic research, Android notifications, Google Play IP, ETS score consistency. Nguồn gốc, claim/limitation ghi tại `STAGE02_EVIDENCE_SOURCE_LEDGER_V1.0.md`. Không có dữ liệu thí nghiệm mới. `VAL-013L/R` vẫn NOT RUN / OPTIONAL / ON HOLD, `VAL-003` tài liệu mẫu và `VAL-010` phí vẫn DEFERRED. H-003 PDF/audio feasibility/value, AI correctness, tương đương điểm vẫn OPEN. Chưa duyệt MVP, PRD/SRS, UX/UI, architecture/code.

**ĐẦU RA:** `STAGE02_GATE_REVIEW_V1.0.md` + `STAGE02_TO_STAGE03_OPEN_RISKS_V1.0.md` + `STAGE02_GATE_DECISION_SHEET_V1.0.md`. **NEXT:** nhận đúng *một quyết định Gate* của PO, không yêu cầu thêm chuỗi VAL nhỏ.

---

## HISTORICAL REGISTER V2.6 (preserved below)

# VALIDATION REGISTER V2.6 — TOEIC Learning App

**Ngày cập nhật:** 2026-11-21  
**CURRENT — VAL-025 / USER PROCESS CHANGE (2026-11-21):** Product Owner yêu cầu **ưu tiên tham khảo nghiên cứu khoa học, khảo sát và ứng dụng đã có; ChatGPT chủ động đối chiếu và trình các nhóm quyết định để Product Owner duyệt**, KHÔNG bắt người dùng thực hiện từng phép baseline nhỏ tốn thời gian khi có nguồn thứ cấp đáng tin cậy. Ghi nhận đây là **yêu cầu thay đổi phương pháp từ Product Owner**, không phải kết quả nghiên cứu hành vi mới, không phê duyệt MVP hay Phase 02 gate. Phương pháp và các điều kiện mới trình trong `docs/EVIDENCE_FIRST_DECISION_PACK_V0.1.md` (D-025A–F **PROPOSED / awaiting PO approval**). Desk evidence: ETS (định dạng), STUDY4 (luyện đề tiêu chuẩn), PREP/Migii (lộ trình), Quizlet (file->flashcard), nghiên cứu spaced retrieval/mobile learning, Android (notifications), Google Play (IP). Những dữ kiện này **không tự chứng minh** import PDF/audio hoặc điểm mock chính xác trên app tương lai. `VAL-013L/R` vẫn **NOT RUN**, chuyển thành **OPTIONAL / ON HOLD, không chặn Gate Review** theo chỉ đạo PO, thay vì chờ kết quả batch mới tiếp tục. `VAL-003` mẫu và `VAL-010` giá vẫn DEFERRED; Product Vision V1.0 APPROVED; Stage 02 IN PROGRESS / GATE HOLD; Stage 03 NOT STARTED; NO CODE/UX/UI/ARCH/MVP/PRD/SRS.

---

## Historical Register through V2.5 (unmodified evidence history)

- **Ngày cập nhật:** 2026-11-21
- **CURRENT — VAL-024 (2026-11-21):** Product Owner chọn **C — tự thực hiện CẢ hai phép đo baseline Listening (`VAL-013L`) và Reading (`VAL-013R`), sau đó gửi kết quả **CÙNG MỘT LẦN**. Không ấn định ngày thực hiện, không yêu cầu thứ tự L/R, mỗi nhánh giữ log độc lập. Đây là **quyết định lên lịch/cách gửi bằng chứng**, **KHÔNG phải kết quả thực nghiệm**. `VAL-013L` và `VAL-013R`: **READY TO RUN / NOT RUN — BATCH REPORT PLANNED**. Active protocol: `docs/VAL_013_LIBRARY_NO_CODE_TEST_PLAN_V0.8.md`; recording: `docs/VAL_024_DESKTOP_BASELINE_BATCH_LOG_V0.4.md`. Chỉ phân tích sau khi nhận số liệu thực tế; nếu nhánh nào chưa chạy, ghi `NOT RUN/PARTIAL` rõ thay vì coi đã hoàn thành. H-003-VALUE-L/R **INCONCLUSIVE**; VAL-003/010 **DEFERRED**; Product Vision V1.0 APPROVED, Phase 02 HOLD, NO MVP/PRD/SRS/UX/UI/ARCHITECTURE/CODE.
- **CURRENT — VAL-023 (2026-11-21):** Product Owner chọn **A — trên laptop đã có tài liệu đầy đủ cho CẢ Listening và Reading**, bao gồm câu hỏi, đáp án và audio khớp tương ứng ở phần Listening. **Đây là tự báo cáo mức sẵn sàng, không phải kiểm kê/kiểm định file, tính hợp pháp hay khả năng tự động nhập liệu.** Hai phiên baseline solo trên laptop `VAL-013L` và `VAL-013R` **READY TO RUN / NOT RUN**; không cần upload tài liệu, người hỗ trợ hoặc code. Kế hoạch hiện hành: `docs/VAL_013_LIBRARY_NO_CODE_TEST_PLAN_V0.7.md`; phiếu ghi: `docs/VAL_023_DESKTOP_BASELINE_LOG_V0.3.md`. **NEXT:** thực hiện một lượt Listening Part 3/3 câu và một lượt Reading Part 5/5 câu theo quy trình thực tế, ghi số liệu hoặc dấu `ước lượng/không đo`; gửi CHỈ số liệu, cảm nhận để phân tích. Không có kết quả baseline ở thời điểm VAL-023. `H-003-VALUE-L/R`: INCONCLUSIVE; `VAL-003` file mẫu và `VAL-010` giá vẫn DEFERRED. Product Vision V1.0 APPROVED; Stage 02 IN PROGRESS/HOLD; no MVP/PRD/SRS/UX/UI/architecture/code.
- **Giai đoạn:** 02/11 — Market Research & Validation (IN PROGRESS)
- **Product Vision:** V1.0 APPROVED, không thay đổi
- **Phase 02 Gate:** HOLD — cần bằng chứng thực tế trước khi duyệt Requirements
- **Code / UX / architecture:** NOT AUTHORIZED
- **Historical observation (VAL-017):** Product Owner chọn **A — ứng dụng Android cần thay thế PC cho việc luyện đề TOEIC đầy đủ**, không chỉ là kênh microlearning phụ trợ. Đây là **ý định sử dụng và kỳ vọng sản phẩm** của người học #1; chưa có thử nghiệm học/thi liên tục trên Android. Mục tiêu Android phone trong Product Vision V1.0 nhất quán nhưng yêu cầu thực tế về phiên dài cần kiểm chứng; không tự động chốt full-mock 120 phút nằm trong MVP. **Baseline VAL-013L/R** vẫn đo trên desktop/laptop, solo, NOT RUN. **Mobile-fit protocol:** `VAL_017_ANDROID_LONGFORM_FIT_NO_CODE_PLAN_V0.1.md` (PLANNED / NOT RUN). **NEXT VAL-018:** làm rõ “luyện đề đầy đủ” đối với phiên 120 phút và các phiên tách Part. Các câu hỏi cũ phía dưới là lịch sử.
- **Latest observation (VAL-020, 2026-11-21):** Product Owner chọn **A — đã từng hoàn thành ít nhất một bài Full Mock TOEIC Listening & Reading trọn vẹn (khoảng 200 câu/120 phút liên tục) trên điện thoại Android**. Đây là **hồi tưởng trải nghiệm trực tiếp tự báo cáo**, nâng mức bằng chứng về khả năng hoàn thành trên smartphone so với VAL-019 (>=30 phút). **Không** phải phép thử M2 có người quan sát/biên bản, không biết ứng dụng, định dạng đề, thời lượng đo thực tế, vấn đề phát sinh, cảm giác mỏi mắt, tình trạng gián đoạn, độ tin cậy câu hỏi hay điểm số. `H-PLATFORM-01F` có **DIRECT RETROSPECTIVE COMPLETION SIGNAL / STILL INCONCLUSIVE** đối với sự tiện dụng, ổn định và tái sử dụng; **không yêu cầu lặp lại 120 phút ngay**. Nhánh M1 Android và VAL-013L/R PC vẫn **NOT RUN**; nhánh M2 no-code structured trial **NOT RUN**. **NEXT VAL-021:** hỏi một câu về trở ngại đáng kể nhất trong lần Full Mock Android đã hoàn thành.
- **CURRENT / VAL-022 (2026-11-21):** Người học #1 làm rõ lựa chọn C ở VAL-021: **mỏi mắt khi nhìn màn hình điện thoại lâu** trong lần Full Mock TOEIC trên Android; đồng thời trước đó báo cáo đọc/cuộn văn bản Reading dài bất tiện (VAL-021 A). **CHỈ mỏi mắt** được xác nhận trong nhóm C; **không suy ra** mỏi tay, điện thoại nóng hay hao pin; cũng chưa biết mức độ, mốc thời gian, tần suất, ảnh hưởng tới độ chính xác hoặc bất kỳ tình trạng sức khỏe nào. Bằng chứng = direct retrospective self-report, **không** phải structured mobile test. H-PLATFORM-01F: one-participant past completion supported, long-session comfort/quality **INCONCLUSIVE**. **R-P03 eye strain: reported qualitative risk**. Mobile structured M1/M2 và desktop VAL-013L/R đều **NOT RUN**. Ưu tiên quay về H-003-VALUE (thư viện đề cá nhân / luồng audio–câu hỏi–đáp án thống nhất). Active solo desktop plan: `docs/VAL_013_LIBRARY_NO_CODE_TEST_PLAN_V0.6.md`. **NEXT VAL-023 một câu:** liệu tài liệu hiện có trên laptop đã ghép được câu hỏi + đáp án + audio đúng bộ để tự chạy baseline Listening và Reading, chỉ một kỹ năng, hay chưa rõ/không có? **Không yêu cầu upload.** VAL-003 PDF/audio và VAL-010 giá **DEFERRED**; Vision V1.0 Approved, Phase 02 HOLD, no MVP/PRD/SRS/UX/UI/architecture/code authorization.
- **Latest observation (VAL-021, 2026-11-21):** Khi hỏi về điều gây bất tiện trong lần làm Full Mock TOEIC trên Android, Product Owner chọn **A và C**. **A:** đọc văn bản dài, cuộn màn hình và theo dõi câu hỏi Reading bất tiện. **C:** gặp ít nhất một vấn đề thuộc nhóm mỏi mắt / mỏi tay / nóng máy / hao pin; **CHƯA BIẾT yếu tố nào xảy ra, mức độ hay ảnh hưởng cụ thể**, do C là một phương án gộp. Đây là phản hồi hồi cứu trực tiếp của người học #1, không phải kết quả thử nghiệm đo được. H-PLATFORM-01F có bằng chứng hoàn thành ít nhất một lần (VAL-020), nhưng **không xác thực khả dụng/thoải mái dài hạn**; rủi ro R-P01 (đọc Reading dài) có bằng chứng pain định tính; R-P03 (mệt mỏi/thiết bị) còn phải phân rã. M1/M2 Android có log vẫn **NOT RUN**; VAL-013L/R PC **NOT RUN**; VAL-003 và VAL-010 vẫn **DEFERRED**. **NEXT VAL-022:** chỉ hỏi yếu tố nào trong nhóm C người dùng thực sự gặp (mỏi mắt, mỏi tay, nóng máy, hao pin; có thể chọn nhiều), không yêu cầu làm lại mock 120 phút ngay.
- **Nguồn bằng chứng:** Người dùng pilot #1 tự báo cáo (bao gồm VAL-009, quyết định hoãn VAL-010, lời kể lại người học #2 tại VAL-011 và khó khăn luyện đề tại VAL-013), tài liệu chính thức Android Developers/Google Play; chưa chạy thử notification hoặc xem tài liệu TOEIC mẫu; VAL-013 mới mô tả vấn đề, chưa có thử nghiệm hành vi.

- **Latest observation (VAL-019, 2026-11-21):** Người học #1 trả lời **A: đã từng học hoặc làm TOEIC liên tục ít nhất 30 phút trên Android và thấy khá thuận tiện**. Đây là **hồi tưởng trải nghiệm cá nhân, không phải phép thử VAL-017/M1/M2 có ghi log**, không rõ Part, độ dài thực tế, ứng dụng hoặc mức độ hoàn thành. Nó làm giảm bất định về mức chấp nhận phiên Android >=30 phút cho một người học, nhưng **không xác nhận được Full Mock 120 phút, đủ 7 Part, dùng lại lâu dài hoặc khả năng thay PC hoàn toàn**. **NEXT VAL-020:** đã từng hoàn thành **một bài Full Mock 200 câu / khoảng 120 phút liên tục** trên điện thoại Android chưa? Hai track no-code vẫn NOT RUN, PC baseline vẫn NOT RUN. Các dòng NEXT trong nhật ký phía dưới chỉ là lịch sử.

## 1. Validation Log

| ID | Nội dung | Dữ liệu thu thập được | Phân loại | Trạng thái |
|---|---|---|---|---|
| VAL-001 | Trải nghiệm các app TOEIC hiện có | Người dùng thấy cá nhân hóa hạn chế, nhiều thao tác, phí cao; khó ôn tài liệu sẵn có | Nhu cầu định tính một người; chưa đại diện thị trường | RECORDED — NOT MARKET VALIDATED |
| VAL-002 | Kho tài liệu TOEIC | Có kết hợp PDF/sách/audio nhiều loại | Tự báo cáo; chưa kiểm kê/chứng minh quyền | RECORDED — NOT FEASIBILITY VALIDATED |
| VAL-003 | Kiểm định một bộ đề mẫu | Người dùng hiện không thể tải bộ đề lên | Thiếu dữ liệu đầu vào, không phải kết quả thất bại | DEFERRED / PENDING EVIDENCE |
| VAL-004 | Thời điểm học cực nhanh | Người dùng có thời gian rảnh bất kỳ; mong thấy từ mới không cần mở app và khi rảnh khai báo thời lượng để được gợi ý bài | Nhu cầu cá nhân đã được ghi nhận | RECORDED — NOT USABILITY TESTED |
| VAL-005 | Vị trí hiển thị từ vựng | Người dùng chọn **thông báo Android** (không chọn widget/home hay màn hình khóa tùy chỉnh) | Lựa chọn trải nghiệm của một người | RECORDED — ANDROID FEASIBILITY PARTIAL |
| VAL-006 | Chế độ xuất hiện thông báo từ vựng | Người dùng chọn **kiểm chứng phương án ít gây phiền và hiệu quả nhất**; không chọn theo lịch/thường trực/mỗi lần bật màn hình | Quyết định chiến lược kiểm chứng; **không** là phê duyệt phương án kỹ thuật | RECORDED — EVALUATION PLAN REQUIRED |
| VAL-007 | Tương tác ngay trên thông báo | Muốn **Đã nhớ → từ khác**, **Ẩn từ**, **Tắt tất cả thông báo từ vựng**, **Nhắc sau X phút**; đã làm rõ phạm vi tắt tại VAL-008 | Nhu cầu thực tế từ một người pilot; chưa phải UX/MVP/implementation sign-off | RECORDED — FEASIBILITY PARTIAL / USABILITY NOT TESTED |
| VAL-008 | Phân biệt ẩn từ và tắt kênh học từ | **Ẩn từ này** chỉ ảnh hưởng từ đang xem; **Tắt tất cả** dừng mọi thông báo từ vựng cho tới khi người dùng bật lại; là hai lựa chọn tách biệt | Quyết định về ý nghĩa hành vi; KHÔNG phải phê duyệt nút UI hay logic ôn tập | RECORDED — INTENT CONFIRMED / IMPLEMENTATION OPEN |
| VAL-009 | Quyền chọn mức âm/rung khi có thông báo | Người dùng yêu cầu **tự chọn im lặng, rung hoặc âm thanh**; chưa chọn chế độ mặc định, giờ yên tĩnh, nhịp gửi | Trải nghiệm đã xác nhận; chưa thử mức gây phiền, chưa phê duyệt UI/MVP | RECORDED — USER CONTROL CONFIRMED / EFFECTIVENESS INCONCLUSIVE |
| VAL-010 | Trải nghiệm chi phí và giới hạn dịch vụ của các app TOEIC khác | Product Owner chọn **tạm thời bỏ qua** việc cung cấp tên app/giá từng trả/cân nhắc; không có thêm bằng chứng trải nghiệm cá nhân. Đối chiếu sơ bộ từ trang chính thức đã được ghi riêng tại mục Market Snapshot. | Quyết định tạm hoãn thu thập bằng chứng; không phải phủ nhận nhu cầu hay xác nhận giá thị trường cao | **DEFERRED BY PRODUCT OWNER — NOT VALIDATED** |
| VAL-011 | Đối chiếu vấn đề của người học pilot #2 | Product Owner trả lời người #2 “cũng như tôi thôi”: có các khó khăn tương tự người #1 ở mức tổng quát; chưa xác nhận từng vấn đề hoặc thứ tự ưu tiên, đặc biệt nhu cầu thư viện tài liệu cá nhân | Báo cáo gián tiếp từ Product Owner, KHÔNG phải phỏng vấn trực tiếp / quan sát hành vi người #2 | **RECORDED — SECOND-HAND EVIDENCE; NEEDS INDEPENDENT CONFIRMATION** |
| VAL-012 | Chọn ưu tiên kiểm chứng đầu tiên | Product Owner chọn **C — giá trị tận dụng thư viện TOEIC cá nhân**, thay vì A microlearning hay B lộ trình theo thời lượng | Quyết định ưu tiên kiểm chứng; không phải kết quả thử nghiệm hoặc phê duyệt MVP | **PRIORITIZED — EXPERIMENT NOT RUN** |
| VAL-013 | Vấn đề ưu tiên khi dùng đề cá nhân | Product Owner chọn **E — mọi bước đều bất tiện**: mở đề, chuyển qua nhiều tab/ứng dụng để nghe audio và chọn đáp án, rồi dò đáp án/lời giải. Muốn trải nghiệm làm bài tích hợp **tương tự website luyện đề phổ biến**, trên bộ tài liệu mình đã có; không yêu cầu phát minh cách làm bài mới. | Phản hồi định tính trực tiếp từ pilot #1; chưa quan sát thao tác, chưa có dữ liệu thời gian hoặc file mẫu; không chứng minh sự khả thi nhập đề | **PAIN POINT CONFIRMED BY OWNER — H-003-VALUE INCONCLUSIVE; TEST PLAN REVISED, NOT RUN** |

| VAL-014 | Phạm vi thử nghiệm no-code cho luồng luyện đề cá nhân | Product Owner chọn **C: cả Listening và Reading nhưng tách riêng**; không gộp số liệu hai kỹ năng; không yêu cầu upload file | Quyết định thiết kế phép thử, không phải dữ liệu đo, phê duyệt tính năng hay kết luận hiệu quả | **PLAN SCOPE CONFIRMED — VAL-013L / VAL-013R NOT RUN** |

| VAL-015 | Điều kiện tổ chức thử nghiệm không code | Product Owner chọn **B — tự thử một mình, không có người hỗ trợ**. Không thể giả định B Wizard-of-Oz có facilitator. Chuyển sang (1) đo baseline luồng tài liệu cá nhân riêng L/R, (2) benchmark định tính trải nghiệm luyện đề tích hợp của website khác khi có quyền truy cập. | Điều kiện thử nghiệm từ lời người dùng; **không phải** kết quả test hay bằng chứng hiệu quả | **PLAN ADAPTED TO SOLO — BASELINE / BENCHMARK NOT RUN** |

| VAL-016 | Thiết bị thường dùng khi tự luyện PDF/audio | Product Owner chọn **B — chủ yếu máy tính/laptop**, không phải điện thoại Android. Đây là môi trường xảy ra pain point mở PDF, audio, chuyển tab và dò đáp án. | Phản hồi trực tiếp của người học #1 về **bối cảnh sử dụng**, chưa phải kết quả đo | **ENVIRONMENT CONFIRMED: DESKTOP/LAPTOP; BASELINE NOT RUN; ANDROID TRANSFER UNVALIDATED** |

| VAL-017 | Vai trò mong muốn của Android so với PC | Product Owner chọn **A — thay PC cho việc luyện đề Listening & Reading đầy đủ**; không chỉ bổ trợ học nhanh. Hiện tại người học vẫn chủ yếu mở PDF/audio trên PC (VAL-016). | Nhu cầu/kỳ vọng trực tiếp từ người học #1; **không** phải bằng chứng hành vi, khả thi UX, hoặc chấp nhận làm mock 120 phút trên điện thoại | **INTENT CONFIRMED — LONG-FORM MOBILE FIT NOT TESTED; MVP UNDECIDED** |
| VAL-018 | Mục tiêu hai hình thức Android | Product Owner muốn cả luyện Part 1–7 linh hoạt và Full Mock liên tục khoảng 120 phút | Nhu cầu trực tiếp; KHÔNG là bằng chứng đã thử full mock | **EXPERIENCE INTENT CONFIRMED — M1/M2 NOT RUN** |
| VAL-019 | Trải nghiệm học/luyện TOEIC >=30 phút liên tục trên Android | Product Owner chọn **A — đã từng thực hiện và thấy khá thuận tiện** | Hồi tưởng trực tiếp; chưa có thời lượng chính xác, Part, nội dung hay log phiên; không khẳng định full mock 120 phút | **SELF-REPORTED POSITIVE PRIOR EXPERIENCE — M1/M2 NOT RUN** |
| VAL-020 | Đã từng hoàn thành Full Mock TOEIC đầy đủ trên Android chưa? | Product Owner chọn **A — đã hoàn thành ít nhất một Full Mock ~200 câu/~120 phút liên tục trên Android** | **Tự báo cáo về trải nghiệm quá khứ**; không phải dữ liệu đo trong protocol, chưa rõ app/nguồn đề/số lần/tính liền mạch thực đo, vấn đề, độ tin cậy điểm số | **RETROSPECTIVE FULL-MOCK COMPLETION REPORTED — STRUCTURED M2 NOT RUN / FIT STILL INCONCLUSIVE** |
| VAL-021 | Bất tiện trong Full Mock Android đã hoàn thành | Owner chọn **A** (đọc/cuộn Reading dài, theo dõi câu hỏi bất tiện) và **C** (nhóm mỏi mắt/mỏi tay/nóng máy/hao pin, **chưa rõ mục nào thực sự gặp**) | Hồi tưởng trực tiếp, định tính; chưa có tên app, mức độ, tần suất, số liệu hoặc kiểm tra độc lập | **REPORTED FRICTION: READING CONFIRMED; FATIGUE/DEVICE TYPE TO CLARIFY; STRUCTURED TESTS NOT RUN** |
| VAL-022 | Cụ thể vấn đề thuộc nhóm C trong Full Mock Android | Product Owner xác nhận **mỏi mắt khi nhìn màn hình lâu**; không xác nhận nóng máy, hao pin, mỏi tay | Bằng chứng định tính hồi cứu trực tiếp, chưa có mức độ, tần suất hoặc log; không phải phép thử nghiệm thu | **EYE STRAIN SELF-REPORTED — MOBILE LONG-SESSION UX INCONCLUSIVE; NO NEW TEST RUN** |

## 2. Validation Register — Hypothesis & Evidence

| ID | Giả thuyết | Bằng chứng hiện có | Cần kiểm chứng | Trạng thái |
|---|---|---|---|---|
| H-001 | Người học cần cá nhân hóa sâu hơn và thao tác đơn giản hơn | VAL-001 | Benchmark có thang đo, phản hồi pilot #2+ | INCONCLUSIVE |
| H-002 | Học nhanh 1 từ / 1 câu giúp người dùng dễ bắt đầu | VAL-001, VAL-004 | Quan sát số thao tác, thời gian tới bài đầu tiên, sử dụng lặp | INCONCLUSIVE |
| H-003 | Thư viện TOEIC cá nhân đem lại giá trị | Có PDF/sách/audio, VAL-001/002/013/014 | Đo riêng `H-003-VALUE-L` (Listening) và `H-003-VALUE-R` (Reading) bằng A/B mô phỏng no-code; kiểm kê/đề mẫu/audio/đáp án/quyền sau | INCONCLUSIVE; BOTH TESTS NOT RUN; VAL-003 DEFERRED |
| H-004 | AI tạo đáp án/lời giải và câu hỏi nguyên bản đạt chất lượng với chi phí thấp | Ý tưởng Discovery | Gold set, kiểm duyệt chuyên môn, tính đúng, quyền, chi phí | NOT TESTED |
| H-005 | Full Mock Test phù hợp để so sánh tiến bộ qua nhiều lần | Định hướng Product Vision | Đề tương đương, độ khó, quy đổi điểm, tránh nhớ đề | NOT TESTED |
| H-006 | Thông báo từ vựng giúp tăng cơ hội tiếp xúc/học mà không gây phiền | VAL-004, VAL-005, VAL-006; Android hỗ trợ thông báo | So sánh hình thức thông báo, mức nhớ từ và gây phiền, opt-in/opt-out, thử trên thiết bị | INCONCLUSIVE |
| H-007 | Đề xuất bài theo thời gian rảnh giúp tăng tần suất học | VAL-004 | Thử nghiệm luồng chọn thời lượng và hoàn tất bài phù hợp | INCONCLUSIVE |
| H-008 | Pilot 2–5 người có thể vận hành gần như miễn phí | Ràng buộc ngân sách PD-020 | Ước tính API/host/audio/free tier | NOT TESTED |

**Lưu ý về ID:** H-006 tại phiên bản V0.3 là giả thuyết về chi phí, nay chuẩn hóa thành **H-008** để tránh trùng với H-006 đã dùng trong phiên trao đổi VAL-004/005. Không thay đổi nội dung giả thuyết cũ.

| H-PLATFORM-01 | Người học có thể và muốn chuyển toàn bộ luyện đề, kể cả các phiên dài Listening/Reading, từ PC sang điện thoại Android với chất lượng trải nghiệm chấp nhận được | VAL-016 (PC hiện tại), VAL-017 (mong muốn chuyển sang Android) | Kiểm chứng hành vi trên phone với một phiên Listening và Reading riêng, độ dễ đọc Part 6/7, audio–câu hỏi, mệt mỏi, gián đoạn, khả năng duy trì phiên dài; phân biệt full mock 120 phút với luyện Part | **INCONCLUSIVE / NO MOBILE SESSION RUN** |

## 3. Android Notification — Feasibility (Desk Research Only)

**Nhu cầu xác nhận:** Người dùng muốn nhìn thấy từ vựng TOEIC từ hệ thống thông báo mà không cần mở app, đồng thời ưu tiên hiệu quả học tập **và** ít gây phiền. Việc hiển thị ở màn hình khóa phụ thuộc cài đặt Android và quyền riêng tư của người dùng.

**VAL-006 (2026-11-20):** Người dùng chọn hướng **thử nghiệm rồi quyết định**. Chưa chọn chế độ theo lịch, một thông báo thường trực, kết hợp, hay kích hoạt mỗi lần bật màn hình. Không mặc định việc bật màn hình là một trigger notification được hệ điều hành bảo đảm.

| Khía cạnh | Bằng chứng / giới hạn | Kết luận |
|---|---|---|
| Nội dung thông báo | Android cho phép title/body; nội dung hiển thị phụ thuộc trạng thái mở rộng/cài đặt | Feasible in principle |
| Quyền thông báo | Android 13+ có runtime `POST_NOTIFICATIONS` cho non-exempt notifications | Permission needed |
| Notification channel | Android 8.0+ yêu cầu tạo channel | Platform requirement |
| Lock-screen visibility | Android hỗ trợ PUBLIC/PRIVATE/SECRET; người dùng có quyền cấu hình | Not guaranteed |
| Gửi đúng giờ | Doze/App Standby và OEM có thể trì hoãn công việc nền | Must test |
| Mỗi lần bật/mở màn hình nhận từ mới | Khác với thông báo định kỳ; chưa kiểm chứng khả năng/độ ổn định/quyền | NOT VALIDATED |
| Google Play | Thông báo phải phù hợp tính năng cốt lõi, không giả hệ thống, không dùng làm quảng cáo gây phiền | Policy check necessary |
| Không gây phiền | Tần suất, tạm dừng, giờ yên tĩnh, tùy chọn opt-in | UX hypothesis |

**Nguồn tham khảo (Android Developers):**
- https://developer.android.com/develop/ui/compose/notifications/create-notification?hl=en
- https://developer.android.com/training/monitoring-device-state/doze-standby
- https://developer.android.com/develop/background-work/services/alarms
- https://developer.android.com/develop/ui/compose/notifications/channels
- https://developer.android.com/develop/ui/compose/notifications/notification-permission
- https://support.google.com/googleplay/android-developer/answer/9969861?hl=en

## 4. Quyết định, mở và rủi ro

### Decision Log
- **VAL-D006 (APPROVED VALIDATION STRATEGY):** So sánh các cách hiển thị thông báo theo tiêu chí **ít gây phiền, giúp nhớ từ/học thật, dễ kiểm soát**; không khóa bất cứ chế độ kỹ thuật nào vào MVP. Ưu tiên thử nghiệm tự nguyện, cho phép dừng, không ép nhận thông báo.
- **VAL-D005:** Product Owner chọn **Notification** làm nơi hiển thị nhanh từ vựng; đây là lựa chọn trải nghiệm cần kiểm chứng, **không khóa chức năng MVP, UI hay cơ chế kỹ thuật**.
- **VAL-D004:** Có 2 tình huống học: (a) tiếp xúc từ mới trong khoảnh khắc ngắn, (b) chủ động nêu thời lượng rảnh và nhận đề xuất bài.
- **VAL-D003:** Hoãn kiểm định file mẫu do chưa thể upload; không tự đánh giá nội dung đã phù hợp.

### Open Questions
- **OQ-N01 (RESOLVED BY VAL-006):** Chưa chọn cơ chế xuất hiện; sẽ so sánh phương án thay vì chốt theo trực giác.
- OQ-N02 (PARTIALLY RESOLVED BY VAL-009): Người dùng được quyền chọn **im lặng/rung/âm thanh**. Mặc định, giờ yên tĩnh, tần suất và ngưỡng gây phiền còn OPEN.
- OQ-N03: Nội dung notification: từ mới, từ ôn, nghĩa, ví dụ, cách phát âm hay bài hỏi nhanh?
- OQ-N04: Tiêu chí thử nghiệm (bắt đầu học, nhớ từ, khó chịu, tỷ lệ tắt thông báo).
- OQ-N05: Hiện thị đúng trên những phiên bản Android và thiết bị khác nhau; độ tin cậy khi Doze/tiết kiệm pin.
- OQ-C01: Content inventory, cấu trúc, chất lượng, audio mapping, bản quyền — chờ tài liệu mẫu.

### Risks
- **R-N01:** Quá nhiều thông báo khiến người dùng tắt quyền hoặc gỡ app.
- **R-N02:** Doze/khóa màn hình/bộ tiết kiệm pin khiến thời gian/hiển thị không như kỳ vọng.
- **R-N03:** Hiểu nhầm thông báo định kỳ có thể tự đổi từ ở mỗi lần sáng màn hình.
- **R-N04:** Quyền thông báo bị từ chối, app vẫn phải học được bình thường.

## 5. Kế hoạch kiểm chứng đề xuất — CHƯA triển khai, không viết code

**Mục tiêu:** Xem thông báo có giúp người dùng tiếp xúc, nhớ từ và tự nguyện tiếp tục sử dụng mà không làm họ khó chịu hay không; không lấy số thông báo đã gửi làm thước đo thành công.

| Phương án thử nghiệm | Cách giả lập ban đầu (không code sản phẩm) | Điểm cần đo |
|---|---|---|
| A — Theo lịch, ít lần | Gửi 1–2 thẻ từ vựng/ngày vào khung giờ người tham gia tự nguyện chọn, dùng công cụ nhắc/tin nhắn sẵn có | Số lần xem, nhớ từ sau ~24 giờ, mức gây phiền |
| B — Một từ có sẵn để xem khi rảnh | Để một thẻ từ dễ truy cập (ví dụ ghi chú ghim) làm **proxy cho mô hình thường trực**, không giả vờ đã thử notification thật | Số lần chủ động xem, tỷ lệ nhớ, chủ động dùng tiếp |
| C — Kết hợp | Chỉ thử sau A/B nếu giá trị kỳ vọng rõ, đồng thời tránh nội dung trùng | Lợi ích bổ sung so với mức gây phiền tăng thêm |

- Tập hợp ít nhất người dùng 01 và 02 nếu họ đồng ý; thử các phương án trong khoảng thời gian ngắn tương đương, cho phép tắt/bỏ cuộc bất kỳ lúc nào. Thời lượng và ngưỡng đạt cần được Product Owner duyệt trước khi tiến hành.
- Đo dự kiến: lượt **đã nhìn thấy** (không chỉ đã gửi), số từ nhớ sau khoảng 24 giờ, cảm nhận gây phiền (thang 1–5), số lần bỏ qua/tắt, và mức sẵn sàng tiếp tục. Các chỉ số và ngưỡng nghiệm thu vẫn là **đề xuất**.
- Các bản giả lập không chứng minh Android hiển thị ổn định; kiểm tra trên máy thật, quyền, lock-screen và Doze phải thực hiện sau khi có quyền làm feasibility test.
- Không đề nghị `exact alarm`, foreground service hoặc screen-on trigger khi không có nhu cầu kỹ thuật hợp lệ và chưa đánh giá tác động.
- Nếu không đo được hiệu quả ghi nhớ và mức phiền một cách đáng tin, đánh dấu **INCONCLUSIVE**, không tự phê duyệt MVP.

## 6. Gate & Next Question

- **Vision V1.0:** APPROVED.
- **Phase 02:** IN PROGRESS, HOLD — no sign-off to Requirements.
- **MVP/PRD/SRS/Architecture/Code:** NOT AUTHORIZED.
- **Historical prompt after VAL-008 (answered at VAL-009):** thông báo mặc định im lặng/rung/âm thanh; VAL-009 đã quyết định người dùng tự chọn, mặc định còn để mở.
- **VAL-006 status:** CHOICE OF EVALUATION APPROVED; hiệu quả học & mức gây phiền chưa kiểm chứng; MVP NOT LOCKED.


## 7. Validation 07 — Notification Actions (2026-11-20)

**Nguồn:** Product Owner phản hồi trực tiếp về trải nghiệm mong muốn: trên thông báo có các lựa chọn (1) đã nhớ từ, hiển thị từ khác; (2) tắt không hiện nữa; (3) hiện lại sau một khoảng phút lựa chọn. Đây là yêu cầu về hành vi và quyền kiểm soát, **không chốt MVP/UI/công nghệ**.

| ID | Yêu cầu/giả thuyết | Đã xác nhận | Chưa xác minh |
|---|---|---|---|
| VAL-007A | `Đã nhớ` để nhận từ khác | Mong muốn có thao tác trên thông báo | Từ đã nhớ sẽ được ôn lại hay đánh dấu thành thạo? Thời điểm chuyển từ? |
| VAL-007B | `Tắt, không hiện nữa` | Cần một cách từ chối hiển thị | **Chỉ từ hiện tại**, toàn bộ thông báo từ vựng, hay cả hai? |
| VAL-007C | `Hiện sau X phút` | Mong muốn trì hoãn linh hoạt | Hoãn chính từ hiện tại hay tất cả; các mốc thời gian; độ tin cậy scheduler |
| VAL-007D | Thao tác không cần mở ứng dụng | Giảm số bước học | Thử trên các phiên bản Android và thiết bị pilot; giao diện hệ điều hành có thể thay đổi |

**Android feasibility desk research:** Android notification có thể chứa tới ba action buttons; nhận action qua pending intent/receiver, không nhất thiết mở app. Từ Android 13, thông báo thông thường cần quyền `POST_NOTIFICATIONS`. Các lệnh 'nhắc sau X phút' phụ thuộc cơ chế lên lịch có thể bị Doze/battery saver trì hoãn; không cam kết thời điểm chính xác tuyệt đối cho notification học từ. Các action cụ thể và trạng thái học phải được kiểm chứng trước khi đặc tả.

**Sources (official):**
- https://developer.android.com/develop/ui/compose/notifications/create-notification
- https://developer.android.com/reference/android/app/Notification.Builder
- https://developer.android.com/develop/background-work/services/alarms
- https://developer.android.com/develop/ui/compose/notifications/notification-permission

**Risks/validation:**
- `Đã nhớ` tự báo cáo không đồng nghĩa đã thuộc từ bền vững; cần đo nhớ sau 24 giờ hoặc thời gian phù hợp trong thử nghiệm.
- Bấm `Tắt` với ý nghĩa mơ hồ có thể vô tình chặn toàn bộ notification, gây mất kiểm soát.
- Khi hệ thống chưa cấp quyền/đang chế độ tiết kiệm pin, không thể bảo đảm hiển thị đúng hẹn.
- Tối đa 3 action có thể khiến nhãn, nội dung thu gọn không hiển thị đồng nhất trên mọi thiết bị.

**Status:** Interaction concept RECORDED; technical feasibility PARTIAL; user value/effectiveness INCONCLUSIVE; MVP NOT APPROVED. VAL-003 vẫn DEFERRED cho tới khi có file đề.

**NEXT QUESTION:** Từ lựa chọn `Tắt không hiện nữa`, người dùng muốn (A) chỉ bỏ từ hiện tại, (B) tắt mọi thông báo học từ cho đến khi tự bật lại, hay (C) cần cả hai lựa chọn tách biệt? Chỉ hỏi điểm này trước khi thiết lập thử nghiệm chi tiết.


## 8. Validation 08 — Separate "Hide Word" and "Disable All Vocabulary Notifications" (2026-11-20)

**Evidence / decision (VAL-D008, confirmed by Product Owner):** Người dùng chọn cả hai hành vi tách biệt. Đây là quyết định về **ngữ nghĩa hành động**, không phải phê duyệt số lượng/nội dung nút giao diện hay phạm vi MVP.

| Behavior ID | Hành vi mong muốn đã xác nhận | Không được tự suy diễn | Trạng thái |
|---|---|---|---|
| N-A01 | `Đã nhớ` ghi nhận phản hồi và yêu cầu chuyển sang từ khác | Không đánh dấu từ đã thuộc vĩnh viễn; thời điểm ôn lại chưa chốt | EXPERIENCE CONFIRMED, LOGIC OPEN |
| N-A02 | `Ẩn từ này` loại từ đang hiển thị ra khỏi nội dung notification trước mắt; thông báo với từ khác vẫn có thể đến | Không tự tắt tất cả notification; chưa chốt ẩn từ vô thời hạn hay chỉ tạm thời | INTENT CONFIRMED, DURATION OPEN |
| N-A03 | `Tắt tất cả` dừng **tất cả thông báo học từ vựng** cho đến khi người dùng tự bật lại | Không tự suy diễn là tắt thông báo khác trong app hay tắt bằng một nút system-setting không thể đảo ngược | INTENT CONFIRMED, UX OPEN |
| N-A04 | `Nhắc lại sau X phút` cho người học hoãn lời nhắc | Chưa chốt hoãn từ đang xem hay cả loạt thông báo, các khoảng thời gian và độ chính xác | INTENT CONFIRMED, SCHEDULING OPEN |

**Android feasibility constraint (official documentation):** Một notification mở rộng hỗ trợ tối đa **ba action buttons**, trong khi hiện có **bốn hành vi**. Không hứa bốn nút cùng hiển thị; nhóm giải pháp cần nghiên cứu ở giai đoạn UX/feasibility có thể gồm thao tác trong app/settings hoặc gộp luồng có chủ đích, nhưng chưa chọn cách nào. Người dùng có thể thay đổi quyền, âm/rung/importance qua Notification Channels; hiển thị thực tế phụ thuộc máy, Android version, quyền và trạng thái nền.

**Nguồn chính thức:**
- https://developer.android.com/develop/ui/compose/notifications/create-notification (tối đa 3 notification actions)
- https://developer.android.com/develop/ui/compose/notifications/channels (người dùng điều khiển notification channel)
- https://developer.android.com/training/monitoring-device-state/doze-standby (thời điểm nhắc có thể bị trì hoãn)

**Rủi ro cập nhật:**
- **R-N05:** `Ẩn từ này` và `Tắt tất cả` dễ bị hiểu nhầm/bấm nhầm; đánh giá phân biệt nhãn và kiểm soát khôi phục.
- **R-N06:** Bốn chức năng vượt số lượng action trực tiếp tối đa (3) của notification mở rộng; cần thử usability trên Android thật trước khi yêu cầu UX/UI.
- **R-N07:** `Đã nhớ` không bảo đảm ghi nhớ bền vững; cần thử nhớ lại, không loại vĩnh viễn khỏi lịch ôn dựa trên một lần chạm.

**Validation experiment bổ sung (chưa triển khai):** Cho người dùng pilot phân biệt hai tình huống `không muốn thấy lại từ X` và `không muốn nhận thông báo từ vựng nữa`, quan sát họ có chọn đúng hành động và biết cách bật lại không. Thu thập mức gây phiền, tỷ lệ bấm nhầm và phản hồi về sự tự chủ.

**Open questions còn lại, không hỏi dồn:**
1. **NEXT (VAL-009):** Mặc định thông báo nên im lặng, rung nhẹ hay có âm thanh? Đây là một đầu vào cho thử nghiệm mức gây phiền.
2. Khi nào một từ đã ẩn có thể được đưa trở lại để ôn (nếu có)?
3. Các mốc `X phút` và nội dung nào được nhắc lại?
4. Từ vựng có phù hợp để hiện trên thiết bị/màn hình khóa theo thiết lập riêng tư của người học không?
5. Đặt tiêu chí nghiệm thu thử nghiệm, đo khả năng ghi nhớ, việc sử dụng tự nguyện và tần suất tắt.

**Gate:** Product Vision V1.0 APPROVED; Stage 02 IN PROGRESS/HOLD; **no MVP approval, no UI architecture or code**. VAL-003 content sample remains DEFERRED.


## 9. Validation 09 — Tùy chọn âm thanh / rung / im lặng (2026-11-20)

**Nguồn bằng chứng:** Product Owner chọn phương án D: **người học tự tùy chỉnh âm thanh, rung hoặc im lặng** cho thông báo từ vựng. Chưa có thử nghiệm hành vi trên thiết bị hoặc với người học #2.

### Quyết định VAL-D009

- **CONFIRMED EXPERIENCE INTENT:** Cho phép người học chọn giữa **im lặng / rung / âm thanh**; không ép tất cả dùng chung một mức độ làm phiền.
- **NOT DECIDED:** Chế độ mặc định, khung giờ yên tĩnh, tần suất tối đa, thời điểm xin quyền, cơ chế thay đổi tùy chọn, UX màn hình cài đặt, các channel kỹ thuật.
- Giữ nguyên VAL-D008: `Ẩn từ này` khác `Tắt tất cả thông báo học từ vựng`; cả hai khác với việc bật/tắt âm thanh.
- Đây là **quyết định về nhu cầu người dùng**, không phải phê duyệt chức năng MVP hoặc kiến trúc.

### Đánh giá khả thi Android (desk research, chưa thử máy)

| Khía cạnh | Căn cứ chính thức / rủi ro | Kết luận |
|---|---|---|
| User control | Android 8.0+ dùng notification channels; người dùng có thể điều chỉnh importance/âm thanh/rung của kênh | FEASIBLE IN PRINCIPLE |
| Quyền ứng dụng | Android 13+ yêu cầu `POST_NOTIFICATIONS` cho thông báo thường | PHẢI CÓ QUYỀN |
| Khả năng app thay đổi thuộc tính channel | Sau khi channel được tạo, app không được tự thay đổi hành vi âm thanh/hiển thị của channel; chỉ người dùng thay đổi ở system settings | CẦN ĐÁNH GIÁ LUỒNG THAY ĐỔI TÙY CHỌN, KHÔNG HỨA CÔNG TẮC ỨNG DỤNG SẼ LUÔN GHI ĐÈ CÀI ĐẶT HỆ THỐNG |
| Chế độ hệ thống | DND, tùy biến nhà sản xuất/Android và cài đặt riêng tư có thể điều chỉnh việc rung/phát âm | PHẢI KIỂM THỬ TRÊN THIẾT BỊ |
| Giá trị người học | Thêm quyền tùy chỉnh có thể giảm cảm giác bị làm phiền nhưng chưa đo được | H-006 INCONCLUSIVE |

**Nguồn chính thức:**
- https://developer.android.com/develop/ui/compose/notifications/channels
- https://developer.android.com/develop/ui/compose/notifications/notification-permission
- https://developer.android.com/design/ui/mobile/guides/home-screen/notifications

### Giả thuyết / kế hoạch kiểm chứng (chưa thực hiện)

- **H-006 (INCONCLUSIVE):** Có tùy chọn âm/rung/im lặng và quyền ẩn/tắt sẽ làm thông báo học từ **dễ chấp nhận hơn**, nhưng hiệu quả học và mức phiền chưa xác định.
- **H-009 (NEW — NOT TESTED):** Khi có quyền chọn mức thông báo, người học sẽ duy trì việc sử dụng nhiều hơn so với một chế độ cố định; phải kiểm chứng bằng hành vi thực tế, không suy luận từ lựa chọn khảo sát.
- **Phương án thử nghiệm, chưa duyệt:** Bắt đầu im lặng như một **điểm xuất phát thử nghiệm** (không chốt mặc định sản phẩm), người tham gia được chủ động đổi rung/âm thanh; so sánh số lần xem, tỷ lệ tắt/ẩn/hoãn, mức gây phiền 1–5, nhớ từ sau khoảng 24 giờ, mong muốn tiếp tục. Thử nghiệm thủ công không chứng minh khả thi Android; cần kỹ thuật test thiết bị ở giai đoạn phù hợp.
- **R-N08:** Hứa có tùy chỉnh trong app nhưng bị giới hạn bởi cài đặt Notification Channel của Android; cần kiểm chứng và hướng dẫn rõ khi người dùng cần mở system settings.

### Open Questions — không chặn việc chuyển sang giả thuyết khác

- OQ-N02A: Mặc định âm thanh/rung/im lặng là gì? Đánh giá qua thử nghiệm, **chưa quyết định**.
- OQ-N02B: Giờ yên tĩnh và tần suất thế nào để không gây phiền?
- OQ-N02C: Cách chỉnh tùy chọn và hành vi khi Android system settings xung đột với lựa chọn trong app?
- OQ-N02D: Mức nhớ từ và tỷ lệ tắt/ẩn/hoãn có cải thiện khi có tùy chỉnh?

### Phase 02 Gate và bước tiếp theo

- **Product Vision V1.0:** APPROVED, không đổi.
- **Phase 02:** IN PROGRESS / HOLD. **MVP, PRD/SRS, UX/UI, architecture, code: NOT AUTHORIZED.**
- **VAL-003:** Đánh giá PDF/audio mẫu DEFERRED do chưa thể tải file, không yêu cầu tải lại vào lúc này.
- **NEXT VALIDATION PRIORITY — VAL-010:** Quay lại Market/Price Validation; hỏi Product Owner 1–3 ứng dụng TOEIC họ từng dùng/cân nhắc, gói giá (nếu nhớ), và nỗi đau cụ thể. Bằng chứng cá nhân chưa đủ kết luận thị trường hiện có giá cao. Song song lên kế hoạch benchmark giá và trải nghiệm từ nguồn công khai/hands-on.


---

## VAL-010 UPDATE (2026-11-20) — PRICE EXPERIENCE DEFERRED, MARKET SNAPSHOT ONLY

**Quyết định VAL-D010 — DEFERRED:** Product Owner chọn **tạm thời bỏ qua** câu hỏi về những app TOEIC đã dùng và mức giá/giới hạn cụ thể từng trải nghiệm. Không hỏi lại ở các bước ngay tiếp theo. Việc này **không hủy bỏ** mong muốn chi phí dễ tiếp cận và **không khẳng định** các app đối thủ đều quá đắt.

### Đối chiếu dữ liệu công khai (desk research; không trải nghiệm trực tiếp)

| Đối thủ | Bằng chứng từ nhà cung cấp | Giới hạn kết luận |
|---|---|---|
| STUDY4 | Trang khóa học TOEIC niêm yết khóa Complete TOEIC **1.050.000đ (giá ưu đãi)** và giá gốc **1.800.000đ** khi tra cứu | Giá khóa học, không phải phí subscription tương đương; khuyến mãi thay đổi |
| PREP | Trang luyện đề TOEIC công bố **25 đề cơ bản** và gói PRO mở khóa kho đề/tính năng khác | Chưa xác định trải nghiệm thực tế, giá PRO tại cùng mốc |
| Migii TOEIC | Trang sản phẩm mô tả lộ trình TOEIC và khả năng nâng cấp Premium | Không khẳng định giá chính xác hoặc giới hạn theo thị trường VN tại thời điểm này |

**Nguồn chính thức (truy cập ngày 2026-11-20):**
- https://study4.com/courses/online/toeic/
- https://prepedu.com/vi/toeic/test-practice
- https://migii.net/vi/toeic

**Đánh giá:** Có mô hình miễn phí, khóa học trả phí, Premium ở nhiều nền tảng, nhưng **chưa đủ bằng chứng về khả năng chi trả, tính tương đương của các gói, sự hài lòng, hoặc mức giá thị trường bị cho là quá cao**. H-001 (giá trị khác biệt) vẫn **INCONCLUSIVE**. Chiến lược monetization của app chưa phê duyệt.

### Cập nhật giả thuyết/đầu việc

- **H-PRICE-01 (INCONCLUSIVE / DATA COLLECTION DEFERRED):** Giá là rào cản đáng kể với người học Việt. Nguồn: phản hồi 1 người; chưa có dữ liệu về mức sẵn lòng trả, lựa chọn giữa gói và tính năng, hoặc đánh giá gói cạnh tranh. Sẽ xem xét lại vào thời điểm quyết định chiến lược thương mại, **chỉ khi Product Owner muốn**.
- **VAL-003:** kiểm định PDF/audio vẫn DEFERRED do chưa thể upload; không gán thất bại kỹ thuật.
- **H-006/H-009:** thông báo tùy chỉnh mới chỉ được ghi nhận về nhu cầu; hiệu quả học và mức độ gây phiền chưa thử nghiệm.
- **NEXT — VAL-011:** Thu thêm bằng chứng từ **người học #2 (~650 TOEIC chính thức, mục tiêu 750–850)**: khó khăn khi học, kỳ vọng app, và khả năng bắt đầu phiên học ngắn. Không suy đoán hai người có cùng nhu cầu. Nếu chưa trao đổi với người #2, ghi NOT COLLECTED và chuẩn bị 3–5 câu phỏng vấn ngắn, không ép người dùng cung cấp ngay.
- **Stage gate:** Product Vision V1.0 APPROVED; Phase 02 IN PROGRESS / HOLD; **NO MVP APPROVAL, NO UX/UI, NO ARCHITECTURE, NO CODE**.
- **Canonical register:** `docs/VALIDATION_REGISTER_V1.1.md`; các bản V0.3–V1.0 lưu lịch sử.

---

## VAL-011 UPDATE (2026-11-20) — SECOND PILOT LEARNER, INDIRECT REPORT

**Nguồn:** Product Owner trả lời về người học #2: “Cũng như tôi thôi.” Đây là thông tin do Product Owner truyền đạt, **chưa có lời kể trực tiếp, phỏng vấn hay quan sát** của người học #2.

**Kết luận ghi nhận:**
- Có tín hiệu người học #2 (~650 TOEIC chính thức, mục tiêu 750–850) gặp các trở ngại học TOEIC tương tự người #1 (~550 mock, mục tiêu 650–750).
- Có thể tạm xem **khó tìm lộ trình phù hợp, học không đều, thiếu cá nhân hóa và học nhanh chưa thuận tiện** là các vấn đề chia sẻ theo báo cáo của Product Owner. Chưa biết mức độ hoặc thứ tự ưu tiên của từng vấn đề.
- Không suy ra người #2 sở hữu kho PDF/audio hoặc chắc chắn gặp khó khăn riêng về nhập tài liệu.
- Một lời kể gián tiếp **không được tính là bằng chứng độc lập thứ hai**, và không cho phép kết luận nhu cầu toàn thị trường đã VALIDATED.

**Validation Register changes:**
- `VAL-011 = RECORDED / SECOND-HAND EVIDENCE / DIRECT CONFIRMATION PENDING`.
- `H-001 = INCONCLUSIVE`; đã có tín hiệu phù hợp của hai người trong nhóm pilot, nhưng cần hỏi trực tiếp và quan sát hành vi.
- `H-002`, `H-003`, `H-007 = INCONCLUSIVE`, chờ ưu tiên bài kiểm chứng có thể thực hiện **không cần code và không cần file PDF**.
- `VAL-003 = DEFERRED` (chưa thể upload mẫu PDF/audio); `VAL-010 = DEFERRED BY PRODUCT OWNER` (giá đối thủ).

**NEXT — VAL-012: chọn một giả thuyết kiểm chứng đầu tiên (không code):**
1. `A`: Một từ / một câu TOEIC trong khoảng 30–60 giây, tối thiểu thao tác.
2. `B`: Người học nhập thời gian rảnh và được đề xuất một bài ngắn phù hợp.
3. `C`: Đo mức ưu tiên của kho tài liệu cá nhân bằng mô phỏng tình huống, **không khẳng định xử lý file**.
Quyết định ưu tiên thử nghiệm **không đồng nghĩa phê duyệt MVP**. Khi phù hợp, xác minh trực tiếp với người học #2 bằng vài câu hỏi ngắn, không bắt người dùng kể lại lần nữa ngay lúc này.

**Stage Gate:** Product Vision V1.0 APPROVED; Phase 02 Market Research & Validation IN PROGRESS / HOLD; Requirements/MVP/UX/UI/architecture/code NOT AUTHORIZED.


---

## VAL-012 UPDATE (2026-11-20) — ƯU TIÊN KIỂM CHỨNG GIÁ TRỊ THƯ VIỆN ĐỀ CÁ NHÂN

**Product Owner selection:** C — kiểm chứng **giá trị sử dụng** của `Personal TOEIC Library` trước các hướng microlearning nhanh và bài theo thời lượng. Product Vision V1.0 giữ nguyên APPROVED; giai đoạn 02 vẫn IN PROGRESS / HOLD.

### Tách bạch các giả thuyết, không đánh đồng ưu tiên với bằng chứng

| ID | Giả thuyết / câu hỏi | Bằng chứng hiện có | Kết quả hiện tại | Cần làm |
|---|---|---|---|---|
| H-003-VALUE | Một kho câu hỏi từ tài liệu người học đã có, được lập chỉ mục và truy cập thuận tiện, làm giảm ma sát bắt đầu và hoàn thành bài luyện | Người dùng có PDF/sách/audio và thấy việc ôn bằng nguồn sẵn có bất tiện; VAL-012 chọn ưu tiên thử | **INCONCLUSIVE; experiment selected, not run** | So sánh quy trình sử dụng PDF gốc với bản chỉ mục thủ công (no-code) |
| H-003-INGEST | Có thể tự động trích xuất chính xác câu, đáp án, hình, transcript, mốc audio từ tài liệu nhiều loại | Có tài liệu đa dạng, chưa có file mẫu | **PENDING EVIDENCE / VAL-003 DEFERRED** | Kiểm định tài liệu thực khi Product Owner có thể cung cấp |
| H-003-RIGHTS | Có thể dùng nội dung cho pilot và phân phối công khai với quyền tương ứng | Chưa có giấy phép/chứng cứ cụ thể | **UNKNOWN — LICENSING BLOCKER FOR PUBLIC DISTRIBUTION** | Kiểm kê tác giả, điều kiện sử dụng, phạm vi sao chép/chia sẻ |

### Đề xuất VAL-013 — thử nghiệm hành vi không cần code, không cần tải file

**Tên:** Manual Library Convenience Test / Wizard-of-Oz thủ công.

**Mục tiêu:** Kiểm tra việc người học dùng tài liệu *đã được lập chỉ mục theo Part, trang, câu, đáp án và vị trí audio* có thuận tiện hơn cách tự mở PDF/sách/audio hiện tại hay không. Chưa đánh giá tự động nhập file và chưa chứng minh tăng điểm TOEIC.

**Đối tượng:** người học #1 và (nếu tự nguyện) người học #2. Không biến thông tin do người #1 kể lại thành quan sát trực tiếp của #2.

**Chuẩn bị (không gửi file lên ChatGPT):**
1. Chọn **1 bộ đề mà từng người có quyền sử dụng phù hợp** và chọn một nhóm câu có đáp án (ưu tiên một Part Reading, nơi không bị nhiễu bởi thao tác audio; audio thử riêng sau). Không sao chép/tái phân phối nội dung sang bên không có quyền truy cập.
2. Soạn *chỉ mục riêng* khoảng 10–12 câu: `mã nguồn/tập`, `Part`, `trang/câu`, `trang đáp án`, `vị trí audio (nếu có)`, `độ khó ước lượng (nếu biết)`. Có thể dùng giấy ghi chú/ứng dụng ghi chú sẵn có. Không cần nhập nội dung câu hỏi có bản quyền vào dịch vụ ngoài.
3. Hai điều kiện: **A — hiện trạng:** tự mở PDF/sách và tìm câu/lời giải; **B — hỗ trợ thủ công:** sử dụng chỉ mục đã chuẩn bị để đến câu/đáp án. Mỗi điều kiện dùng 5 câu **khác nhau nhưng cùng Part/độ khó gần tương đương**; không tái sử dụng cùng câu.
4. Đổi thứ tự A/B giữa hai người nếu có thể để giảm tác động do quen thao tác. Cho phép tự học như thường ngày, không hỗ trợ trực tiếp khác nhau giữa hai điều kiện.
5. Dùng đồng hồ điện thoại để ghi mốc và phản hồi trong một bảng nhỏ. Ghi cả **thời gian tạo chỉ mục** (chi phí chuẩn bị), không chỉ thời gian học.

**Chỉ số đề xuất:**
- `T_start`: từ lúc quyết định học đến khi **nhìn thấy câu đầu tiên** (giây).
- `T_feedback`: từ khi trả lời đến khi **mở được đáp án/lời giải** (giây).
- `Completion`: số câu hoàn thành / 5 trong cùng một khoảng thời gian; ghi số lần bỏ dở vì thao tác.
- `Steps`: số thao tác chuyển màn hình/tìm trang đáng kể, đếm tương đối nhất quán.
- `Ease`: độ thuận tiện tự đánh giá 1–5 sau mỗi điều kiện; `Would use again`: Có/Không/Tùy điều kiện.
- `Prep cost`: phút chuẩn bị chỉ mục / 10 câu; ghi cả lỗi chỉ mục, đáp án không khớp, audio không ghép được (nếu thử).

**Ngưỡng quyết định sơ bộ (đề xuất để Product Owner duyệt trước khi thực hiện; không phải ngưỡng đã phê duyệt):**
- **Tín hiệu tích cực** nếu cả hai người (khi có hai người tham gia) thích B, `T_start` hoặc `T_feedback` của B giảm khoảng **30% trở lên**, và không phát sinh lỗi đối chiếu đáp án; đồng thời công sức chuẩn bị được đánh giá có thể chấp nhận. Đây chỉ là tín hiệu định tính/pilot, không kết luận thị trường.
- **Cần điều chỉnh** nếu lợi ích thời gian nhỏ, hoặc chỉ số thuận tiện tăng nhưng chuẩn bị quá tốn thời gian; xem xét ưu tiên tự động hóa nhập liệu trong Feasibility sau.
- **Inconclusive** nếu chưa thực hiện, chỉ có một vài quan sát quá ít, hoặc hai điều kiện không tương đồng; không được ghi `VALIDATED` chỉ từ mong muốn.

**Rủi ro diễn giải:** Bản chỉ mục thủ công không tương đương một app có trải nghiệm hoàn chỉnh; phép thử chỉ đo *giá trị của việc tổ chức nguồn tài liệu*, không đo độ chính xác OCR, matching audio, chất lượng AI, retention 4 tuần hay tác động tăng điểm TOEIC. Người dùng đã nói không thể upload file ở thời điểm hiện tại: **không hỏi lại file lúc này**.

**Chi tiết thao tác, phiếu ghi dữ liệu, cách kết luận:** `docs/VAL_013_LIBRARY_NO_CODE_TEST_PLAN_V0.1.md`.

### Gate & Next Question

- **VAL-012:** PRIORITY SELECTED; experiment NOT RUN; H-003-VALUE INCONCLUSIVE.
- **VAL-003:** DEFERRED (sample upload unavailable) — không được gán `FAILED`.
- **VAL-010:** DEFERRED BY PRODUCT OWNER — không thúc ép dữ liệu giá ở bước liền sau.
- **NEXT VAL-013:** Hỏi người dùng **bước thao tác nào phiền nhất khi dùng PDF/sách/audio hiện có** để xác định chính xác ma sát cần đo trước (tìm câu, mở audio đúng đoạn, dò đáp án, hay lưu lại lỗi sai). Một câu hỏi, không chuyển sang thiết kế UI hay code.
- **Product Vision:** V1.0 APPROVED, không đổi. **Phase 02:** IN PROGRESS/HOLD. **MVP/PRD/SRS/UX/UI/architecture/code:** NOT AUTHORIZED.


---

## VAL-013 UPDATE (2026-11-20) — MA SÁT CHÍNH LÀ QUY TRÌNH LUYỆN ĐỀ RỜI RẠC

**User evidence (direct, pilot #1):** “Tất cả, cần quy trình thống nhất”; phải mở đề, dò đáp án, chuyển nhiều tab để vừa nghe audio vừa chọn đáp án. Người dùng nói trải nghiệm luyện như các website luyện đề hiện có là đủ; điểm đau nằm ở **khả năng dùng chính kho đề hiện có theo luồng này**. Đây là mô tả nhu cầu, **không** phải bằng chứng rằng mọi website hiện có đều làm được, rằng nội dung có quyền để upload, hay rằng hệ thống đã có khả năng trích xuất PDF/audio.

**PAIN-004 refined:**
- `PAIN-004A`: Phải mở nhiều nguồn/tab để tìm và làm câu hỏi.
- `PAIN-004B`: Audio không được ghép thuận tiện với câu hỏi Listening.
- `PAIN-004C`: Chọn/lưu đáp án và dò đáp án/lời giải còn rời rạc.
- `PAIN-004D`: Lưu lỗi sai/ôn lại khó thao tác. Đây là vấn đề đã ghi nhận trước đó, chưa đo độc lập ở VAL-013.
- `PAIN-004E`: Có tài liệu nhưng khó biến thành bộ đề dùng được trong trải nghiệm luyện thi tiêu chuẩn.

**H-003 split, status unchanged:**
- `H-003-VALUE`: Nếu quy trình luyện đề được tổ chức thành một phiên liền mạch (đề + audio + đáp án + kết quả), người học giảm chuyển đổi ngữ cảnh, bắt đầu/hoàn tất nhanh hơn và muốn tiếp tục dùng. **INCONCLUSIVE** — chỉ mới có báo cáo định tính.
- `H-003-INGEST`: Tự động chuyển PDF/sách/audio sang dữ liệu câu hỏi có cấu trúc. **PENDING SAMPLE / VAL-003 DEFERRED**.
- `H-003-RIGHTS`: Có quyền số hóa, lưu trữ, chia sẻ và khai thác từng nguồn theo phạm vi sử dụng. **NOT VERIFIED**.

**VAL-013 TEST PLAN v0.2:** `docs/VAL_013_LIBRARY_NO_CODE_TEST_PLAN_V0.2.md` thay thế bản nháp V0.1 về mục tiêu và phép đo (bản cũ giữ lịch sử). So sánh (A) luồng tài liệu rời rạc hiện tại với (B) một **mô phỏng thủ công/Wizard-of-Oz** nơi người hỗ trợ đưa đúng câu, bật đúng audio, ghi đáp án và cung cấp kết quả trong một luồng, không cần app/copy đề lên dịch vụ khác. Nếu không có người hỗ trợ, có thể dùng ví dụ luyện đề hợp pháp đang công khai để *đối chiếu quy trình thao tác*, nhưng **không** so thời gian làm câu hay khả năng nghe hiểu giữa hai kho đề khác nhau như thí nghiệm tương đương.

**Primary measurements:** thời gian vào câu đầu (`T_start`), thời gian tìm/bật audio đúng câu (`T_audio`), số lần chuyển tab/tài liệu (`N_switch`), thời gian từ trả lời đến xem kết quả/giải thích (`T_feedback`), hoàn thành phiên, lỗi đối chiếu, độ thuận tiện 1–5, mong muốn dùng lại; **ghi riêng chi phí chuẩn bị thủ công của người hỗ trợ**. Tách Listening và Reading khi đọc kết quả. Tất cả ngưỡng chỉ là đề xuất, **chưa được owner phê duyệt**.

**Không được kết luận từ dữ liệu hiện tại:** tự động nhập tài liệu thành công, có quyền dùng thương mại, audio mapping chính xác, AI giải thích đúng, MVP phải có chức năng nào, hoặc điểm TOEIC tăng.

**VAL-014 — NEXT VALIDATION QUESTION:** Trong lần thử đầu tiên nên mô phỏng **Listening (PDF + audio + chọn đáp án)** hay **Reading (câu hỏi + chọn đáp án + lời giải)**? Hỏi người dùng **một câu trọng tâm** để chọn tình huống đo trước; không hỏi lại về giá đối thủ hoặc việc tải tài liệu lúc này.

**Gate:** Product Vision V1.0 APPROVED; Stage 02 IN PROGRESS / HOLD; **NO MVP, PRD/SRS, UX/UI, ARCHITECTURE OR CODE**.


## 8. Market Validation 14 — 2026-11-20 (current)

**Owner decision VAL-D014 — APPROVED VALIDATION SCOPE (NOT PRODUCT SCOPE):** Chọn **C — cả Listening và Reading, thử nghiệm TÁCH RIÊNG**. Hai nhánh:

- **VAL-013L / H-003-VALUE-L — Listening:** cách A = người học tự điều phối PDF/sách + audio + chọn/ghi đáp án + dò; cách B = người hỗ trợ điều phối cùng quy trình bằng tài liệu hợp lệ, KHÔNG code. Đo `T_start`, `T_audio_locate` (không tính thời lượng nghe), `N_switch`, `T_feedback`, sai ghép audio/câu, hoàn tất, tiện lợi, ý định dùng lại, thời gian chuẩn bị.
- **VAL-013R / H-003-VALUE-R — Reading:** A = tự mở PDF/sách, chọn/ghi đáp án, dò; B = người hỗ trợ điều phối thủ công. Đo tương tự, trừ `T_audio_locate = N/A`; bổ sung thời gian tìm câu/đáp án.

**Quy tắc so sánh:** chỉ so A vs B **trong cùng kỹ năng và cùng Part**, với câu *chưa làm* khác nhau nhưng gần tương đương; có thể đổi thứ tự giữa người tham gia. Không so điểm L với R, không tổng hợp thời gian hoặc độ chính xác hai Part thành một kết luận. Ghi số thao tác, thời gian và mức tiện thực tế của từng phiên; ghi tách chi phí chuẩn bị/điều phối B và khả năng sai khác độ khó.

**Proposed example, not locked:** Listening Part 3 mỗi điều kiện 1 đoạn hội thoại / 3 câu, nếu có audio được ghép đúng; Reading Part 5 khoảng 5 câu/điều kiện. Có thể thay nếu tài liệu hiện có không phù hợp; không đoán audio hoặc tạo đáp án mới.

**Evidence status:** Đây là lựa chọn của Product Owner về cách kiểm chứng; chưa có hành vi quan sát, số liệu, phép thử, kết quả lợi ích hoặc feasibility tự động nhập file. `H-003-VALUE-L` và `H-003-VALUE-R`: **NOT TESTED / INCONCLUSIVE**. `H-003-INGEST`: **DEFERRED** bởi VAL-003. `H-003-RIGHTS`: **UNKNOWN**.

**Artifacts:** `docs/VAL_013_LIBRARY_NO_CODE_TEST_PLAN_V0.3.md` (active); `docs/VAL_014_TWO_TRACK_TEST_LOG_V0.1.md` (blank capture sheet). `VAL_013_LIBRARY_NO_CODE_TEST_PLAN_V0.2.md` retained as history.

**NEXT — VAL-015:** Khảo sát **điều kiện thực hiện thử nghiệm**, cụ thể có người hỗ trợ điều phối độc lập (người đọc câu, phát đúng audio và dò đáp án) hay không. Nếu không, điều chỉnh phương án mô phỏng minh bạch, không giả định Wizard-of-Oz đã diễn ra. Chỉ hỏi một câu này, không yêu cầu upload PDF/audio.

**Stage Gate unchanged:** Product Vision V1.0 **APPROVED**. Stage 02 **IN PROGRESS — HOLD**. VAL-010 price comparison **DEFERRED BY PRODUCT OWNER**. Chưa thông qua PRD/SRS/MVP, UX/UI, kiến trúc hoặc lập trình.


## 9. Market Validation 15 — 2026-11-20 (CURRENT OVERRIDES V0.3 FACILITATOR ASSUMPTION)

**VAL-D015 — SOLO TEST CONSTRAINT CONFIRMED:** Product Owner chọn **B: không có người hỗ trợ, tự thực hiện một mình**. Vì thế *không thực hiện* điều kiện B Wizard-of-Oz trong `VAL_013_LIBRARY_NO_CODE_TEST_PLAN_V0.3.md`; bản V0.3 giữ lịch sử, **không còn là active test protocol**. Chuyển active protocol sang `docs/VAL_013_LIBRARY_NO_CODE_TEST_PLAN_V0.4.md` và phiếu `docs/VAL_015_SOLO_TEST_LOG_V0.1.md`.

**Trình tự 2 nhánh tách biệt, không cần code hoặc upload:**
- **VAL-013L — Listening:** đo thực tế một lượt làm từ PDF/audio/đáp án riêng của người học, ưu tiên Part 3 khi có tài liệu hợp lệ khớp nguồn; ghi thời gian vào bài, tìm audio, đổi tab/nguồn, lỗi ghép, tìm lời giải, mức tiện.
- **VAL-013R — Reading:** đo một lượt làm từ PDF/sách/đáp án, gợi ý Part 5; ghi vào bài, đổi nguồn, dò lời giải, mức tiện. Không đo tìm audio.
- **Benchmark tham chiếu định tính (optional, tách khỏi baseline):** trên website luyện đề đang có chức năng tích hợp mà người học được phép truy cập, mô tả luồng học và thao tác yêu/không thích. Khác nguồn/nội dung/thiết bị/độ khó nên **không** tính % hiệu quả, thời gian tiết kiệm hay kết quả TOEIC của sản phẩm dự kiến. Không có website sẵn thì ghi `NOT AVAILABLE`, vẫn chạy baseline được.

**Evidence and boundaries:** Đây là lựa chọn phương pháp và điều kiện của Product Owner. `H-003-VALUE-L/R` vẫn **INCONCLUSIVE / NOT RUN**; `H-003-INGEST` **DEFERRED** theo VAL-003; `H-003-RIGHTS` **UNVERIFIED**. Không phê duyệt sản phẩm, design/UI, stack, MVP, code hoặc quyền nội dung. Nếu người dùng tự đo thời gian, phân biệt timestamp quan sát được với ước lượng. Không bắt buộc quay màn hình; nếu quay thì chỉ lưu cục bộ và tự kiểm tra thông tin nhạy cảm.

**NEXT — VAL-016 (one question):** Các bất tiện mở PDF/audio/chọn đáp án/dò kết quả hiện xảy ra chủ yếu **trên điện thoại Android, máy tính hay cả hai**? Dùng câu trả lời xác định môi trường baseline; không mặc định cảm nhận từ desktop đã chứng minh Android app giải quyết vấn đề.

**Gate unchanged:** Product Vision V1.0 APPROVED; Stage 02 IN PROGRESS/HOLD; VAL-003 và VAL-010 giữ DEFERRED; **NO MVP, PRD/SRS, UX/UI, architecture or code approvals**.


---

## VAL-016 UPDATE (2026-11-20) — DESKTOP/LAPTOP IS THE BASELINE ENVIRONMENT

**Owner answer:** “B. Chủ yếu máy tính/laptop” khi làm TOEIC từ PDF/sách/audio. Đây là mô tả nơi khó khăn diễn ra, không phải một phiên học hay kết quả benchmark đã được thực hiện.

**Impact on VAL-013 protocol:**
- **Active protocol V0.5** replaces V0.4 for execution; V0.4 retained as history. Keep **two independent tracks**: VAL-013L (Listening) and VAL-013R (Reading).
- **Solo baseline on PC/laptop:** chọn nguồn PDF/sách/audio có quyền dùng, thao tác đúng như thường ngày và đo `T_start`, `N_switch`, `T_feedback`, `Completion`, `N_source_errors`, `Ease_1_5`; đo thêm `T_audio_locate` only Listening, không tính thời lượng playback. Ghi ứng dụng/loại nguồn đang mở (trình duyệt, trình đọc PDF, ứng dụng audio, tài liệu giấy) và cách ghi đáp án chỉ để tái lập bối cảnh, không để chốt UI.
- **Benchmark optional:** nếu có quyền truy cập web luyện đề hiện có, nên quan sát trên cùng laptop/PC để bớt nhiễu bởi thiết bị; chỉ đối chiếu **định tính** sự liền mạch/thao tác. Nếu khác đề, độ khó, nền tảng hoặc Part, không kết luận A/B tương đương, không tính % giảm thời gian/điểm hay hiệu quả ứng dụng tương lai.
- **Android is a target product platform, NOT the baseline device.** Một điểm rủi ro chưa đóng: người học hiện ưu tiên PC trong luyện đề, trong khi pilot nhắm Android-only. Không suy ra họ muốn chuyển full mock sang Android, hoặc Android sẽ giải quyết pain point desktop. Cần xác minh use case trên mobile.
- **Evidence:** `VAL-016 = RECORDED / DEVICE CONTEXT CONFIRMED`; `VAL-013L/R = NOT RUN`; `H-003-VALUE-L/R = INCONCLUSIVE`; `H-003-INGEST = DEFERRED (VAL-003)`; `H-003-RIGHTS = UNKNOWN`.

**NEXT — VAL-017 (one question):** Khi có app **Android**, người học muốn app **thay máy tính cho các phiên luyện đề dài**, **chủ yếu dùng cho học nhanh khi rảnh**, hay **cả hai**? Câu hỏi về **bối cảnh/kỳ vọng trải nghiệm**, chưa chốt MVP hay UI.

**Stage gates unchanged:** Product Vision V1.0 APPROVED; Stage 02 Market Research & Validation IN PROGRESS/HOLD; VAL-010 price DEFERRED BY OWNER; **NO MVP/PRD/SRS/UX/UI/ARCHITECTURE/CODE**.

---

## VAL-017 UPDATE (2026-11-21) — ANDROID REPLACES PC FOR FULL TOEIC PRACTICE

### Ghi nhận & chứng cứ
- **VAL-D017 — USER EXPERIENCE INTENT RECORDED:** Product Owner chọn **A: ứng dụng Android cần thay thế máy tính/laptop để luyện đề Listening & Reading đầy đủ**. Không diễn giải câu trả lời thành “chỉ học nhanh trên điện thoại”; microlearning vẫn là giá trị bổ trợ trong Product Vision.
- **VAL-016 remains factual context:** Người #1 **hiện chủ yếu luyện bằng PDF/audio trên PC**, việc chuyển sang điện thoại là **kỳ vọng tương lai**, chưa quan sát phiên luyện đề tương đương trên mobile.
- **Product Vision impact:** Android phone-only pilot phù hợp mục tiêu đã được duyệt; ưu tiên kiểm chứng trải nghiệm phiên luyện dài và đầy đủ. **Không chỉnh sửa Product Vision V1.0 đã APPROVED theo kiểu âm thầm**; ghi nhận một điều kiện/rủi ro mới và đưa vào Change Review nếu kết quả buộc thay đổi mục tiêu/nền tảng. PD-012 về Full Mock như thước đo tiến bộ giữ nguyên; chưa xác nhận người học muốn làm **120 phút liên tục** trên điện thoại trong giai đoạn đầu.
- **No feature/MVP sign-off:** Không tự đưa timer, audio player, exam engine, tự động import PDF, đồng bộ PC, support tablet hoặc hỗ trợ offline vào MVP/PRD/SRS.

### Rủi ro & phạm vi desk research
| Risk ID | Rủi ro cần kiểm chứng | Bằng chứng/gợi ý kiểm chứng | Tình trạng |
|---|---|---|---|
| R-P01 | Văn bản Part 6/7, hình và nhiều đoạn đọc khó theo dõi trên màn hình nhỏ | Thử đọc các Part trên điện thoại thật, ghi cảm nhận và lỗi cuộn/chọn | OPEN |
| R-P02 | Nghe audio đồng thời theo dõi câu hỏi và lựa chọn trong Listening dễ mất tập trung | Thử một bài Part 3/4 trên phone, ghi lỗi chọn câu, thao tác | OPEN |
| R-P03 | Phiên dài làm người học mỏi mắt/tay, pin tiêu hao, bị gọi/nhắn tin, gián đoạn mạng, mất tiến độ | Đánh giá phiên ngắn trước, rồi phiên dài nếu người dùng tự nguyện; ghi số lần gián đoạn, mệt, mong muốn tiếp tục; không tạo yêu cầu kỹ thuật | OPEN |
| R-P04 | Tư liệu PDF/audio cá nhân không tự chuyển thành bài trắc nghiệm native được | Chờ kiểm định file mẫu VAL-003; rà soát map audio/câu/đáp án và quyền sử dụng | DEFERRED |
| R-P05 | Ứng dụng “luyện đề tích hợp trên điện thoại” đã có trên thị trường; lợi thế khác biệt chưa rõ | Benchmark sản phẩm có full mock trên Android, kết hợp giả thuyết thư viện cá nhân/cá nhân hóa | OPEN |
| R-P06 | So baseline desktop bằng tài liệu cá nhân với app Android dùng đề khác tạo nhiễu | Giữ hai tập dữ liệu riêng, chỉ benchmark định tính, không tự tính % cải thiện hoặc kết luận tăng điểm | MITIGATION RECORDED |

**Nguồn tham khảo công khai, chưa thử nghiệm người dùng:**
- ETS TOEIC L&R gồm **200 câu trong 120 phút**: Listening 100 câu/45 phút, Reading 100 câu/75 phút: https://www.ets.org/toeic/about/listening-reading.html ; https://www.iibc-global.org/english/toeic/test/lr/about/format.html
- Android Developers: bảo toàn trạng thái khi có đổi cấu hình/đóng ứng dụng và vòng đời Activity: https://developer.android.com/guide/components/activities/activity-lifecycle.html
- Android Developers: nút chạm được khuyến nghị tối thiểu 48dp, văn bản cần dễ đọc: https://developer.android.com/guide/topics/ui/accessibility/apps
- Ví dụ thị trường (listing, không phải hands-on): https://play.google.com/store/apps/details?id=org.iibc.global.toeic.officialapp công bố chế độ thực hành 200 câu; https://play.google.com/store/apps/details?id=com.englishtest công bố full test 200 câu/120 phút. Không đồng nghĩa mọi trải nghiệm mobile đã được chứng minh tốt.

### Định hướng validation tiếp theo (không code)
- **Active PC baseline không đổi:** `VAL_013_LIBRARY_NO_CODE_TEST_PLAN_V0.5.md` và `VAL_016_DESKTOP_SOLO_TEST_LOG_V0.2.md`, hai nhánh Listening/Reading, SOLO, NOT RUN.
- **Mobile-fit study tách biệt:** `VAL_017_ANDROID_LONGFORM_FIT_NO_CODE_PLAN_V0.1.md`; dùng app luyện TOEIC sẵn có/hợp pháp trên Android để đánh giá khả năng làm đề dài theo cảm nhận, không tạo giao diện hay code. **NOT RUN**. Không đòi hỏi file PDF cá nhân hoặc website cùng kho đề.
- **NEXT VAL-018 — one question:** Khi bạn nói “luyện đề đầy đủ trên Android”, bạn muốn **có thể làm một full mock TOEIC liên tục khoảng 120 phút**, hay **hoàn thành tất cả Part theo nhiều phiên ngắn có thể tiếp tục** (hoặc cả hai)? Chưa dùng câu trả lời này như kết quả test.
- **H-PLATFORM-01:** INCONCLUSIVE / MOBILE-FIT NOT RUN. **H-003-VALUE-L/R:** INCONCLUSIVE, PC BASELINE NOT RUN. **H-003-INGEST:** DEFERRED (VAL-003). **VAL-010:** DEFERRED BY PRODUCT OWNER.
- **Stage gates unchanged:** Product Vision V1.0 APPROVED; Phase 02 IN PROGRESS/HOLD. **No MVP, PRD/SRS, UX/UI, architecture or app code authorized.**


---

## VAL-018 UPDATE — 2026-11-21 — DUAL PRACTICE MODES ON ANDROID (CURRENT)

### 1. Owner answer and evidence classification
- **VAL-D018 (RECORDED EXPERIENCE INTENT):** Product Owner chọn **C — cả hai**: (i) **Part Practice**: luyện đủ cả 7 Part TOEIC Listening & Reading linh hoạt theo các phiên; (ii) **Full Mock Test**: làm một bài TOEIC Listening & Reading **liên tục ~120 phút** khi muốn tự đánh giá.
- Điều này **làm rõ** VAL-017 (mong Android thay PC), không hủy VAL-016 (hiện việc luyện đề bằng PDF/audio chủ yếu trên PC/laptop). Hai loại phiên phục vụ hai mục tiêu khác nhau; **không** chốt số câu mỗi phiên Part, tính năng tạm dừng/tiếp tục, cách tính điểm hay phạm vi MVP.
- **Mức chứng cứ:** Direct, self-reported **preference/intended behavior** from người học #1; **NOT OBSERVED** actual extended mobile learning, full mock completion, ease of use, score validity, feature availability or importer feasibility.

### 2. Product Vision impact
- **Product Vision V1.0 remains APPROVED AND UNCHANGED.** Pilot chỉ Android phone; cá nhân hóa, học khi rảnh, full mock theo dõi tiến bộ vẫn phù hợp. Không tạo Product Vision V1.1, không mặc định tất cả giá trị vision phải thuộc MVP.
- **Learning modes NOT MVP commitments:** (M1) luyện từng Part và có thể sắp xếp buổi học ngắn; (M2) full timed 120-minute mock; Instant Microlearning là nhu cầu song song, tách khỏi hai phép thử.
- Đề luyện Part **không có giá trị điểm thi tổng tương đương Full Mock**. Điểm Full Mock chỉ dùng theo dõi khi bộ đề có chất lượng, độ khó, cách chấm tương đương được thẩm định; không trình bày là điểm TOEIC chính thức.
- ETS TOEIC Listening & Reading linear test: **200 questions, 120 minutes** (Listening 100 / 45 minutes; Reading 100 / 75 minutes). Official source: https://www.ets.org/toeic/about/listening-reading.html .

### 3. Revised hypothesis and experiment matrix
| ID | Hypothesis / question | Method (no-code) | Status |
|---|---|---|---|
| H-PLATFORM-01M | Có thể luyện Listening & Reading theo các phiên Part ngắn trên Android mà vẫn đủ dễ đọc, dễ nghe, ít mỏi | Solo walkthrough trên app Android hợp pháp, một bài L (Part 3/4), một bài R dài (Part 6/7); nếu đủ nguồn thì khảo sát các Part còn lại sau | INCONCLUSIVE / NOT RUN |
| H-PLATFORM-01F | Có thể và muốn hoàn thành full mock 200 câu/120 phút liên tục trên phone | Kiểm tra app có bài tương đương; thử ngắn phát hiện blocker trước; sau đó FULL MOCK 120 phút **chỉ nếu tự nguyện, đủ nguồn, phù hợp thời gian** | INCONCLUSIVE / NOT RUN |
| H-PLATFORM-01S | Gián đoạn Android không dẫn đến mất câu trả lời/tiến độ hoặc khiến mock không đáng tin | Chỉ ghi nhận interruptions phát sinh tự nhiên; không buộc tạo lỗi hay can thiệp trước khi có kế hoạch kiểm thử kỹ thuật | INCONCLUSIVE |
| H-003-VALUE-L/R | Quy trình luyện đề tích hợp giảm ma sát so với PDF/audio phân mảnh trên PC | VAL-013L/R PC baseline solo và benchmark định tính, tách riêng khỏi study Android | INCONCLUSIVE / NOT RUN |
| H-003-INGEST / H-003-RIGHTS | Tài liệu cá nhân nhập chính xác, dùng hợp pháp | Chờ sample và kiểm tra quyền riêng | DEFERRED / UNKNOWN |

### 4. Updated no-code study / measurement
- **Active plan:** `docs/VAL_017_ANDROID_LONGFORM_FIT_NO_CODE_PLAN_V0.2.md` (supersedes V0.1; retain V0.1 as history). Recording sheet `docs/VAL_018_ANDROID_DUAL_MODE_TEST_LOG_V0.1.md` (blank; no fabricated results).
- **M1 short Part study:** Thử độc lập Listening Part 3 hoặc 4 và Reading Part 6 hoặc 7 trên Android, ghi số câu, thời gian phiên, time-to-first-question, navigation friction, audio/reading ease 1–5, difficulty, disruptions, fatigue, completion and willingness to reuse; mở rộng thêm Part khác khi thực tế có nội dung hợp pháp, KHÔNG yêu cầu xong cả 7 Part trước khi ghi nhận bước đầu.
- **M2 continuous full mock:** Kiểm tra nguồn app/mock hợp lệ có cấu trúc 200 câu/120 phút. Thử dùng app ngắn 20–30 phút để nhận diện blockers **không tính là full mock**. Nếu và chỉ nếu sẵn sàng và có nguồn phù hợp, tự nguyện làm full mock liên tục; ghi completion, elapsed time, interruptions, fatigue, text/audio difficulty, loss of progress, desire to retry. Không bắt người dùng làm 120 phút ngay hoặc nếu chưa có nguồn.
- **Control boundaries:** Tách dữ liệu M1/M2, Listening/Reading, Android/PC; không tính % cải thiện giữa đề và thiết bị khác, không suy ra score uplift. Nội dung không được copy/distribute nếu thiếu quyền. Ghi `NOT RUN`, `NOT AVAILABLE`, `ESTIMATED` khi đúng thực tế.
- **Acceptance thresholds:** chưa được Product Owner phê duyệt; trải nghiệm này chỉ là một phần bộ bằng chứng Stage 02.

### 5. Risks and open questions
- **R-P01:** Đọc Part 6/7 và đa đoạn trên điện thoại; **R-P02:** phối hợp audio/câu hỏi trong Part 3/4; **R-P03:** mỏi mắt/tay và áp lực 120 phút; **R-P07:** ngắt quãng/sập app/khóa màn hình, phiên luyện Part có thể linh hoạt nhưng mock cần tính nhất quán; **R-P08:** các sản phẩm đối thủ có thể quảng bá “full test” nhưng không bảo đảm nội dung/scoring tương đương.
- **Open:** Thời gian người dùng đã từng học dài trên Android là bao nhiêu? Có đủ app/đề hợp pháp để tự test? Chấp nhận tạm dừng/resume cho Part, còn full mock có quy tắc gián đoạn như thế nào? Không đóng các câu này bằng suy luận.

### 6. Next question and gate
- **NEXT VAL-019 (one question):** Người học #1 **đã từng thực sự làm một phiên luyện TOEIC >=30 phút trên điện thoại Android chưa**? Nếu đã có, ghi kinh nghiệm thuận tiện/khó khăn; nếu chưa, không coi mong muốn như hành vi chứng thực. Mục đích: quyết định có thử bước cơ bản trước hay lên thử mock, không lựa chọn UI/stack.
- **Stage:** Product Vision V1.0 APPROVED; Stage 02 Market Research & Validation IN PROGRESS / HOLD, waiting for actual evidence and explicit owner sign-off. VAL-003 sample **DEFERRED**; VAL-010 price **DEFERRED BY OWNER**. **NO MVP, PRD, SRS, UI, ARCHITECTURE, CODE APPROVAL**.

---

## VAL-019 UPDATE — 2026-11-21 (CURRENT) — ANDROID >=30-MIN PRIOR EXPERIENCE

**Owner's exact answer:** A — "Đã từng, và thấy khá thuận tiện" đối với câu hỏi "đã từng học hoặc làm TOEIC liên tục từ 30 phút trở lên trên điện thoại Android chưa?"

### Evidence ladder

- **CONFIRMED SELF-REPORT:** Người học #1 đã có trải nghiệm TOEIC >=30 phút liên tục trên Android và cảm nhận **khá thuận tiện**. Không phải suy đoán thuần túy về mobile; đây là kinh nghiệm trước đó do người dùng thuật lại.
- **UNKNOWN:** App nào, Part Listening/Reading nào, thời lượng chính xác, kích thước điện thoại, có thực sự hoàn thành bài/không, bất tiện còn lại, tỷ lệ duy trì theo tuần, có phải thi 200 câu/120 phút hay không.
- **NOT VALIDATED:** `H-PLATFORM-01M` ở mức toàn bộ 7 Part; `H-PLATFORM-01F` continuous Full Mock 200q/120m; việc Android thay PC cho kho PDF/audio cá nhân; việc tự động nhập và ghép audio; khả năng chấm điểm và bản quyền nội dung.
- **Structured experiments remain NOT RUN:** Trải nghiệm trước đây không thay thế được log `VAL-013L/R` trên PC hoặc hai nhánh Android M1/M2 của kế hoạch VAL-017; không tự tạo giá trị định lượng hay kết quả thử nghiệm.

### Practical revision for no-code plan

1. **Không bắt buộc thử lại phiên 20–30 phút chỉ để chứng minh đã từng dùng điện thoại lâu hơn 30 phút**. Có thể ghi nhận trải nghiệm hồi cứu là qualitative evidence và bổ sung chi tiết về sau.
2. Với **M1**, vẫn cần quan sát riêng ít nhất một mẫu Listening audio + answer và một mẫu Reading đoạn dài; không đồng nghĩa một phiên trước đại diện đủ 7 Part.
3. Với **M2**, ưu tiên xác minh có từng **hoàn thành** Full Mock liên tục 200 câu/~120 phút trên điện thoại không, trước khi quyết định có cần chạy thử mới; không bắt người dùng làm 120 phút lúc này.
4. Tách nhánh PC (ma sát xử lý file cá nhân) khỏi nhánh Android (khả dụng luyện Part/mock); không so sánh % cải thiện khác nguồn.

**Hypothesis statuses:** `H-PLATFORM-01M = QUALITATIVE SUPPORT FROM PRIOR EXPERIENCE / STILL INCONCLUSIVE` ; `H-PLATFORM-01F = INCONCLUSIVE / NO VERIFIED 120-MIN TEST` ; `H-003-VALUE-L/R = INCONCLUSIVE / NOT RUN`.

**Latest no-code plan:** `docs/VAL_017_ANDROID_LONGFORM_FIT_NO_CODE_PLAN_V0.3.md` ; recording sheet: `docs/VAL_018_ANDROID_DUAL_MODE_TEST_LOG_V0.1.md` remains blank because no new monitored test occurred.

**NEXT — VAL-020 (ONE QUESTION):** Bạn đã **từng hoàn thành trọn vẹn một Full Mock TOEIC 200 câu, khoảng 120 phút liên tục, trên điện thoại Android** chưa? A. Có, hoàn thành; B. Đã thử nhưng chưa hoàn thành; C. Chưa từng. Chỉ lựa chọn này; chưa thêm câu hỏi về app hoặc lý do, chưa yêu cầu chạy thử ngay.

**Unchanged gates:** Product Vision V1.0 APPROVED; Stage 02 IN PROGRESS/HOLD; Stage 03 NOT STARTED; VAL-003 và VAL-010 DEFERRED. NO MVP/PRD/SRS/UX/UI/ARCHITECTURE/CODE approvals.


---

## VAL-020 UPDATE — 2026-11-21 (CURRENT) — REPORTED FULL MOCK COMPLETION ON ANDROID

### Confirmed report and boundaries
- **Direct Product Owner response:** Chọn **A — Có, đã hoàn thành ít nhất một bài Full Mock TOEIC 200 câu/khoảng 120 phút liên tục trên điện thoại Android**. Đây là **bằng chứng hồi tưởng từ người dùng trực tiếp**, không còn chỉ là ý định (VAL-017) hoặc phiên >=30 phút (VAL-019).
- **What this supports:** Có ít nhất một trải nghiệm cá nhân mà người học #1 hoàn thành một bài Full Mock dài trên Android. Do đó giả thuyết *không thể làm bài dài trên điện thoại* kém phù hợp với người này; có cơ sở giảm ưu tiên kiểm chứng khả năng hoàn thành tối thiểu.
- **What remains unknown:** Tên app, chất lượng và tính hợp pháp của đề, số câu/thời gian thực đo, đã sử dụng cả audio L/R đúng cấu trúc chưa, mỏi mắt/tay, độ dễ đọc Part 7, số lần gián đoạn và tác động, có mất dữ liệu hoặc phải làm lại không, mong muốn tiếp tục dùng Android để làm full mock, độ tin cậy điểm số. **Không tự điền kết quả, thời lượng chính xác, điểm thi hoặc tình trạng ít gây phiền.**
- **Protocol vs recollection:** `VAL-017 M2` **STRUCTURED NO-CODE TEST NOT RUN**. Trải nghiệm quá khứ đã được ghi nhận là `RETROSPECTIVE SELF-REPORT`, không điền như log thử nghiệm có giám sát. `M1` Part Practice vẫn `NOT RUN`; `VAL-013L/R` baseline PC solo vẫn `NOT RUN`; `H-003-INGEST` DEFERRED; `H-003-RIGHTS` UNKNOWN.

### Hypothesis update
| Hypothesis | Revised evidence level | Status |
|---|---|---|
| H-PLATFORM-01F — Hoàn thành full mock liên tục trên Android | Có báo cáo thực tế đã hoàn thành ít nhất một lần | **SUPPORTED FOR ONE PARTICIPANT'S COMPLETION / OVERALL FIT STILL INCONCLUSIVE** |
| H-PLATFORM-01M — Part Practice linh hoạt trên Android | VAL-019 là tín hiệu dùng Android >=30 phút, VAL-020 không cung cấp dữ liệu cụ thể theo Part | **INCONCLUSIVE / STRUCTURED M1 NOT RUN** |
| H-PLATFORM-01S — Gián đoạn và lưu tiến độ | Chưa có thông tin về lỗi/interruption | **INCONCLUSIVE** |
| H-003-VALUE-L/R — Thư viện cá nhân cải thiện ma sát PC | VAL-020 liên quan app Android, không đo PDF/audio cá nhân | **INCONCLUSIVE / PC BASELINES NOT RUN** |

### Updated no-code validation plan and next action
- **Active protocol:** `docs/VAL_017_ANDROID_LONGFORM_FIT_NO_CODE_PLAN_V0.4.md` kế thừa V0.3; không bắt người học lặp lại Full Mock hai giờ chỉ để chứng minh “có thể hoàn thành”. Trước tiên thu thập **chất lượng trải nghiệm sau khi hoàn thành** qua một câu hỏi trọng tâm; có thể ghi lại thêm bằng chứng hoặc chạy structured test *nếu sau đó còn bất định ảnh hưởng đến quyết định*.
- **M1** cần kiểm chứng riêng cách đọc Reading dài và làm Listening trên điện thoại; không coi đã full mock là đủ để xác định toàn bộ 7 Part đều tiện.
- **M2** cần hiểu các bất tiện, gián đoạn và khả năng dùng lại, không tự nhận điểm của mock tương đương TOEIC thật.
- **NEXT VAL-021 (one question):** Trong lần đã hoàn thành Full Mock TOEIC trên Android, **điều gì bất tiện nhất**: (A) đọc/cuộn đề dài, (B) nghe audio/chọn đáp án, (C) mỏi mắt/tay hoặc pin/nóng máy, (D) cuộc gọi/thông báo/gián đoạn, (E) không gặp bất tiện đáng kể, (F) khác? Đây là một câu hỏi nhằm ưu tiên kiểm chứng rủi ro còn lại, không phải thiết kế UI.
- **Gates unchanged:** Product Vision V1.0 APPROVED; Stage 02 IN PROGRESS/HOLD; Stage 03 NOT STARTED; VAL-003 và VAL-010 DEFERRED; **NO MVP/PRD/SRS/UX/UI/ARCHITECTURE/CODE approved**.


---

## VAL-021 UPDATE — 2026-11-21 (CURRENT) — READING LONG-FORM AND COMFORT/DEVICE FRICTION

### What the participant actually reported
- Product Owner answered **"A c"** to a multiple-choice question and is interpreted as **two choices, A and C** (not just one most important issue). No evidence of a rank between them.
- **A (direct pain):** long Reading passages, scrolling, and tracking questions on a phone screen are inconvenient.
- **C (composite category):** a discomfort/device issue exists in **at least one** of eye fatigue, hand fatigue, device heat, battery drain. Do not infer all four, the degree of severity, or that the device overheated or shut down.
- **Unknown:** exact issue(s) within C, ease rating, whether this caused pauses, app name, phone model, data loss, battery percentage, reuse intention, performance or exam-score validity.

### Hypothesis/risk implications
| Hypothesis / risk | Evidence level after VAL-021 | Status |
|---|---|---|
| H-PLATFORM-01F — full mock on Android | Completion self-reported VAL-020; frictions A & C self-reported VAL-021 | **ONE-PARTICIPANT COMPLETION SUPPORTED; COMFORT/REPEATABILITY INCONCLUSIVE** |
| H-PLATFORM-01M — flexible Part use | Prior >=30-min session VAL-019, but VAL-021 does not prove all Parts | **INCONCLUSIVE / STRUCTURED M1 NOT RUN** |
| R-P01 — long Reading on phone | Direct reported inconvenience, without quantified metrics | **PAIN REPORTED; PRIORITY FOR TARGETED NO-CODE REVIEW** |
| R-P03 — fatigue/device during long mock | Composite choice C; type unknown | **CONCERN REPORTED; TYPE/SEVERITY UNKNOWN** |
| H-003-VALUE-L/R — personal PDF/audio integration | Not measured by third-party Android mock | **INCONCLUSIVE / PC BASELINES NOT RUN** |

### Revised no-code validation activity
- Active mobile plan `docs/VAL_017_ANDROID_LONGFORM_FIT_NO_CODE_PLAN_V0.5.md` supersedes V0.4; history retained.
- Do **not** require another two-hour mock merely to confirm that the participant finished one. First clarify C and document the Reading difficulty in retrospection. An **optional** short lawful Android Reading Part 7 observation later can capture navigation burden and ease, recorded as a **new** session only if performed.
- Keep separate: self-report versus structured test, PC baseline versus Android mobile fit, Part practice versus continuous full mock, user experience versus automatic PDF/audio import.
- **Next one question (VAL-022):** In choice C, which issue(s) did you actually experience: **eye fatigue, hand fatigue, phone heat, battery drain**? Multiple selection permitted; do not silently combine them.

**Stage gates unchanged:** Product Vision V1.0 APPROVED; Phase 02 IN PROGRESS/HOLD; Phase 03 NOT STARTED; VAL-003 & VAL-010 DEFERRED; no MVP, PRD/SRS, UX/UI, architecture or code authorization.

---

## VAL-022 — GHI NHẬN VÀ PIVOT VỀ THƯ VIỆN ĐỀ CÁ NHÂN (2026-11-21)

### Bằng chứng / giả thuyết
- **Observed retrospectively:** Người học #1 báo cáo mỏi mắt sau khi nhìn màn hình điện thoại lâu khi thực hiện Full Mock; Reading dài và cuộn nhiều gây bất tiện (VAL-021).
- **Không quan sát hay đo:** mức độ mỏi, ngưỡng phút, tác động điểm, các triệu chứng khác; người học #2 chưa được hỏi trực tiếp.
- **H-PLATFORM-01F:** hoàn thành một Full Mock trong quá khứ (VAL-020) ở mức self-report; **continuous 120-minute usability fit = INCONCLUSIVE**. Không lặp lại 120 phút chỉ để có thêm xác nhận.
- **H-003-VALUE-L/R:** ưu tiên số 1 trở lại: người dùng muốn audio–câu hỏi–chọn đáp án–xem lời giải trong một trải nghiệm liền mạch, ưu tiên tận dụng kho đề cá nhân. Có pain point định tính VAL-013 nhưng **baseline desktop solo cho L/R chưa chạy**.

### Phép thử hoạt động kế tiếp (NO CODE)
- Dùng tài liệu đang có trên laptop/PC để thực hiện **hai baseline tách biệt** (Listening Part 3 một đoạn/3 câu; Reading Part 5 năm câu) khi bộ đề khớp câu hỏi–đáp án và, riêng Listening, audio tương ứng; tự đo thời gian chuẩn bị, thời gian tìm đúng audio, số lần chuyển tab, thời gian dò đáp án, số lỗi và mức tiện 1–5.
- Không yêu cầu nộp nội dung đề, gửi link có bản quyền, xây prototype, dùng trợ lý điều phối hoặc đo A/B causal. Website luyện đề tích hợp có thể benchmark **định tính tùy chọn** cùng môi trường PC, không suy ra tỷ lệ cải thiện vì nội dung khác.
- **Readiness gate VAL-023:** xác nhận có bộ tài liệu phù hợp để đo L/R; câu hỏi chỉ về mức sẵn sàng của file **trên máy người dùng**, không lặp lại yêu cầu upload VAL-003 đã hoãn.
- Hoàn tất đo baseline chỉ xác nhận pain point đang xảy ra, **không** xác nhận tự động ingest, quyền sao chép/đăng tải, điểm mock hợp lệ hay tạo ra giá trị thị trường.

### Stage Gates
Product Vision V1.0 **APPROVED / UNCHANGED**; Stage 02 **IN PROGRESS / HOLD**; Stage 03 **NOT STARTED**; MVP, PRD, SRS, UI, architecture, coding **NOT APPROVED**. VAL-003 và VAL-010 vẫn **DEFERRED**.


---

## VAL-023 — TÀI LIỆU BASELINE ĐÃ SẴN SÀNG (2026-11-21)

### Phản hồi trực tiếp của Product Owner
- Chọn **A — Đủ cả Listening và Reading** khi hỏi laptop có sẵn bộ câu hỏi, đáp án và audio phù hợp để tự thực hiện hai nhánh hay không.
- **Classification:** Self-reported readiness; **không phải** kết quả xem/kiểm kê tài liệu, đo lường hành vi, xác minh giấy phép, hay kết quả tự động trích xuất.
- **Decision VAL-D023:** Mở cổng thực hiện baseline thủ công trên PC/laptop cho `VAL-013L` (Listening) và `VAL-013R` (Reading). Thực hiện riêng biệt, một người tự đo. Không cần tải PDF/audio lên, gửi ảnh, thiết kế UI, xây prototype hay viết code.

### Trạng thái thực nghiệm
| Thành phần | Trạng thái sau VAL-023 | Bằng chứng còn thiếu |
|---|---|---|
| `VAL-013L` Listening baseline | **READY TO RUN / NOT RUN** | Thời gian tìm audio, số lần chuyển tab, thời gian tìm đáp án, điểm thuận tiện, lỗi thao tác |
| `VAL-013R` Reading baseline | **READY TO RUN / NOT RUN** | Thời gian bắt đầu, số lần chuyển tab, thời gian tìm đáp án, điểm thuận tiện, lỗi thao tác |
| `H-003-VALUE-L/R` | **INCONCLUSIVE** | Quan sát ma sát baseline; đánh giá tích hợp cần phép kiểm chứng riêng, không được suy ra từ baseline đơn thuần |
| `H-003-INGEST` | **DEFERRED / NOT FEASIBILITY TESTED** | Tệp thực tế và kiểm nghiệm tự động trích xuất/ghép âm thanh sau khi người dùng sẵn sàng |
| `H-003-RIGHTS` | **UNKNOWN** | Quyền dùng nội bộ, chia sẻ, phát hành hoặc thương mại hóa theo từng nguồn |

### Bước thực hiện tiếp theo (không cần code)
1. Dùng chính bộ tài liệu sẵn có trên **laptop/PC**; chuẩn bị đồng hồ bấm giờ và phiếu `docs/VAL_023_DESKTOP_BASELINE_LOG_V0.3.md`. Chỉ xác nhận nguồn có các thành phần phù hợp; không mở trước chính xác vị trí câu hỏi/audio/đáp án để tránh làm sai lệch hành vi tìm kiếm tự nhiên.
2. Chạy `VAL-013L` Listening một đoạn Part 3, 3 câu (hoặc nhóm tương đương); ghi thời gian đến câu đầu tiên, thời gian tìm đúng audio **không tính độ dài nghe**, số lần chuyển tab/ứng dụng/tài liệu, thời gian tìm đáp án sau khi trả lời xong, số lỗi ghép, mức độ thuận tiện 1–5.
3. Chạy `VAL-013R` Reading năm câu Part 5, **tách phiên**, ghi các chỉ số tương ứng (không có audio).
4. Gửi **chỉ các số đo và cảm nhận**, không gửi đề/audio; nếu số liệu không chính xác, gắn nhãn `ước lượng`/`không đo`. Nếu không có phần giải thích, ghi `chỉ có đáp án` thay vì tự chế lời giải.
5. Sau khi nhận log, phân tích hai nhánh riêng, chỉ ra ma sát ưu tiên. Có thể benchmark trải nghiệm website hợp pháp **định tính** về sau nếu hữu ích, không suy ra % cải thiện từ đề/nguồn khác nhau.

### Giới hạn, Stage Gates
- **Baseline hiện chưa được thực hiện**. Readiness ≠ observed baseline ≠ xác thực giá trị giải pháp.
- Phase 02 vẫn HOLD; chưa phê duyệt Stage 03, MVP, PRD/SRS, UI, kiến trúc, code. Product Vision V1.0 giữ nguyên.
- `VAL-003` kiểm định file mẫu và `VAL-010` thăm dò giá tiếp tục tạm hoãn theo người dùng.


---

## VAL-024 — HAI PHIÊN BASELINE, MỘT LẦN BÁO CÁO (2026-11-21)

**Phản hồi Product Owner:** `C — Thực hiện cả hai rồi gửi kết quả cùng lúc`.

**Decision VAL-D024:**
- Chủ động thực hiện hai phiên **solo trên PC/laptop** theo cách học thường ngày, mỗi nhánh sử dụng bộ tài liệu có câu hỏi/đáp án tương ứng (Listening có audio phù hợp).
- **Không yêu cầu thứ tự cố định** giữa `VAL-013L` Listening (Part 3, 1 đoạn/3 câu) và `VAL-013R` Reading (Part 5, 5 câu). Có thể làm khác ngày; ghi ngày từng phiên, không suy ra cùng điều kiện nếu khác ngày.
- **Gửi kết quả cùng một lần** để phân tích sau; mỗi nhánh phải tách riêng các trường `T_start_s`, `N_switch`, `T_feedback_s`, `N_source_errors`, `Ease_1_5`, số câu hoàn thành, và riêng Listening có `T_audio_locate_s`. Đánh dấu MEASURED / ESTIMATED / UNAVAILABLE cho mỗi số.
- Không gửi PDF/audio, không yêu cầu facilitator, không cần prototype/code/UI; không đặt deadline.

**Status & evidence:**

| Mục | Trạng thái hiện tại | Điều kiện cập nhật sau |
|---|---|---|
| VAL-024 — thứ tự và cách gửi | **RECORDED / BATCH REPORT CHOSEN** | Không cần thêm quyết định |
| VAL-013L Listening | **READY TO RUN / NOT RUN** | Cần log thực tế hoặc báo cáo không thể thực hiện |
| VAL-013R Reading | **READY TO RUN / NOT RUN** | Cần log thực tế hoặc báo cáo không thể thực hiện |
| H-003-VALUE-L/R | **INCONCLUSIVE** | Baseline đo ma sát; muốn xác minh lợi ích giải pháp tích hợp cần bằng chứng riêng |
| VAL-003 / VAL-010 | **DEFERRED** | Chỉ mở lại theo kế hoạch sau |

**Active documents:** `docs/VAL_013_LIBRARY_NO_CODE_TEST_PLAN_V0.8.md`; `docs/VAL_024_DESKTOP_BASELINE_BATCH_LOG_V0.4.md`. Các bản V0.7 và V0.3 được giữ lịch sử.

**NEXT evidence gate (không phải câu hỏi mới):** Chờ Product Owner gửi **một báo cáo gồm kết quả cả hai nhánh** (hoặc đánh dấu chính xác nhánh chưa chạy). Khi có dữ liệu, đối chiếu ma sát theo từng kỹ năng, nhận diện yếu tố nào thật sự cần giải quyết trước; cân nhắc benchmark web tích hợp chỉ theo hướng định tính nếu thiết yếu. **Không khẳng định có cải thiện bao nhiêu % hoặc tính khả thi PDF/audio importer chỉ từ baseline.**

**Stage gates:** Vision V1.0 APPROVED/UNCHANGED. Stage 02 IN PROGRESS/HOLD. Stage 03 NOT STARTED. Chưa phê duyệt MVP, PRD/SRS, UX/UI, kiến trúc hay code.
