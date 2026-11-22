package vn.toeiclearning.alpha.ui

import android.content.res.AssetManager
import android.media.AudioAttributes
import android.media.MediaPlayer
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import java.io.FileNotFoundException
import java.io.IOException
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import vn.toeiclearning.alpha.domain.ListeningAsset
import vn.toeiclearning.alpha.domain.PlaybackEvent
import vn.toeiclearning.alpha.domain.PlaybackState

/** Owns a single player on the main thread for one foreground DEMO screen. */
internal class LocalListeningPlayer(
    private val assets: AssetManager,
    private val asset: ListeningAsset,
    private val scope: CoroutineScope,
) {
    var state by mutableStateOf(PlaybackState.IDLE)
        private set

    private var player: MediaPlayer? = null
    private var verification: Job? = null

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
        verification = scope.launch {
            val failure = withContext(Dispatchers.IO) { verifyAsset() }
            if (failure == null) prepare() else fail(failure)
        }
    }

    private fun verifyAsset(): PlaybackEvent? = try {
        assets.openFd(asset.path).use { file ->
            if (file.length == asset.size && assets.open(asset.path).use { asset.matches(it.readBytes()) }) {
                null
            } else {
                PlaybackEvent.INVALID_ASSET
            }
        }
    } catch (_: FileNotFoundException) {
        PlaybackEvent.MISSING_ASSET
    } catch (_: IOException) {
        PlaybackEvent.PLAYER_ERROR
    } catch (_: RuntimeException) {
        PlaybackEvent.PLAYER_ERROR
    }

    private fun prepare() {
        try {
            assets.openFd(asset.path).use { file ->
                val pending = MediaPlayer()
                player = pending
                pending.setAudioAttributes(
                    AudioAttributes.Builder()
                        .setUsage(AudioAttributes.USAGE_MEDIA)
                        .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
                        .build(),
                )
                pending.setDataSource(file.fileDescriptor, file.startOffset, file.length)
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
        verification?.cancel()
        verification = null
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
