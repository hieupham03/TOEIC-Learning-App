package vn.toeiclearning.alpha.domain

import java.security.MessageDigest

internal data class ListeningFixture(
    val part: Int,
    val groupId: String,
    val itemId: String,
    val audioId: String,
    val order: Int,
    val version: Int,
    val sha256: String,
) {
    val assetPath: String get() = "listening_demo/$audioId.wav"
    val asset: ListeningAsset get() = ListeningAsset(assetPath, ListeningDemo.TONE_SIZE, sha256)
}

internal data class ListeningAsset(val path: String, val size: Long, val sha256: String) {
    fun matches(bytes: ByteArray): Boolean = bytes.size.toLong() == size &&
        MessageDigest.getInstance("SHA-256").digest(bytes).toHexString() == sha256
}

internal object ListeningDemo {
    const val TONE_SIZE = 192044L // 44-byte header + 6 s × 16 kHz × 2 bytes.
    val fixtures = listOf(
        fixture(1, "97b157773f1c7e52461a37d2fb25420651725b34f2a00c4f092b0a34d3a24f2c"),
        fixture(2, "4ca4ac157e335a9e1e9dd1093e363896b346b8d4128f7a2d43d02fbb5fb98305"),
        fixture(3, "a0188fd2f8f5f3bf6a79a5cd40dd735c60e82e5f44326516c0d1767a83a2bb38"),
        fixture(4, "d43097ce9535f521be144e20ce7c26717fd283d80e7fbc69d3ceb7c68a05c932"),
    )

    private fun fixture(part: Int, hash: String) = ListeningFixture(
        part = part,
        groupId = "CX04-DEMO-P$part-G01",
        itemId = "CX04-DEMO-P$part-G01-I01",
        audioId = "cx04_tone_p${part}_v1",
        order = part,
        version = 1,
        sha256 = hash,
    )

    fun resolve(part: Int, catalogue: List<ListeningFixture> = fixtures): ListeningFixture? {
        // The demo has a fixed versioned inventory. Reject changes to any association,
        // duplicate entries, and reorderings before choosing an asset.
        if (part !in 1..4 || catalogue != fixtures) return null
        return catalogue[part - 1]
    }

    fun assetFailure(fixture: ListeningFixture, bytes: ByteArray?): PlaybackEvent? {
        if (bytes == null) return PlaybackEvent.MISSING_ASSET
        if (resolve(fixture.part) != fixture || bytes.size.toLong() != TONE_SIZE) {
            return PlaybackEvent.INVALID_ASSET
        }
        return if (fixture.asset.matches(bytes)) null else PlaybackEvent.INVALID_ASSET
    }
}

internal enum class PlaybackEvent {
    LOAD, START, PAUSE, STOP, END, MISSING_ASSET, INVALID_ASSET, PLAYER_ERROR
}

internal enum class PlaybackState {
    IDLE, LOADING, PLAYING, PAUSED, STOPPED, COMPLETED, MISSING, INVALID, ERROR;

    val active: Boolean get() = this == LOADING || this == PLAYING || this == PAUSED

    fun next(event: PlaybackEvent): PlaybackState = when (event) {
        PlaybackEvent.LOAD -> if (this == LOADING) this else LOADING
        PlaybackEvent.START -> if (this == LOADING || this == PAUSED) PLAYING else this
        PlaybackEvent.PAUSE -> if (this == PLAYING) PAUSED else this
        PlaybackEvent.STOP -> if (active) STOPPED else this
        PlaybackEvent.END -> if (this == PLAYING || this == PAUSED) COMPLETED else this
        PlaybackEvent.MISSING_ASSET -> if (this == LOADING) MISSING else this
        PlaybackEvent.INVALID_ASSET -> if (this == LOADING) INVALID else this
        PlaybackEvent.PLAYER_ERROR -> if (active) ERROR else this
    }
}
