# D05-ARCH-002 — Feasibility Investigation Direction — One-Packet PO Decision V0.1

**Project:** TOEIC Learning App  
**Prepared:** 2026-11-21  
**Stage05:** IN PROGRESS; ARCH-01 document/evidence mapping complete.  
**PO decision status:** **PENDING**.  
**Only authority requested:** authorize/adjust **ARCH-02 feasibility comparative RESEARCH**, NOT choose a technical architecture or create an implemented POC.

## 1. Findings brought to this decision

- 16 material architecture drivers (AD-01..16) extracted; 19/19 MVP FR and 13/13 NFR trace to drivers and acceptance/governance checkpoints.
- 16 evidence gaps EG-01..16 and 10 contradiction watchpoints CW-01..10 recorded; no item marked TEST PASS.
- Strict 120-minute mock integrity + audio, durable answer ACK, family data isolation/deletion and validated content are **P0 obligations** for pilot, not proof that any particular technology is suitable.
- The two PO-inventoried Full Mock A/B forms remain mandatory; do not re-ask inventory or source rights. No budget, framework or hosting choice is required to make this research-direction decision.

## 2. Grouped alternatives

### A — APPROVE research direction: Integrity-first comparative study (ANALYST RECOMMENDATION)

Authorize **ARCH-02 ONLY AS DOCUMENT-BASED FEASIBILITY COMPARISON** with ranked questions:

| Priority | Study objective (not a design choice) | Feasibility evidence the analyst must bring back |
|---|---|---|
| 1 | Full Mock time/audio/attempt integrity, process death and interrupted validity | Alternative *conceptual responsibility models*, falsifiable failure cases, source-backed platform constraints, trade-off matrix against BR-01..04 |
| 2 | Confirmed answer durability, ambiguous retry and learner isolation/deletion | Alternative *trust/evidence models* and their risks, no premature DB/API/cloud selection |
| 3 | QA-ready form/content/version, practice isolation and raw scoring correction history | Source/version/failure matrix, QA checkpoint ownership without claiming audits complete |
| 4 | Reading/context restoration, accessibility and pilot feasibility | 2-device verification criteria, UX04/UIA open risks, evidence due |

**Deliverable:** a single options-and-tradeoffs decision pack showing at least two meaningful alternatives per material question, evidence/unknowns and recommended **direction for further architecture candidate development**. No option becomes binding until a **separate future PO technical choice decision**. If research uncovers a direct conflict with a signed baseline, submit change impact instead of silently weakening it.

### B — APPROVE research direction: Balanced parallel comparison

Permit ARCH-02 desk research across **four axes at equal depth** — Mock integrity, data/privacy, content/scoring and device/UX — with a comparative matrix returned as one bundle. **Benefit:** broad early coverage. **Trade-off:** less depth on the pilot's most sensitive trust semantics in the first pass.

### C — APPROVE research direction: Content/device feasibility first

Permit ARCH-02 to research content release/version integrity, audio mapping and Reading/accessibility first, then examine Mock timing/ACK/privacy in a clearly scheduled second pass **before any later architectural selection**. **Benefit:** surfaces corpus and device constraints early. **Risk:** most sensitive time/data integrity questions remain open longer.

### D — AMEND the study brief

Product Owner revises study prioritization or boundaries in one pass. **ARCH-02 remains on HOLD until amended direction is explicitly approved.** No changed business scope inferred.

### E — HOLD

Retain Stage05 IN PROGRESS with ARCH-01 complete; do not authorize ARCH-02. Baselines, CPs, QA and budget deferral unchanged.

## 3. Strict authorization fence for A/B/C

This next approval would grant **research/comparison and writing only**, not permission to implement, choose stack/framework, draw a definitive system architecture, select auth/database/backend/cloud provider, write API/schema/code, run POCs, consume funds, scrape or publish the content bank, or call requirements/QA PASS. Later PO review is compulsory for material technical decisions. Preserve UI-G01..16, UX04/UIA open issues, the two Full Mock forms and signed retention/deletion limits.

## 4. Owner-facing decision text

- **A (recommended):** `Tôi, Product Owner, PHÊ DUYỆT D05-ARCH-002 = A: cho phép ARCH-02 nghiên cứu so sánh tính khả thi theo thứ tự integrity-first đúng Decision Pack V0.1. Chỉ nghiên cứu tài liệu và chuẩn bị các phương án/đánh đổi, chưa lựa chọn công nghệ, kiến trúc, backend, API, DB, cloud, không viết code/POC, không chi tiêu; mọi quyết định kỹ thuật quan trọng phải trình tôi duyệt riêng. Giữ nguyên các baseline, B1, CP, QA và ngân sách DEFERRED.`
- **B:** `Tôi, Product Owner, PHÊ DUYỆT D05-ARCH-002 = B: cho phép ARCH-02 nghiên cứu tài liệu bốn trục với mức ưu tiên tương đương; không chọn công nghệ/kiến trúc hoặc code, mọi ràng buộc giữ nguyên.`
- **C:** `Tôi, Product Owner, PHÊ DUYỆT D05-ARCH-002 = C: cho phép ARCH-02 nghiên cứu tài liệu về content/media/Android trước, nhưng vẫn phải so sánh đầy đủ timing, save và privacy trước bất kỳ quyết định kiến trúc. Không chốt công nghệ hoặc code.`
- **D:** `Tôi chọn D05-ARCH-002 = D: AMEND brief; yêu cầu trình một bảng chỉnh sửa gộp. ARCH-02 chưa được phép bắt đầu.`
- **E:** `Tôi chọn D05-ARCH-002 = E: HOLD ARCH-02; giữ ARCH-01 đã hoàn thành hồ sơ, Stage05 đang thực hiện, chưa kiến trúc/code.`

**No implicit approval:** Stage05 Gate is not being decided now. `D05-ARCH-002` alone concerns the permissible *scope and priority of further feasibility investigation*.
