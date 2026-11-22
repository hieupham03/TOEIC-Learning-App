package vn.toeiclearning.alpha.study

internal data class MockForm(val id: String, val version: String, val evidence: String, val groups: List<StudyGroup>)
internal data class MockAvailability(val ready: Boolean, val missing: Map<String, Int>, val issues: List<String>)
internal val mockPartCounts = listOf(6, 25, 39, 30, 30, 16, 54)

internal fun checkMockForms(forms: List<MockForm>, practice: List<StudyGroup>): MockAvailability {
    val issues = mutableListOf<String>()
    val missing = listOf("A", "B").associateWith { id ->
        val form = forms.singleOrNull { it.id == id }
        val verifiedGroups = form?.groups.orEmpty().filter(::mockGroupComplete)
        val missingItems = mockPartCounts.withIndex().sumOf { (index, expected) ->
            val count = verifiedGroups.filter { it.part == index + 1 }.sumOf { it.items.size }
            (expected - count).coerceAtLeast(0)
        }
        if (form == null || form.version.isBlank() || form.evidence.isBlank()) issues += "Đề $id thiếu hồ sơ kiểm chứng."
        else {
            val formItems = form.groups.flatMap { it.items }
            val counts = (1..7).map { part -> form.groups.filter { it.part == part }.sumOf { it.items.size } }
            if (counts != mockPartCounts || form.groups != verifiedGroups ||
                formItems.map { it.number } != (1..200).toList() ||
                form.groups.map { it.part }.zipWithNext().any { (before, after) -> before > after }
            ) issues += "Đề $id sai cấu trúc, thứ tự hoặc còn mục chưa kiểm chứng."
        }
        missingItems
    }
    if (forms.size != 2 || forms.map { it.id }.toSet() != setOf("A", "B")) {
        issues += "Cần đúng hai hồ sơ đề A và B độc lập."
    }
    val grouped = forms.flatMap { it.groups } + practice
    val ids = grouped.flatMap { group -> group.items.map { it.id } }
    val groupIds = grouped.map { it.id }
    val audio = grouped.mapNotNull { it.audio?.sha256 }
    val text = grouped.flatMap { group ->
        group.items.map { item ->
            val content = (listOf(item.prompt) + item.choices).joinToString("\u0000").normalized()
            val context = if (group.part <= 4) group.audio?.sha256 else
                (group.passage.orEmpty() + group.images.joinToString("") { it.sha256 }).normalized()
            "$context\u0000$content"
        }
    }
    if (forms.isNotEmpty() && (ids.size != ids.toSet().size || groupIds.size != groupIds.toSet().size ||
            audio.size != audio.toSet().size || text.size != text.toSet().size)) {
        issues += "Phát hiện trùng ID, nội dung hoặc audio giữa các đề và ngân hàng luyện."
    }
    return MockAvailability(issues.isEmpty() && missing.values.all { it == 0 }, missing, issues)
}

private fun String.normalized(): String = trim().lowercase().replace(Regex("\\s+"), " ")

private fun mockGroupComplete(group: StudyGroup): Boolean {
    val length = group.items.size
    val requiredLength = when (group.part) {
        1, 2, 5 -> length == 1
        3, 4 -> length == 3
        6 -> length == 4
        else -> length in 2..5
    }
    return requiredLength && group.items.all { it.key != null } &&
        (group.part !in 1..4 || group.audio != null) &&
        (group.part != 1 || group.image != null) &&
        (group.part !in 6..7 || group.image != null || !group.passage.isNullOrBlank())
}

internal data class MockTime(val boot: Int, val elapsed: Long, val wall: Long)
internal enum class MockPhase { LISTENING, READING, ENDED, INTERRUPTED }

internal data class MockRun(
    val form: String,
    val version: String,
    val boot: Int,
    val started: Long,
    val played: Set<String> = emptySet(),
    val pendingAudio: String? = null,
) {
    fun phase(time: MockTime): MockPhase {
        if (boot < 0 || time.boot != boot || time.elapsed < started) return MockPhase.INTERRUPTED
        val elapsed = time.elapsed - started
        return when {
            elapsed < LISTENING_END -> MockPhase.LISTENING
            elapsed < READING_END -> MockPhase.READING
            else -> MockPhase.ENDED
        }
    }

    fun secondsLeft(time: MockTime): Long {
        val limit = when (phase(time)) {
            MockPhase.LISTENING -> LISTENING_END
            MockPhase.READING -> READING_END
            else -> return 0
        }
        return ((limit - (time.elapsed - started)).coerceAtLeast(0) + 999) / 1000
    }

    companion object {
        const val LISTENING_END = 45 * 60_000L
        const val READING_END = 120 * 60_000L
    }
}

internal fun StudyAttempt.advanceMock(time: MockTime, recovering: Boolean = false): StudyAttempt {
    val run = mock ?: return this
    if (complete) return this
    if (recovering && run.pendingAudio != null) return finish(time.wall, interrupted = true)
    val phase = run.phase(time)
    if (phase == MockPhase.INTERRUPTED) return finish(time.wall, interrupted = true)
    if (phase == MockPhase.LISTENING) return this
    if (groups.any { it.part <= 4 && it.id !in run.played }) return finish(time.wall, interrupted = true)
    return if (phase == MockPhase.ENDED) finish(time.wall) else move(position.coerceAtLeast(100))
}

internal fun StudyAttempt.reserveMockAudio(groupId: String): StudyAttempt {
    val run = mock ?: return this
    if (complete || run.pendingAudio != null || group.part > 4) return this
    val next = groups.firstOrNull { it.part <= 4 && it.id !in run.played }
    return if (next?.id == groupId && group.id == groupId) copy(mock = run.copy(pendingAudio = groupId)) else this
}

internal fun StudyAttempt.completeMockAudio(groupId: String): StudyAttempt {
    val run = mock ?: return this
    if (complete || run.pendingAudio != groupId) return this
    return copy(mock = run.copy(played = run.played + groupId, pendingAudio = null))
}
