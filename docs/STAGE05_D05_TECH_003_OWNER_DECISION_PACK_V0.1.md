# D05-TECH-003 — Separate PO Decision on Integrity Evidence Research Direction V0.1

**Project:** TOEIC Learning App — Stage05 Technical Feasibility & Architecture  
**Presented:** 2026-11-21  
**Status:** **PENDING PO — NOT YET APPROVED**  
**Predecessor:** `D05-ARCH-002=A` approved Integrity-first **document research only**; ARCH-02 resulting evidence register, comparative matrices and falsifiable negative cases available.  
**This decision is NOT Stage05 Gate, final architecture, or technology selection.**

## I. What can reasonably be decided with present evidence

ARCH-02 found multiple plausible conceptual models for timing, audio, data persistence, privacy, content-version and raw scoring; **none has been tested as a system**. The only safe selection today is which **evidence-responsibility family to prioritize for later approved architecture-option evaluation**, with alternative models retained as comparators. No framework/backend/API/database/server/client clock authority is preselected.

Signed constraints that CANNOT change in this decision: two B1 200-item Full Mocks, 100 L/~45m +100 R/75m, no arbitrary clean-mock pause/replay, honest noncomparable classification, answer ACK truthfulness, learner isolation, deletion ≤7 calendar days, ordinary retention ≤30 days after pilot, source/version QA, raw score interpretation, controlled Design Baseline, existing CP/QA/budget-deferred controls.

## II. Single grouped choice (avoid multiple serial PO approvals)

| Choice | Research/reference shortlist emphasis | What it authorizes if PO approves | Trade-off / risk | Analyst view |
|---|---|---|---|---|
| **A — Evidence reconciliation first** | Prioritize comparison of independent continuity/ACK evidence, explicit uncertainty and contradiction handling; retain device-contained and separately corroborated models as challengers | Develop an **approved next-step evaluation brief only** describing what further architectural options would have to prove | More conceptual complexity and no guarantee feasible under network outages | **RECOMMENDED for next research direction, not a chosen architecture** |
| **B — Device-contained proof first** | Prioritize minimal live connectivity dependency in the evidence model; strict invalidate/unknown when continuity cannot be shown | Same limited evaluation-brief authority | Reboot/tampering/shared-device trust and deletion risks remain major blockers | Acceptable only if those risks are not silently waived |
| **C — Independent corroboration first** | Prioritize independently retrievable continuity/answer confirmation with explicit outage-invalidity scenarios | Same limited evaluation-brief authority | Availability, privacy and response-latency trade-offs untested | Conditional alternate |
| **D — AMEND** | PO adjusts model emphasis, required evidence or constraints | No study change until approved amendment | Extra review | Available |
| **E — HOLD** | Preserve completed ARCH-02; no new technical direction | Nothing further | Study remains descriptive | Available |

**IMPORTANT:** Approval of A/B/C does **NOT** approve any chosen technology, database, backend, API, clock placement, architecture component diagram, prototype implementation, POC, deployment or code. If PO later wants actual architecture candidates, an additional explicit authorization (`D05-ARCH-004`, proposed ID only) must authorize that separate activity first. No hidden automatic execution.

## III. Recommended safeguard / follow-on obligations

- Preserve T-A/T-B/T-C, S-A/S-B/S-C, P-A/P-B/P-C and C-A/C-B/C-C as documented alternatives. Mark **NOT TESTED**.
- Do not set numeric recovery/clock/network/latency thresholds in ARCH-02. The signed acceptance catalogue requires later AC-08 test-plan checkpoint for such thresholds.
- A future architecture option comparison must include failure-mode coverage FM-01..FM-18 and constraints AD-01..AD-16, EG-01..EG-16, CW-01..CW-10.
- Any baseline conflict goes through controlled PO change request, not an implicit research selection.
- No spending and no reopening budget discussions before PO explicit separate instruction.

## IV. Exact PO decision examples

- **A (recommended):** `Tôi, Product Owner, PHÊ DUYỆT D05-TECH-003 = A: chọn hướng nghiên cứu ưu tiên evidence reconciliation, có cơ chế đánh dấu không chắc chắn và kiểm chứng đối chiếu, đồng thời giữ các mô hình đơn nguồn/độc lập làm phương án đối chứng. Chỉ cho phép hoàn thiện brief đánh giá kỹ thuật cho quyết định sau, chưa phê duyệt kiến trúc, clock authority, framework, backend, API, database, code/POC hoặc chi tiêu. Giữ nguyên mọi baseline, B1, QA, CP và ngân sách DEFERRED.`
- **B:** `Tôi PHÊ DUYỆT D05-TECH-003 = B: ưu tiên nghiên cứu evidence device-contained, với rủi ro reboot/tampering, privacy và unproven continuity bắt buộc kiểm chứng; chưa duyệt kiến trúc/code.`
- **C:** `Tôi PHÊ DUYỆT D05-TECH-003 = C: ưu tiên nghiên cứu independently corroborated evidence với outage/privacy/latency risks cần kiểm chứng; chưa duyệt kiến trúc/code.`
- **D:** `Tôi chọn D05-TECH-003 = D: AMEND; trình một bảng điều chỉnh tổng hợp. Không tự triển khai bước kế tiếp.`
- **E:** `Tôi chọn D05-TECH-003 = E: HOLD; không lựa chọn hướng kỹ thuật, không ARCH-03/code.`

**Owner signature required separately.** No further research, design or implementation begins solely from this pending decision pack.
