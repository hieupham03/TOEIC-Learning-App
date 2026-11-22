package vn.toeiclearning.alpha.ui

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.widthIn
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.semantics.LiveRegionMode
import androidx.compose.ui.semantics.liveRegion
import androidx.compose.ui.semantics.selected
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.unit.dp
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleEventObserver
import androidx.lifecycle.compose.LocalLifecycleOwner
import vn.toeiclearning.alpha.domain.ListeningDemo
import vn.toeiclearning.alpha.domain.PlaybackState

private const val DemoNotice = "DEMO · Âm thanh thử nghiệm · Không phải bài nghe TOEIC · Chưa QA"

@Composable
internal fun ListeningDemoPicker(onBack: () -> Unit, onPart: (Int) -> Unit) {
    DemoPage {
        ScreenHeader("Listening DEMO", onBack)
        Notice(DemoNotice)
        for (part in 1..4) {
            OutlinedButton(
                onClick = { onPart(part) },
                modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp),
            ) { Text("Mở Part $part DEMO") }
        }
    }
}

@Composable
internal fun ListeningDemoItem(
    part: Int,
    answers: Map<String, String>,
    onSelect: (itemId: String, option: String) -> Unit,
    onBack: () -> Unit,
    onPrevious: (() -> Unit)?,
    onNext: () -> Unit,
) {
    val fixture = ListeningDemo.resolve(part)
    val assets = LocalContext.current.assets
    val lifecycle = LocalLifecycleOwner.current.lifecycle
    val playback = remember(assets, part) { LocalListeningPlayer(assets, part) }

    DisposableEffect(lifecycle, playback) {
        val observer = LifecycleEventObserver { _, event ->
            if (event == Lifecycle.Event.ON_PAUSE) playback.stop()
        }
        lifecycle.addObserver(observer)
        onDispose {
            lifecycle.removeObserver(observer)
            playback.stop()
        }
    }

    DemoPage {
        ScreenHeader("Part $part · Listening DEMO", onBack, showNotice = false)
        Notice(DemoNotice)
        if (fixture == null) {
            Notice("Không tìm thấy nhóm thử nghiệm hợp lệ. Không thể phát.", warning = true)
            return@DemoPage
        }
        Text("Mẫu $part/4 · Mỗi Part có một câu minh họa", style = MaterialTheme.typography.bodyMedium)
        PlaybackControls(playback)
        if (part == 1) Notice("Ô ảnh minh họa Part 1 · chỉ là nội dung giữ chỗ")
        val choice = answers[fixture.itemId]
        Text("Chọn một đáp án mẫu", style = MaterialTheme.typography.titleMedium)
        for (option in listOf("A", "B", "C", "D")) {
            OutlinedButton(
                onClick = { onSelect(fixture.itemId, option) },
                modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp)
                    .semantics { selected = choice == option },
            ) {
                Text(if (choice == option) "Mẫu $option · Đã chọn" else "Mẫu $option")
            }
        }
        Text("Lựa chọn được giữ trong phiên DEMO. Listening không chấm đúng/sai.")
        Button(
            onClick = onNext,
            modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp),
        ) { Text(if (part < 4) "Part tiếp theo" else "Xem lại phiên DEMO") }
        if (onPrevious != null) {
            OutlinedButton(
                onClick = onPrevious,
                modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp),
            ) { Text("Part trước") }
        }
    }
}

@Composable
private fun PlaybackControls(playback: LocalListeningPlayer) {
    val state = playback.state
    val status = when (state) {
        PlaybackState.IDLE -> "Chưa phát"
        PlaybackState.LOADING -> "Đang tải âm thanh thử nghiệm"
        PlaybackState.PLAYING -> "Đang phát"
        PlaybackState.PAUSED -> "Đã tạm dừng"
        PlaybackState.STOPPED -> "Đã dừng"
        PlaybackState.COMPLETED -> "Đã phát xong"
        PlaybackState.MISSING -> "Thiếu tệp âm thanh thử nghiệm. Không thể phát."
        PlaybackState.INVALID -> "Tệp âm thanh không khớp. Không thể phát."
        PlaybackState.ERROR -> "Không thể phát âm thanh thử nghiệm."
    }
    Text(
        status,
        modifier = Modifier.semantics { liveRegion = LiveRegionMode.Polite },
        style = MaterialTheme.typography.bodyLarge,
    )
    val error = state in setOf(PlaybackState.MISSING, PlaybackState.INVALID, PlaybackState.ERROR)
    Button(
        enabled = state != PlaybackState.LOADING,
        onClick = playback::toggle,
        modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp),
    ) {
        Text(when (state) {
            PlaybackState.PLAYING -> "Tạm dừng"
            PlaybackState.PAUSED -> "Tiếp tục phát"
            PlaybackState.COMPLETED, PlaybackState.STOPPED -> "Phát lại"
            else -> if (error) "Thử phát lại" else "Phát âm thanh"
        })
    }
    if (state.active) {
        OutlinedButton(
            onClick = playback::stop,
            modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp),
        ) { Text("Dừng") }
    }
}

@Composable
private fun DemoPage(content: @Composable () -> Unit) {
    Box(Modifier.fillMaxSize(), contentAlignment = Alignment.TopCenter) {
        Column(
            modifier = Modifier.widthIn(max = 720.dp).fillMaxWidth().verticalScroll(rememberScrollState())
                .padding(horizontal = 20.dp, vertical = 16.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp),
        ) { content() }
    }
}
