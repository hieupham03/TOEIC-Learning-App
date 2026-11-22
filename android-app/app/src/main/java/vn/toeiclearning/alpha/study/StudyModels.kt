package vn.toeiclearning.alpha.study

import vn.toeiclearning.alpha.domain.ListeningAsset

internal data class StudyKey(val choice: Int, val evidence: String, val explanation: String? = null) {
    init { require(evidence.isNotBlank()) }
}

internal data class StudyItem(
    val id: String,
    val number: Int,
    val prompt: String,
    val choices: List<String>,
    val key: StudyKey? = null,
) {
    init {
        require(id.isNotBlank() && number > 0 && choices.size in 3..4 && choices.none(String::isBlank))
        require(key == null || key.choice in choices.indices)
    }
}

internal data class StudyGroup(
    val id: String,
    val part: Int,
    val version: String,
    val items: List<StudyItem>,
    val source: String = "synthetic",
    val passage: String? = null,
    val audio: ListeningAsset? = null,
    val image: ListeningAsset? = null,
) {
    init {
        require(id.isNotBlank() && part in 1..7 && version.isNotBlank() && source.isNotBlank())
        require(items.isNotEmpty() && items.map { it.id }.distinct().size == items.size)
        require(items.zipWithNext().all { (a, b) -> b.number > a.number })
    }
}

internal data class StudyScore(val total: Int, val attempted: Int, val graded: Int, val correct: Int) {
    val wrong get() = graded - correct
    val ungraded get() = attempted - graded
}

internal data class StudyAttempt(
    val groups: List<StudyGroup>,
    val id: Long = 0,
    val revision: Int = 0,
    val position: Int = 0,
    val selections: Map<String, Int> = emptyMap(),
    val readingOffsets: Map<String, Int> = emptyMap(),
    val finishedAt: Long? = null,
    val interrupted: Boolean = false,
) {
    val items = groups.flatMap { it.items }
    val item get() = items[position]
    val group get() = groups.first { g -> g.items.any { it.id == item.id } }
    val complete get() = finishedAt != null

    init {
        require(position in items.indices && items.size <= 200)
        require(items.map { it.id }.distinct().size == items.size)
        require(selections.all { (id, index) -> items.any { it.id == id && index in it.choices.indices } })
        require(readingOffsets.all { (id, offset) -> offset >= 0 && groups.any { it.id == id } })
    }

    fun select(choice: Int): StudyAttempt {
        require(choice in item.choices.indices)
        return if (complete) this else copy(selections = selections + (item.id to choice))
    }

    fun move(index: Int): StudyAttempt = copy(position = index.coerceIn(items.indices))

    fun finish(at: Long, interrupted: Boolean = false): StudyAttempt =
        if (complete) this else copy(finishedAt = at, interrupted = interrupted)

    fun score(part: Int? = null): StudyScore {
        val scoped = if (part == null) items else groups.filter { it.part == part }.flatMap { it.items }
        val attempted = scoped.filter { it.id in selections }
        val graded = attempted.filter { it.key != null }
        val correct = graded.count { selections[it.id] == it.key?.choice }
        return StudyScore(scoped.size, attempted.size, graded.size, correct)
    }

    fun mistakes(): List<StudyItem> = items.filter { item ->
        val selection = selections[item.id]
        val key = item.key
        key != null && selection != null && selection != key.choice
    }
}

internal data class PartStats(val part: Int, val graded: Int, val correct: Int) {
    val wrong get() = graded - correct
    val accuracy get() = if (graded == 0) null else correct.toDouble() / graded
}

internal fun recommendedPart(available: Set<Int>, stats: List<PartStats>): Int? =
    stats.filter { it.part in available && it.graded > 0 && it.wrong > 0 }
        .minWithOrNull(compareBy<PartStats> { it.accuracy }.thenByDescending { it.wrong }.thenBy { it.part })?.part
        ?: available.minOrNull()
