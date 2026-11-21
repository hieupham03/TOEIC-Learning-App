# Product Requirements Document (PRD) — DRAFT V0.1

**Trạng thái:** ANALYST WORKING DRAFT — NOT APPROVED. Không phải MVP baseline.  
**Định hướng:** WP-02 B Balanced Family Pilot có điều kiện, được Product Owner chọn để phân tích.  
**Tham chiếu:** Product Vision V1.0 Approved; CP-01..05 active; Feasibility V0.1.

## 1. Product problem & target audience
Người học TOEIC tại Việt Nam có quỹ thời gian không đều, muốn vừa luyện toàn bộ 7 Part, vừa làm Full Mock trên Android; muốn audio–câu hỏi–đáp án–lỗi sai thống nhất thay vì mở nhiều tab hoặc chuyển file. Nhóm thử đầu tiên 2–5 người trong gia đình, 4 tuần; người học #1 ~550 qua mock hướng tới 650–750, #2 ~650 thi chính thức hướng tới 750–850; các baseline khác chuẩn, không suy ra tăng điểm bằng cách so trực tiếp.

## 2. Outcome/Success hypotheses — chưa duyệt ngưỡng
| ID | Outcome candidate | Chỉ số quan sát | Không được tự kết luận |
|---|---|---|---|
| O-01 | Người học bắt đầu nhanh hơn | Thời gian mở phiên/câu và số phiên | Không nói đã cải thiện trước đo |
| O-02 | Học đủ L&R | % Part có hoạt động hợp lệ, số câu thực hành | Không suy ra cải thiện năng lực |
| O-03 | Học từ lỗi sai | % câu sai có phản hồi nguồn và thử lại | Không đánh đồng nhớ tức thời với nhớ lâu |
| O-04 | Theo dõi tiến độ | Thống kê correct/attempt/Part; mock A/B khi đạt content gate | Không nói điểm tương đương ETS |
| O-05 | Duy trì 4 tuần | Weekly active, sessions/user, feedback tuần | N=2–5 mang tính pilot, không đại diện thị trường |
| O-06 | Chi phí có kiểm soát | OPEX 4 tuần và one-time content riêng | Không gắn mác zero-cost nếu chưa đo |

## 3. Candidate user jobs
1. Chọn Part, mục tiêu và thời lượng có sẵn để luyện câu liên quan.
2. Nghe đoạn audio đúng, trả lời và xem đáp án, giải thích đã kiểm duyệt.
3. Xem và ôn lỗi sai; hệ thống gợi ý bài kế tiếp theo quy tắc minh bạch.
4. Làm Full Mock liên tục với cấu trúc 200 câu nếu nguồn 2 form được phép và QA đạt.
5. Xem thống kê điểm đúng thô và Part; chỉ diễn giải chênh lệch hai đề khi có cơ sở.
6. Người quản lý có thể thêm/chỉnh sửa nội dung **được cấp phép rõ** bằng quy trình kiểm duyệt; không tự tạo importer phổ quát.
7. Bảo vệ lịch sử học, thực hiện quyền xóa dữ liệu khi có tài khoản và hợp tác trong pilot.

## 4. Scope Candidate — In / Conditional / Out
| Nhóm | Đề xuất | Ghi chú |
|---|---|---|
| Android online-only 2–5 pilot users | IN CANDIDATE | Không chốt UI/tech |
| L&R Part 1–7 | CONDITIONAL IN | Phụ thuộc nguồn hợp lệ, QA, phủ Part |
| Audio-question-answer-review | CONDITIONAL IN | Kiểm tra mapping 100% item dùng |
| Làm một câu / chọn Part và thời lượng | IN CANDIDATE | Phiên học ngắn, không cần notification |
| Error history và Part diagnostics | IN CANDIDATE | Không tạo điểm TOEIC chính thức |
| Simple rule-based activity suggestion | IN CANDIDATE | Không tuyên bố AI adaptive |
| Manual rights-aware content curation | CONDITIONAL IN | Chỉ với quyền nội dung hợp lệ |
| Full Mock A/B 200 câu | **BLOCKED — CONTENT+RIGHTS+QA GATE** | Chưa có 400 câu được chứng minh |
| Raw correct/percentage/internal report | CONDITIONAL IN | Phải hiện rõ ý nghĩa điểm |
| 990 official-equivalent score conversion | OUT / UNPROVEN | Không tự quy đổi |
| PDF/audio auto-import | OUT for this draft | Không phủ nhận nhu cầu dài hạn |
| AI question/explanation generation | OUT for this draft | Đánh giá sau nếu có nhu cầu |
| Interactive vocab notifications | OUT for this draft | Có nhu cầu trải nghiệm, chưa MVP |
| iOS, offline, ads, public paywall | OUT for this pilot draft | Không đồng nghĩa bị loại khỏi roadmap |

## 5. Business journeys (không phải UI)
- `J-01`: Khởi tạo mục tiêu + thời lượng học → nhận lựa chọn Part/hoạt động → thực hành → phản hồi nguồn → lưu tiến độ.
- `J-02`: Người học chọn Full Mock hợp lệ → làm bài L&R liên tục → nộp/hoàn tất → nhận số đúng/Part; không bị hiển thị điểm tương đương ETS giả mạo.
- `J-03`: Người biên tập kiểm tra quyền nguồn → cấu trúc nội dung và mapping → QA → công bố vào tập pilot → có khả năng sửa/thu hồi mục lỗi.
- `J-04`: Người học xem câu sai → xem giải thích có nguồn → chọn ôn lại → cập nhật lịch sử.

## 6. Quality principles / nonfunctional goals (draft)
- Không sử dụng dữ liệu nội dung chưa có quyền phù hợp; không chuyển sang AI third-party khi chưa kiểm tra quyền và quyền riêng tư.
- Không làm mất kết quả các câu đã được xác nhận mà không cảnh báo khi có gián đoạn; trạng thái timer/recovery cho mock phải được đặc tả trước pilot.
- Test Reading nhiều đoạn dài trên màn hình điện thoại, đặc biệt rủi ro mỏi mắt PO đã báo.
- Mỗi bản ghi câu, lựa chọn, đáp án, audio và nguồn có version/traceability; sửa answer key có audit trail.
- Phải có luồng xóa tài khoản và dữ liệu nếu tạo account; chính sách privacy và sự đồng ý theo tình huống thực tế.
- OPEX trần 4 tuần và trần mua nội dung phải PO duyệt, chi phí xây dựng không được gọi là miễn phí.

## 7. Rủi ro và điều kiện khóa baseline
`G-CONTENT` (số item, quyền, QA), `G-MOCK` (2 forms + cách diễn giải điểm), `G-LEGAL`, `G-COST`, `G-ANDROID`, `G-PRIVACY`. Trước khi duyệt MVP cuối cùng, PO phải có quyết định B1/B2/B3 nếu G-CONTENT hoặc G-MOCK không đạt. PRD V0.1 là cơ sở thảo luận, không phải hợp đồng delivery.

## 8. Open decisions for Product Owner (gộp, không hỏi lẻ)
- Có sẵn nguồn hợp pháp và đủ cho bao nhiêu Part, mock? Khi kiểm kê được mới khóa feature.
- Nếu hai mock không đủ: B1 nguồn bổ sung, B2 thu gọn có sửa mục tiêu score, hay B3 Lean pre-pilot?
- Trần ngân sách nội dung một lần và OPEX 4 tuần; mức độ chấp nhận manual curation.
- Các thước đo pilot và ngưỡng nghiệm thu đề xuất cần phê duyệt sau khi biết thực lực nguồn.


---

## V0.2 EVIDENCE-FIRST ADDENDUM (2026-11-21) — DRAFT ONLY

V0.1 retained above as analysis baseline for review; V0.2 does NOT promote any item into approved MVP.

- P-NEW-01: The working project name `TOEIC Learning App` must not be treated as cleared public app name; independent brand and compliant descriptive reference required before store listing.
- P-NEW-02: Two 200-item full mocks require 400 distinct **authorized and QA-reviewed** questions with all audio/images; Part-practice pool cannot leak both assessment forms.
- P-NEW-03: Do not claim official TOEIC equivalence or score gain without psychometric substantiation; show raw/Part results with prominent limitations only if authorized by PO.
- P-NEW-04: Vendor infrastructure may have free quotas, but content authoring/licensing, audio/graphics and QA are separate dominant risk; no 0-VND assumption.
- P-NEW-05: PO must explicitly choose B1/B2/B3 conditional fallback in `STAGE03_SCOPE_LOCK_DECISION_PACK_V0.1.md`; no automatic scope change.
- P-NEW-06: Pilot family 2–5 participants does not substitute for Google Play production testing requirements for new personal developer accounts (12 testers/14 days, condition applies before public production).

**Not approved:** MVP lock, acceptance thresholds, public name, user content rehosting, copyright status, mock score equivalence, UI/architecture/code.
