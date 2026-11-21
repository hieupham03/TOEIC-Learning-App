package vn.toeiclearning.alpha.domain

import java.io.File
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Test
import vn.toeiclearning.alpha.domain.PlaybackEvent.*
import vn.toeiclearning.alpha.domain.PlaybackState.*

class ListeningDemoTest {
    private val fixtures = ListeningDemo.fixtures
    private fun bytes(part: Int) = File("src/main/assets", fixtures[part - 1].assetPath).readBytes()

    @Test fun eachPartResolvesToItsOwnVerifiedTone() {
        for (part in 1..4) {
            val fixture = checkNotNull(ListeningDemo.resolve(part))
            assertEquals(part, fixture.order)
            assertEquals(1, fixture.version)
            assertEquals("CX04-DEMO-P$part-G01-I01", fixture.itemId)
            assertNull(ListeningDemo.assetFailure(fixture, bytes(part)))
        }
        assertNull(ListeningDemo.resolve(5))
    }

    @Test fun missingGroupAndAssetFailClosed() {
        assertNull(ListeningDemo.resolve(1, fixtures.drop(1)))
        assertEquals(MISSING_ASSET, ListeningDemo.assetFailure(fixtures.first(), null))
    }

    @Test fun mismatchedGroupItemAndMediaAreRejected() {
        val first = fixtures.first()
        for (bad in listOf(
            first.copy(groupId = fixtures[1].groupId),
            first.copy(itemId = "CX04-DEMO-P1-G01-I02"),
            first.copy(audioId = fixtures[1].audioId),
            first.copy(version = 2),
            first.copy(sha256 = fixtures[1].sha256),
        )) {
            assertNull(ListeningDemo.resolve(1, listOf(bad) + fixtures.drop(1)))
        }
        assertEquals(INVALID_ASSET, ListeningDemo.assetFailure(first, bytes(2)))
        assertEquals(INVALID_ASSET, ListeningDemo.assetFailure(first, bytes(1).take(44).toByteArray()))
        assertEquals(INVALID_ASSET, ListeningDemo.assetFailure(first, ByteArray(ListeningDemo.TONE_SIZE.toInt())))
    }

    @Test fun duplicateAndOutOfOrderInventoryIsRejected() {
        val first = fixtures.first()
        val second = fixtures[1]
        for (duplicate in listOf(first, second.copy(groupId = first.groupId),
            second.copy(itemId = first.itemId), second.copy(audioId = first.audioId))) {
            assertNull(ListeningDemo.resolve(2, listOf(first, duplicate) + fixtures.drop(2)))
        }
        assertNull(ListeningDemo.resolve(1, fixtures.reversed()))
        assertNull(ListeningDemo.resolve(1, listOf(first.copy(order = 0)) + fixtures.drop(1)))
    }

    @Test fun playPauseResumeStopReplayAndCompletion() {
        val loading = IDLE.next(LOAD)
        assertEquals(LOADING, loading)
        val playing = loading.next(START)
        assertEquals(PLAYING, playing)
        val paused = playing.next(PAUSE)
        assertEquals(PAUSED, paused)
        assertEquals(PLAYING, paused.next(START))
        val stopped = paused.next(STOP)
        assertEquals(STOPPED, stopped)
        assertEquals(LOADING, stopped.next(LOAD))
        val completed = stopped.next(LOAD).next(START).next(END)
        assertEquals(COMPLETED, completed)
        assertEquals(LOADING, completed.next(LOAD))
        assertEquals(STOPPED, loading.next(STOP))
        assertEquals(STOPPED, playing.next(STOP))
    }

    @Test fun errorsBlockPlaybackAndLateEventsDoNotRestartIt() {
        assertEquals(MISSING, LOADING.next(MISSING_ASSET))
        assertEquals(INVALID, LOADING.next(INVALID_ASSET))
        assertEquals(ERROR, PLAYING.next(PLAYER_ERROR))
        for (state in listOf(IDLE, STOPPED, COMPLETED, MISSING, INVALID, ERROR)) {
            assertEquals(state, state.next(START))
            assertEquals(state, state.next(END))
            assertEquals(state, state.next(PAUSE))
        }
        assertEquals(LOADING, ERROR.next(LOAD))
    }

    @Test fun demoDoesNotUnlockBankOrFullMock() {
        for (part in 1..4) assertFalse(SyntheticCatalogue.canStartAlphaPart(part))
        for (form in listOf("A", "B")) assertFalse(SyntheticCatalogue.canStartRealFullMock(form))
    }
}
