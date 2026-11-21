# Stage 04 — UX-03 Low-Fidelity Wireframe OPTIONS V0.1

**Status:** TEXTUAL LOW-FIDELITY SKETCHES; NOT approved screens, UI visual system, prototype, code, nor software architecture.  
**Intent:** Compare user-facing content grouping/interaction semantics on a narrow Android phone; exact pixels, components, colors, typography, behavior and technical persistence are undecided. All bracketed items are *placeholders*, not implemented controls.

## W-01A: Task Hub home — pairs with IA-A, recommended for comparison

```text
┌──────────────────────────────────┐
│ Xin chào [người học]             │
│ Mục tiêu: [điểm/Part] [Chỉnh]   │
├──────────────────────────────────┤
│ [ Luyện nhanh / Luyện Part      ]│
│ [ Tự chọn Part • 1 câu • 10'    ]│
│                                  │
│ [ Thi thử Full Mock            ]│
│ [ 2 đề • 200 câu • 120 phút     ]│
├──────────────────────────────────┤
│ Gợi ý theo mục tiêu [Bỏ qua]     │
│ [Part nên ôn] [Chọn nội dung khác]│
├──────────────────────────────────┤
│ Bắt đầu     Tiến độ     Cá nhân  │
└──────────────────────────────────┘
```

Notes: same visible weight for two routes; no automatic mock launch; suggestion optional; use neutral 120-min copy only on full mock. `10'` is a *sample learner-selected duration*, not a prescribed time; copy can be `[Thời lượng bạn chọn]` in actual design.

## W-01B: Mode-centred start — pairs with IA-B, comparison only

```text
┌──────────────────────────────────┐
│ Chọn cách học hôm nay            │
├──────────────────────────────────┤
│ [ LUYỆN TẬP ] [ THI THỬ ]        │
│                                  │
│ Bạn còn [x] phút? [Đổi]         │
│ [Một câu] [Chọn Part]            │
│                                  │
│ [Xem trạng thái hai Full Mock]   │
├──────────────────────────────────┤
│ Luyện tập  Thi thử  Lỗi sai  ... │
└──────────────────────────────────┘
```

Notes: the content below mode selector must not make mock less discoverable or deceptively imply that one-question practice is a mock. Need test for four-destination crowding.

## W-02A: Reading U2-A — context return, two named views (recommended hypothesis)

```text
┌──────────────────────────────────┐
│ Part 7 • Câu [n]/[m]            │
│ [Đoạn văn]  [Câu hỏi]           │
├──────────────────────────────────┤
│ ĐOẠN VĂN                        │
│ [Toàn bộ passage có thể cuộn]    │
│ [Bảng / ảnh mở để xem đầy đủ]    │
│                                  │
│ [Quay lại câu hỏi [n]]           │
├──────────────────────────────────┤
│ [Tiến độ: Đã lưu / Đang lưu / !]│
└──────────────────────────────────┘
              ⇅ giữ vị trí đọc
┌──────────────────────────────────┐
│ Part 7 • Câu [n]/[m]            │
│ [Đoạn văn]  [Câu hỏi]           │
├──────────────────────────────────┤
│ CÂU HỎI [n]                     │
│ [A] ... [B] ... [C] ... [D] ... │
│ [Xem đoạn liên quan]            │
│ [Câu trước]       [Câu sau]     │
├──────────────────────────────────┤
│ [Lưu: đã xác nhận / đang chờ]   │
└──────────────────────────────────┘
```

**Invariant:** Return passage must restore *its previous useful position and the matching item group*; full tables and figures accessible; large text cannot clip content. **W-02A is not permission to add an arbitrary pause/replay to mock.**

## W-02B: Reading U2-A — anchored accordion alternative (same approved principle)

```text
┌──────────────────────────────────┐
│ Part 6/7 • Câu [n]/[m]          │
├──────────────────────────────────┤
│ [▾ Xem đoạn văn liên quan]       │
│ [Passage scrollable / full image]│
│ [Thu gọn đoạn]                  │
├──────────────────────────────────┤
│ Câu [n]                         │
│ A ○   B ○   C ○   D ○          │
│ [Mở lại đoạn tại vị trí cũ]      │
├──────────────────────────────────┤
│ [Trước]                   [Sau] │
│ [Đáp án: chờ lưu / đã xác nhận] │
└──────────────────────────────────┘
```

**Tradeoffs W-02A/B:** explicit tab switching reduces visible screen crowding but adds switches; accordion reduces view changes but may leave long scroll and awkward keyboard/font scaling. Both must be tested on two compact phone contexts later; neither is approved design.

## W-03A: Full Mock gate + contextual integrity (U3-A)

```text
┌──────────────────────────────────┐
│ Thi thử Full Mock — Đề [A / B] │
│ 200 câu • L ~45' / R 75'       │
├──────────────────────────────────┤
│ Để lượt thi đủ điều kiện so sánh│
│ • Không chủ động tạm dừng       │
│ • Không tua/nghe lại tùy ý L    │
│ • Gián đoạn có thể mất tính     │
│   so sánh, nhưng không xóa     │
│   đáp án đã xác nhận            │
├──────────────────────────────────┤
│ [Đã hiểu — Bắt đầu bài thi]     │
│ [Quay lại chọn chế độ]           │
└──────────────────────────────────┘
```

```text
┌──────────────────────────────────┐
│ Đề A  Listening • [thời gian]   │
│ [Đang phát audio] • câu [n]     │
│                                  │
│ [Câu hỏi/ảnh theo đề]            │
│ A ○   B ○   C ○   D ○          │
│                                  │
│ [Đang lưu…]  (KHÔNG 'Đã lưu')   │
│  ───── khi xác nhận ─────       │
│ [Đã lưu]                        │
│ [Xem trạng thái bài thi]         │
└──────────────────────────────────┘
```

During clean Mock, hide ordinary navigation chrome if it risks false exit or distraction, but preserve accessible truthful time, save and integrity info. No manual pause or arbitrary replay. Reading stage visibly has 75-minute period as approved, not a silently reset time budget.

## W-03B: Interruption and non-comparability — must be distinguishable

```text
┌──────────────────────────────────┐
│ ! Lượt thi bị gián đoạn          │
├──────────────────────────────────┤
│ Trạng thái: [KHÔNG SO SÁNH ĐƯỢC]│
│ [Lần lưu cuối đã xác nhận: ...] │
│ [Đang chờ lưu: ...]             │
│ [Thời gian / giai đoạn còn ghi]│
│                                  │
│ [Xem lựa chọn hợp lệ]           │
│ [Thoát / kết thúc không hợp lệ]  │
└──────────────────────────────────┘
```

**No claim** that every interruption always invalidates the attempt; its classification follows the approved material-integrity policy. Do not invent automatic continuation, silent time reset or lossless restore when it cannot be verified. The recovery and timeout threshold remain software test-plan TBD.

## W-04A: Results and practice feedback (U4-A)

```text
┌──────────────────────────────────┐
│ KẾT QUẢ LUYỆN [Part n]          │
│ Đúng / đã làm / bỏ trống        │
│ [Câu sai] [Câu chưa chắc]        │
│                                  │
│ Đáp án đúng: [đã kiểm duyệt]    │
│ Lời giải: [được QA / chưa có]  │
├──────────────────────────────────┤
│ [Luyện thêm Part này]           │
│ [Chọn Part khác]  [Kết thúc]    │
└──────────────────────────────────┘
```

```text
┌──────────────────────────────────┐
│ KẾT QUẢ FULL MOCK — Đề [A/B]    │
│ [Hoàn tất / Không đủ so sánh]   │
│ L: đúng [x]/100  R: [y]/100    │
│ Theo Part: ...                  │
│ [Không phải điểm ETS chính thức]│
│ [Giới hạn so sánh giữa hai đề]  │
│                                  │
│ [Xem lỗi sau khi nộp]           │
│ [Trở lại tiến độ]               │
└──────────────────────────────────┘
```

No correct key or explanation reveals during an ongoing clean Mock. `Câu chưa chắc` is a *wireframe wording candidate*, not a new user flagging feature; omit unless baseline enables such metadata, otherwise show only wrong/blank.

## Cross-cutting empty, error, blocked, privacy states (mandatory variants)

| Component / journey | Variant that must be explored | Never do |
|---|---|---|
| Answer | `Chưa chọn` → `Đang lưu` → `Đã xác nhận` or `Không xác nhận được` | Claim saved before acknowledged |
| Source readiness | `Không sẵn sàng`/`Đề đang được kiểm tra` | Present incomplete form as playable clean mock |
| Account | Own data / no cross-user history / verified deletion process | Reveal family member history without authorization |
| Connectivity | Explicit offline/unavailable + last known save; retry only if permitted | Promise offline-first behavior or silently forge save |
| Explanation | Verified explanation available / no vetted explanation | Invent answer explanation or call runtime AI |
| Timeout/quit | Distinct from normal submission and non-comparable | Show false clean complete result |
| Long Reading | No clipped passage, figure or table at larger text | Force permanent side-by-side on narrow phone |
| Feedback | After eligible practice / after submitted mock | Reveal key before full mock ends |

## Review checklist

- Are **both** practice and mock equally apparent at entry?
- Can a reader reliably return to the correct passage and previous position in Part 6/7?
- Does saved/pending/error language make sense without inventing storage technology?
- Are clean mock rules visible before starting, but not crowded during questions?
- Can a user distinguish raw score, valid attempt and non-comparable outcome?
- Are errors, deletion/privacy and withdrawn content states covered?
- What is untestable at low-fi and must wait for prototype/device testing?

**Explicit exclusion:** No colors, design-system components, final layouts, XML/Compose/Figma implementation, backend, database, API or code in these sketches. No paid tool/vendor usage.
