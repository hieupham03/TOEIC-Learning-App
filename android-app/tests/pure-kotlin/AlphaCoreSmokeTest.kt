package vn.toeiclearning.alpha.tests

import vn.toeiclearning.alpha.domain.*

/** Run with the installed Kotlin compiler; this is NOT a Gradle Android or device test. */
fun main() {
    var assertions = 0
    fun verify(condition: Boolean, message: String) {
        check(condition) { message }
        assertions++
    }
    verify(SyntheticCatalogue.parts.size == 7, "Part catalogue must have 7 entries")
    verify((1..4).all { !SyntheticCatalogue.canStartAlphaPart(it) }, "Listening has no audio/QA")
    verify((5..7).all { SyntheticCatalogue.canStartAlphaPart(it) }, "Only synthetic reading demo")
    verify(!SyntheticCatalogue.canStartRealFullMock("A"), "Real Full Mock A blocked")
    verify(!SyntheticCatalogue.canStartRealFullMock("B"), "Real Full Mock B blocked")
    verify(SyntheticCatalogue.questions(5).all { it.syntheticOnly }, "No real items")
    verify(SyntheticCatalogue.questions(6).all { it.syntheticOnly }, "No real items Part6")
    verify(SyntheticCatalogue.questions(7).all { it.syntheticOnly }, "No real items Part7")
    verify(SyntheticCatalogue.questions(1).isEmpty(), "Listening content blocked")
    val q = SyntheticCatalogue.questions(5).first()
    val blank = PracticeState()
    verify(PracticeRules.feedback(blank, q) == null, "Never reveal before choice")
    verify(PracticeRules.requestFeedback(blank, q) == blank, "No reveal with no choice")
    val chosen = PracticeRules.select(blank, q, 1)
    verify(chosen.selectedById[q.id] == 1, "Selected answer stays in volatile UI")
    verify(PracticeRules.feedback(chosen, q) == null, "Selection isn't feedback")
    val revealed = PracticeRules.requestFeedback(chosen, q)
    verify(PracticeRules.feedback(revealed, q)?.correct == true, "Synthetic feedback")
    verify(PracticeRules.select(revealed, q, 0) == revealed, "Choice immutable after reveal")
    val qNoExplanation = q.copy(id = "DEMO-NO-EXPLAIN", explanation = null)
    val qNoExpChosen = PracticeRules.select(blank, qNoExplanation, 0)
    verify(PracticeRules.requestFeedback(qNoExpChosen, qNoExplanation) == qNoExpChosen,
        "No unverified explanation")
    val passage = SyntheticCatalogue.passage(7)!!
    val r1 = SyntheticCatalogue.questions(7)[0]
    val r2 = SyntheticCatalogue.questions(7)[1]
    val anchor = ReadingContext(passage.id, null).withPassageAnchor(4, 36).withQuestion(r1)
    verify(anchor.itemIndex == 4 && anchor.itemOffset == 36, "Long passage anchor retained")
    verify(anchor.withQuestion(r2).itemIndex == 4, "Question switch doesn't reset passage")
    verify(anchor.withQuestion(r2).questionId == r2.id, "Question ID restored")
    val readingSession = ReadingSession(ReadingPane.PASSAGE, ReadingContext(passage.id, r1.id))
        .openQuestions(4, 36)
        .selectQuestion(r2)
        .returnToPassage()
    verify(readingSession.pane == ReadingPane.PASSAGE, "Reading session returns to passage")
    verify(readingSession.context.itemIndex == 4 && readingSession.context.itemOffset == 36,
        "Reading session retains captured passage anchor")
    verify(readingSession.context.questionId == r2.id, "Reading session retains selected question")
    val foreignQuestion = SyntheticCatalogue.questions(6)[0]
    verify(runCatching { anchor.withQuestion(foreignQuestion) }.isFailure, "Foreign passage blocked")
    verify(SyntheticCatalogue.parts.all { it.number in 1..7 }, "Part type constrained")
    verify(SyntheticCatalogue.passagesOrProofAreSynthetic(), "No production answer evidence")
    println("ALPHA PURE-KOTLIN CORE CHECKS: PASS ($assertions assertions); this is not an Android build")
}

/** Extra explicit synthetic fixture assertion to prevent production misrepresentation. */
private fun SyntheticCatalogue.passagesOrProofAreSynthetic(): Boolean =
    (5..7).all { id -> questions(id).all { it.syntheticOnly && it.id.startsWith("DEMO-") } }
