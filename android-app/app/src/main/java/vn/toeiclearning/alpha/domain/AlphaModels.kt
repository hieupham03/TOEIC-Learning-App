package vn.toeiclearning.alpha.domain

/** Synthetic Alpha-only content. No PO-inventoried B1 content or real TOEIC material. */
enum class ContentReadiness { SYNTHETIC_DEMO_ONLY, NOT_QA_READY }

data class PracticePart(
    val number: Int,
    val title: String,
    val mode: String,
    val readiness: ContentReadiness,
) {
    val canEnterSyntheticAlpha: Boolean get() = readiness == ContentReadiness.SYNTHETIC_DEMO_ONLY
}

data class SyntheticQuestion(
    val id: String,
    val part: Int,
    val passageId: String?,
    val prompt: String,
    val choices: List<String>,
    val correctIndex: Int,
    val explanation: String?,
    val syntheticOnly: Boolean = true,
) {
    init {
        require(part in 1..7)
        require(choices.size >= 2)
        require(correctIndex in choices.indices)
        require(syntheticOnly) { "Alpha forbids real user/test material" }
    }
}

data class SyntheticPassage(
    val id: String,
    val title: String,
    val paragraphs: List<String>,
) {
    init { require(paragraphs.isNotEmpty()) }
}

/** Kept entirely in memory; never a durable ACK or persistence claim. */
data class PracticeState(
    val currentQuestionId: String? = null,
    val selectedById: Map<String, Int> = emptyMap(),
    val explanationVisibleFor: Set<String> = emptySet(),
)

data class PracticeFeedback(
    val correct: Boolean,
    val selectedText: String,
    val correctText: String,
    val explanation: String,
    val syntheticOnly: Boolean = true,
)

object PracticeRules {
    fun select(state: PracticeState, question: SyntheticQuestion, index: Int): PracticeState {
        require(index in question.choices.indices) { "Invalid choice" }
        if (question.id in state.explanationVisibleFor) return state // lock after feedback
        return state.copy(
            currentQuestionId = question.id,
            selectedById = state.selectedById + (question.id to index),
        )
    }

    fun requestFeedback(state: PracticeState, question: SyntheticQuestion): PracticeState {
        if (!question.syntheticOnly || question.explanation.isNullOrBlank()) return state
        if (question.id !in state.selectedById) return state
        return state.copy(explanationVisibleFor = state.explanationVisibleFor + question.id)
    }

    fun feedback(state: PracticeState, question: SyntheticQuestion): PracticeFeedback? {
        if (question.id !in state.explanationVisibleFor) return null
        val chosen = state.selectedById[question.id] ?: return null
        val explanation = question.explanation ?: return null
        return PracticeFeedback(
            correct = chosen == question.correctIndex,
            selectedText = question.choices[chosen],
            correctText = question.choices[question.correctIndex],
            explanation = explanation,
        )
    }
}

data class ReadingContext(
    val passageId: String,
    val questionId: String?,
    val itemIndex: Int = 0,
    val itemOffset: Int = 0,
) {
    init { require(itemIndex >= 0); require(itemOffset >= 0) }

    fun withQuestion(question: SyntheticQuestion): ReadingContext {
        require(question.passageId == passageId) { "Question not part of passage" }
        return copy(questionId = question.id)
    }

    fun withPassageAnchor(index: Int, offset: Int): ReadingContext {
        require(index >= 0 && offset >= 0)
        return copy(itemIndex = index, itemOffset = offset)
    }
}
