# Stage04 — State Transition, UX Copy and Content QA Policy V0.2

**Status:** Design Candidate, traces to signed Stage03 business policies; no software implementation chosen.

## 1. Answer confirmation state machine for representation only

`selected (local)` → `pending acknowledgement` → (`confirmed durable ACK` **or** `unknown/failed`); failure allows `retry confirmation` and a safe return to item. **No selected/pending transition directly to “saved”**. UI must distinguish selected choice from persistently acknowledged choice. Post-reconnect resolution is implementation/test work.

| UI state | User-visible phrase | Visible next action | Evidence condition in actual product |
|---|---|---|---|
| UI-06 | `Đang xác nhận lưu` | wait / return safely | pending persistence confirmation |
| UI-07 | `Đã xác nhận lưu` | next item | durable ACK actually observed |
| UI-08 | `Chưa thể xác nhận lưu` | retry; return to inspect | unknown/failed outcome; no false success |

## 2. Evaluative Mock integrity

Full Mock A/B each comprises 200 independent questions, Listening 100 (~45 minutes) then Reading 100 (75 minutes), no voluntary pause/arbitrary audio replay for comparable evaluative attempt. Distinguish `in progress` / `interrupted, integrity uncertain` / `noncomparable` / `valid completed` / `expired`; UI must not promise timer reset or clean status. A static mock-up cannot adjudicate exact interruption policy in a real app. Preserve last actually acknowledged responses and disclose inability to compare.

## 3. Result transparency

Only raw correct/attempted/unanswered, per-Part L/R, form/version/date and attempt validity, subject to verified source data; no ETS-equivalent scaled score, no proven improvement between non-equated mock forms. **All 130/200, 70/100, 60/100 values in screenshots are dummy data**.

## 4. Content and privacy

`QA not ready` / `QA ready` / `withdrawn` require explicit content status. Only vetted item keys/explanations can show verified copy. Before actual pilot: QA-01..06 content audit; QA-07..08 real app/device integrity. Verified learner-data deletion request ≤7 calendar days and routine pilot retention ≤30 days after pilot except approved exceptions; no assumed login, backend or deletion automation in design.

## 5. Wording/exclusions

Never use `đã lưu`, `đã kiểm duyệt`, `thi hợp lệ`, `đã đồng bộ`, `đã xóa` or personalized target values unless the corresponding condition is true. All static concepts labelled `MẪU THIẾT KẾ • CHƯA KIỂM THỬ`. No gamification, runtime AI tutor, automatic PDF/audio ingestion, iOS, Speaking/Writing or official TOEIC conversion is added by visual design.
