# D05-ECP00-008 — Separate Product Owner Decision on ECP-00 Evidence Policy Review V0.1

**Status:** PENDING PO. **Not** a technical architecture or testing decision.  
**Previous binding approval:** `D05-EVIDCP-007=A` approved ECP-00..06 **PLAN ONLY**.  
**Reviewed as proposed materials:** `STAGE05_ECP00_POLICY_AND_EVIDENCE_CONTRACT_REVIEW_BRIEF_V0.1.md`, `STAGE05_ECP00_PENDING_POLICY_REGISTER_V0.1.md`, `STAGE05_ECP00_SEPARATE_AUTHORIZATIONS_AND_STOP_CHECKLIST_V0.1.md`, `STAGE05_ECP00_EV_FM_POLICY_DEPENDENCY_BRIDGE_V0.1.md`.

## One decision — explicitly separate policy protocol from unresolved values

| Option | Exact effect of a future PO signature | Still withheld |
|---|---|---|
| **A — APPROVE ECP-00 REVIEW PROTOCOL ONLY (recommended)** | Accept the **document-only ECP-00 policy-review method**: inherited vs pending policy classification, 16-question register, evidence-admissibility contract, stop/hold semantics, equal A/B/C burden and dependency bridge. Treat this as a controlled review protocol; allow **preparing** a separate, concrete future policy-values / scoped-execution decision pack when ready. | No numeric grace/skew/time parameters, clock authority/precedence, durable-ACK source, framework/backend/API/DB, architecture selection, running ECP-00..06, Android/user/content tests, ARCH-04, Stage05 Gate, code/POC or spending |
| **B — AMEND** | Return one consolidated correction to the ECP-00 policy-review proposal before any signoff | Keep plan approval only, policies undecided, all real work prohibited |
| **C — HOLD** | Keep ECP-00 packet as draft without approving its review protocol | Same prohibitions; no impact on already approved D05-EVIDCP-007 plan |

## Why A can be approved without making unauthorized architecture decisions

This packet **does not offer competing clock authorities or invented numeric performance thresholds**; insufficient M3/M4 evidence makes such a selection premature. It lets PO approve **how future evidence claims must be substantiated**, while explicitly keeping **what thresholds/sources qualify** as a future, separable decision. A would **not complete substantive ECP-00 policy calibration**, authorize ECP-01..06, select A/B/C, or change the signed product policy. No new burden to re-inventory two B1 Full Mocks, reconfirm source rights, or reopen deferred budget.

## Locked interpretation regardless of option

- Signed Vision V1.0, Requirements PRD V0.6/SRS V0.6/Acceptance V0.4, Design V0.3 and UI-G01..16 unchanged; strict Full Mock and durable-ACK rules continue.
- EV01..12 DOCUMENT REVIEWED, no verified app claims; FM01..18 NOT RUN, QA01..08 no actual PASS; Android/learner n=0.
- CP01..05, G03-CP01..07, G04-CP01..08 remain ACTIVE; UX04-I01..08/UIA-01..08 OPEN/PARTIAL.
- ARCH03-A/B/C, 16 technical domain alternatives all UNSELECTED. Stage05 IN PROGRESS; ARCH-04/Gate not opened; **all budget work DEFERRED**.

## Ready-to-use Product Owner responses (not prior authorization)

- **A:** “Tôi, Product Owner, PHÊ DUYỆT D05-ECP00-008=A: chấp thuận **ECP-00 Policy & Evidence Contract Review Brief V0.1** và ma trận chính sách/điều kiện chứng cứ **chỉ như quy trình đánh giá tài liệu**; POL-01..16 tiếp tục mở ở phần cần chọn giá trị/nguồn bằng chứng. Chỉ cho phép chuẩn bị gói quyết định chính sách cụ thể tiếp theo nếu cần; chưa phê duyệt clock authority, ngưỡng thời gian, nguồn ACK, kiến trúc, kiểm thử/QA, ARCH-04, code/POC hay chi tiêu. Giữ nguyên toàn bộ baseline, B1, CP, QA và ngân sách DEFERRED.”
- **B:** “Tôi chọn D05-ECP00-008=B: yêu cầu chỉnh tài liệu ECP-00 trong một lượt, chưa phê duyệt giao thức hay chính sách thực thi.”
- **C:** “Tôi chọn D05-ECP00-008=C: HOLD. Giữ D05-EVIDCP-007=A đã phê duyệt kế hoạch, ECP-00 ở trạng thái đề xuất, không thực thi hay thiết kế/code.”

**Current:** This `D05-ECP00-008` decision **PENDING**. D05-EVIDCP-007=A is already APPROVED as a checkpoint plan, not policy or execution.
