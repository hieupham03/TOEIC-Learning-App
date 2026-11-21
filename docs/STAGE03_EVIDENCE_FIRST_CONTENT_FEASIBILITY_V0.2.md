# Stage 03 — Evidence-First Content & Two-Mock Feasibility V0.2

**Ngày nguồn được đối chiếu:** 2026-11-21. **Trạng thái:** DESK-RESEARCH COMPLETE FOR PUBLIC FACTS; SOURCE-SPECIFIC RIGHTS & CONTENT NOT VERIFIED.  
**Hướng:** B Balanced Family Pilot **conditional**; CP-01..CP-05 active. Không phải chứng nhận pháp lý; cần đọc hợp đồng/giấy phép cụ thể trước khi sử dụng.

## 1. Executive finding
- **Điểm chặn thực sự:** quyền và độ sẵn sàng của nội dung số (đặc biệt 2 mock), KHÔNG phải đã có bằng chứng backend quá đắt.
- 2 full mock 200 câu mỗi bộ = 400 câu **không trùng giữa hai bộ**; chưa có bằng chứng bất kỳ 400 câu cụ thể có license phù hợp và được QA.
- Bốn tuần, 2–5 người chỉ là điều kiện thử nghiệm; không tự động làm cho việc sao chép/re-host tài liệu bên thứ ba trở nên hợp pháp.
- ETS TOEIC licensing: quyền cấp phép cho **Test Sample Questions, Answer Key** có bảng phí công khai nhưng **entire disclosed test form** và **single test questions** được liệt kê là *not available for licensing* trong chính sách ETS. ETS không phải lối mua 2 đề hoàn chỉnh qua bảng phí nói trên.
- Tên `TOEIC Learning App` là tên làm việc NỘI BỘ. Trước khi phát hành cần kiểm tra hướng dẫn ETS về nhãn hiệu, vì dùng TOEIC làm tên sản phẩm có giới hạn. Không sử dụng logo/không ngụ ý chứng thực.

## 2. Nguồn học liệu — kiểm tra tính khả dụng cho sản phẩm
| Path | Ví dụ nguồn | Rights proof currently | Pilot cloud 2–5 | Public release | Recommended status |
|---|---|---|---|---|---|
| S-A | Tự biên soạn câu hỏi/đoạn văn/ảnh/audio gốc | Chưa có content bank/author declarations | Có thể nếu bảo đảm nguồn gốc toàn bộ asset | Có thể nếu sở hữu mọi quyền | **CANDIDATE, content NOT READY** |
| S-B | Nhà xuất bản / đối tác B2B cấp phép bằng hợp đồng | Chưa có nhà cung cấp/quote/license | Chỉ khi hợp đồng cho phép app, cloud, nhóm | Chỉ khi phân phối/territory/commercial được phép | **CANDIDATE, rights UNKNOWN** |
| S-C | PDF/sách/audio người dùng đã mua/tải | Chưa kiểm kê license từng nguồn | **Không được tự suy ra** quyền upload/chia sẻ | **Không được tự suy ra** quyền phân phối | **ON HOLD for shared app** |
| S-D | ETS/IIBC handbook, sample items, official books | Có chính sách ETS, chưa có hợp đồng | Không nhúng/đưa lên cloud nếu chưa có quyền hợp lệ | Không nhúng/đưa lên công khai nếu chưa có quyền | **NOT A SOURCE FOR 2 WHOLE MOCKS** |
| S-E | CC BY/CC0 hoặc nguồn open | Chưa tìm được bộ TOEIC đủ 400 câu có nguồn & quyền xác minh | Theo đúng license + attribution + quyền audio/hình | Chỉ nếu license cho phép mục đích đó | **EXPLORATORY, NOT VERIFIED INVENTORY** |
| S-F | Sinh câu hỏi/đoạn nghe bằng AI | Chưa kiểm định nguồn gốc, tính đúng, rights/provider | Chưa cam kết B; chỉ sau eval/rights | Chưa đủ chứng cứ | **OUT OF B CORE FOR NOW** |
| S-G | Crawl website/app luyện đề | Không có quyền riêng của tác giả | Không được coi public web = quyền tái phân phối | Không có cơ sở | **REJECT by default absent license** |

**Rights Matrix tối thiểu:** source ID, author/rightsholder, URL/tài liệu pháp lý, quốc gia, loại license, ngày hết hạn, quyền sao chép, số hóa, thay đổi, host server, cung cấp cho family testers, public release, mục đích thương mại, gửi dữ liệu qua bên thứ ba/AI, hình ảnh/giọng đọc, ghi công. Status per use-case = `AUTHORIZED / RESTRICTED / UNKNOWN / REJECTED`. `UNKNOWN` không được phát hành.

### Nhãn hiệu và chính sách ETS
- ETS TOEIC Licensing Policy effective June 2017: mẫu câu & answer key *electronic format* **USD 1,500** (danh mục cấp phép ETS, thông thường 1 năm; chưa gồm thuế/phí theo quốc gia); đây **KHÔNG phải phí cho 2 full mock**.
- ETS stated **entire disclosed test form** and **single test questions** are not available for licensing under its published list; requests for other rights need written permission and review.
- ETS trademark guidelines restrict using TOEIC in third-party product name/domain and forbid implying endorsement. Plan independent brand name; descriptive mention only if reviewed as compliant.
- Google Play IP policies prohibit infringing copyright/trademarks; không dựa vào việc app khác có nội dung như bằng chứng chúng ta được quyền sao chép.

## 3. Hai Full Mock: item accounting theo chuẩn ETS
| Part | Per form | Two forms | Source/QA dependencies |
|---|---:|---:|---|
| P1 Photographs | 6 | 12 | 12 ảnh được phép + audio, câu đúng |
| P2 Question–Response | 25 | 50 | câu hỏi/3 lựa chọn trong audio, key |
| P3 Conversations | 39 | 78 | 13 cuộc hội thoại x 3 câu mỗi form; audio/bảng biểu tùy item |
| P4 Talks | 30 | 60 | 10 bài nói x 3 câu mỗi form; audio/bảng biểu |
| P5 Incomplete Sentences | 30 | 60 | câu/4 lựa chọn/key |
| P6 Text Completion | 16 | 32 | 4 đoạn x 4 câu mỗi form; ngữ cảnh |
| P7 Reading Comprehension | 54 | 108 | đoạn đơn/đa văn bản, ảnh/bảng nếu có |
| **Total** | **200** | **400** | **200 L + 200 R across two forms** |

Mỗi form có 6+25+13+10 = **54 prompts/recording-groups** Listening (không mặc định 54 file audio), 108 nhóm/prompt cho 2 form; thêm ảnh/biểu. Hai đề thi nên không dùng lại câu đã lộ trong Part Practice; nếu practice và test dùng chung đề thì số đúng bị nhiễm do học thuộc. Với bank luyện 7 Part phải có nội dung bổ sung **ngoài 400 item** hoặc có chính sách khóa mock trước khi làm.

## 4. Điểm chất lượng và score integrity
**Q-LEGAL:** 100% asset active có proof/source-rights phù hợp ngữ cảnh sử dụng (đề xuất gate, chưa được PO duyệt).  
**Q-CONTENT:** Đủ nội dung, không sai key, không mất context; 100% item được kiểm tra logic và định dạng trước khi cho học.  
**Q-LISTENING:** ghép 100% audio↔group↔item↔key/transcript khi có; phát lại kiểm thử trên thiết bị.  
**Q-MOCK:** hai form 200 câu độc lập, đúng phân bố, 45 phút Listening +75 phút Reading, không duplicate, mô phỏng end-to-end.  
**Q-REVIEW:** tiêu chuẩn review đề xuất 2 lượt (lượt độc lập nếu có người phù hợp); nếu solo thì phải khai là single-review risk, không giả là đã kiểm chứng độc lập.  
**Q-REPORT:** báo **số đúng, tỷ lệ đúng, phân bố lỗi theo Part**. Nếu không có nghiên cứu equating, không tuyên bố conversion chính xác sang 10–990, không gọi 'điểm ETS chính thức' và không dùng delta hai form làm bằng chứng tăng điểm TOEIC.  
**Q-ANDROID:** Reading dài tránh mất nội dung; kiểm tra mỏi mắt, audio, gián đoạn lưu tiến độ trước nghiệm thu.  
**Q-PROVENANCE:** cập nhật key có version và rà soát attempt cũ.

**GATE hiện tại:** Q-LEGAL=BLOCK; Q-CONTENT=BLOCK; Q-LISTENING=BLOCK; Q-MOCK=BLOCK; Q-REPORT=CONDITIONAL. Public official format verified but NOT actual assets.

## 5. Desk research kết luận và lỗ hổng không thể lấp bằng tìm kiếm
**Đã biết từ nguồn công khai:** chuẩn format, cấu trúc 400 câu, licensing ETS, Google Play trademark/IP, cơ chế score equating, các lựa chọn infrastructure/TTS no-cost/low cost.  
**Chưa biết, không suy diễn:** tên/giấy phép thực tế của PDF/audio của PO; tổ chức nào sẽ bán quyền *app/cloud/family/public* đủ 400 item; chất lượng 2 forms và chi phí thực tế; thời lượng nhân công biên soạn/QA; chi phí cho bên thứ ba. Chưa tìm được **bộ 400 câu hoàn chỉnh, được chứng minh có quyền tái phân phối**, phải để **NOT VERIFIED** chứ không gán ngầm cho CC/open sources.

## 6. Sources and observations (checked 2026-11-21)
- ETS format: https://www.ets.org/toeic/about/listening-reading.html
- ETS handbook, per-Part counts + scoring: https://www.ets.org/pdfs/toeic/toeic-listening-reading-test-examinee-handbook.pdf
- ETS TOEIC licensing (licensable samples / nonlicensable complete test): https://www.ets.org/legal/permissions/licensing.html
- ETS trademark policy: https://www.ets.org/legal/trademarks.html
- Google Play IP: https://support.google.com/googleplay/android-developer/answer/18265346
- ETS official prep app shows 400 questions in its FREE product; this is **an existence/benchmark fact**, NOT permission to copy: https://www.etsglobal.org/pm/en/content/toeic-test-application
- CC BY4: https://creativecommons.org/licenses/by/4.0/deed.en ; CC BY-NC4 restriction: https://creativecommons.org/licenses/by-nc/4.0/deed.en
- ETS score conversion methodology: ETS handbook linked above + https://www.iibc-global.org/english/toeic/test/lr/guide05.html
