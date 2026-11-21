# Stage 03 — B1 Content Effort and Cost Sensitivity V0.1

**Status:** scenario model for decision support; no quotations, approved rates, spending authorization or schedule commitments. Currency VND. The assumptions are not market-certified productivity data.

## 1. Time assumptions
Because Parts 1/3/4/6/7 involve more than standalone questions, a per-item average is a deliberately crude estimate. Real authoring will vary greatly by group and may exceed these bands.

| Quantity | Low scenario | Mid scenario | High scenario | Basis |
|---|---:|---:|---:|---|
| Mock items | 400 | 400 | 400 | 2 × 200 |
| Author minutes per item (illustration) | 15 | 30 | 45 | Analyst assumption, **not observed data** |
| Independent review minutes per item (illustration) | 5 | 10 | 15 | Analyst assumption |
| Writing hours | 100 | 200 | 300 | `400 × minutes ÷ 60` |
| Independent QA hours | 33.3 | 66.7 | 100 | `400 × minutes ÷ 60` |
| Subtotal author + QA hours | **133.3** | **266.7** | **400** | Excludes scripts/audio/recording/pictures, coordination, revisions, practice bank |

## 2. Sensitivity, NOT supplier rates
| Illustrative paid-hour value | Low (133.3h) | Mid (266.7h) | High (400h) |
|---|---:|---:|---:|
| 0đ/h volunteer | 0đ cash + 133h time | 0đ + 267h time | 0đ + 400h time |
| 100.000đ/h **hypothetical** | ~13,3 triệuđ | ~26,7 triệuđ | 40 triệuđ |
| 200.000đ/h **hypothetical** | ~26,7 triệuđ | ~53,3 triệuđ | 80 triệuđ |

**No paid rates were sourced; these are inputs to the formula, NOT pricing claims.** Even volunteer work has substantial real opportunity cost. Due to grouped items, text QA alone may underestimate script production and audio and image QA. A separate practice bank adds effort on top of this.

## 3. Cash cost buckets still unquantified
- **Rights/licensing quote:** none received. Public ETS $1,500/year sample-item/key license is NOT a quote for our two forms and is therefore excluded as candidate B1 price.
- **Audio:** writing scripts, synthetic or recorded speech and legal rights, voice check, mastering, speaker variety; TTS API costs alone do not capture quality.
- **Pictures/passage assets:** original creation or license + QC.
- **Four-week cloud OPEX:** depends on storage footprint, audio stream frequency, DB reads, chosen infrastructure, logging, backups, unexpected traffic; provider free-tier listing != guarantee $0.
- **Administrative/release:** Google Play developer account and possible legal review, excluded if no store release in pilot.
- **Reserve:** unknown until paid proposals or representative creation run exists.

## 4. Budget approval envelope — placeholders for PO
| Cap | PO value | Gate status |
|---|---|---|
| One-time learning-material cash | NOT SET | RED |
| Four-week operations in VND | NOT SET | RED |
| Hours available for subject-matter QA | NOT SET | RED |
| Contingency | NOT SET | RED |
| Deadline for secured rights/assets | NOT SET | RED |

**Decision rule proposed:** If the two form requirement remains mandatory and content rights or QA capacity not evidenced within approved caps, hold the MVP scope lock; do not silently downgrade B1 or claim an achievable low-cost content bank.

## 5. Official cost references (not a design decision)
- Firebase pricing: https://firebase.google.com/pricing (free quotas vary by product; may require Blaze for certain storage configurations)
- Cloudflare R2 pricing: https://developers.cloudflare.com/r2/pricing/ (10GB-month Standard free-tier quota, other limits apply)
- Amazon Polly price examples: https://aws.amazon.com/polly/pricing/ (pay-by-character and free/credits conditions change)
- ETS licensing: https://www.ets.org/legal/permissions/licensing.html (no price for two entire mock forms)
