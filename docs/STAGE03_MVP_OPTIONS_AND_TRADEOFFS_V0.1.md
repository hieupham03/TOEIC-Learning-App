# TOEIC Learning App — WP-02 MVP Scope Options & Tradeoffs V0.1

**Date:** 2026-11-21  
**State:** **OPTIONS ONLY — Product Owner decision pending**. Not an approved MVP.  
**Prepared after:** Stage03 kickoff G03-KO-DEC-001 and WP-01 baseline.

## 1. Decision frame

The approved Vision expects Android L&R, a 4-week family pilot, flexible learning, personalization and credible progress evidence. The leading unproven value claim is convenience of using personal legally usable material in an integrated practice journey. The biggest blocking dependencies are content supply/rights, the audio–question–answer mapping and mock comparability. Compare three feasible *scope concepts*, NOT complete effort or price quotes.

## 2. Option A — Lean Practice Feasibility (pre-pilot)

**Purpose:** Verify one coherent Android practice journey with low content and operational burden. **This is a pre-pilot / smoke test, not a complete substitute for the approved 4-week progress-oriented pilot.**

**Candidate IN:**
- Android online practice in a small **verified** subset of Listening + Reading Parts, e.g. one each, using manually structured original/licensed items and correct audio.
- Answer selection, source-backed result review, error list/history, a short session, basic self-select.
- Private rights-aware content references / curated example items; no automatic imported-PDF ingestion.
- Basic learner data protection, operational logs and content corrections.

**Candidate OUT:** full 7-Part coverage, continuous 200-question Full Mock, mock score progress, AI, automatic PDF/audio import, personalized rule engine, advanced notifications, monetization, offline/iOS.

**Pros:** smallest content inventory and QA exposure, fastest to demonstrate core flow, lowest relative recurrent expense. **Cons:** cannot test the primary Vision success metric of comparable Full Mock progress; weak match for 'Android replacing PC' and the full pilot goal. Selecting A requires PO to explicitly label it pre-pilot, schedule a second scope decision and not represent it as completed family MVP.

## 3. Option B — Balanced Family Pilot (recommended conditionally)

**Purpose:** Support broad TOEIC practice and directional progress while bounding AI/import and operating costs.

**Candidate IN (all subject to content gates):**
- Android online practice spanning **all 7 TOEIC L&R Parts** with a modest but QA-verified item pool, including matched Listening audio, answer review, error history and basic Part-level feedback.
- Learner enters goal/current level and time available, chooses Part or receives **simple rules-based** next-activity suggestion; no claim of adaptive AI optimisation.
- Short one-question practice as an activity within the standard flow (not notification automation).
- **Two comparable and legally usable Full Mock forms** if legitimate supply and test-quality review can be demonstrated; transparently report raw correct/% and only defensible internal scoring. **Never imply official ETS score/990 conversion.** One form alone is insufficient as strong evidence of score improvement across the four-week pilot.
- A **manually curated, controlled content library** (source provenance, permissions, structured question/audio/answer links) drawn only from original/licensed/permitted material. If personal PDF cannot be lawfully or accurately converted, do not ingest/rehost it; use a valid source fallback.
- Minimal privacy protections and a measurable pilot OPEX budget; user-controlled content correction path.

**Candidate OUT initially:** general automatic PDF/audio importer; AI-generated answers and recommendations; custom question-generation service; interactive multi-action vocabulary notifications; offline, iOS, ads/subscriptions and cloud sharing of unverified third-party content.

**Critical dependency:** This option is **not ready for final MVP approval merely by choosing B**. Before a binding feature baseline, PO must see a plausible/legal inventory for all 7 Parts and *at least two comparable mock forms*; otherwise reduce/revise B openly (e.g., run pilot on Part-level diagnostics without TOEIC-score improvement claims) via a follow-up scope amendment. No silent de-scoping of Full Mock.

**Pros:** closer to Vision and user preferences; tests a coherent value loop while avoiding costly/uncertain AI/auto-ingestion. **Cons:** significant curated content and QA effort; risk to 4-week pilot if reliable full forms unavailable; even with two forms, changes in score may reflect form difficulty or practice effects.

## 4. Option C — Extended AI & Personal Library Bet (high uncertainty)

**Purpose:** Pursue the differentiated feature set in a single scope, subject to explicit technical/legal proof.

**Candidate IN:** all Option B capabilities plus wider content coverage, proposed PDF/audio extraction and review workflow, possible AI explanation/question quality-checked against a reference set, richer diagnostics/spaced review, configurable vocabulary notification controls, and increased automation for personalized content selection.

**Risks:** unknown ingestion reliability across PDF scans/audio formats, legal rights for cloud/AI handling, hallucinations and ongoing token costs, Android notification limitations, content production burden, multi-month integration/testing complexity. **Extra features do not prove better learning outcomes.**

**Decision:** **Not recommended for the first low-OPEX family pilot** absent a separated proof-of-feasibility with trusted sample files and auditable rights. Choosing C means a *research-heavy proposed scope*, not authorization to promise PDF automation or implement AI.

## 5. Capability comparison (✓ proposed, – absent, ◐ limited/conditional)

| Capability | A Lean pre-pilot | B Balanced family pilot | C Extended |
|---|---|---|---|
| Android + online-only | ✓ | ✓ | ✓ |
| Listening + Reading practice | ◐ 1–2 sampled Parts | ✓ all 7 Parts, limited QA-ed set | ✓ expanded |
| Audio mapped to question/answer | ✓ sampled | ✓ required per Listening content | ✓ extended |
| Learner chooses Part/time | ◐ | ✓ | ✓ |
| History/error review | ◐ basic | ✓ Part-level | ✓ richer |
| Activity recommendation | – | ✓ rule-based | ◐ advanced AI proposal |
| Full Mock 200 items | – | ◐ 2 rights-clear comparable forms gate | ◐ wider bank and scoring gates |
| Personal library | ◐ catalog/references | ◐ controlled manual curation | ◐ import automation subject to feasibility |
| One-question quick practice | ◐ | ✓ in-app | ✓ plus potential notifications |
| Interactive vocabulary notifications | – | – | ◐ opt-in and feasibility |
| AI explanations/generation | – | – | ◐ eval/rights/cost gates |
| Pilot OPEX | Lowest (relative) | Low–medium (relative, unknown amount) | Higher and uncertain |
| Content curation burden | Low | Medium–high | Very high |
| Fit with four-week family pilot | Low / pre-pilot only | Highest if content gate passes | High scope risk |

## 6. Recommendation & why it is conditional

**Analyst recommendation: OPTION B, CONDITIONAL**. It best preserves the two critical learner jobs—full practice on Android and progress tracking—while excluding unvalidated auto-import and AI, and still includes personal-library value through controlled structured content. However, **B has a HARD CONTENT GO/NO-GO**: source rights and QA-ed all-7-Part coverage and mock test forms must be plausible before PO locks the MVP. If supply fails, ask PO to revise scope explicitly rather than invent tests or claim the pilot measures scores. A is an appropriate preliminary proof only; C should be separated as a future research program.

## 7. Gating criteria by option

| Gate | A | B | C |
|---|---|---|---|
| CP-03 provenance/licensing | Required for every used item | Required for all content, tests and any family sharing | Required plus AI/cloud/third-party pipeline rights |
| CP-04 answer/audio QA | Essential small set | Essential across 7 Parts and Full Mock | Essential plus automation metrics |
| Q-MOCK comparability | Not applicable; no score claim | Mandatory before score-delta claims; compare forms, not official-scale | Same, higher scope |
| Q-IMPORT accuracy | Out of scope | Manual structured content; no automated importer promised | Representative-file spike and verified accuracy before commitment |
| Q-AI | Out of scope | Out of scope | Human review, eval, token cap, opt-out/fallback |
| Q-ANDROID long Reading | Basic check | Mandatory long Part 7 and 120-min recovery criteria | Same plus more feature interactions |
| Q-COST pilot | Simple spending log | Numeric cost ceiling and content budget from PO prior to implementation | Detailed recurring-cost sensitivity estimate needed |

## 8. Decision points after selection (do not ask serial 20+ questions)

1. **Choose A / B / C / customized** as the *direction for drafting requirements*. Choosing it does not approve an MVP baseline, PRD/SRS, architecture or code.
2. In WP-03 and WP-04, receive one **combined content & quality feasibility pack** before binding all-7-Part or 2-mock commitments (source status, rights, score labels, fallback, operational cost).
3. Review a single **PRD/SRS draft + in/out scope decision + acceptance** package and explicitly approve or amend.

## 9. Evidence and limitations

**Official format:** ETS: https://www.ets.org/toeic/about/listening-reading.html . **Existing workflow benchmark:** STUDY4 (https://study4.com/posts/4447/); Migii (https://migii.net/vi/toeic). **IP rule:** Google Play (https://support.google.com/googleplay/android-developer/answer/18265346?hl=en). Stage 02 evidence (https links plus user self-report) is recorded in `STAGE02_EVIDENCE_SOURCE_LEDGER_V1.0.md`. No existing competitor feature demonstrates this application's accuracy, licensing or demand for automatic uploads.
