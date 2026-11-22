package vn.toeiclearning.alpha.study

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class StudyAttemptTest {
    private val options = listOf("One", "Two", "Three", "Four")
    private val group = StudyGroup("g", 5, "fixture-v1", listOf(
        StudyItem("q1", 1, "Practice prompt", options, StudyKey(1, "Fixture evidence")),
        StudyItem("q2", 2, "Unreviewed prompt", options),
        StudyItem("q3", 3, "Blank prompt", options, StudyKey(0, "Fixture evidence")),
    ))

    @Test fun onlyReviewedSelectionsAreGradedAndBlanksStayUnattempted() {
        val state = StudyAttempt(groups = listOf(group)).select(0).move(1).select(2).finish(1000)
        assertEquals(StudyScore(3, 2, 1, 0), state.score())
        assertEquals(listOf("q1"), state.mistakes().map { it.id })
        assertNull(state.items[1].key)
    }

    @Test fun completionIsIdempotentAndSelectionsCannotChangeAfterFinish() {
        val final = StudyAttempt(groups = listOf(group)).select(1).finish(1000)
        assertEquals(final, final.finish(2000))
        assertEquals(final, final.select(0))
        assertEquals(1, final.score().correct)
        assertTrue(final.complete)
        assertFalse(final.interrupted)
    }

    @Test fun suggestionUsesWeakestGradedPartOrLeastAttemptedAvailablePart() {
        assertEquals(3, recommendedPart(setOf(1, 3, 5), listOf(PartStats(1, 2, 1), PartStats(3, 4, 1))))
        assertEquals(3, recommendedPart(setOf(1, 3, 5), listOf(PartStats(1, 0, 0, 3))))
        assertNull(recommendedPart(emptySet(), emptyList()))
    }

    @Test fun evidenceAndReviewMustMatchTheExactItemSnapshotBeforeScoring() {
        val original = group.items[1]
        val source = StudyAnswerProof(group.id, original.id, group.source, group.version,
            studyItemDigest(group, original), 2, "a".repeat(64))
        val pending = applyStudyAnswer(group, original, source, null)
        assertTrue(pending.hasSourceKey)
        assertNull(pending.key)
        val review = StudyAnswerReview(source, "synthetic reviewer", "synthetic evidence")
        val eligible = applyStudyAnswer(group, original, source, review)
        assertEquals(2, eligible.key?.choice)
        val reordered = original.copy(choices = options.reversed())
        assertNull(applyStudyAnswer(group, reordered, source, review).key)
        assertNull(applyStudyAnswer(group.copy(version = "fixture-v2"), original, source, review).key)
        assertNull(applyStudyAnswer(group, original, source, review.copy(proof = source.copy(choice = 1))).key)
        assertNull(applyStudyAnswer(group, original, source, review.copy(reviewer = "")).key)
        assertEquals(2, eligible.key?.choice)
    }
}
