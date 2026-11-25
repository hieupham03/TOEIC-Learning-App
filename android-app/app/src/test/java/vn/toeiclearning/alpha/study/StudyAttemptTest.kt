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

    @Test fun oceanChoiceOrderMapsSelectionsAndResultsToTheOriginalIndices() {
        val ocean = group.copy(source = "${OCEAN_SOURCE_PREFIX}fixture")
        val start = (1L..10L).map { StudyAttempt(listOf(ocean), id = it) }
            .first { it.displayChoiceOrder().indexOf(1) != 1 }
        val visible = start.displayChoiceOrder()
        assertEquals(options.indices.toSet(), visible.toSet())
        val chosen = visible.indexOf(ocean.items.first().key!!.choice)
        val saved = start.select(visible[chosen]).move(2)
        val resumed = saved.copy(selections = saved.selections.toMap()).move(0)
        assertEquals(visible, resumed.displayChoiceOrder())
        assertEquals(1, resumed.selections["q1"])
        assertEquals(1, resumed.finish(1000).score().correct)
        assertTrue(start.select(visible[(chosen + 1) % options.size]).finish(1000).mistakes().any { it.id == "q1" })
    }

    @Test fun displayOrderVariesAcrossOceanAttemptsAndSurvivesKeyRevocation() {
        val ocean = group.copy(source = "${OCEAN_SOURCE_PREFIX}fixture")
        val attempt = StudyAttempt(listOf(ocean), id = 7)
        val updated = ocean.copy(items = ocean.items.map { it.copy(key = null) })
        assertEquals(attempt.displayChoiceOrder(), attempt.retainCurrentPracticeKeys(listOf(updated)).displayChoiceOrder())
        val positions = (1L..40L).map { attempt.copy(id = it).displayChoiceOrder().indexOf(1) }
        assertEquals(options.indices.toSet(), positions.toSet())
        assertEquals(options.indices.toList(), attempt.copy(groups = listOf(group)).displayChoiceOrder())
    }

    @Test fun speechWithLetteredOptionsKeepsTheRecordedChoiceOrder() {
        val ocean = group.copy(source = "${OCEAN_SOURCE_PREFIX}fixture", part = 1)
        for (id in 1L..10) {
            assertEquals(options.indices.toList(), StudyAttempt(listOf(ocean), id = id).displayChoiceOrder())
        }
    }

    @Test fun gradedAndUngradedPracticeKeepExistingIdsAndSeparateTheirKeys() {
        val graded = studyPracticeGroups(listOf(group), scored = true).single()
        val ungraded = studyPracticeGroups(listOf(group), scored = false).single()
        assertEquals(group.id, graded.id)
        assertEquals(listOf("q1", "q3"), graded.items.map { it.id })
        assertEquals(listOf("q2"), ungraded.items.map { it.id })
        for (item in graded.items) assertEquals(studyItemDigest(group, item), studyItemDigest(graded, item))
        val practice = StudyAttempt(listOf(graded)).select(1).retainCurrentPracticeKeys(listOf(group))
        assertEquals(1, practice.finish(1000).score().correct)
        assertEquals(1, StudyAttempt(listOf(ungraded)).select(0).finish(1000).score().ungraded)
    }

    @Test fun dailyBatchesKeepCompleteGroupsAtTheBoundary() {
        val groups = (1..7).map { num ->
            group.copy(id = "group$num", items = group.items.map { it.copy(id = "group$num:${it.id}") })
        }
        val batches = dailyStudyBatches(groups)
        assertEquals(listOf(5, 2), batches.map { it.size })
        assertEquals(groups, batches.flatten())
        assertTrue(batches.all { batch -> batch.sumOf { it.items.size } <= 15 })
    }

    @Test fun suggestionUsesWeakestGradedPartOrLeastGradedAvailablePart() {
        assertEquals(3, recommendedPart(setOf(1, 3, 5), listOf(PartStats(1, 2, 1), PartStats(3, 4, 1))))
        assertEquals(1, recommendedPart(setOf(1, 3, 5), listOf(PartStats(1, 0, 0, 30), PartStats(3, 1, 1))))
        assertEquals(3, recommendedPart(setOf(1, 3), listOf(PartStats(1, 4, 4), PartStats(3, 2, 2, 20))))
        assertNull(recommendedPart(emptySet(), emptyList()))
    }

    @Test fun savingAPassageOffsetPreservesAnswersAndHistoricalState() {
        val passage = group.copy(part = 7, passage = "Fixture passage.")
        val open = StudyAttempt(listOf(passage)).select(1).move(1)
        val saved = open.rememberReadingOffset(135)
        assertEquals(mapOf(passage.id to 135), saved.readingOffsets)
        assertEquals(open.selections, saved.selections)
        assertEquals(open.position, saved.position)
        assertEquals(saved, saved.rememberReadingOffset(135))
        assertTrue(saved.rememberReadingOffset(0).readingOffsets.isEmpty())
        val finished = saved.finish(1000)
        assertEquals(finished, finished.rememberReadingOffset(20))
        assertEquals(1, finished.score().correct)
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
        assertFalse(eligible.key!!.batchAccepted)
        assertTrue(applyStudyAnswer(group, original, source, review.copy(batchAccepted = true)).key!!.batchAccepted)
        assertTrue(applyStudyAnswer(group, original, source, review.copy(practiceOnly = true)).key!!.practiceOnly)
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
