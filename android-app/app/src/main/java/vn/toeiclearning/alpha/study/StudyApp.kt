package vn.toeiclearning.alpha.study

import android.net.Uri
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

private enum class StudyPage { HOME, UNGRADED, SESSION, HISTORY, REVIEW, SETTINGS, MOCK }

@Composable
internal fun StudyApp() {
    val context = LocalContext.current.applicationContext
    val store = remember(context) { StudyStore(context) }
    val scope = rememberCoroutineScope()
    var page by remember { mutableStateOf(StudyPage.HOME) }
    var returnFromSession by remember { mutableStateOf(StudyPage.HOME) }
    var pack by remember { mutableStateOf<StudyPack?>(null) }
    var dashboard by remember { mutableStateOf<StudyDashboard?>(null) }
    var session by remember { mutableStateOf<StudyAttempt?>(null) }
    var busy by remember { mutableStateOf(false) }
    var error by remember { mutableStateOf<String?>(null) }
    var clearDialog by remember { mutableStateOf(false) }
    var goalInput by remember { mutableStateOf("") }
    fun day() = LocalDate.now().toString()
    fun mockTime() = MockTime(
        runCatching { Settings.Global.getInt(context.contentResolver, Settings.Global.BOOT_COUNT, -1) }.getOrDefault(-1),
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

    fun start(groups: List<StudyGroup>, position: Int = 0) {
        val origin = page
        runLocal({ store.start(groups, position) to store.dashboard(day()) }) { (attempt, stats) ->
            session = attempt
            dashboard = stats
            returnFromSession = origin
            page = StudyPage.SESSION
        }
    }

    fun continueAttempt(id: Long) {
        val currentPack = pack
        val origin = page
        runLocal({
            val previous = checkNotNull(store.attempt(id))
            val time = mockTime()
            val mock = previous.mock
            val checked = if (!previous.complete && mock != null &&
                (currentPack?.mocks?.ready != true ||
                    currentPack.forms.none { it.id == mock.form && it.version == mock.version })
            ) previous.finish(time.wall, interrupted = true)
            else previous.retainCurrentPracticeKeys(currentPack?.groups.orEmpty()).advanceMock(time, recovering = true)
            (if (previous == checked) previous else store.save(checked, day(), updateSnapshot = previous.groups != checked.groups)) to
                store.dashboard(day())
        }) { (saved, stats) ->
            session = saved
            dashboard = stats
            clock = mockTime()
            returnFromSession = if (origin == StudyPage.HOME && saved.mock == null && saved.items.none { it.key != null })
                StudyPage.UNGRADED else origin
            page = StudyPage.SESSION
        }
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

    BackHandler(enabled = page != StudyPage.HOME && page != StudyPage.SESSION) {
        refresh(if (page == StudyPage.REVIEW) StudyPage.HISTORY else StudyPage.HOME)
    }

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
                StudyPage.HOME -> StudyHome(pack!!, dashboard!!, busy, ::continueAttempt,
                    onStart = { start(it) },
                    onUngraded = { page = StudyPage.UNGRADED },
                    onMock = { page = StudyPage.MOCK })
                StudyPage.UNGRADED -> StudyPageContent {
                    StudyHeading("Luyện chưa chấm", onBack = { page = StudyPage.HOME })
                    Text("Bài luyện vẫn lưu lựa chọn và lịch sử. Điểm số chỉ có ở bài đã xác minh đáp án.")
                    StudyPartList(studyPracticeGroups(pack!!.groups, scored = false),
                        dashboard!!.active == null && !busy, scored = false, onStart = { start(it) })
                }
                StudyPage.SESSION -> session?.let { attempt ->
                    StudySession(
                        attempt, busy,
                        marked = dashboard!!.reviews.any { it.item.id == attempt.item.id && it.marked },
                        clock = clock,
                        returnLabel = when (returnFromSession) {
                            StudyPage.HISTORY -> "Về tiến độ"
                            StudyPage.REVIEW -> "Về ôn tập"
                            StudyPage.UNGRADED -> "Về bài chưa chấm"
                            else -> "Về luyện tập"
                        },
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
                        onBack = { current ->
                            if (!attempt.complete && attempt.mock?.pendingAudio != null) {
                                saveAttempt(attempt.finish(System.currentTimeMillis(), interrupted = true))
                            } else if (!attempt.complete && attempt.mock == null && current != attempt) {
                                runLocal({
                                    store.save(current, day())
                                    store.dashboard(day())
                                }) {
                                    dashboard = it
                                    page = returnFromSession
                                }
                            } else refresh(returnFromSession)
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
                        val currentGroup = pack!!.groups.firstOrNull { group ->
                            group.id == row.group.id && group.items.any { it.id == row.item.id }
                        }
                        Text("Part ${row.group.part} · Câu ${row.item.number}", style = MaterialTheme.typography.titleMedium)
                        Text(listOfNotNull(if (row.wrong) "Câu sai" else null, if (row.marked) "Đã đánh dấu" else null).joinToString(" · "))
                        Text(row.item.prompt)
                        if (currentGroup == null) Text("Câu này hiện không có trong ngân hàng luyện tập.")
                        else StudyButton("Luyện lại câu ${row.item.number}", !busy && dashboard!!.active == null) {
                            start(listOf(currentGroup), currentGroup.items.indexOfFirst { it.id == row.item.id })
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
                                    returnFromSession = StudyPage.HOME
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
    onResume: (Long) -> Unit, onStart: (List<StudyGroup>) -> Unit, onUngraded: () -> Unit, onMock: () -> Unit,
) = StudyPageContent {
    val scored = remember(pack) { studyPracticeGroups(pack.groups, scored = true) }
    val scoreable = scored.sumOf { it.items.size }
    val ungraded = pack.groups.sumOf { it.items.size } - scoreable
    StudyHeading("Luyện có chấm điểm")
    Text("Hôm nay ${dashboard.today}/${dashboard.goal} câu", style = MaterialTheme.typography.titleMedium)
    val parts = scored.map { it.part }.toSet()
    val active = dashboard.active
    if (active != null) {
        val title = active.mock?.let { run -> "đề ${run.form}" } ?: "Part ${active.group.part}"
        StudyButton("Tiếp tục $title · Câu ${active.item.number}", !busy, primary = true) { onResume(active.id) }
    } else {
        recommendedPart(parts, dashboard.stats)?.let { part ->
            val partStats = dashboard.stats.firstOrNull { it.part == part }
            val reason = if ((partStats?.wrong ?: 0) > 0) "độ chính xác thấp nhất trong các Part có câu sai"
            else "ít câu đã chấm nhất"
            val lesson = dailyStudyBatches(scored.filter { it.part == part }
                .groupBy { it.source to it.version }.values.first()).first()
            Text("Gợi ý Part $part · $reason")
            StudyButton("Luyện Part $part theo gợi ý", !busy, onClick = { onStart(lesson) })
        }
    }
    if (pack.unavailable || pack.skipped > 0) Notice("Một phần học liệu chưa mở được. Hãy kiểm tra gói nội dung.", warning = true)
    Text("$scoreable câu có thể chấm điểm")
    if (ungraded > 0) StudyButton("Luyện chưa chấm · $ungraded câu", !busy, onClick = onUngraded)
    StudyPartList(scored, dashboard.active == null && !busy, scored = true, onStart = onStart)
    StudyButton("Full Mock A / B", !busy, onClick = onMock)
}

@Composable
private fun StudyPartList(
    groups: List<StudyGroup>, enabled: Boolean, scored: Boolean, onStart: (List<StudyGroup>) -> Unit,
) {
    for ((part, partGroups) in groups.groupBy { it.part }.toSortedMap()) {
        val count = partGroups.sumOf { it.items.size }
        Text("Part $part · ${if (part <= 4) "Listening" else "Reading"}", style = MaterialTheme.typography.titleMedium)
        Text("$count câu ${if (scored) "chấm được" else "chưa chấm"}")
        val editions = partGroups.groupBy { it.source to it.version }.values
        val publisherCounts = editions.groupingBy { studyPublisher(it.first().source) }.eachCount()
        for (edition in editions) {
            val first = edition.first()
            val repeatedPublisher = (publisherCounts[studyPublisher(first.source)] ?: 0) > 1
            val label = when {
                first.source == VOA_SUPPLEMENTAL_SOURCE -> "Luyện nghe bổ sung · VOA Learning English"
                !scored && editions.size == 1 -> "Luyện Part $part"
                else -> "Luyện Part $part · ${studyEditionLabel(first, repeatedPublisher)}"
            }
            val batches = dailyStudyBatches(edition)
            batches.forEachIndexed { index, batch ->
                val title = if (batches.size == 1) label else "$label · lượt ${index + 1}"
                StudyButton(title, enabled) { onStart(batch) }
            }
        }
        HorizontalDivider()
    }
}

internal fun studyPublisher(source: String): String =
    if (source.startsWith(OCEAN_SOURCE_PREFIX)) "TOEIC Question Ocean"
    else Uri.parse(source).host?.removePrefix("www.") ?: source

private fun studyEditionLabel(group: StudyGroup, showEdition: Boolean): String {
    val publisher = studyPublisher(group.source)
    if (!showEdition) return publisher
    if (group.source.startsWith(OCEAN_SOURCE_PREFIX)) return "$publisher · ${group.version.take(8)}"
    val edition = Uri.parse(group.source).lastPathSegment?.takeIf(String::isNotBlank)
    return if (edition == null) "$publisher · ${group.version.take(8)}"
    else "$publisher · $edition · ${group.version.take(8)}"
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
        val ungraded = dashboard.stats.sumOf { it.attempted - it.graded }
        if (ungraded > 0) Text("$ungraded câu đã trả lời chưa chấm")
        Text("Lịch sử", style = MaterialTheme.typography.titleLarge)
        if (dashboard.history.isEmpty()) Text("Chưa có bài đã hoàn thành.")
        dashboard.history.forEach { item ->
            val date = Instant.ofEpochMilli(item.endedAt).atZone(ZoneId.systemDefault())
                .format(DateTimeFormatter.ofPattern("dd/MM HH:mm"))
            val title = if (item.part == 0) "Full Mock" else "Part ${item.part}"
            val tally = if (item.score.graded > 0) "${item.score.correct}/${item.score.graded} đúng"
            else if (item.score.ungraded > 0) "chưa chấm" else "chưa trả lời"
            StudyButton("$title · $date · ${item.score.attempted}/${item.score.total} đã trả lời · $tally", !busy) { onOpen(item.id) }
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
