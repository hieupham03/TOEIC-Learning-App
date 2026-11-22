package vn.toeiclearning.alpha.domain

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

/** Android Gradle local JVM unit tests; NOT EXECUTED unless testDebugUnitTest is run. */
class AlphaRulesTest {
    @Test fun preventsNonQaAndFullMock() {
        assertFalse(SyntheticCatalogue.canStartRealFullMock("A"))
        assertFalse(SyntheticCatalogue.canStartRealFullMock("B"))
        (1..4).forEach { assertFalse(SyntheticCatalogue.canStartAlphaPart(it)) }
        (5..7).forEach { assertTrue(SyntheticCatalogue.canStartAlphaPart(it)) }
    }

    @Test fun noFeedbackBeforeSelectionOrExplicitReveal() {
        val q = SyntheticCatalogue.questions(5).first()
        val empty = PracticeState()
        assertNull(PracticeRules.feedback(empty, q))
        assertEquals(empty, PracticeRules.requestFeedback(empty, q))
        val chosen = PracticeRules.select(empty, q, 1)
        assertNull(PracticeRules.feedback(chosen, q))
        assertTrue(PracticeRules.feedback(PracticeRules.requestFeedback(chosen, q), q)?.correct == true)
    }

    @Test fun anchorRetainsReadingPositionAcrossQuestions() {
        val qs = SyntheticCatalogue.questions(7)
        val anchor = ReadingContext("DEMO-P7-TEXT", null).withPassageAnchor(5, 40)
        val next = anchor.withQuestion(qs.first()).withQuestion(qs.last())
        assertEquals(5, next.itemIndex)
        assertEquals(40, next.itemOffset)
        assertEquals(qs.last().id, next.questionId)
    }

    @Test fun readingSessionReturnsToCapturedPassageAnchor() {
        val questions = SyntheticCatalogue.questions(7)
        val original = ReadingSession(
            ReadingPane.PASSAGE,
            ReadingContext("DEMO-P7-TEXT", questions.first().id),
        )

        val questionPane = original.openQuestions(itemIndex = 5, itemOffset = 40)
            .selectQuestion(questions.last())
        val returned = questionPane.returnToPassage()

        assertEquals(ReadingPane.PASSAGE, returned.pane)
        assertEquals(5, returned.context.itemIndex)
        assertEquals(40, returned.context.itemOffset)
        assertEquals(questions.last().id, returned.context.questionId)
    }

    @Test fun selectionsAndRevealedFeedbackAreIndependentAcrossParts() {
        val part5 = SyntheticCatalogue.questions(5).first()
        val part7 = SyntheticCatalogue.questions(7).first()
        var session = PracticeRules.select(PracticeState(), part5, part5.correctIndex)
        session = PracticeRules.requestFeedback(session, part5)
        session = PracticeRules.select(session, part7, part7.correctIndex)
        assertEquals(setOf(part5.id, part7.id), session.selectedById.keys)
        assertEquals(setOf(part5.id), session.explanationVisibleFor)
        assertEquals(session, PracticeRules.select(session, part5, 0))
        assertTrue(PracticeRules.feedback(session, part5)?.correct == true)
        assertNull(PracticeRules.feedback(session, part7))
    }
}
