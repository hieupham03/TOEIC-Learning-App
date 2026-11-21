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
}
