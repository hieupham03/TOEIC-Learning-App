# Stage05 ARCH-03 — Scope, Comparative Method and Evidence Control V0.1

**Authority:** D05-ARCH03-005=A; **mode:** DESK / PAPER ONLY; **date:** 2026-11-21.

## How this study compares candidates

1. Compare **conceptual evidence-responsibility boundaries**, not language/runtime/provider/library or actual component topology. A/B/C are competing hypotheses, not deployable designs.
2. Apply **identical adversarial inputs**: signed FR/NFR/AT, EV01..12, FM01..18, content QA obligations, user-facing truth states, Stage02–04 CP and privacy/deletion.
3. For each case report **proposed explanation, weakest falsifier, missing observed proof, future checkpoint and reversibility**. Published Android/OWASP statements establish platform/security constraints, **not app-level feasibility**.
4. Use qualitative comparisons only. No fabricated latency, uptime, cloud costs, test success percentages, sample sizes, risk weights or numerical scores.
5. Distinguish 5 evidence categories: *signed requirement*, *PO attestation*, *official platform fact*, *analyst option hypothesis*, *observed product test*. The last category currently has **zero** entries.
6. A later PO may: select a **conceptual direction** conditionally, order amendments, or defer selection until evidence exists. No direction chosen by this report.

## Candidate independence

- A/B/C differ in **where a proposed validity/durability claim would derive evidence from**, not from a presupposed technology stack.
- T-A/B/C, L-A/B, S-A/B/C, P-A/B/C, C-A/B/C and R-A/B from ARCH02 are **independent domain-level choices**. No model family automatically inherits every other choice; combining them has not been proven compatible.
- Distinction between **clock readings**, **clock authority** and **policy for incomplete/conflicting evidence** is preserved. None has been selected.
- Cloud synchronization, on-device durable store, event journal, identity server, or duplicate-write handling are **possible concepts only**; any concrete placement requires later PO approval.

## Evidence already checked against published documentation

| Source | Supportable claim | Non-supportable leap |
|---|---|---|
| Android `SystemClock` — https://developer.android.com/reference/android/os/SystemClock | elapsed since boot includes sleep; wall clock is distinct | anti-tamper cross-reboot clock authority proven |
| Android processes — https://developer.android.com/guide/components/activities/process-lifecycle | app processes may be reclaimed | this app recovers a clean Full Mock |
| Android UI saving — https://developer.android.com/topic/libraries/architecture/saving-states | transient UI state and persistent data have different properties | user answer durable ACK proven |
| Android audio focus — https://developer.android.com/media/optimize/audio-focus | playback/focus subject to interruptions and version-dependent conditions | uninterrupted Listening for all versions |
| OWASP MASVS — https://mas.owasp.org/MASVS/ | mobile secure storage/auth/authorization expectations | learner isolation / deletion proven |
| Google Play user data — https://support.google.com/googleplay/android-developer/answer/10144311?hl=en | account/deletion rules depend on product/distribution | signed 7-day and 30-day commitments came from Google Play |

**No external design recommendation is treated as a PO product requirement.** Prior official evidence ledger `STAGE05_EVAL004_OFFICIAL_EVIDENCE_REVALIDATION_LEDGER_V0.1.md` remains source of record for more references.

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
