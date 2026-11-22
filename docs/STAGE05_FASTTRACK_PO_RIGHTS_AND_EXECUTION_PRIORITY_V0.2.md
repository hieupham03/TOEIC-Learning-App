# Stage05 Fast Track — PO Rights/Legal Attestation and Execution Priority V0.2

**Status: CURRENT PO DIRECTION RECORDED — 2026-11-22.**

**Exact latest PO instruction:** "đẩy nhanh tiến độ nhưng vẫn đảm bảo tuân thủ các bước, đặc biệt hãy bỏ qua các vấn đề về bản quyền vì tôi đã xử lý mọi vấn đề bản quyền, pháp lý 100%".

**Authority interpretation:** The PO explicitly declares that copyright/legal rights to the relevant source materials have been fully handled. Treat this as an **owner attestation**; do **not** send the PO through repeated generic copyright research, licensing checklists, vendor emails, payments or re-approval of existing rights. This replaces the earlier *operational* copyright-discovery/reconfirmation queues for the Fast Track. It does not claim the engineering agent independently saw an asset-specific contract, nor does it waive platform terms, access controls, privacy, correctness, content-quality testing or any other approved stage gates.

**Precedence:** On branch `development/fasttrack-48h-preview`, use this *latest PO workflow guidance* for engineering task prioritization if older Fast Track documents demand repetitive copyright research/proof before building; retain all unrelated earlier controls. Do not rewrite older approval records, baseline policies or invent asset-level permissions.

## Two deadline-driven deliverables

**P0 by 2026-11-24:** a stable offline Android APK for **two consenting internal preview users**, with useful Listening and Reading DEMO flows, clear feedback, no P0 crash/incorrect mapping and true state labels. Prefer functional, small-scope product over 400 unverified questions, cloud/backend, accounts or speculative architecture.

**P1 by 2026-12-06:** Google Play *Internal/Closed Testing* submission-ready AAB and policy/privacy/asset checklist, Android targetSdk 36+ as required for new mobile apps. Actual store upload/Production requires the account owner to act/approve and platform eligibility to be satisfied; no promise of public release.

## No more rights-research loop — operational handling

- Accept `PO_RIGHTS_CONFIRMED` for **scope planning** for the sources already named in D03-WEB-SOURCE-003, including Zenlish/TheTOEICLab/Study4. No new rights-only web searches, contract procurement, or legal debate requested by Codex.
- Keep minimal **technical provenance**, not a legal audit: source group ID, item ID, URL, source version, local file hash, and PO declaration record. This is needed to debug audio–question mismatches, version/duplicates and response to store inquiries, not to challenge PO authority.
- **Local engineering/preview:** Codex may test and normalize the PO-sourced four Zenlish sample groups in **gitignored local storage** for the two-user demonstration. Content **with unverified keys** must be distinctly `DEMO / CHƯA QA`, without scored right/wrong claims. If technical audio mapping and decoding verify, a source-aware private preview loader can be prepared; do not upload extracted raw source media/questions to a **public Git repository**. A private locally assembled preview-only binary with PO-declared content may be evaluated technically under this Fast Track instruction, but must label unverified content and not imply verified answers or clean Full Mock. Codex must respect Android file/app-private storage, security and test evidence; this is not a public release gate waiver.
- **Production and public distribution:** still verify that the exact distributed assets match the PO-owned material using IDs/hashes and that app-content QA and store disclosures are accurate. A separate owner attestation may satisfy ownership declarations; **Codex should not demand another generic license investigation**. If Play Console asks for proof, the owner supplies it through their account; never invent evidence.
- Never bypass login/CAPTCHA/HTTP blocks/robots or other computer-access controls, regardless of content ownership. Stop live crawling outside already approved finite batch; concentrate on Android engineering.

## Critical quality gates retained (mandatory)

1. Correct audio–group/item association; playable media format and proper end/error/replay behavior; output verification; image for Part1; no lost selection.
2. Answer keys are currently **unverified for 8 scraped questions**. Do not generate or guess answer keys, auto-grade the live questions, or mark the real Listening bank QA_READY without actual checks. Prefer unscored sample practice or controlled original synthetic answers for the two-user preview.
3. Full Mock A/B still requires independent 200+200 content inventory/QA and timed/saved-integrity criteria; do not silently unlock it. Stage05 is CONDITIONAL Development, G05-CP01..08 active, POL01..16 open, no formal QA/ECP claim and no pilot/release claim.
4. Test build, offline usability, accessibility, local data behavior/clear action, Android version and 2 actual user installations before claiming two-person readiness. Formal QA, privacy/Data safety and actual Play eligibility cannot be bypassed.
5. No paid dependency, server, account, production clock, remote durable ACK, vendor contract or store publication without separate material approval. Budget stays DEFERRED.

## Codex execution simplification

Run **ONE autonomous FAST-01+02 engineering session**, then one consolidated FAST-03+04 release-preparation session. Each session: implement -> self-check -> repair P0/P1 -> rerun tests -> report truthful PASS/FAIL/BLOCKED -> commit/push. Avoid extra policy memos and microapprovals. Ship safe partial value when blocked rather than waiting indefinitely. Stop at the approved boundary.

**Success** = genuine functional APK with evidence by Nov 24 and genuinely store-ready test-track package by Dec 6; do not equate a date target with actual QA/Play Production approval.
