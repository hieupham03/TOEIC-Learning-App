# Stage 03 — Pilot Cost & Effort Sensitivity Scenarios V0.1

**2026-11-21. Trạng thái:** ANALYST ILLUSTRATIONS, NOT A QUOTE, NOT A STACK/BUDGET APPROVAL.  
**Phạm vi mô phỏng:** Android online; family pilot 2–5 người, 4 tuần, không AI runtime, không auto-import PDF; chưa chọn nhà cung cấp. Chi phí tiền mặt và công sức phải hạch toán riêng.

## 1. Verified publicly posted prices / quotas (not vendor selection)
- Google Play Console: **US$25 one-time** account registration, chỉ phát sinh nếu mở tài khoản mới / dùng Play distribution. Với tài khoản cá nhân mới từ 13/11/2023, public production cần closed test **>=12 người, >=14 ngày**; *internal testing* hỗ trợ tối đa **100 tester**, do đó nhóm 2–5 có thể dùng cho pilot qua Play Console mà không đồng nghĩa đủ điều kiện ra public.
- Cloudflare R2 Standard: **10 GB-month storage, 1M write ops, 10M read ops free/month**; outbound egress to Internet không tính phí data transfer đối với standard, nhưng phí xử lý khác/provider khác vẫn cần xét. Không chọn R2 ở Stage03.
- Firebase Spark: free quotas một số thành phần như Auth, Firestore; một số tính năng cần Blaze/billing và Storage có điều kiện. Không coi toàn bộ tổ hợp Firebase lưu/stream ảnh+audio là miễn phí.
- Amazon Polly neural TTS: **US$16 per million billable characters** ngoài free credit/tier; bài audio cần TTS tự nhiên và kiểm duyệt nội dung. Ví dụ 100,000 characters = **US$1.60** tiền tổng hợp *theo bảng giá chỉ riêng TTS*, chưa kể dịch vụ, biên tập, chất lượng, asset licensing, ngoại tệ/thuế.
- ETS published TOEIC Test Sample Questions+Answer Key: **US$1,500 electronic** (1 năm theo quy định licensing, chưa thuế/country fees), KHÔNG cấp hai Full Mock. Giá được dẫn để **tránh sai lầm nghĩ có thể mua 400 câu ETS bằng phí nhỏ**; không phải khuyến nghị mua.

## 2. Transparent hypothetical workload
**SCENARIO A (pilot 5 người):** 5 học viên x 5 phiên/tuần x 4 tuần x 15 MB audio tải/phiên = **1,500 MB (~1.5 GB)** truyền trong 4 tuần; nội dung giả định 2 GB lưu trữ; đọc câu hỏi vài nghìn đến vài chục nghìn lượt. Đây là giả định minh họa, **không phải lưu lượng thực tế hay dự báo chi phí cloud đầy đủ**. Với một số free quotas, riêng storage/object reads có thể không tính phí; API/backend/backup/monitoring/egress từ nhà cung cấp khác có thể phát sinh. 

**SCENARIO B (2 Full Mock hoàn toàn tự biên soạn):** 400 câu x [10–30 phút biên soạn/câu + 5–15 phút QA/câu] = **100–300 giờ** *minh họa* (không bao gồm thu/biên tập audio, tạo ảnh, đoạn văn dài, tái kiểm nghiệm hoặc tích hợp). Đây KHÔNG phải số liệu ngành, KHÔNG phải estimate cam kết, và AI/Codex code assistance không thay việc QA học thuật.

**SCENARIO C (mua bản quyền):** License phải cho app/cloud/user group/territory/derivative/commercial tương ứng; chi phí = `vendor_quote + license_review + metadata_conversion + QA + ongoing royalties if any`. **Chưa có báo giá đủ điều kiện, nên phải để TBD, không bịa giá.**

## 3. Budget boundary to decide — NOT YET SET
| Cost bucket | Measurable basis | Evidence | Proposed control |
|---|---|---|---|
| One-time content licensing | Quote/contract/territory/allowed users | UNKNOWN | PO approves cap before any purchase |
| Original authoring | hours x agreed rate or volunteer hours | UNKNOWN; hypothetical above | Timebox by approved content inventory |
| Audio/graphics | TTS characters or recording hours, photo/image licenses | TTS list price known, workload unknown | Source ledger + review + hard allowance |
| Storage/media transfer | GB-month, read ops, egress | Provider quotas known, architecture UNKNOWN | quota and billing alerts when chosen |
| Backend/auth/DB | active users, reads, writes | free tiers exist but vendor unknown | No-cost candidate must meet quality/security |
| AI runtime | tokens x price | Candidate B excludes runtime AI | **Budget=0 only if not implemented**, not promise without scope lock |
| Release | Play Console / testing policies | US$25 one-time if new Play account | Separate from 4w OPEX |
| QA/device/backup | personnel, devices, data restoration | UNKNOWN | Explicit labor accounting and test plan |

**Cost formula:** `TCO = content_license_once + authoring_QA_effort + audio_image_rights + 4w_hosting_operations + distribution_one_time + contingency`.  
**Unapproved caps:** `BUDGET_CONTENT_ONE_TIME_MAX_VND`, `BUDGET_OPEX_MAX_VND_4W`, `BUDGET_CONTENT_QA_HOURS_MAX`. No vendor/paid cloud may be assumed approved. Default plan should be **no AI calls**, **no unaudited content uploads** and **no purchase without PO**.

## 4. Three decisionable cost paths
| Path | Likely cash infra | Hidden effort | Content availability | Risk |
|---|---|---|---|---|
| LOW-CLOUD / original small practice bank | Could fit no-cost provider quotas | High manual authoring/QA | Moderate for small bank, not 2 mocks | Scope mismatch with primary score KPI |
| FULL-B / 2 original independent mocks | Cloud still potentially low | **Very high content authoring, audio, QA** | Not presently produced | Delay/quality risk HIGH |
| LICENSED-B / partner 2 forms+practice | Infra still potentially low | Contract/licensing + QA/integration | No validated quote | Commercial/legal risk HIGH |

**Key takeaway:** infrastructure plausibility ≠ feasibility for two mocks. Quantity and rights determine schedule/money. No reliable official full-mock vendor quote was found in reviewed public sources.

## Sources, checked 2026-11-21
- Play fee: https://support.google.com/googleplay/android-developer/answer/6112435
- Play new personal account testing: https://support.google.com/googleplay/android-developer/answer/14151465
- Internal testing: https://support.google.com/googleplay/android-developer/answer/9845334
- Cloudflare R2 Standard: https://developers.cloudflare.com/r2/pricing/
- Firebase Spark/Blaze: https://firebase.google.com/pricing
- Amazon Polly Neural: https://aws.amazon.com/polly/pricing/
- ETS TOEIC rights/licensing: https://www.ets.org/legal/permissions/licensing.html
