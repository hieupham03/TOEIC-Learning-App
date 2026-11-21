# Stage 04 — UX-03 Information Architecture Options V0.1

**Status:** ANALYST DESIGN EXPLORATION — NOT PO APPROVED, NOT FINAL UI.  
**Source:** D04-UX-002 APPROVED U1-A/U2-A/U3-A/U4-A; immutable PRD V0.6, SRS V0.6, Acceptance V0.4.  
**Meaning of IA here:** information grouping, wayfinding and user-facing navigation; **NOT software/system architecture**.

## Shared non-negotiables in every option

- First interaction must reveal **both practice and mock with equal discoverability**, not bury Full Mock or pressure a single mandated recommendation (U1-A).
- A full mock is a formal evaluative journey with pre-start rule disclosure, ordered Listening ~45 min and Reading 75 min, 200 questions × two PO-inventoried forms, no discretionary pause or arbitrary Listening replay for clean comparable attempts.
- Practice is flexible, includes Parts 1–7 and one-item sessions; protected A/B items never used for pre-exposure practice. U4 feedback comes after eligible practice or after full mock completion.
- Long Reading must allow return to relevant passage/figure *and prior reading position*, full figures/tables readable, no clipped content (U2-A).
- Raw result and caveat, no fake ETS score; contextual saved/pending/error/integrity semantics (U3-A). Family learner data separation, verified deletion rule 7 calendar days; routine retention ≤30 days after pilot absent valid continuation agreement.
- Content management/QA exists as governance journey; this UX deliverable does not assert a new embedded admin console or technical backend.

## IA-A — Task Hub / 3 primary destinations — analyst recommendation for LOW-FI evaluation

```text
APP
├── BẮT ĐẦU  (first visit / home)
│   ├── [Luyện nhanh / Luyện Part]  ──> Chọn Part / 1 câu / khoảng thời gian
│   │                                ├── Làm câu (audio/reading)
│   │                                └── Phản hồi và câu tiếp / đổi Part
│   └── [Thi thử Full Mock]        ──> Chọn A hoặc B / kiểm tra sẵn sàng
│                                    ├── Quy tắc lượt thi (no pause/replay)
│                                    ├── Listening → Reading
│                                    └── Nộp / hết giờ / gián đoạn → kết quả trạng thái
├── TIẾN ĐỘ
│   ├── Lịch sử luyện Part
│   ├── Lỗi sai và ôn lại
│   └── Lịch sử Mock A/B / số đúng thô / độ tin cậy so sánh
└── CÁ NHÂN
    ├── Mục tiêu và thời gian học
    ├── Thông tin quyền riêng tư / dữ liệu
    └── Yêu cầu xóa dữ liệu / trạng thái xử lý
```

**Persistent model (candidate only):** 3 bottom destinations `Bắt đầu | Tiến độ | Cá nhân` in normal browsing; **do not show bottom nav as an intrusive distraction during clean Mock**, where back/exit must be explicit and policy-consistent. First-launch profile/goal is an optional lightweight prerequisite only where needed, not invented login architecture.

**Strengths:** one obvious hub for both modes; only three primary destinations; one place for errors/progress; straightforward to explain in a 2–5-person pilot.

**Tradeoffs:** more navigation to historical errors than a dedicated errors tab; need conspicuous both-route cards and a non-blocking 'continue last eligible session' action.

## IA-B — Mode-centred / 4 primary destinations — credible alternative

```text
APP
├── LUYỆN TẬP  (visible equal route on initial chooser)
│   ├── Luyện nhanh 1 câu / lựa Part và thời lượng
│   ├── Câu hỏi theo Part → phản hồi sau câu/phiên
│   └── Gợi ý tiếp theo (bỏ qua được)
├── THI THỬ  (visible equal route on initial chooser)
│   ├── Full Mock A/B và tình trạng sẵn sàng
│   ├── Quy tắc → Listening → Reading
│   └── Kết quả / trạng thái integrity
├── LỖI SAI
│   ├── Câu sai trong luyện Part
│   └── Câu sai từ Mock **chỉ sau khi hợp lệ cho xem lại**
└── TIẾN ĐỘ
    ├── Lịch sử Mock, raw score, caveats
    └── Hồ sơ người học / dữ liệu / quyền riêng tư (sub-area)
```

**Strengths:** mock stays one-tap discoverable, error history direct, separates mindsets.

**Tradeoffs:** 4 destinations compete on compact Android width; privacy/account buried; repeated result/error links; novice may confuse a quick 1-item session with an evaluative mock unless copy is strong. Initial access MUST show both equal routes to satisfy U1-A; do not set a practice-only default entry.

## Choice matrix (preliminary hypothesis, not measured)

| Dimension | IA-A Task Hub | IA-B Mode-centred | Rationale |
|---|---|---|---|
| Entry route parity | Strong — two equal hero actions | Strong — equal mode entry | U1-A mandatory |
| Low navigation complexity on small phone | **Stronger** (3 top destinations) | Weaker (4 areas) | Long-term pilot habit |
| Error-review discoverability | Through Tiến độ | Dedicated area | U4-A |
| Privacy discoverability | Dedicated Cá nhân | Nested in Tiến độ | R4 / AT-18 |
| Mock clean-state focus | Requires deliberate immersive screen | Same requirement | S2-A, U3-A |
| Reading reference preservation | Shared component requirement | Shared component requirement | U2-A; not decided by IA |
| Added product scope | None | None | Same approved MVP |

**Analyst recommendation for PO:** authorize **IA-A as the first low-fi route to compare**, retain IA-B as challenger until walkthrough. This is a recommendation to *study*, **not an approved navigation structure**.

## Decisions the PO may select in one packet

`IA-A` as preferred wireframe direction, `IA-B` as preferred, `COMPARE` both without selecting, or `AMEND` a particular branch. No option overrides the baseline or constitutes an implementation permission.
