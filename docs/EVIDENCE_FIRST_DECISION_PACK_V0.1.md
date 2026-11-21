# TOEIC Learning App — Evidence-First Validation & Decision Pack V0.1

**Ngày:** 2026-11-21  
**Quy trình Evidence-First theo chỉ đạo Product Owner; các quyết định sản phẩm D-025C–F còn chờ phê duyệt**  
**Giai đoạn:** 02/11 Market Research & Validation — IN PROGRESS / GATE HOLD  
**Product Vision:** V1.0 APPROVED — không thay đổi  
**Không tạo code, kiến trúc, UX/UI, PRD/SRS hay chốt MVP.**

## 1. Tại sao cần đổi cách làm

Theo phản hồi Product Owner, quá trình hỏi từng bước và yêu cầu baseline Listening / Reading làm mất thời gian so với lợi ích dự kiến. Phương pháp đề xuất: **Secondary Research First / Evidence-First Validation**, sau đó Product Owner xem một gói phương án và ra quyết định. Chỉ thực hiện thử nghiệm hoặc phỏng vấn bổ sung khi rủi ro quyết định quan trọng còn thiếu bằng chứng mà nghiên cứu công khai không trả lời được.

### Quy tắc nguồn bằng chứng

1. **Official standard/policy:** ETS, Android Developers, Google Play — làm nguồn chuẩn cho format, khả năng API, giới hạn chính sách.
2. **Peer-reviewed research / systematic reviews:** đủ để hỗ trợ nguyên tắc học tập, không chứng minh tính năng cụ thể của dự án sẽ hiệu quả.
3. **Competitor product documentation:** đủ để biết sản phẩm *công bố/cung cấp* một chức năng, không chứng minh người dùng thực sự thích, hiệu quả học tăng hoặc không có lỗi.
4. **Product Owner direct self-report:** giá trị để xác định pain point và ngữ cảnh; chỉ đại diện bản thân người học số 1.
5. **Secondary/second-hand pilot #2:** phản hồi gián tiếp, không ngang bằng phỏng vấn độc lập.
6. **Unresolved risks:** ghi rõ là giả thuyết, không tự đánh dấu VALIDATED vì có sản phẩm khác làm được.

## 2. Bằng chứng đối chiếu đã tìm được (desk research ngày 2026-11-21)

| ID | Chủ đề | Nguồn & bằng chứng | Mức độ rút ra được | Giới hạn / áp dụng |
|---|---|---|---|---|
| E-01 | TOEIC L&R standard | ETS công bố format 200 câu / 2 giờ, 100 Listening (45') + 100 Reading (75'). https://www.ets.org/toeic/about/listening-reading.html | **HIGH — official specification** | Áp dụng blueprint đề thi; không có nghĩa đề trong app tự đạt tương đương ETS |
| E-02 | Practice từng Part, full test, chữa lỗi | STUDY4 công bố chọn từng Part, tùy chọn thời gian, highlight, kiểm tra kết quả, ôn câu sai, tra từ. https://study4.com/posts/4447/huong-dan-luyen-de-toeic-tren-study4-hieu-qua/ | **HIGH cho existence, LOW cho quality** | Chuẩn benchmark luồng chức năng; không tự gọi là lợi thế cạnh tranh |
| E-03 | Cá nhân hóa/lộ trình | Migii và PREP công bố kiểm tra đầu vào, study plan, mini/full tests, giải thích. https://migii.net/vi/toeic ; https://prepedu.com/vi/toeic/test-practice | **MEDIUM cho công bố tính năng** | Chỉ cá nhân hóa là chưa đủ khác biệt; cần đánh giá chiều sâu, UX, kết quả nếu quyết định cạnh tranh |
| E-04 | Nhập học liệu từ người dùng | Quizlet Smart Assist chuyển ghi chú hoặc tệp tải lên thành flashcards. https://help.quizlet.com/hc/en-us/articles/39606772122509-Creating-study-sets-with-Smart-Assist | **HIGH cho existence** | KHÔNG chứng minh OCR, nhận diện format TOEIC, ghép audio chính xác hoặc quyền tái xuất bản |
| E-05 | Mobile learning research | Tổng quan/meta-analysis về mobile-assisted vocabulary learning ghi nhận tác động tích cực lên học từ vựng; kết quả phụ thuộc nghiên cứu, phương pháp và người học. https://www.cambridge.org/core/journals/recall/article/metaanalysis-on-mobileassisted-vocabulary-learning-do-mobile-applications-help/79C8F00E48D521ED3BCFE0625B5549F3 | **MEDIUM cho nguyên tắc di động** | Không cho phép kết luận thông báo từ đơn sẽ tăng điểm TOEIC |
| E-06 | Ôn cách quãng, recall, feedback | Nghiên cứu thực nghiệm về spacing, feedback, testing trong app học từ vựng: https://pmc.ncbi.nlm.nih.gov/articles/PMC8638698/ ; meta-analysis distributed practice: https://pmc.ncbi.nlm.nih.gov/articles/PMC12189222/ | **MEDIUM–HIGH cho nguyên tắc học** | Không chứng minh thuật toán lịch ôn cụ thể của sản phẩm hiệu quả nhất |
| E-07 | Thông báo Android | Android có hỗ trợ notification actions, tối đa 3 nút trực tiếp: https://developer.android.com/develop/ui/compose/notifications/create-notification | **HIGH — platform fact** | Người học muốn 4 hành vi; cách tổ chức chưa chốt, cần kiểm tra UX/Android permission |
| E-08 | Quyền sở hữu trí tuệ | Google Play cấm ứng dụng xâm phạm quyền của bên thứ ba: https://support.google.com/googleplay/android-developer/answer/9888072?hl=en | **HIGH — publisher policy** | Sở hữu PDF/sách không mặc nhiên có quyền phân phối/đăng lại; phải kiểm tra theo nguồn/giấy phép và luật áp dụng |
| E-09 | Mobile long-form fit | Product Owner báo cáo đã hoàn thành một Full Mock trên Android, nhưng bất tiện đọc Reading dài và mỏi mắt (VAL-020–022) | **MEDIUM cho pain/experience cá nhân, LOW cho quần thể** | Không cần ép làm lại 120 phút trước khi bắt đầu Stage 03, nhưng không xem mobile UX đã validated |
| E-10 | Library workflow pain | Product Owner báo cáo phải mở PDF, tìm audio, chuyển tab, dò đáp án (VAL-013), thường học trên PC (VAL-016) | **MEDIUM — trực tiếp nhưng chủ quan** | Đã đủ để định nghĩa pain/problem, chưa đủ để xác nhận giải pháp import tự động sẽ thành công |

## 3. Tổng hợp theo khả năng kế thừa

**Có thể dựa vào chuẩn/benchmark thay vì tự tổ chức thử nghiệm sơ khai:** TOEIC format chính thức; quy trình chọn Part, mock timed, nghe và trả lời, chấm, giải thích, transcript, lưu lỗi sai; nguyên tắc spacing + retrieval + feedback; các cơ chế notification đã có trên Android.

**Đặc biệt có giá trị cho Product Discovery nhưng chưa được sản phẩm khác giải quyết thay mình:** Mức độ tiện lợi khi đưa **tài liệu người học sở hữu** vào luồng làm đề thống nhất; chất lượng map PDF câu hỏi/đáp án/audio; provenance & quyền nội dung; sự phù hợp với thói quen rảnh thất thường; chi phí và năng lực vận hành nhóm pilot 2–5 người.

**Các kết luận KHÔNG được đưa ra:** “Không ai có tính năng này”, “ứng dụng của ta chắc chắn tăng điểm”, “đề mua được phép số hóa lên kho chung”, “AI có thể giải thích đúng mọi câu”, “điểm các đề bất kỳ so sánh được”, “phản hồi 2 người chứng minh thị trường”.

## 4. Gói quyết định: đổi phương pháp đã chốt, lựa chọn sản phẩm còn chờ duyệt

| Mã | Đề xuất | Lý do & ranh giới | Trạng thái |
|---|---|---|---|
| D-025A | Áp dụng **Evidence-First Validation**; không hỏi chuỗi VAL tuần tự khi nghiên cứu thứ cấp giải quyết đủ | Rút ngắn Stage 02, PO vẫn kiểm soát gate | **APPROVED BY PO DIRECTIVE** |
| D-025B | Chuyển `VAL-013L/R` baseline tự chạy trên PC từ `READY/REQUIRED` sang **OPTIONAL / ON HOLD** | Pain đã được PO báo cáo; không yêu cầu test thủ công để tiếp tục nghiên cứu | **APPROVED BY PO DIRECTIVE** |
| D-025C | Dùng **market-standard TOEIC practice flows** làm benchmark yêu cầu; tập trung khác biệt vào thư viện cá nhân + luồng học + tiến độ | Tránh dựng lại những thứ đã có, nhưng không kết luận khả thi import tự động | PROPOSED |
| D-025D | Tách **hiệu quả học** (spaced review, recall, feedback) khỏi **kênh nhắc** (notification); giữ thông báo là tùy chọn, không quyết định MVP lúc này | Nghiên cứu học tập không chứng minh tần suất thông báo nào tốt nhất | PROPOSED |
| D-025E | Chỉ giữ các **high-risk gates** trước khi xuất bản công khai: quyền nội dung, chất lượng đề/audio/đáp án, độ tin cậy đánh giá điểm và AI; chuyển các đánh giá này sang kế hoạch Quality/Risk và làm khi có mẫu | Không chặn việc lập PRD/SRS chỉ vì chưa thể upload file; nhưng không tuyên bố nội dung có thể phát hành | PROPOSED |
| D-025F | Đưa **Stage 02 vào GATE REVIEW** sau khi PO phê duyệt gói phương pháp và chấp nhận các giả thuyết còn mở; Stage 03 chỉ bắt đầu khi PO chấp thuận gate riêng | Không âm thầm vượt quy trình | PROPOSED |

## 5. Phương pháp rút gọn từ nay

1. **Một vòng desk research đủ sâu theo nhóm chủ đề**, ghi citation, ngày truy cập, loại nguồn, độ tin cậy.
2. **Gap map**: khẳng định được / có bằng chứng hỗ trợ / chưa biết / rủi ro.
3. **Decision Pack**: 3–6 phương án/gói quyết định với khuyến nghị; PO phê duyệt hoặc sửa cả nhóm thay vì câu hỏi lẻ.
4. **Gate Review**: kiểm tra các blocker thực sự cần thiết cho giai đoạn sau. Phần chưa thể xác minh vì thiếu file/chi phí/chưa pilot được đưa vào Risk Register và có điều kiện kiểm tra sau, không coi là đã xác thực.
5. Chỉ tiến hành **test thực tế ngắn, có mục tiêu quyết định** khi desk evidence không giải quyết high-risk uncertainty.

## 6. Stage Gate hiện tại — không tự đổi

- Product Vision V1.0: **APPROVED**.
- Stage 02: **IN PROGRESS / HOLD**, nay chuẩn bị **Gate Review**, chưa tự động PASS.
- Stage 03: **NOT STARTED**.
- VAL-003 file mẫu: **DEFERRED**, chưa thể kiểm chứng audio/PDF/rights.
- VAL-010 price perception: **DEFERRED BY PRODUCT OWNER**, không tự mở lại.
- `VAL-013L/R`: **NOT RUN / OPTIONAL / ON HOLD**, không phải điều kiện để tiếp tục. Đã chuyển theo chỉ đạo mới của Product Owner.
- MVP/PRD/SRS/UX/UI/architecture/code: **NOT APPROVED**.

## 7. Next action

Product Owner đã chỉ đạo áp dụng Evidence-First và bỏ bắt buộc chạy baseline (D-025A/B). Chờ Product Owner chọn **duyệt D-025C–F**, **duyệt có chỉnh sửa**, hoặc **chưa quyết định**. Sau đó cập nhật Decision Log và chuẩn bị **Stage 02 Gate Review** dựa trên bằng chứng; không yêu cầu baseline Listening/Reading chỉ để qua bước.
