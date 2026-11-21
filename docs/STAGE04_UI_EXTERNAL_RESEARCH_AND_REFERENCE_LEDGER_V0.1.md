# Stage 04 — Evidence-first UI Reference Review V0.1

**Date:** 2026-11-21 · **Status:** RESEARCH COMPLETED FOR DRAFT REDESIGN, **NOT** DESIGN BASELINE APPROVAL.  
**Trigger:** Product Owner requested reviewing `letanssang/speak_up_flutter`, other English-learning apps, anti-patterns from AI-generated UI and redesigned aesthetics.  
**Research type:** Desk review of public materials and published visual references, not usability research, source-code audit or permission to reuse copyrighted artwork.

## A. Reference inventory and evidence quality

| Reference | Evidence accessed | What carries over | What does not carry over |
|---|---|---|---|
| Speak Up Flutter | Public repository/README verified, including described interactive lessons, quiz, flashcards, bilingual experience and 10 screenshot links | Discrete and discoverable learning tasks; reusable navigation/feedback ideas | Public README does **not** establish fitness of UI, license for copying assets or applicability of pronunciation/chatbot/reels to TOEIC MVP. Individual original screenshot binaries were not independently accessible here; do not invent a screenshot-by-screenshot audit. |
| Duolingo | 2026 primary-party core-tab redesign post, design system iteration | Common header hierarchy, aligned spacing, purposeful visuals; clarity before ornament | Gamified mascot, streak pressure, candy colors and social/leaderboard tabs need no replication |
| ELSA Speak | 2026 first-party redesign article | Task-oriented entry, learner progress, consistent navigation | AI coach, speaking simulator, premium path and other out-of-scope features |
| Busuu | Designer's exercise-redesign case study | Single exercise grammar, accessible feedback text plus color, early learning flow | Copying proprietary screenshots/visual identity, assuming its results transfer to TOEIC |
| NN/g | Original usability articles | No clutter/duplicate content, recognizable labeled icons, visual prioritization | No fixed empirical universal upper bound on icon count from these sources |
| Google/Material 3, W3C | Published design/accessibility guidance | Semantic color roles, legible typography, >=48dp targets (Android recommendation), text contrast | Static PNG cannot prove real-device compliance |

### Speak Up repository-specific verification

- Repository URL: https://github.com/letanssang/speak_up_flutter  
- README describes authentication/profile, English/Vietnamese UI, light/dark modes, dialogue practice, lessons, quizzes/flashcards, pronunciation, reels and chatbot. This supports **feature/reference discovery**, not a judgement that all its UI is usable.  
- Raw README at https://raw.githubusercontent.com/letanssang/speak_up_flutter/main/README.md exposes ten image URLs under `## Screenshots`; access to the binaries through the GitHub attachment redirect failed in the current review. **Do not claim all ten original screenshots were visually inspected.**
- No Flutter code, assets or proprietary illustrations were reused, fetched into the project or incorporated into the revised concept.

## B. Design conclusions specific to TOEIC Android L&R

1. **Exam mode is not a casual gamified lesson**: protected timing, no voluntary pause/arbitrary replay for comparable attempts, honest saved/invalid status and calm distraction-free screens.
2. **Reading Part 6–7 uses most of the viewport for passage/question**. Keep W-02A semantic anchor and return position as a behavioral requirement; test on actual devices later.
3. **Part Practice has low start friction**: Part choice / time-limited short session / error review from Task Hub; recommendations optional.
4. **Score is not an official ETS scaled score**: display answered/correct and Part breakdown plus form/version/validity rather than fictional scaled improvement.
5. **Learner privacy and content provenance** are UI states, not ornamentation; no mock availability claim beyond demonstration data.
6. **Consistent lightweight academic style**, not oversaturated game/streak pattern, fits longer Reading and Full Mock use cases.

## C. Source ledger

- **Speak Up Flutter — README:** https://github.com/letanssang/speak_up_flutter  
  Basis: Readme reviewed; 10 screenshot links exposed in raw README, but original image binaries not independently inspected. Feature descriptions only; no copied UI/code.
- **Duolingo — Craft of core tabs redesign (2026):** https://blog.duolingo.com/core-tabs-redesign/  
  Basis: First-party case study: consistency in header, spacing/type; asks whether decoration serves a purpose.
- **ELSA Speak — January 2026 redesign:** https://blog.elsaspeak.com/en/discover-the-new-elsa-speak-experience/  
  Basis: First-party feature/UX account; clear navigation and personal learning path, not license for AI tutor in this MVP.
- **Busuu — Exercise redesign case study:** https://www.enricocapone.com/projects/exercise-redesign.html  
  Basis: Practitioner notes red/green-only feedback problematic for colorblind users; consistent exercise components.
- **Nielsen Norman Group — Prompt to Design Interfaces:** https://www.nngroup.com/articles/vague-prototyping/  
  Basis: Research on AI-prototyped visual clutter, content repetition, poor hierarchy from vague prompting.
- **Nielsen Norman Group — Top application design mistakes:** https://www.nngroup.com/articles/top-10-application-design-mistakes/  
  Basis: Icons need labels; avoid obscure commands.
- **Google Android — Material 3 color & typography:** https://developer.android.com/codelabs/m3-design-theming  
  Basis: Semantic colors, scalable typography and role consistency.
- **W3C — WCAG 2.2 contrast:** https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html  
  Basis: Target >=4.5:1 ordinary text, >=3:1 large text; verify actual combinations.
- **Android — Accessible apps:** https://developer.android.com/guide/topics/ui/accessibility/apps  
  Basis: Touch targets >=48dp recommended, screen reader and semantic requirements.
- **2026 visual-complexity research (secondary):** https://www.mdpi.com/2079-9292/15/15/3458  
  Basis: Risks of polished but cluttered AI-created UI; avoid overinterpreting single study.

## D. Evidence limits

- UI image concept generated by AI and visually reviewed; it is **not** a screenshot of the reference repo, Duolingo, ELSA or Busuu.
- Screenshots/marketing renders may differ from live products/version/device; learn transferable patterns, not proprietary graphic assets.
- No tested usability sample (n=0), real Android phones (n=0), AI/UI benchmark experiment, running mock/audio/save or accessibility audit performed.
