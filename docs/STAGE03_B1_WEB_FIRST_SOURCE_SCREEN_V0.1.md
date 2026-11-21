# Stage 03 — B1 Web-First TOEIC Source Screening V0.1

**Status:** Research only; no question banks copied, harvested, downloaded or distributed; 2026-11-21.

## Evidence-based source triage (examples, not legal opinions)
| Source / category | Public information checked | User app reuse status | Recommended handling |
|---|---|---|---|
| PO-owned original material uploaded/hosted by PO | PO attests possessing all needed copyright; individual URLs and ownership evidence not yet identified | **AMBER, attested only** | First priority: itemise exact URLs, ownership and website access terms; if genuinely original and rights permit app rehosting, intake then QA |
| Website with specific signed license or assignment to PO | Agreement, asset list, app rights and access-method terms NOT supplied | **AMBER, conditional** | Prioritise after the actual right+site permission evidenced; check question/audio/image ownership separately |
| CC BY 4.0 original educational items | CC BY allows commercial redistribution/adaptation subject to attribution; site-specific embedded media may have different rights | **AMBER** | Candidate supplemental English content, not a verified complete TOEIC mock bank |
| https://testtoeic.com | Terms grant personal non-commercial study use and prohibit copying, redistribution, mass download and using content to make competing service | **RED for extraction and rehosting on ordinary site terms** | Benchmark UX only; cannot count towards 400 cleared items without separately documented appropriate permissions, including site-use authorisation |
| https://toeic.ai | Terms state all questions/audio/keys are provider-owned/licensed and use is personal, nontransferable; no derivative competing product right | **RED for standard reuse** | Benchmark format only; if separate agreement with rights owner/site exists reassess |
| ETS official materials | ETS permissions/licensing policy has specific restrictions on TOEIC materials and third-party sites | **RED as turnkey full mock source** | Review applicable licensing; do not assume official tests may be copied |

## Minimal evidence to count a question into B1 inventory
1. Exact **source URL / file / owner / creator** and version/date, identity of party supplying it.
2. **Grant or ownership evidence** for question text, prompt, audio/voice, photos, reading passages, transcription, keys, explanations; if same PO is owner, record authorship/assignment basis and any third-party embedded rights.
3. **Permitted uses:** download/automation or permitted delivery route; digital transformation, storage/server transmission, 2–5 pilot users, future public/commercial app and country/term restrictions (separate when necessary).
4. **Complete item mapping:** Form A/B, Part, question ID, media IDs, answer keys, transcript, explanations where present, original file/hash; dedup by text+audio+media.
5. **QA:** independently check every key and media link, licensing metadata, format and content; fix defects before admission.

## Outcome tags
- **GREEN — ready to use**: all required rights + correct access path + content QA checked.
- **AMBER — needs evidence**: PO ownership attested; no documents/URLs/rights scope yet; or source looks open but conditions need analysis.
- **RED — excluded**: site expressly disallows action without additional permission; incomplete/unknown rights or serious QA failure.
- **UNKNOWN — not evaluated**: not counted toward two Full Mocks.

**Important:** SEO labels such as “download free full test”, visible web question text, robots allowance or a purchased account do **not** by themselves authorize a new application to rehost that material.

## Public sources checked
- https://testtoeic.com/legal/terms-of-service
- https://toeic.ai/terms
- https://creativecommons.org/licenses/by/4.0/deed.en
- https://www.ets.org/legal/permissions/licensing.html
- https://support.google.com/googleplay/android-developer/answer/18265346
