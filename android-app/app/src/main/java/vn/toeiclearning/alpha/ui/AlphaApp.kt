package vn.toeiclearning.alpha.ui

import androidx.activity.compose.BackHandler
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.clickable
import androidx.compose.foundation.selection.selectable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.layout.widthIn
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.RadioButton
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.key
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.semantics.clearAndSetSemantics
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import vn.toeiclearning.alpha.domain.PracticeRules
import vn.toeiclearning.alpha.domain.PracticeState
import vn.toeiclearning.alpha.domain.ReadingContext
import vn.toeiclearning.alpha.domain.ReadingPane
import vn.toeiclearning.alpha.domain.ReadingSession
import vn.toeiclearning.alpha.domain.SyntheticCatalogue
import vn.toeiclearning.alpha.domain.SyntheticQuestion

private enum class AlphaRoute { HOME, PARTS, PRACTICE, READING, MOCK_INFO, PROGRESS, PROFILE }
private enum class AlphaTab(val title: String) { START("Bắt đầu"), PROGRESS("Tiến độ"), PROFILE("Cá nhân") }
private val contentPadding = 20.dp

@Composable
fun AlphaApp() {
    var route by rememberSaveable { mutableStateOf(AlphaRoute.HOME) }
    var part by rememberSaveable { mutableIntStateOf(5) }

    val activeTab = when (route) {
        AlphaRoute.PROGRESS -> AlphaTab.PROGRESS
        AlphaRoute.PROFILE -> AlphaTab.PROFILE
        else -> AlphaTab.START
    }

    BackHandler(enabled = route != AlphaRoute.HOME) {
        route = when (route) {
            AlphaRoute.PRACTICE, AlphaRoute.READING -> AlphaRoute.PARTS
            AlphaRoute.MOCK_INFO -> AlphaRoute.HOME
            else -> AlphaRoute.HOME
        }
    }

    Scaffold(
        containerColor = AlphaTokens.Background,
        bottomBar = {
            Surface(color = AlphaTokens.Surface, shadowElevation = 1.dp) {
                Row(
                    modifier = Modifier.fillMaxWidth().padding(horizontal = 12.dp, vertical = 8.dp),
                    horizontalArrangement = Arrangement.spacedBy(6.dp),
                ) {
                    AlphaTab.entries.forEach { tab ->
                        val selected = activeTab == tab
                        val target = when (tab) {
                            AlphaTab.START -> AlphaRoute.HOME
                            AlphaTab.PROGRESS -> AlphaRoute.PROGRESS
                            AlphaTab.PROFILE -> AlphaRoute.PROFILE
                        }
                        TextButton(
                            onClick = { route = target },
                            modifier = Modifier.weight(1f).heightIn(min = 48.dp),
                            colors = ButtonDefaults.textButtonColors(
                                contentColor = if (selected) AlphaTokens.Primary else AlphaTokens.Secondary,
                            ),
                        ) {
                            Text(
                                tab.title,
                                fontWeight = if (selected) FontWeight.Bold else FontWeight.Medium,
                            )
                        }
                    }
                }
            }
        },
    ) { innerPadding ->
        Box(modifier = Modifier.fillMaxSize().padding(innerPadding)) {
            when (route) {
                AlphaRoute.HOME -> TaskHub(
                    onParts = { route = AlphaRoute.PARTS },
                    onMock = { route = AlphaRoute.MOCK_INFO },
                )
                AlphaRoute.PARTS -> PartPicker(
                    onBack = { route = AlphaRoute.HOME },
                    onPart = { selected ->
                        if (SyntheticCatalogue.canStartAlphaPart(selected)) {
                            part = selected
                            route = if (selected in 6..7) AlphaRoute.READING else AlphaRoute.PRACTICE
                        }
                    },
                )
                AlphaRoute.PRACTICE -> key(part) {
                    PracticeScreen(part = part, onBack = { route = AlphaRoute.PARTS })
                }
                AlphaRoute.READING -> key(part) {
                    ReadingScreen(part = part, onBack = { route = AlphaRoute.PARTS })
                }
                AlphaRoute.MOCK_INFO -> MockBlockedScreen(onBack = { route = AlphaRoute.HOME })
                AlphaRoute.PROGRESS -> PlaceholderScreen(
                    title = "Tiến độ",
                    subtitle = "Chưa có kết quả người học",
                    details = "Alpha chỉ thử nghiệm giao diện bằng dữ liệu giả. Không có lịch sử học, chấm điểm, đồng bộ hoặc tài khoản.",
                )
                AlphaRoute.PROFILE -> PlaceholderScreen(
                    title = "Cá nhân",
                    subtitle = "Không thu thập dữ liệu cá nhân",
                    details = "Alpha chưa có đăng nhập, nơi lưu trữ dữ liệu thực hoặc chức năng xóa dữ liệu. Các nghĩa vụ riêng tư của MVP sẽ được kiểm chứng ở giai đoạn được phê duyệt sau.",
                )
            }
        }
    }
}

@Composable
private fun ScreenHeader(title: String, onBack: (() -> Unit)? = null) {
    Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
        if (onBack != null) {
            TextButton(onClick = onBack, modifier = Modifier.heightIn(min = 48.dp)) {
                Text("Quay lại")
            }
        }
        Text(title, style = MaterialTheme.typography.headlineMedium)
        Text(
            "ALPHA · Nội dung giả lập · Chưa QA học liệu",
            color = AlphaTokens.Secondary,
            style = MaterialTheme.typography.bodyMedium,
        )
    }
}

@Composable
private fun Notice(message: String, warning: Boolean = false) {
    Surface(
        color = if (warning) AlphaTokens.WarningBackground else AlphaTokens.Muted,
        shape = RoundedCornerShape(12.dp),
    ) {
        Text(
            text = message,
            color = if (warning) AlphaTokens.Warning else AlphaTokens.Ink,
            modifier = Modifier.fillMaxWidth().padding(14.dp),
            style = MaterialTheme.typography.bodyMedium,
        )
    }
}

@Composable
private fun TaskHub(onParts: () -> Unit, onMock: () -> Unit) {
    Column(
        modifier = Modifier.fillMaxSize().verticalScroll(rememberScrollState())
            .padding(horizontal = contentPadding, vertical = 24.dp),
        verticalArrangement = Arrangement.spacedBy(20.dp),
    ) {
        ScreenHeader(title = "Hôm nay học gì?")
        Text(
            "Chọn cách học phù hợp. Bản Alpha chưa có dữ liệu tiến độ thật.",
            color = AlphaTokens.Secondary,
        )
        HorizontalDivider()
        Text("Bắt đầu", style = MaterialTheme.typography.titleLarge)
        ModeCard(
            title = "Luyện theo Part",
            description = "Khám phá Part 1–7. Chỉ Part 5–7 có nội dung minh họa trong Alpha.",
            buttonText = "Xem các Part",
            onClick = onParts,
        )
        ModeCard(
            title = "Full Mock A / B",
            description = "Hai đề B1 bắt buộc, mỗi đề 200 câu. Chưa QA và không thể làm thi thật trong Alpha.",
            buttonText = "Xem điều kiện mở thi",
            onClick = onMock,
        )
        Notice("Không có câu hỏi, điểm, thời gian thi hoặc lưu đáp án thật trong bản Alpha này.")
    }
}

@Composable
private fun ModeCard(title: String, description: String, buttonText: String, onClick: () -> Unit) {
    Surface(
        shape = RoundedCornerShape(14.dp),
        border = BorderStroke(1.dp, AlphaTokens.Outline),
        color = AlphaTokens.Surface,
    ) {
        Column(
            modifier = Modifier.padding(18.dp).fillMaxWidth(),
            verticalArrangement = Arrangement.spacedBy(12.dp),
        ) {
            Text(title, style = MaterialTheme.typography.titleMedium)
            Text(description, color = AlphaTokens.Secondary)
            OutlinedButton(
                onClick = onClick,
                modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp),
            ) { Text(buttonText) }
        }
    }
}

@Composable
private fun PartPicker(onBack: () -> Unit, onPart: (Int) -> Unit) {
    LazyColumn(
        modifier = Modifier.fillMaxSize(),
        contentPadding = androidx.compose.foundation.layout.PaddingValues(
            horizontal = contentPadding, vertical = 16.dp,
        ),
        verticalArrangement = Arrangement.spacedBy(14.dp),
    ) {
        item { ScreenHeader("Luyện theo Part", onBack) }
        item { Notice("Đây là ngân hàng DEMO tách biệt B1 Full Mock A/B. 'Mở demo' không có nghĩa là học liệu đã QA.") }
        items(SyntheticCatalogue.parts, key = { it.number }) { part ->
            Column(modifier = Modifier.fillMaxWidth()) {
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Column(modifier = Modifier.weight(1f)) {
                        Text("Part ${part.number} · ${part.title}", style = MaterialTheme.typography.titleMedium)
                        Text(part.mode, color = AlphaTokens.Secondary)
                    }
                    Spacer(Modifier.width(12.dp))
                    OutlinedButton(
                        onClick = { onPart(part.number) },
                        enabled = part.canEnterSyntheticAlpha,
                        modifier = Modifier.heightIn(min = 48.dp),
                    ) { Text(if (part.canEnterSyntheticAlpha) "Mở demo" else "Chưa QA") }
                }
                Text(
                    if (part.canEnterSyntheticAlpha) "Chỉ có ví dụ giả lập · không phải nội dung đã kiểm duyệt"
                    else "Chưa có dữ liệu và kiểm duyệt nội dung · bị chặn",
                    color = AlphaTokens.Secondary,
                    style = MaterialTheme.typography.bodyMedium,
                )
                Spacer(Modifier.height(10.dp))
                HorizontalDivider()
            }
        }
    }
}

@Composable
private fun PracticeScreen(part: Int, onBack: () -> Unit) {
    val questions = remember(part) { SyntheticCatalogue.questions(part) }
    var index by rememberSaveable(part) { mutableIntStateOf(0) }
    var practice by remember(part) { mutableStateOf(PracticeState()) }
    if (part != 5 || questions.isEmpty()) {
        PlaceholderScreen("Chưa có học liệu", "Không thể bắt đầu", "Không có nội dung giả lập hợp lệ cho Part này.")
        return
    }
    val question = questions[index.coerceIn(0, questions.lastIndex)]
    Column(
        modifier = Modifier.fillMaxSize().verticalScroll(rememberScrollState())
            .padding(horizontal = contentPadding, vertical = 16.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp),
    ) {
        ScreenHeader("Part 5 · Luyện thử", onBack)
        Notice("Câu hỏi tự tạo để thử UI, không phải TOEIC thật. Đáp án chỉ được chọn tạm trong bộ nhớ; CHƯA LƯU.")
        Text("Câu ${index + 1}/${questions.size}", color = AlphaTokens.Secondary)
        QuestionPanel(
            question = question,
            state = practice,
            onSelect = { choice -> practice = PracticeRules.select(practice, question, choice) },
            onReveal = { practice = PracticeRules.requestFeedback(practice, question) },
        )
        Button(
            onClick = { index = (index + 1) % questions.size },
            modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp),
        ) {
            Text(if (index == questions.lastIndex) "Xem lại câu đầu" else "Câu tiếp theo")
        }
    }
}

@Composable
private fun QuestionPanel(
    question: SyntheticQuestion,
    state: PracticeState,
    onSelect: (Int) -> Unit,
    onReveal: () -> Unit,
) {
    val selection = state.selectedById[question.id]
    val feedback = PracticeRules.feedback(state, question)
    Column(verticalArrangement = Arrangement.spacedBy(12.dp)) {
        Text(question.prompt, style = MaterialTheme.typography.titleMedium)
        question.choices.forEachIndexed { index, choice ->
            Surface(
                modifier = Modifier.fillMaxWidth().heightIn(min = 56.dp),
                shape = RoundedCornerShape(12.dp),
                border = BorderStroke(
                    width = if (selection == index) 2.dp else 1.dp,
                    color = if (selection == index) AlphaTokens.Primary else AlphaTokens.Outline,
                ),
                color = AlphaTokens.Surface,
            ) {
                Row(
                    modifier = Modifier.fillMaxWidth()
                        .selectable(
                            selected = selection == index,
                            enabled = feedback == null,
                            role = Role.RadioButton,
                            onClick = { onSelect(index) },
                        )
                        .semantics { contentDescription = "Đáp án ${('A' + index)}: $choice" }
                        .padding(12.dp),
                    verticalAlignment = Alignment.CenterVertically,
                ) {
                    RadioButton(
                        selected = selection == index,
                        onClick = null, // Entire labelled answer row is the single action target.
                        modifier = Modifier.clearAndSetSemantics { },
                    )
                    Spacer(Modifier.width(10.dp))
                    Text("${'A' + index}. $choice", style = MaterialTheme.typography.bodyLarge)
                }
            }
        }
        Text("${if (selection == null) "Chưa chọn" else "Đã chọn trên màn hình"} · chưa lưu bền vững",
            color = AlphaTokens.Secondary, style = MaterialTheme.typography.bodyMedium)
        if (feedback == null) {
            Button(
                onClick = onReveal,
                enabled = selection != null,
                modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp),
            ) { Text("Xem giải thích mẫu") }
        } else {
            Notice(
                "${if (feedback.correct) "Đúng (ví dụ giả lập)" else "Chưa đúng (ví dụ giả lập)"}. " +
                    "Đáp án mẫu: ${feedback.correctText}. ${feedback.explanation}",
            )
        }
    }
}

@Composable
private fun ReadingScreen(part: Int, onBack: () -> Unit) {
    val passage = remember(part) { SyntheticCatalogue.passage(part) }
    val questions = remember(part) { SyntheticCatalogue.questions(part) }
    if (part !in 6..7 || passage == null || questions.isEmpty()) {
        PlaceholderScreen("Reading", "Chưa có dữ liệu", "Part này chưa có đoạn văn Alpha phù hợp.")
        return
    }

    var session by remember(part) {
        mutableStateOf(ReadingSession(ReadingPane.PASSAGE, ReadingContext(passage.id, questions.first().id)))
    }
    var answers by remember(part) { mutableStateOf(PracticeState()) }
    val passageScroll = rememberLazyListState()

    BackHandler(enabled = session.pane == ReadingPane.QUESTIONS) { session = session.returnToPassage() }
    LaunchedEffect(session.pane, session.context.itemIndex, session.context.itemOffset) {
        if (session.pane == ReadingPane.PASSAGE) {
            passageScroll.scrollToItem(
                index = session.context.itemIndex.coerceIn(0, passage.paragraphs.size),
                scrollOffset = session.context.itemOffset,
            )
        }
    }

    BoxWithConstraints(modifier = Modifier.fillMaxSize()) {
        val readingGutter = if (maxWidth < 400.dp) 16.dp else contentPadding
        // Cap the incoming width before filling the remaining space.
        Column(
            modifier = Modifier
                .widthIn(max = 720.dp)
                .fillMaxSize()
                .align(Alignment.TopCenter),
        ) {
            Column(
                modifier = Modifier.fillMaxWidth().padding(horizontal = readingGutter, vertical = 8.dp),
                verticalArrangement = Arrangement.spacedBy(8.dp),
            ) {
                ScreenHeader("Part $part · Reading", onBack)
                Notice("Đoạn văn và câu hỏi DEMO. Vị trí đọc được giữ trong phiên màn hình này, chưa kiểm chứng khôi phục sau Android process death.")
                if (session.pane == ReadingPane.PASSAGE) {
                    Button(
                        onClick = {
                            session = session.openQuestions(
                                passageScroll.firstVisibleItemIndex,
                                passageScroll.firstVisibleItemScrollOffset,
                            )
                        },
                        modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp),
                    ) { Text("Sang câu hỏi") }
                } else {
                    OutlinedButton(
                        onClick = { session = session.returnToPassage() },
                        modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp),
                    ) { Text("Về đoạn văn") }
                }
                Text(
                    if (session.pane == ReadingPane.PASSAGE) "Đang đọc · trở về đúng vị trí trong phiên"
                    else "Đang trả lời · có thể quay lại đoạn văn",
                    color = AlphaTokens.Secondary,
                    style = MaterialTheme.typography.bodyMedium,
                )
                HorizontalDivider()
            }
            if (session.pane == ReadingPane.PASSAGE) {
                LazyColumn(
                    modifier = Modifier.fillMaxWidth().weight(1f),
                    state = passageScroll,
                    contentPadding = androidx.compose.foundation.layout.PaddingValues(
                        start = readingGutter, end = readingGutter, bottom = 32.dp,
                    ),
                    verticalArrangement = Arrangement.spacedBy(18.dp),
                ) {
                    item { Text(passage.title, style = MaterialTheme.typography.titleMedium) }
                    itemsIndexed(
                        items = passage.paragraphs,
                        key = { index, _ -> "${passage.id}-$index" },
                    ) { _, paragraph ->
                        Text(paragraph, style = MaterialTheme.typography.bodyLarge)
                    }
                }
            } else {
                val chosen = questions.firstOrNull { it.id == session.context.questionId } ?: questions.first()
                Column(
                    modifier = Modifier.fillMaxWidth().weight(1f).verticalScroll(rememberScrollState())
                        .padding(horizontal = readingGutter, vertical = 10.dp),
                    verticalArrangement = Arrangement.spacedBy(16.dp),
                ) {
                    Text("Câu hỏi gắn với đoạn: ${passage.title}", color = AlphaTokens.Secondary)
                    LazyRow(
                        modifier = Modifier.fillMaxWidth()
                            .semantics { contentDescription = "Chọn câu hỏi gắn với đoạn văn" },
                        horizontalArrangement = Arrangement.spacedBy(8.dp),
                    ) {
                        itemsIndexed(questions, key = { _, question -> question.id }) { idx, question ->
                            val selected = chosen.id == question.id
                            if (selected) {
                                Button(
                                    onClick = { session = session.selectQuestion(question) },
                                    modifier = Modifier.heightIn(min = 48.dp)
                                        .semantics { contentDescription = "Câu hỏi ${idx + 1}, đang chọn" },
                                ) { Text("${idx + 1}") }
                            } else {
                                OutlinedButton(
                                    onClick = { session = session.selectQuestion(question) },
                                    modifier = Modifier.heightIn(min = 48.dp)
                                        .semantics { contentDescription = "Câu hỏi ${idx + 1}" },
                                ) { Text("${idx + 1}") }
                            }
                        }
                    }
                    QuestionPanel(
                        question = chosen,
                        state = answers,
                        onSelect = { i -> answers = PracticeRules.select(answers, chosen, i) },
                        onReveal = { answers = PracticeRules.requestFeedback(answers, chosen) },
                    )
                    OutlinedButton(
                        onClick = { session = session.returnToPassage() },
                        modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp),
                    ) { Text("Đọc lại đoạn văn") }
                }
            }
        }
    }
}

@Composable
private fun MockBlockedScreen(onBack: () -> Unit) {
    Column(
        modifier = Modifier.fillMaxSize().verticalScroll(rememberScrollState())
            .padding(horizontal = contentPadding, vertical = 20.dp),
        verticalArrangement = Arrangement.spacedBy(18.dp),
    ) {
        ScreenHeader("Full Mock A / B", onBack)
        Notice("CHƯA THỂ BẮT ĐẦU. Hai bộ đề B1 bắt buộc (mỗi đề 200 câu) mới được PO xác nhận kiểm kê; nội dung và ứng dụng chưa QA.", warning = true)
        Text("Điều kiện còn thiếu", style = MaterialTheme.typography.titleMedium)
        Text("• QA từng câu, đáp án, audio và phiên bản đề.\n• Bằng chứng thời gian và gián đoạn.\n• Xác nhận lưu bền vững, quyền riêng tư và các checkpoint được phê duyệt.")
        Notice("Bản Alpha không có đồng hồ thi thật, chấm điểm ETS, bằng chứng lưu chính thức hay nội dung B1.")
    }
}

@Composable
private fun PlaceholderScreen(title: String, subtitle: String, details: String) {
    Column(
        modifier = Modifier.fillMaxSize().verticalScroll(rememberScrollState())
            .padding(horizontal = contentPadding, vertical = 24.dp),
        verticalArrangement = Arrangement.spacedBy(18.dp),
    ) {
        ScreenHeader(title)
        Text(subtitle, style = MaterialTheme.typography.titleLarge)
        Text(details, color = AlphaTokens.Secondary)
        Notice("Chỉ là giao diện Alpha với dữ liệu giả. Không có dữ liệu người học, kiểm thử QA hoặc dịch vụ ngoài.")
    }
}
