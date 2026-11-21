package vn.toeiclearning.alpha.domain

/** Written-from-scratch toy text, not a TOEIC question bank. */
object SyntheticCatalogue {
    val parts: List<PracticePart> = listOf(
        PracticePart(1, "Photographs", "Listening", ContentReadiness.NOT_QA_READY),
        PracticePart(2, "Question–Response", "Listening", ContentReadiness.NOT_QA_READY),
        PracticePart(3, "Conversations", "Listening", ContentReadiness.NOT_QA_READY),
        PracticePart(4, "Short Talks", "Listening", ContentReadiness.NOT_QA_READY),
        PracticePart(5, "Incomplete Sentences", "Reading", ContentReadiness.SYNTHETIC_DEMO_ONLY),
        PracticePart(6, "Text Completion", "Reading", ContentReadiness.SYNTHETIC_DEMO_ONLY),
        PracticePart(7, "Reading Comprehension", "Reading", ContentReadiness.SYNTHETIC_DEMO_ONLY),
    )

    val fullMockAReadiness: ContentReadiness = ContentReadiness.NOT_QA_READY
    val fullMockBReadiness: ContentReadiness = ContentReadiness.NOT_QA_READY

    private val part5 = listOf(
        SyntheticQuestion(
            id = "DEMO-P5-Q1", part = 5, passageId = null,
            prompt = "The community workshop will begin ___ nine o'clock on Friday.",
            choices = listOf("in", "at", "on", "by"), correctIndex = 1,
            explanation = "Trong câu minh họa này, 'at' được dùng trước giờ cụ thể. Đây không phải lời giải đã QA của ngân hàng TOEIC.",
        ),
        SyntheticQuestion(
            id = "DEMO-P5-Q2", part = 5, passageId = null,
            prompt = "Please ___ the registration form before the event.",
            choices = listOf("complete", "completion", "completely", "completed"),
            correctIndex = 0,
            explanation = "Sau 'please' dùng động từ nguyên mẫu. Nội dung chỉ được tạo để kiểm tra luồng UI.",
        ),
    )

    private val part6 = listOf(
        SyntheticQuestion(
            id = "DEMO-P6-Q1", part = 6, passageId = "DEMO-P6-TEXT",
            prompt = "The team will send a ___ by Tuesday.",
            choices = listOf("summary", "summarize", "summarized", "summarizing"), correctIndex = 0,
            explanation = "Vị trí sau mạo từ 'a' cần danh từ. Ví dụ Alpha giả lập.",
        ),
        SyntheticQuestion(
            id = "DEMO-P6-Q2", part = 6, passageId = "DEMO-P6-TEXT",
            prompt = "What is the main purpose of the note?",
            choices = listOf("Cancel a meeting", "Share project updates", "Sell equipment", "Announce a holiday"),
            correctIndex = 1,
            explanation = "Thông báo mô tả cách chia sẻ tiến độ dự án. Ví dụ Alpha giả lập.",
        ),
    )

    private val part7 = listOf(
        SyntheticQuestion(
            id = "DEMO-P7-Q1", part = 7, passageId = "DEMO-P7-TEXT",
            prompt = "Where will the workshop take place?",
            choices = listOf("At a library", "At a station", "At a hotel", "At a museum"),
            correctIndex = 0,
            explanation = "Đoạn văn đầu nêu địa điểm là thư viện cộng đồng. Ví dụ Alpha giả lập.",
        ),
        SyntheticQuestion(
            id = "DEMO-P7-Q2", part = 7, passageId = "DEMO-P7-TEXT",
            prompt = "What should participants bring?",
            choices = listOf("A laptop", "A printed ticket", "A notebook", "A passport"),
            correctIndex = 2,
            explanation = "Đoạn văn yêu cầu người học mang sổ tay. Ví dụ Alpha giả lập.",
        ),
        SyntheticQuestion(
            id = "DEMO-P7-Q3", part = 7, passageId = "DEMO-P7-TEXT",
            prompt = "Why should participants register early?",
            choices = listOf("To book food", "Because seating is limited", "To receive a refund", "To borrow a computer"),
            correctIndex = 1,
            explanation = "Thư ghi rõ số lượng chỗ ngồi hạn chế. Ví dụ Alpha giả lập.",
        ),
    )

    private val passages = mapOf(
        "DEMO-P6-TEXT" to SyntheticPassage(
            "DEMO-P6-TEXT", "Project team note · đoạn mẫu",
            listOf(
                "To: Project Team. Subject: Weekly update. We have completed the first round of planning for the neighborhood workshop.",
                "The team will send a summary by Tuesday. Please review the shared checklist before the Friday meeting.",
                "Everyone may suggest adjustments. These notes were written only for interface development and are not part of any examination.",
                "If you need more time, tell the coordinator in advance so the agenda can be updated. Thank you for supporting the project.",
            ),
        ),
        "DEMO-P7-TEXT" to SyntheticPassage(
            "DEMO-P7-TEXT", "Community library workshop · đoạn mẫu dài",
            listOf(
                "Subject: Your Community Workshop Registration",
                "Thank you for your interest in our Saturday workshop at the community library. The session introduces basic methods for organizing small volunteer projects and keeping simple progress notes.",
                "The workshop begins at 9:30 a.m. Participants are encouraged to arrive at least fifteen minutes early to sign in and receive a printed schedule. The library's main entrance will be open from 9:00 a.m.",
                "Please bring a notebook and something to write with. A few shared computers are available at the venue, but participants do not need to bring their own devices. Refreshments will be provided during the break.",
                "Seating is limited because the activity room accommodates only a small group. If you would like to attend, submit the online registration form early in the week. A coordinator will reply by email with more information.",
                "During the first session, the organizers will discuss how to define a practical goal. They will also show examples of meeting notes and short status updates. The second session focuses on reviewing progress and planning the next steps.",
                "If you can no longer attend, please contact the coordinator so that your place may be offered to someone else. Thank you for helping us make the workshop welcoming and useful for everyone.",
                "This entire English passage is synthetic demonstration content created for Alpha CX-03. It must never be described as a vetted TOEIC question, an official test passage, or real learner data.",
            ),
        ),
    )

    fun part(number: Int): PracticePart? = parts.firstOrNull { it.number == number }
    fun questions(number: Int): List<SyntheticQuestion> = when (number) {
        5 -> part5
        6 -> part6
        7 -> part7
        else -> emptyList()
    }
    fun passage(number: Int): SyntheticPassage? = when (number) {
        6 -> passages["DEMO-P6-TEXT"]
        7 -> passages["DEMO-P7-TEXT"]
        else -> null
    }
    fun canStartAlphaPart(number: Int): Boolean =
        part(number)?.canEnterSyntheticAlpha == true && questions(number).isNotEmpty()
    fun canStartRealFullMock(form: String): Boolean =
        (form == "A" || form == "B") && realMockApprovedForLaunch

    private const val realMockApprovedForLaunch: Boolean = false // No authorization, no B1 QA
}
