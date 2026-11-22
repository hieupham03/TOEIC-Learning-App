package vn.toeiclearning.alpha.study

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test
import vn.toeiclearning.alpha.domain.ListeningAsset

class MockStudyTest {
    @Test fun requiresBothCompleteIndependentReviewedForms() {
        val a = form("A")
        val b = form("B")
        assertTrue(checkMockForms(listOf(a, b), emptyList()).ready)
        val short = b.copy(groups = b.groups.filter { it.part != 7 })
        assertEquals(54, checkMockForms(listOf(a, short), emptyList()).missing.getValue("B"))
        assertFalse(checkMockForms(listOf(a, short), emptyList()).ready)
        assertFalse(checkMockForms(listOf(a, b), listOf(a.groups[0])).ready)
        assertFalse(checkMockForms(listOf(a, b.copy(groups = a.groups)), emptyList()).ready)
        assertEquals(200, checkMockForms(emptyList(), emptyList()).missing.getValue("A"))
    }

    @Test fun retainsTwoHundredSelectionsAcrossSectionsAndScoresByPart() {
        val form = form("A")
        val start = MockTime(3, 1000, 100_000)
        var attempt = StudyAttempt(form.groups, mock = MockRun(form.id, form.version, start.boot, start.elapsed))
        for (index in 0..99) attempt = attempt.move(index).select(0)
        for (group in form.groups.filter { it.part <= 4 }) {
            attempt = attempt.move(group.items.first().number - 1).reserveMockAudio(group.id).completeMockAudio(group.id)
        }
        attempt = attempt.advanceMock(start.copy(elapsed = 2_701_000))
        assertEquals(100, attempt.position)
        for (index in 100..199) attempt = attempt.move(index).select(1)
        attempt = attempt.advanceMock(start.copy(elapsed = 7_201_000, wall = 200_000))
        assertTrue(attempt.complete)
        assertFalse(attempt.interrupted)
        assertEquals(StudyScore(200, 200, 200, 100), attempt.score())
        assertEquals(StudyScore(54, 54, 54, 0), attempt.score(7))
    }

    @Test fun unfinishedAudioCannotReplayAfterRecoveryAndRebootDoesNotResetTime() {
        val form = form("B")
        val start = MockTime(8, 50_000, 123_000)
        val attempt = StudyAttempt(form.groups, mock = MockRun("B", "v1", start.boot, start.elapsed)).select(0)
        assertNull(attempt.reserveMockAudio(form.groups[1].id).mock?.pendingAudio)
        val playing = attempt.reserveMockAudio(form.groups[0].id)
        for (end in listOf(
            playing.advanceMock(start.copy(elapsed = 51_000), recovering = true),
            attempt.advanceMock(start.copy(boot = 9, elapsed = 90_000)),
            attempt.advanceMock(start.copy(elapsed = 2_750_000)),
        )) {
            assertTrue(end.complete && end.interrupted)
            assertEquals(1, end.selections.size)
        }
        assertEquals(attempt, attempt.advanceMock(start.copy(wall = 87)))
    }

    private fun form(id: String): MockForm {
        val counts = listOf(6, 25, 39, 30, 30, 16, 54)
        var number = 0
        val groups = counts.flatMapIndexed { index, count ->
            val part = index + 1
            val size = when (part) { 3, 4 -> 3; 6 -> 4; 7 -> 2; else -> 1 }
            List(count / size) { ordinal ->
                val groupId = "$id-$part-$ordinal"
                val media = ListeningAsset("test/$groupId", 20, "fixture-$groupId")
                StudyGroup(groupId, part, "v1", List(size) {
                    number++
                    StudyItem("$id-$number", number, "Synthetic $id prompt $number",
                        if (part == 2) listOf("A", "B", "C") else listOf("A", "B", "C", "D"),
                        StudyKey(0, "Original fixture key"))
                }, passage = if (part >= 6) "Original $groupId passage" else null,
                    audio = if (part <= 4) media else null, image = if (part == 1) media else null)
            }
        }
        return MockForm(id, "v1", "Synthetic review record $id", groups)
    }
}
