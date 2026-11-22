package vn.toeiclearning.alpha.study

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test
import vn.toeiclearning.alpha.domain.ListeningAsset

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

    @Test fun imageOrderAndRevocationAffectNewAttemptsWithoutRescoringHistory() {
        val item = group.items[1]
        val original = group.copy(items = listOf(item), image = ListeningAsset("one.png", 100, "1".repeat(64)),
            extraImages = listOf(ListeningAsset("two.png", 100, "2".repeat(64)), ListeningAsset("three.png", 100, "3".repeat(64))))
        val proof = StudyAnswerProof(original.id, item.id, original.source, original.version,
            studyItemDigest(original, item), 2, "a".repeat(64))
        val review = StudyAnswerReview(proof, "synthetic reviewer", "synthetic evidence")
        val reviewed = original.copy(items = listOf(applyStudyAnswer(original, item, proof, review)))
        val historical = StudyAttempt(listOf(reviewed)).select(2).finish(1000)
        assertEquals(1, historical.score().correct)
        val imageOrderChanged = original.copy(extraImages = original.extraImages.reversed())
        assertNull(applyStudyAnswer(imageOrderChanged, item, proof, review).key)
        val revoked = original.copy(items = listOf(applyStudyAnswer(original, item, proof, null)))
        assertEquals(1, StudyAttempt(listOf(revoked)).select(2).finish(1000).score().ungraded)
        assertEquals(1, historical.score().correct)
    }

    @Test fun applyingAContentUpdateRevokesInFlightKeysWithoutRescoringHistory() {
        val open = StudyAttempt(listOf(group)).select(0).move(2).select(0)
            .copy(readingOffsets = mapOf(group.id to 20))
        val unreviewed = group.items[0].copy(key = null)
        val current = group.copy(items = listOf(unreviewed, group.items[1], group.items[2]))
        val resumed = open.retainCurrentPracticeKeys(listOf(current))
        assertEquals(open.selections, resumed.selections)
        assertEquals(open.position, resumed.position)
        assertEquals(open.readingOffsets, resumed.readingOffsets)
        assertTrue(resumed.items[0].hasSourceKey)
        assertEquals(StudyScore(3, 2, 1, 1), resumed.finish(2000).score())
        assertTrue(resumed.finish(2000).mistakes().isEmpty())
        assertEquals(resumed, resumed.retainCurrentPracticeKeys(listOf(group)))
        val history = open.finish(1000)
        assertEquals(history, history.retainCurrentPracticeKeys(emptyList()))
        assertEquals(StudyScore(3, 2, 2, 1), history.score())
    }

    @Test fun resumingDropsKeysForMissingOrAlteredEvidenceAndNeverAddsNewKeys() {
        val open = StudyAttempt(listOf(group)).select(1)
        val replaced = group.copy(items = listOf(
            group.items[0].copy(choices = options.reversed()),
            group.items[1].copy(key = StudyKey(0, "New approval"), hasSourceKey = true),
            group.items[2].copy(key = StudyKey(2, "New approval")),
        ))
        val resumed = open.retainCurrentPracticeKeys(listOf(replaced))
        assertTrue(resumed.items.none { it.key != null })
        assertEquals(options, resumed.items[0].choices)
        assertFalse(resumed.items[0].hasSourceKey)
        assertTrue(open.retainCurrentPracticeKeys(emptyList()).items.none { it.hasSourceKey })
        assertEquals(open, open.retainCurrentPracticeKeys(listOf(group)))
    }
}
