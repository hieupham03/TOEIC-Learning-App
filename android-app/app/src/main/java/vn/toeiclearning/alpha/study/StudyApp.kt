package vn.toeiclearning.alpha.study

import android.os.SystemClock
import android.provider.Settings
import androidx.activity.compose.BackHandler
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ColumnScope
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.WindowInsets
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.safeDrawing
import androidx.compose.foundation.layout.widthIn
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Button
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import java.time.Instant
import java.time.LocalDate
import java.time.ZoneId
import java.time.format.DateTimeFormatter
import kotlinx.coroutines.CancellationException
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import vn.toeiclearning.alpha.ui.AlphaTokens
import vn.toeiclearning.alpha.ui.Notice

private enum class StudyPage { HOME, SESSION, HISTORY, REVIEW, SETTINGS, MOCK }

@Composable
internal fun StudyApp() {
    val context = LocalContext.current.applicationContext
    val store = remember(context) { StudyStore(context) }
    val scope = rememberCoroutineScope()
    var page by remember { mutableStateOf(StudyPage.HOME) }
    var pack by remember { mutableStateOf<StudyPack?>(null) }
    var dashboard by remember { mutableStateOf<StudyDashboard?>(null) }
    var session by remember { mutableStateOf<StudyAttempt?>(null) }
    var busy by remember { mutableStateOf(false) }
    var error by remember { mutableStateOf<String?>(null) }
    var clearDialog by remember { mutableStateOf(false) }
    var goalInput by remember { mutableStateOf("") }
    fun day() = LocalDate.now().toString()
    fun mockTime() = MockTime(
        Settings.Global.getInt(context.contentResolver, Settings.Global.BOOT_COUNT, -1),
        SystemClock.elapsedRealtime(), System.currentTimeMillis(),
    )
    var clock by remember { mutableStateOf(mockTime()) }

    fun <T> runLocal(action: () -> T, update: (T) -> Unit) {
        if (busy) return
        busy = true
        error = null
        scope.launch {
            try {
                val result = withContext(Dispatchers.IO) { action() }
                update(result)
            } catch (cancel: CancellationException) {
                throw cancel
            } catch (_: Exception) {
                error = "Không thể đọc hoặc lưu dữ liệu. Kiểm tra dung lượng rồi thử lại."
            } finally {
                busy = false
            }
        }
    }

    fun refresh(destination: StudyPage = page) = runLocal({ store.dashboard(day()) }) {
        dashboard = it
        page = destination
        if (goalInput.isBlank()) goalInput = it.goal.toString()
    }

    fun start(groups: List<StudyGroup>, position: Int = 0) =
        runLocal({ store.start(groups, position) to store.dashboard(day()) }) { (attempt, stats) ->
            session = attempt
            dashboard = stats
            page = StudyPage.SESSION
        }

    fun continueAttempt(id: Long) = runLocal({
        val previous = checkNotNull(store.attempt(id))
        val checked = previous.advanceMock(mockTime(), recovering = true)
        (if (previous == checked) previous else store.save(checked, day())) to store.dashboard(day())
    }) { (saved, stats) ->
        session = saved
        dashboard = stats
        clock = mockTime()
        page = StudyPage.SESSION
    }

    fun saveAttempt(next: StudyAttempt) = runLocal({
        store.save(next, day()) to if (next.complete) store.dashboard(day()) else null
    }) { (saved, fresh) ->
        session = saved
        if (fresh != null) dashboard = fresh
    }

    LaunchedEffect(page, session?.id) {
        while (page == StudyPage.SESSION && session?.mock != null && session?.complete == false) {
            val attempt = checkNotNull(session)
            clock = mockTime()
            val advanced = attempt.advanceMock(clock)
            if (advanced != attempt) saveAttempt(advanced)
            delay(500)
        }
    }

    LaunchedEffect(store) {
        runLocal({ loadStudyPack(context.assets) to store.dashboard(day()) }) { (newPack, stats) ->
            pack = newPack
            dashboard = stats
            goalInput = stats.goal.toString()
        }
    }

    BackHandler(enabled = page != StudyPage.HOME && page != StudyPage.SESSION) { refresh(StudyPage.HOME) }

    Scaffold(
        containerColor = AlphaTokens.Background,
        contentWindowInsets = WindowInsets.safeDrawing,
        bottomBar = {
            if (page != StudyPage.SESSION) Surface(color = AlphaTokens.Surface) {
                Row(Modifier.fillMaxWidth().navigationBarsPadding().padding(horizontal = 8.dp)) {
                    listOf(StudyPage.HOME to "Luyện tập", StudyPage.HISTORY to "Tiến độ", StudyPage.SETTINGS to "Cá nhân")
                        .forEach { (destination, title) ->
                            TextButton(onClick = { refresh(destination) }, enabled = !busy,
                                modifier = Modifier.weight(1f).heightIn(min = 48.dp)) { Text(title) }
                        }
                }
            }
        },
    ) { padding ->
        Column(Modifier.fillMaxSize().padding(padding)) {
            error?.let { Notice(it, warning = true) }
            if (dashboard == null || pack == null) {
                StudyPageContent {
                    StudyHeading("Học tập trên thiết bị")
                    Text(if (busy) "Đang mở dữ liệu…" else "Không mở được dữ liệu.")
                    if (!busy) StudyButton("Thử lại") {
                        runLocal({ loadStudyPack(context.assets) to store.dashboard(day()) }) { (p, d) ->
                            pack = p
                            dashboard = d
                            goalInput = d.goal.toString()
                        }
                    }
                }
            } else when (page) {
                StudyPage.HOME -> StudyHome(pack!!, dashboard!!, busy, ::continueAttempt, { start(it) }) {
                    page = StudyPage.MOCK
                }
                StudyPage.SESSION -> session?.let { attempt ->
                    StudySession(
                        attempt, busy,
                        marked = dashboard!!.reviews.any { it.item.id == attempt.item.id && it.marked },
                        clock = clock,
                        onChange = { next ->
                            if (attempt.complete) session = next
                            else if (attempt.mock == null) saveAttempt(next)
                            else {
                                val currentTime = mockTime()
                                val advanced = attempt.advanceMock(currentTime)
                                val sameSection = (next.group.part <= 4) ==
                                    (attempt.mock.phase(currentTime) == MockPhase.LISTENING)
                                if (advanced != attempt) saveAttempt(advanced)
                                else if (sameSection || next.complete) saveAttempt(next)
                            }
                        },
                        onBookmark = {
                            runLocal({ store.toggleBookmark(attempt.group, attempt.item.id); store.dashboard(day()) }) {
                                dashboard = it
                            }
                        },
                        onBack = {
                            if (!attempt.complete && attempt.mock?.pendingAudio != null) {
                                saveAttempt(attempt.finish(System.currentTimeMillis(), interrupted = true))
                            } else refresh(StudyPage.HOME)
                        },
                    )
                }
                StudyPage.HISTORY -> StudyHistoryPage(dashboard!!, busy, ::continueAttempt) { page = StudyPage.REVIEW }
                StudyPage.REVIEW -> StudyPageContent {
                    StudyHeading("Ôn tập", onBack = { page = StudyPage.HISTORY })
                    val reviews = dashboard!!.reviews
                    if (reviews.isEmpty()) Text("Chưa có câu sai đã chấm hoặc câu đánh dấu.")
                    if (dashboard!!.active != null) Notice("Hoàn thành bài đang làm trước khi bắt đầu ôn.")
                    reviews.forEach { row ->
                        Text("Part ${row.group.part} · Câu ${row.item.number}", style = MaterialTheme.typography.titleMedium)
                        Text(listOfNotNull(if (row.wrong) "Câu sai" else null, if (row.marked) "Đã đánh dấu" else null).joinToString(" · "))
                        Text(row.item.prompt)
                        StudyButton("Luyện lại câu ${row.item.number}", !busy && dashboard!!.active == null) {
                            start(listOf(row.group), row.group.items.indexOf(row.item))
                        }
                        HorizontalDivider()
                    }
                }
                StudyPage.SETTINGS -> StudyPageContent {
                    StudyHeading("Cá nhân")
                    Text("Tiến độ và lựa chọn được lưu trên điện thoại này. Mỗi máy có dữ liệu riêng.")
                    OutlinedTextField(goalInput, { value -> if (value.length <= 3 && value.all(Char::isDigit)) goalInput = value },
                        label = { Text("Mục tiêu mỗi ngày (số câu)") }, singleLine = true, modifier = Modifier.fillMaxWidth())
                    val goal = goalInput.toIntOrNull()
                    StudyButton("Lưu mục tiêu", !busy && goal != null && goal in 1..200) {
                        runLocal({ store.setGoal(checkNotNull(goal)); store.dashboard(day()) }) { dashboard = it }
                    }
                    StudyButton("Xóa dữ liệu học tập", !busy) { clearDialog = true }
                }
                StudyPage.MOCK -> StudyPageContent {
                    StudyHeading("Full Mock A / B", onBack = { page = StudyPage.HOME })
                    val current = checkNotNull(pack)
                    if (!current.mocks.ready) {
                        Notice("Full Mock đang khóa.", warning = true)
                        for ((id, missing) in current.mocks.missing) Text("Đề $id · thiếu $missing/200 câu đã kiểm chứng")
                        current.mocks.issues.forEach { Text(it) }
                    } else {
                        Text("Mỗi đề 200 câu · 45 phút Listening và 75 phút Reading. Thời gian tính trên thiết bị.")
                        Text("Audio theo thứ tự và phát một lần. Gián đoạn khi đang phát sẽ kết thúc bài và giữ lựa chọn.")
                        if (dashboard!!.active != null) Text("Hoàn thành bài đang làm trước khi bắt đầu đề khác.")
                        current.forms.sortedBy { it.id }.forEach { form ->
                            StudyButton("Bắt đầu đề ${form.id}", dashboard!!.active == null && !busy) {
                                val time = mockTime()
                                if (time.boot < 0) error = "Thiết bị không cung cấp mốc khởi động. Chưa thể bắt đầu đề."
                                else runLocal({
                                    val run = MockRun(form.id, form.version, time.boot, time.elapsed)
                                    val started = store.start(form.groups, mock = run)
                                    started to store.dashboard(day())
                                }) { (attempt, stats) ->
                                    session = attempt
                                    dashboard = stats
                                    clock = time
                                    page = StudyPage.SESSION
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    if (clearDialog) AlertDialog(
        onDismissRequest = { clearDialog = false },
        title = { Text("Xóa dữ liệu học tập?") },
        text = { Text("Bài đang làm, lịch sử, câu đánh dấu và mục tiêu trên máy này sẽ bị xóa.") },
        confirmButton = {
            TextButton(onClick = {
                clearDialog = false
                runLocal({ store.clear(); store.dashboard(day()) }) {
                    dashboard = it
                    session = null
                    goalInput = it.goal.toString()
                }
            }) { Text("Xác nhận xóa") }
        },
        dismissButton = { TextButton(onClick = { clearDialog = false }) { Text("Hủy") } },
    )
}

@Composable
private fun StudyHome(
    pack: StudyPack, dashboard: StudyDashboard, busy: Boolean,
    onResume: (Long) -> Unit, onStart: (List<StudyGroup>) -> Unit, onMock: () -> Unit,
) = StudyPageContent {
    StudyHeading("Luyện tập")
    Text("Hôm nay ${dashboard.today}/${dashboard.goal} câu", style = MaterialTheme.typography.titleMedium)
    val byPart = pack.groups.groupBy { it.part }
    val suggestion = recommendedPart(byPart.keys, dashboard.stats)
    if (suggestion != null) {
        val reason = if (dashboard.stats.any { it.part in byPart && it.wrong > 0 }) "tỷ lệ đúng thấp trong các Part đã chấm"
        else "Part khả dụng có ít câu đã luyện nhất"
        Text("Gợi ý Part $suggestion · $reason")
    }
    dashboard.active?.let {
        val title = it.mock?.let { run -> "đề ${run.form}" } ?: "Part ${it.group.part}"
        StudyButton("Tiếp tục $title · Câu ${it.item.number}", !busy, primary = true) { onResume(it.id) }
    }
    if (pack.unavailable || pack.skipped > 0) Notice("Một phần học liệu chưa mở được. Hãy kiểm tra gói nội dung.", warning = true)
    (1..7).forEach { part ->
        val groups = byPart[part].orEmpty()
        val items = groups.flatMap { it.items }
        Text("Part $part · ${if (part <= 4) "Listening" else "Reading"}", style = MaterialTheme.typography.titleMedium)
        Text("${items.size} câu khả dụng · ${items.count { it.key != null }} có đáp án đã xác minh")
        StudyButton("Luyện Part $part", groups.isNotEmpty() && dashboard.active == null && !busy) { onStart(groups) }
        HorizontalDivider()
    }
    StudyButton("Full Mock A / B", !busy, onClick = onMock)
}

@Composable
private fun StudyHistoryPage(dashboard: StudyDashboard, busy: Boolean, onOpen: (Long) -> Unit, onReview: () -> Unit) =
    StudyPageContent {
        StudyHeading("Tiến độ")
        Text("Hôm nay ${dashboard.today}/${dashboard.goal} câu")
        StudyButton("Câu sai và đánh dấu", !busy, onClick = onReview)
        if (dashboard.stats.none { it.graded > 0 }) Text("Chưa có câu đã chấm bằng đáp án xác minh.")
        dashboard.stats.filter { it.graded > 0 }.forEach { row ->
            Text("Part ${row.part} · ${row.correct} đúng, ${row.wrong} sai · ${row.correct * 100 / row.graded}%")
        }
        Text("Lịch sử", style = MaterialTheme.typography.titleLarge)
        if (dashboard.history.isEmpty()) Text("Chưa có bài đã hoàn thành.")
        dashboard.history.forEach { item ->
            val date = Instant.ofEpochMilli(item.endedAt).atZone(ZoneId.systemDefault())
                .format(DateTimeFormatter.ofPattern("dd/MM HH:mm"))
            val title = if (item.part == 0) "Full Mock" else "Part ${item.part}"
            StudyButton("$title · $date · ${item.score.attempted}/${item.score.total} đã trả lời", !busy) { onOpen(item.id) }
        }
    }

@Composable
internal fun StudyPageContent(content: @Composable ColumnScope.() -> Unit) {
    Box(Modifier.fillMaxSize(), contentAlignment = Alignment.TopCenter) {
        Column(Modifier.widthIn(max = 720.dp).fillMaxWidth().verticalScroll(rememberScrollState()).padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp), content = content)
    }
}

@Composable
internal fun StudyHeading(title: String, onBack: (() -> Unit)? = null) {
    if (onBack != null) TextButton(onBack, Modifier.heightIn(min = 48.dp)) { Text("Quay lại") }
    Text(title, style = MaterialTheme.typography.headlineMedium)
}

@Composable
internal fun StudyButton(label: String, enabled: Boolean = true, primary: Boolean = false, onClick: () -> Unit) {
    val modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp)
    if (primary) Button(onClick, modifier, enabled) { Text(label) }
    else OutlinedButton(onClick, modifier, enabled) { Text(label) }
}
