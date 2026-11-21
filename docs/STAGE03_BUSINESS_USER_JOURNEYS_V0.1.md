# TOEIC Learning App — WP-01 Business User Journeys V0.1

**State:** BUSINESS-LEVEL DRAFT, not UI flows and not feature acceptance.  
**Source:** Product Vision V1.0 + direct user evidence VAL-001–024. The exact mechanics depend on the future PO scope decision.

## JNY-01 — Begin and decide what to learn

1. Learner declares current confidence / available baseline / target and how much time is available now (flexible, not a rigid daily commitment).
2. Learner can self-select a Part or accept an appropriate candidate recommendation.
3. Learner begins relevant study and sees how their attempt contributes to record of areas to improve.
4. Learner can end an ordinary practice session and return later; timed Full Mock uses separately defined exam conditions.

**Exceptions:** no reliable baseline; no content for selected Part; learner has only seconds; no internet. **Do not assume** offline support in initial pilot.

## JNY-02 — Integrated Listening practice

1. Learner selects a Listening Part session and receives corresponding questions/audio with verified mapping.
2. Learner follows the audio, chooses answers, completes/navigates allowed questions.
3. Learner reviews results and correct explanations only after appropriate practice-mode rules.
4. Attempt and mistakes can inform future practice if included in approved scope.

**Key risk:** wrong audio/question/answer match; audio unavailable; phone interruptions. Audio play policy differs between free practice and timed mock, not determined at this stage.

## JNY-03 — Long Reading practice

1. Learner selects a Reading Part with text/attachments.
2. Learner reads and answers without losing essential context, including long passages and multiple questions.
3. Learner reviews errors, notes issues and exits session.

**Key risk:** long Part 6/7 passage and question navigation creates eye strain and excess scrolling on phone, already reported by learner 01; no UI solution approved.

## JNY-04 — Full Mock Test

1. Learner selects a legitimately sourced, quality-reviewed full test and acknowledges strict timed conditions.
2. Learner completes Listening & Reading and receives completion/accuracy data.
3. Learner can examine question errors and discuss next practice goal.
4. Progress comparison occurs **only** with tests for which comparability and score semantics have been established.

**Exception/risk:** lack of legally usable 200-item tests, interruption, loss of progress, fatigue, inaccurate attempt mapping. No official ETS score implied.

## JNY-05 — Use personal materials (two distinct levels)

**Level 1 (low-risk benchmark):** Learner keeps a rights-aware reference/catalog of their material; a curator manually constructs approved structured questions/audio/answers from material that may lawfully be used for the intended context.

**Level 2 (future hypothesis):** Learner supplies a permitted PDF/audio and system converts it with extraction QA, ambiguity flags, provenance, review and errors/fallback. No automatic ingestion presumed feasible.

**Key open distinction:** personal private access vs transfer to cloud vs sharing to family vs public publishing. Ownership of a copy proves none of the broader rights.

## JNY-06 — Microlearning and notifications (potential later feature)

1. Learner wishes to learn one word or question with minimal friction.
2. Candidate activity can fit seconds/minutes and align with learning needs.
3. If opted into notifications, learner can choose silence/vibrate/sound; wants actions for known-word, hide-current-word, disable-all, postpone.
4. Learner may opt out at any time; exact handling and action presentation are NOT decided.

**Key risk:** Android notification action/permission limits, interruption burden, efficacy not established.

## JNY-07 — Pilot content stewardship and correction

1. Curator logs source/provenance/license and allowed processing/sharing context.
2. Curator checks question–audio–answer–explanation mapping and removes incorrect items.
3. Learner can report ambiguity; curator fixes, quarantines or removes item.
4. Any test or analytics that used changed items must flag implications to comparability.

**Note:** These are acceptance-relevant business outcomes, not roles/permissions architecture.
