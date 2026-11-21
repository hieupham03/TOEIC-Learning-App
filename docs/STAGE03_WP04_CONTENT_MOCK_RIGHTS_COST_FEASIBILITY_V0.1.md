# Stage 03 — Gói kiểm tra khả thi nội dung, Full Mock, quyền và chi phí V0.1

**Trạng thái:** **DESK-RESEARCH + CHECK PLAN; FEASIBILITY NOT YET PROVED.** Ngày 2026-11-21.  
**Phạm vi:** B — Balanced Family Pilot (WP-02 direction approved conditionally).  
**Nguyên tắc:** không yêu cầu người dùng gửi file ngay; không tự khẳng định có giấy phép, quyền chia sẻ hay điểm tương đương ETS.

## 1. Kết luận nhanh / traffic lights
| Gate | Đã có bằng chứng | Thiếu bằng chứng | Mức độ |
|---|---|---|---|
| F-01: 7 Part | Cấu trúc và số câu được công bố chính thức | Nội dung có quyền và chất lượng ở từng Part | **AMBER** |
| F-02: Hai Full Mock | Mỗi form 200 câu, 45+75 phút; 2 form lý thuyết 400 câu | Chưa xác nhận 400 câu tách biệt, đáp án/audio, giấy phép và tính tương đương | **RED** cho cam kết MVP |
| F-03: Audio–question–answer integrity | Phương pháp QA có thể định nghĩa | Chưa có tài liệu mẫu hoặc kết quả QA | **RED** cho phát hành nội dung |
| F-04: Rights | ETS/Google Play công bố quy định | Chưa có rights inventory cho học liệu của PO | **RED** cho rehost/sharing |
| F-05: Pilot OPEX | Có mô hình ngân sách và tier no-cost từ nhà cung cấp tham khảo | Chưa chọn công nghệ, workload, giới hạn thanh toán hay giá nội dung | **AMBER** |
| F-06: Score meaning | ETS dùng equating; %correct khác điểm TOEIC | Không có nghiên cứu tương đương giữa các form của app | **RED** cho tuyên bố điểm tương đương |
| F-07: Android long-form | PO đã tự hoàn thành một mock Android | Đã báo khó cuộn Reading và mỏi mắt; chưa có nghiệm thu | **AMBER** |

Màu **RED/AMBER** không chặn việc *viết Requirements draft*, nhưng chặn việc **cam kết feature/copying/scoring/pilot** tương ứng cho đến khi vượt gate.

## 2. Chuẩn nội dung cho một bài Full Mock và hai bộ đề
Nguồn chính thức IIBC/ETS: 200 câu/120 phút, Listening 100 câu/45 phút, Reading 100 câu/75 phút.

| Part | Số câu/một form | Hai form tối thiểu | Phụ thuộc dữ liệu đặc thù |
|---|---:|---:|---|
| 1 — Photographs | 6 | 12 | Hình ảnh có quyền, audio, đúng lựa chọn |
| 2 — Question–Response | 25 | 50 | Audio, transcript nội bộ nếu hợp pháp, key |
| 3 — Conversations | 39 | 78 | 13 nhóm * 3 câu/form, audio và có thể hình/biểu |
| 4 — Talks | 30 | 60 | 10 nhóm * 3 câu/form, audio/biểu đồ nếu có |
| 5 — Incomplete Sentences | 30 | 60 | Câu, lựa chọn, key |
| 6 — Text Completion | 16 | 32 | 4 đoạn * 4 câu/form; giữ ngữ cảnh |
| 7 — Reading Comprehension | 54 | 108 | Ngữ liệu dài, nhiều đoạn, hình/bảng hợp lệ |
| **Tổng** | **200** | **400** | 200 Listening + 200 Reading cho 2 forms |

**400 là số câu mục tiêu về mặt cấu trúc, KHÔNG phải số câu đã có hoặc được cấp phép.** Chỉ coi hai form độc lập nếu không reuse câu giữa form A và B; cần ngân hàng luyện Part tách khỏi assessment để tránh học thuộc đề. Nếu tái sử dụng nội dung qua practice/mock, buộc đánh dấu nguy cơ contamination, không so sánh điểm tiến bộ như độc lập.

## 3. Audit nguồn: quy tắc kiểm tra bắt buộc
Mỗi tập nội dung phải có **SOURCE-ID**, tên chủ sở hữu, loại giấy phép/cơ sở quyền, vùng lãnh thổ, hạn/điều kiện, các quyền `private/local`, `upload-cloud`, `share-to-family`, `distribute-public`, `modify/translate`, `commercial`, `AI-third-party`, và bằng chứng bản quyền (hợp đồng, trang license, sự đồng ý bằng văn bản). Lưu ngày kiểm tra.

- **S-01 tự tạo gốc + audio tự sản xuất:** ứng viên ưu tiên; xác minh nội dung không sao chép và quyền voice/sounds/images nếu dùng tư liệu khác.
- **S-02 nguồn mua/được cấp phép:** chỉ dùng trong phạm vi giấy phép (cần văn bản nói rõ quyền số hóa/lưu máy chủ/chia sẻ nhóm và về sau public).
- **S-03 PDF/sách/audio PO đã mua/tải:** sở hữu bản sao **không tự động cấp quyền** số hóa, đưa lên cloud, trích xuất, phát tán cho người khác hoặc thương mại hóa; để `UNKNOWN` cho đến khi có bằng chứng.
- **S-04 tài liệu ETS/IIBC mẫu:** quy định bản quyền đặc thù. **Theo chính sách ETS, entire disclosed test form và single test questions không nằm trong danh mục cấp phép thông thường**; không coi các PDF đề ETS tải trên web là đầu vào hợp lệ cho app.
- **S-05 CC/public domain:** tra đúng giấy phép từng nguồn, điều kiện attribution/SA/NC/ND, tác phẩm phái sinh, tác giả âm thanh/hình ảnh; không suy rằng mọi nội dung miễn phí đều dùng thương mại được.
- **S-06 câu hỏi tạo bằng AI:** không mặc định nguyên gốc, đúng kiến thức hay được phép dùng mọi output; cần kiểm tra đạo văn, provenance, QA và điều khoản nhà cung cấp.
- **S-07 website crawler:** đọc ToS, robots và quyền; không suy `public page == redistributable`.

**Gating outcome:** `AUTHORIZED`/`RESTRICTED`/`UNKNOWN`/`REJECTED`. Chỉ `AUTHORIZED` cho ngữ cảnh dùng cụ thể mới được đưa vào hoạt động tương ứng.

## 4. Kiểm tra chất lượng nội dung
**Cổng nội dung Q-01 (đề xuất bắt buộc trước pilot):**
1. 100% mục nội dung được dùng có SOURCE-ID và trạng thái quyền phù hợp.
2. 100% câu được duyệt có lựa chọn, 1 đáp án nguồn hợp lệ (nếu format tương ứng), ngữ cảnh group/Part và nguồn giải thích hoặc tag `no_explanation` được công bố; câu nhập mơ hồ bị chặn.
3. 100% câu Listening được QA đối chiếu audio ↔ group ↔ câu ↔ đáp án ↔ thời điểm phát; không ghép thiếu/nhầm.
4. Ít nhất hai lượt kiểm tra logic/answer key cho mọi form từ 2 lần xem độc lập khi có thể; khi không có người thứ hai, dùng hai lần kiểm tra cách quãng và ghi giới hạn bằng chứng (không gọi là independent review).
5. Thi thử end-to-end từng form: 200 câu, đúng thứ tự và 45+75 phút, ảnh/đoạn dài hợp lệ, mất mạng/cuộc gọi được kiểm tra ở giai đoạn testing.
6. Truy vết phiên bản: khi sửa câu/đáp án phải ghi version + tác động tới attempt và kết quả đã có.

Các ngưỡng 100% là **ngưỡng QA đề xuất**, chưa được PO phê duyệt và chưa được đo.

## 5. Gate hai Full Mock — Q-MOCK
**M-01 hard prerequisites:** Có bằng chứng bản quyền phù hợp cho mỗi form, đủ số câu và hình/audio, không có mục trùng giữa 2 form, không dùng câu đã luyện ngay trước test.

**M-02 equivalence:** Giống cấu trúc/thời lượng là cần, nhưng **không chứng minh tương đương độ khó**. Đề xuất kiểm tra ma trận độ khó theo Part/nhóm câu bởi người đánh giá đủ năng lực, pilot nhỏ để phát hiện chênh lệch lớn. N=2–5 không đủ để chứng minh statistical equating.

**M-03 reporting policy:**
- Cho phép dự thảo: số đúng, tỷ lệ đúng và phân tích theo Part/section; so sánh mô tả thận trọng A/B.
- Không tuyên bố: điểm TOEIC chính thức/điểm ETS tương đương, tăng 100–200 điểm nhờ app, độ chính xác quy đổi 990 khi chưa có quy trình thẩm định phù hợp.
- Nếu độ khó không thể biện minh: không dùng chênh lệch A/B làm KPI tăng điểm; có thể báo số đúng từng form **không thể so trực tiếp**.

**M-04 fallback cần PO quyết định (không tự động):**
- **B1:** B đầy đủ, nguồn 7 Part + 2 mock hợp lệ và QA đạt ⇒ trình khóa MVP.
- **B2:** Giữ Part practice + diagnostics, tạm loại Full Mock và mọi tuyên bố tăng điểm ⇒ **scope amendment bắt buộc PO duyệt**.
- **B3:** Chỉ chạy pre-pilot Lean hoặc dừng chọn nội dung để mua/biên soạn có quyền ⇒ **PO duyệt lại**.

## 6. Gate chi phí — pilot 2–5 người/4 tuần
Chưa có kiến trúc hoặc báo giá, không được kết luận vận hành = 0 đồng. Hạch toán **chi phí phát triển**, **chi phí một lần nội dung/audio**, **OPEX 4 tuần**, **phí phát hành tương lai** thành các dòng khác nhau.

| Cost-ID | Hạng mục | Đơn vị và biến đo | Hiện trạng | Kiểm soát |
|---|---|---|---|---|
| C01 | Mua/quyền nội dung/audio | VND / bộ / kỳ license | Chưa báo giá, có thể chi phối tổng chi phí | Mua chỉ khi PO đồng ý |
| C02 | Biên soạn, số hóa và QA | giờ công + chi phí thuê ngoài | Chưa ước lượng; **không phải chi phí bằng 0** dù tự làm | Ghi effort/hours |
| C03 | Lưu dữ liệu câu hỏi và audio | GB lưu / tháng | Chưa tính file thật | Quota + cảnh báo |
| C04 | Tải/stream audio và hình | GB transfer / 4 tuần | Chưa có bitrate/time | Phân tích theo workload |
| C05 | Xác thực, dữ liệu và đồng bộ tiến độ | requests/reads/writes | Chưa chọn dịch vụ | Giới hạn và logs |
| C06 | Monitoring / backup / domain | VND / kỳ | Chưa chọn | Tối giản theo pilot |
| C07 | AI API | token * đơn giá | **0 trong ứng viên B**, nếu thật sự không dùng AI | Không tự bật |
| C08 | Hạ tầng/trợ giúp kỹ thuật/thiết bị | VND / lần/ tháng | Chưa chốt | Liệt kê ngoài OPEX |

**Đối chiếu thị trường hạ tầng:** Firebase công bố gói Spark no-cost có quota cho một số dịch vụ, Blaze có tính theo sử dụng. Đây là **ví dụ tham khảo khả năng no-cost**, không phải quyết định dùng Firebase hoặc bằng chứng pilot sẽ hoàn toàn miễn phí. Nguồn: https://firebase.google.com/pricing và https://firebase.google.com/docs/projects/billing/firebase-pricing-plans.

**Công thức ngân sách yêu cầu khi chốt scope:**
`TCO_pilot = one_time_content + setup + (4_week_storage + bandwidth + reads_writes + auth + logs + backup + AI_if_any) + QA_effort_cost`.

**Chỉ số bắt buộc trước triển khai:** PO chốt `BUDGET_OPEX_MAX_VND_4W` và `BUDGET_CONTENT_ONE_TIME_MAX_VND` (chưa điền); không triển khai nếu tình huống bất lợi vượt giới hạn chưa được PO chấp thuận. Có cơ chế theo dõi thực chi và cảnh báo ngưỡng trong execution.

## 7. Rủi ro mức độ cao và chủ sở hữu quyết định
| Risk-ID | Sự cố | Kích hoạt stop | Chủ thể quyết định |
|---|---|---|---|
| R01 | Nội dung không có quyền dùng | `UNKNOWN/REJECTED` tại ngữ cảnh dùng | PO hoặc chủ sở hữu quyền cấp giấy phép; cần tham vấn pháp lý khi phức tạp |
| R02 | Không đủ 2 form/câu hoặc trùng với practice | Không đủ inventory / contamination | PO duyệt fallback |
| R03 | Chấm sai, audio không khớp | QA fail | Không phát hành item/form trước sửa và nghiệm thu |
| R04 | Đề A/B không đủ tương đương | Không có cơ sở so sánh | Cấm claim score delta như ETS |
| R05 | UX Reading dài + mỏi mắt | Người học không thể hoàn thành/bị gián đoạn nghiêm trọng | UX and pilot gates sau này |
| R06 | OPEX/content cost vượt cap | Không có cap hoặc vượt dự báo | PO quyết định giảm scope/ngân sách |
| R07 | Quyền riêng tư, xóa dữ liệu | Chưa có chính sách phù hợp với chức năng dữ liệu | Requirements & release gates |
| R08 | AI/auto import bị đưa lén vào B | Chưa được duyệt hay đánh giá | Block scope creep |

## 8. Phân công và phương pháp chứng minh — không hỏi từng bước
**Desk-based ngay:** Quy định ETS/CC/Google Play, cấu trúc đề, scoring, no-cost quotas; đã có bằng chứng công khai.  
**Chỉ yêu cầu dữ liệu từ PO khi thật cần:** Danh mục nguồn (tên, loại, tình trạng giấy phép) khi chốt MVP; hai ngưỡng ngân sách; review ba fallback B1/B2/B3 nếu content gate fail. Không ép gửi PDF/audio ở Stage 03 khi người dùng chưa tiện.  
**Sau mới cần hands-on:** Sample mapping/QA (trước khi hứa importer hay chốt form), mobile long-form UX trước nghiệm thu và pilot.

## 9. Nguồn chính thức (kiểm tra ngày 2026-11-21)
- TOEIC format and Part counts: https://www.iibc-global.org/english/toeic/test/lr/about/format.html
- ETS TOEIC licensing: https://www.ets.org/legal/permissions/licensing.html — lưu ý **whole form/single questions not ordinarily licensable**.
- Google Play intellectual property: https://support.google.com/googleplay/android-developer/answer/18265346?hl=en
- Scoring/equating: https://www.iibc-global.org/english/toeic/test/lr/guide05.html
- Creative Commons: https://creativecommons.org/faq/
- Google Play data handling: https://support.google.com/googleplay/android-developer/answer/10144311?hl=en
- Firebase no-cost reference: https://firebase.google.com/pricing
