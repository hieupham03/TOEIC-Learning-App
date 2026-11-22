package vn.toeiclearning.alpha.study

import android.graphics.Bitmap
import android.graphics.BitmapFactory
import androidx.activity.compose.BackHandler
import androidx.compose.foundation.Image
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.aspectRatio
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.layout.widthIn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.key
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.produceState
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.semantics.selected
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.unit.dp
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import vn.toeiclearning.alpha.domain.ListeningAsset
import vn.toeiclearning.alpha.ui.Notice
import vn.toeiclearning.alpha.ui.PlaybackControls
import vn.toeiclearning.alpha.ui.rememberListeningPlayer

@Composable
internal fun StudySession(
    attempt: StudyAttempt,
    busy: Boolean,
    marked: Boolean,
    onChange: (StudyAttempt) -> Unit,
    onBookmark: () -> Unit,
    onBack: () -> Unit,
) {
    val group = attempt.group
    val item = attempt.item
    val hasPassage = group.part >= 6
    var showPassage by remember(attempt.id, group.id) { mutableStateOf(hasPassage && !attempt.complete) }
    var confirmFinish by remember(attempt.id) { mutableStateOf(false) }
    val passageScroll = key(attempt.id, group.id) {
        rememberScrollState(attempt.readingOffsets[group.id] ?: 0)
    }
    val goBack = {
        if (!busy) {
            if (hasPassage && !attempt.complete && !showPassage) showPassage = true
            else onBack()
        }
    }
    BackHandler(onBack = goBack)

    Box(Modifier.fillMaxSize(), contentAlignment = Alignment.TopCenter) {
        Column(Modifier.widthIn(max = 720.dp).fillMaxSize().padding(horizontal = 16.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp)) {
            StudyHeading(if (attempt.complete) "Kết quả luyện tập" else "Part ${group.part}", goBack)
            if (!attempt.complete) {
                Text(if (busy) "Đang lưu trên thiết bị…" else "${attempt.selections.size}/${attempt.items.size} đã trả lời")
            }
            if (hasPassage && !attempt.complete) {
                StudyButton(if (showPassage) "Sang câu hỏi" else "Về đoạn văn", !busy, primary = showPassage) {
                    if (showPassage) onChange(attempt.copy(readingOffsets = attempt.readingOffsets + (group.id to passageScroll.value)))
                    showPassage = !showPassage
                }
            }
            if (showPassage && !attempt.complete) {
                Column(Modifier.fillMaxWidth().weight(1f).verticalScroll(passageScroll),
                    verticalArrangement = Arrangement.spacedBy(12.dp)) {
                    Text("Đoạn văn · câu ${group.items.first().number}–${group.items.last().number}",
                        style = MaterialTheme.typography.titleMedium)
                    group.passage?.let { Text(it, style = MaterialTheme.typography.bodyLarge) }
                    group.image?.let { StudyImage(it, "Ảnh đoạn văn", allowZoom = true) }
                }
            } else {
                Column(Modifier.fillMaxWidth().weight(1f).verticalScroll(key(attempt.id, item.id, attempt.complete) { rememberScrollState() }),
                    verticalArrangement = Arrangement.spacedBy(12.dp)) {
                    if (attempt.complete) {
                        val score = attempt.score()
                        Notice("${score.attempted}/${score.total} đã trả lời · ${score.total - score.attempted} bỏ trống")
                        Text(if (score.graded == 0) "Chưa có câu đã chấm bằng đáp án xác minh."
                        else "${score.correct} đúng · ${score.wrong} sai · ${score.ungraded} đã trả lời chưa chấm")
                    }
                    LazyRow(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                        items(attempt.items) { target ->
                            val answered = target.id in attempt.selections
                            OutlinedButton(
                                onClick = { onChange(attempt.move(attempt.items.indexOf(target))) },
                                enabled = !busy,
                                modifier = Modifier.heightIn(min = 48.dp).semantics { selected = target.id == item.id },
                            ) { Text("${target.number}${if (answered) " ✓" else ""}") }
                        }
                    }
                    key(group.id, group.version) {
                        group.audio?.let { PlaybackControls(rememberListeningPlayer(it), study = true) }
                    }
                    group.image?.let { StudyImage(it, if (hasPassage) "Ảnh đoạn văn" else "Ảnh câu hỏi", allowZoom = hasPassage) }
                    if (attempt.complete) group.passage?.let { Text(it, style = MaterialTheme.typography.bodyLarge) }
                    Text("Câu ${item.number}${if (item.prompt.isBlank()) "" else " · ${item.prompt}"}",
                        style = MaterialTheme.typography.titleMedium)
                    item.choices.forEachIndexed { index, choice ->
                        val option = ('A' + index).toString()
                        val chosen = attempt.selections[item.id] == index
                        OutlinedButton(
                            onClick = { onChange(attempt.select(index)) },
                            enabled = !busy && !attempt.complete,
                            modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp).semantics { selected = chosen },
                        ) { Text(if (choice == option) "$option${if (chosen) " · Đã chọn" else ""}"
                        else "$option. $choice${if (chosen) " · Đã chọn" else ""}") }
                    }
                    if (attempt.complete) {
                        val answer = item.key
                        if (answer != null) Text("Đáp án đã xác minh · ${'A' + answer.choice}")
                        else Text("Câu này chưa có đáp án đã xác minh.")
                        Text(answer?.explanation ?: "Chưa có lời giải.")
                    } else {
                        if (item.key == null) Text("Câu này chưa có đáp án đã xác minh.")
                        StudyButton(if (marked) "Bỏ đánh dấu" else "Đánh dấu câu", !busy, onClick = onBookmark)
                    }
                }
            }
            if (!showPassage || attempt.complete) {
                Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    OutlinedButton({ onChange(attempt.move(attempt.position - 1)) },
                        Modifier.weight(1f).heightIn(min = 48.dp), !busy && attempt.position > 0) { Text("Câu trước") }
                    OutlinedButton({ onChange(attempt.move(attempt.position + 1)) },
                        Modifier.weight(1f).heightIn(min = 48.dp), !busy && attempt.position < attempt.items.lastIndex) {
                        Text("Câu tiếp")
                    }
                }
            }
            StudyButton(if (attempt.complete) "Về luyện tập" else "Kết thúc bài luyện", !busy, primary = true) {
                if (attempt.complete) onBack() else confirmFinish = true
            }
        }
    }
    if (confirmFinish) AlertDialog(
        onDismissRequest = { confirmFinish = false },
        title = { Text("Kết thúc bài luyện?") },
        text = { Text("${attempt.items.size - attempt.selections.size} câu chưa trả lời sẽ để trống.") },
        confirmButton = {
            TextButton(onClick = {
                confirmFinish = false
                onChange(attempt.finish(System.currentTimeMillis()))
            }) { Text("Xác nhận kết thúc") }
        },
        dismissButton = { TextButton(onClick = { confirmFinish = false }) { Text("Tiếp tục luyện") } },
    )
}

@Composable
private fun StudyImage(asset: ListeningAsset, description: String, allowZoom: Boolean) {
    val assets = LocalContext.current.assets
    val bitmap by produceState<Bitmap?>(null, asset, assets) {
        value = withContext(Dispatchers.IO) {
            runCatching {
                val bytes = assets.open(asset.path).use { it.readBytes() }
                if (asset.matches(bytes)) BitmapFactory.decodeByteArray(bytes, 0, bytes.size) else null
            }.getOrNull()
        }
    }
    var zoomed by remember(asset) { mutableStateOf(false) }
    bitmap?.let { picture ->
        if (allowZoom) StudyButton(if (zoomed) "Thu ảnh" else "Phóng ảnh đoạn văn") { zoomed = !zoomed }
        val size = if (zoomed) Modifier.horizontalScroll(rememberScrollState()).width(650.dp) else Modifier.fillMaxWidth()
        Image(picture.asImageBitmap(), description, size.aspectRatio(picture.width.toFloat() / picture.height))
    } ?: Text("Đang mở ảnh hoặc ảnh không khả dụng.")
}
