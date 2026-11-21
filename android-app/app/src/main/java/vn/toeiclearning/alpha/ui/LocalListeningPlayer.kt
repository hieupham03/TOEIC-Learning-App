package vn.toeiclearning.alpha.ui

import android.content.res.AssetManager
import android.media.AudioAttributes
import android.media.MediaPlayer
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import java.io.FileNotFoundException
import java.io.IOException
import vn.toeiclearning.alpha.domain.ListeningDemo
import vn.toeiclearning.alpha.domain.PlaybackEvent
import vn.toeiclearning.alpha.domain.PlaybackState

/** Owns a single player on the main thread for one foreground DEMO screen. */
internal class LocalListeningPlayer(private val assets: AssetManager, private val part: Int) {
    var state by mutableStateOf(PlaybackState.IDLE)
        private set

    private var player: MediaPlayer? = null

    fun toggle() {
        when (state) {
            PlaybackState.PLAYING -> usePlayer(PlaybackEvent.PAUSE) { pause() }
            PlaybackState.PAUSED -> usePlayer(PlaybackEvent.START) { start() }
            PlaybackState.LOADING -> Unit
            else -> playFromBeginning()
        }
    }

    private fun playFromBeginning() {
        releasePlayer()
        transition(PlaybackEvent.LOAD)
        val fixture = ListeningDemo.resolve(part)
        if (fixture == null) {
            fail(PlaybackEvent.INVALID_ASSET)
            return
        }
        try {
            // Verify the immutable packaged bytes before preparing the player.
            assets.openFd(fixture.assetPath).use { asset ->
                val failure = if (asset.length != ListeningDemo.TONE_SIZE) {
                    PlaybackEvent.INVALID_ASSET
                } else {
                    ListeningDemo.assetFailure(fixture, assets.open(fixture.assetPath).use { it.readBytes() })
                }
                if (failure != null) {
                    fail(failure)
                    return
                }
                val pending = MediaPlayer()
                player = pending
                pending.setAudioAttributes(
                    AudioAttributes.Builder()
                        .setUsage(AudioAttributes.USAGE_MEDIA)
                        .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
                        .build(),
                )
                pending.setDataSource(asset.fileDescriptor, asset.startOffset, asset.length)
                pending.setOnPreparedListener { current ->
                    if (player === current && state == PlaybackState.LOADING) {
                        usePlayer(PlaybackEvent.START) { start() }
                    }
                }
                pending.setOnCompletionListener { current ->
                    if (player === current) {
                        transition(PlaybackEvent.END)
                        releasePlayer()
                    }
                }
                pending.setOnErrorListener { current, _, _ ->
                    if (player === current) fail(PlaybackEvent.PLAYER_ERROR)
                    true
                }
                pending.prepareAsync()
            }
        } catch (_: FileNotFoundException) {
            fail(PlaybackEvent.MISSING_ASSET)
        } catch (_: IOException) {
            fail(PlaybackEvent.PLAYER_ERROR)
        } catch (_: RuntimeException) {
            fail(PlaybackEvent.PLAYER_ERROR)
        }
    }

    fun stop() {
        releasePlayer()
        transition(PlaybackEvent.STOP)
    }

    private fun usePlayer(event: PlaybackEvent, action: MediaPlayer.() -> Unit) {
        val current = player
        if (current == null) {
            fail(PlaybackEvent.PLAYER_ERROR)
            return
        }
        try {
            current.action()
            transition(event)
        } catch (_: RuntimeException) {
            fail(PlaybackEvent.PLAYER_ERROR)
        }
    }

    private fun fail(event: PlaybackEvent) {
        releasePlayer()
        transition(event)
    }

    private fun transition(event: PlaybackEvent) {
        state = state.next(event)
    }

    private fun releasePlayer() {
        val current = player
        player = null
        current?.release()
    }
}
