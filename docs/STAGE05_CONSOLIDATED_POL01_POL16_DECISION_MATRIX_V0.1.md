# Stage 05 — Single-Batch POL-01..POL-16 Resolution Matrix Candidate V0.1

**Status: CANDIDATE CHECKLIST, NOT A NEW POLICY APPROVAL.** This is a consolidation of signed `STAGE05_ECP00_PENDING_POLICY_REGISTER_V0.1.md` (unchanged) and later narrow review-only approvals D05-POL-009=A, D05-POL-010=A. No one POL domain is fully CLOSED.

**Decision principle:** Resolve **only policies applicable to the specific future claim/test**; avoid requiring 16 separate signoffs for every observation. A source can be signed as admissible for one bounded claim without declaring it authoritative for unrelated claims. The signed baselines and preexisting fixed 7-calendar-day/30-day business policies must not be re-voted.

| ID | Remaining policy question | Lane | EV/FM | When actually needed | Already signed review subset? |
|---|---|---|---|---|---|
| POL-01 | Thẩm quyền quan sát thời gian qua reboot/đổi đồng hồ | K1 | EV01/03; FM03/04 | Khi xin PASS thời gian phải xác định nguồn/đối chiếu có quyền đánh giá; trước quan sát cần mô tả nguồn thu | NO |
| POL-02 | Ngưỡng clock skew/drift/grace | K1 | EV01/03; FM03/04 | Trước bất kỳ PASS định lượng tương ứng; KHÔNG tạo giá trị số tại đây | NO |
| POL-03 | Diễn giải gián đoạn Full Mock | K1 | EV02/04; FM01/02/05/18 | Trước khi kết luận clean/non-comparable; dữ liệu mô tả có thể thu thập nếu có riêng quyền thử | NO |
| POL-04 | Bằng chứng tiến trình audio/Listening | K1 | EV04; FM01/05/18 | Khi kiểm chứng Listening hoặc xin PASS âm thanh/tiến trình | NO |
| POL-05 | Bằng chứng ACK bền vững | K2 | EV05; FM02/07 | P05-R1..R3 reviewer APPROVED; nguồn/quan sát đủ giá trị PASS CHƯA | YES: reviewer only |
| POL-06 | ACK mất/đến trễ, retry, trùng | K2 | EV06; FM08/14 | P06-R1..R4 reviewer APPROVED; cơ chế/giới hạn/nguồn CHƯA | YES: reviewer only |
| POL-07 | Nguồn gốc và độc lập bằng chứng | K2 | EV01/05/06; FM03/08 | P07-R1..R3 reviewer APPROVED; độc lập nguồn thực tế vẫn phải chứng minh | YES: reviewer only |
| POL-08 | Bằng chứng mâu thuẫn/đối chứng | K2 | EV01..08; FM03/04/08/09 | P08-R1..R4 reviewer APPROVED; người/phương thức phân xử thực tế CHƯA | YES: reviewer only |
| POL-09 | Định danh/cách ly người học | K2/K3 | EV07; FM09 | Trước quan sát có ngữ cảnh nhiều người học và trước privacy PASS | NO |
| POL-10 | Bản sao, xóa và lưu giữ | K3 | EV08; FM10/11 | Phạm vi bản sao/ngoại lệ/evidence trước privacy PASS; 7d/30d đã LOCKED | NO |
| POL-11 | Phát hành học liệu và B1 QA | K4 | EV09/11; FM06/13/16 | Trước CONTENT-READY hoặc pilot PASS; không bắt kiểm kê/rights lại | NO |
| POL-12 | Điểm thô và kết quả lịch sử | K4 | EV10; FM12/14/17 | Trước PASS xử lý key revision/history; không suy ra ETS | NO |
| POL-13 | Bối cảnh/phiên bản Android, accessibility | K5 | EV04/12; FM15/18 | Trước device test cụ thể phải phê duyệt môi trường; ≥2 contexts trước pilot | NO |
| POL-14 | Dữ liệu cá nhân/người tham gia và consent | K3/K5 | EV07/12; FM09/15 | Trước hoạt động với người học hoặc dữ liệu thật; dữ liệu tổng hợp cũng phải có ranh giới | NO |
| POL-15 | Sở hữu bằng chứng, signoff, exception/retest | K5 | All EV/FM | Trước xin phép chạy test và nhất là trước bounded PASS | NO |
| POL-16 | Quyền quyết định kiến trúc | K6 | All EV/FM | PO quyết định riêng SAU bằng chứng; không cần chốt trước mọi quan sát mô tả | NO |

## Mandatory separation between policy acceptance and proof

- **Already signed (not to reapprove):** truthful save/UNKNOWN claims; independent/correlated/unknown provenance vocabulary, contradiction escalation, B1 mandatory, 7d/30d deletion/retention, mock clean/noncomparable semantics, raw non-ETS scoring.
- **Still unresolved:** observation authority, tolerances, correct source bindings, real participant/device scope, owners, measured results and architecture selection. These are **NOT APPROVED** merely because a rule subset has been approved.
- **Can wait until a relevant claim is being judged:** unrelated source of truth, target device, content-key correction policy; never waive later mandatory pilot QA.
- **Cannot be skipped for any actual activity:** separate PO authorization, applicable privacy/data consent, test material/environment, accountable evidence recording/stop conditions, no spending without reopening budget.

This matrix is intended to be one decision support attachment for a future **single bundle**, not 16 automatic tasks or decisions.

**Tình trạng dự án áp dụng cho mọi bảng:** Stage05 IN PROGRESS; ARCH03-A/B/C UNSELECTED; ARCH-04 chưa mở; ECP00..06 PLAN ONLY; EV01..12 document reviewed/0 verified app claims; FM01..18 NOT RUN; QA01..08 actual PASS=0; Android/learners n=0; budget DEFERRED. Không tự mở công việc mới, không đổi các Requirements/Design Baseline.
