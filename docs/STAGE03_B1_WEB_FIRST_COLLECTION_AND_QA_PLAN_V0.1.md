# B1 Web-First Content Acquisition and QA Plan V0.1

**Status:** Proposed research/requirements plan. NOT implementation instruction, crawler approval or software design.

## Goal
Find sufficient rights-cleared English test material for **two separate TOEIC-style 200-item forms** plus a distinct Part practice bank, without doing more manual baseline studies and without bulk creating 400 items unnecessarily.

## Single-batch workflow
**Gate 0 — Find:** Collect source URLs via public research and any PO-identified sites; log title, owner, cost, media types, 7-Part coverage and apparent license. Do not harvest questions merely because public.

**Gate 1 — Rights and access:** For every candidate website, record the PO's claimed rights basis, original copyright holder, actual agreement/license, site terms/authorized export or API, and intended pilot/public uses. Question/media rights can differ. Exclude ordinary personal-use services absent separate permission. Do not attempt to bypass paywalls, CAPTCHAs, access controls or bot restrictions.

**Gate 2 — Content inventory:** When legally cleared, establish manifest with Form A 200Q + Form B 200Q, IDs and cross-form duplicate checks. Check Part composition 6/25/39/30/30/16/54 each. Keep practice content separate so learning does not contaminate mock measures. No item is counted merely by URL presence.

**Gate 3 — Quality:** One content reviewer checks 100% keys/audio/figures/text/source provenance, flags ambiguity and invalid media; a second independent review on higher-risk material and a sampled difficulty comparison. Both mock forms must be internally coherent. Do not claim ETS scaled 10–990 equivalence unless supported by appropriate psychometric evidence.

**Gate 4 — Cost:** Estimate only after source scope known: one-time right cost (if any), conversion labour, independent QA hours, missing media/audio production, storage and egress four-week 2–5-person pilot, contingency. Keep content/operational/hour caps as PO approval items.

**Gate 5 — Decision:** Present a **single MVP readiness packet** listing source counts by Part, rights evidence, QA result, A/B mock separation, distinct practice bank and itemised cash/hour exposure. Propose PASS/CONDITIONAL/HOLD; do not change B1 unilaterally.

## Fast-path if the PO owns rights to the web content
If the PO is original rights owner or holds valid sublicensable rights, seek **owner-supplied original export / official downloadable file / approved API** first. This is generally simpler and more reliable than extracting rendered pages, and reduces media mapping errors. Any crawler would be an implementation decision at a later, expressly authorized stage.

## Current gate assessment
- G-SOURCE: RED (no two 200Q manifests evaluated).
- G-RIGHTS: AMBER on PO rights attestation, not independently demonstrated source-by-source; no GREEN rights-clear forms yet.
- G-MOCK: RED (zero validated complete forms as of this record).
- G-QA: RED (no reviewed items).
- G-COST: RED (no PO ceilings and source-specific conversion costs).
- G-PRACTICE: RED (no independent approved practice inventory).
- G-ANDROID: AMBER (phone Reading scroll and eyestrain risks from prior PO self-report).
- MVP LOCK: HOLD. No shortcuts or presumptions of illegality.

## Information that would materially speed inventory (when convenient, all at once)
Up to **3–5 URLs/domains** of websites PO meant, and which are PO-created/authorized or covered by specific agreements; alternatively a list of source titles. Do not request files or multi-step user tests at this point. Without source identities, public research can only screen candidate sites and licenses, not verify the rights of PO-specific web assets.
