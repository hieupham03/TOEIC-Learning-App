package vn.toeiclearning.alpha.study

import android.content.ContentValues
import android.content.Context
import android.database.Cursor
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper
import android.database.sqlite.SQLiteException
import org.json.JSONArray
import org.json.JSONObject

internal data class StudyHistory(val id: Long, val part: Int, val endedAt: Long, val score: StudyScore)
internal data class StudyReview(val group: StudyGroup, val item: StudyItem, val marked: Boolean, val wrong: Boolean)
internal data class StudyDashboard(
    val active: StudyAttempt?,
    val history: List<StudyHistory>,
    val reviews: List<StudyReview>,
    val stats: List<PartStats>,
    val today: Int,
    val goal: Int,
)

internal class StudyStore(context: Context) : SQLiteOpenHelper(context, "phone-study.db", null, 1) {
    override fun onCreate(db: SQLiteDatabase) {
        db.execSQL("""CREATE TABLE attempts(
                id INTEGER PRIMARY KEY, revision INTEGER NOT NULL DEFAULT 0,
                snapshot TEXT NOT NULL, state TEXT NOT NULL, part INTEGER NOT NULL,
                ended INTEGER, day TEXT, total INTEGER NOT NULL, attempted INTEGER NOT NULL DEFAULT 0,
                graded INTEGER NOT NULL DEFAULT 0, correct INTEGER NOT NULL DEFAULT 0
            )""")
        db.execSQL("CREATE UNIQUE INDEX one_active ON attempts((1)) WHERE ended IS NULL")
        db.execSQL("""CREATE TABLE review(
                item_id TEXT PRIMARY KEY, snapshot TEXT NOT NULL,
                marked INTEGER NOT NULL DEFAULT 0, wrong INTEGER NOT NULL DEFAULT 0
            )""")
        db.execSQL("CREATE TABLE settings(name TEXT PRIMARY KEY, value INTEGER NOT NULL)")
    }

    override fun onUpgrade(db: SQLiteDatabase, oldVersion: Int, newVersion: Int) {
        throw SQLiteException("Unsupported study storage migration $oldVersion to $newVersion")
    }

    fun start(groups: List<StudyGroup>, position: Int = 0): StudyAttempt {
        val attempt = StudyAttempt(groups, position = position)
        val snapshot = JSONArray(groups.map(::writeStudyGroup)).toString()
        require(snapshot.toByteArray().size <= 750_000)
        val values = ContentValues().apply {
            put("snapshot", snapshot)
            put("state", encodeState(attempt))
            put("part", groups.map { it.part }.distinct().singleOrNull() ?: 0)
            put("total", attempt.items.size)
        }
        val id = writableDatabase.insertOrThrow("attempts", null, values)
        return attempt.copy(id = id)
    }

    fun active(): StudyAttempt? = readableDatabase.rawQuery("SELECT * FROM attempts WHERE ended IS NULL", null)
        .use { if (it.moveToFirst()) decodeAttempt(it) else null }

    fun attempt(id: Long): StudyAttempt? =
        readableDatabase.rawQuery("SELECT * FROM attempts WHERE id=?", arrayOf(id.toString()))
            .use { if (it.moveToFirst()) decodeAttempt(it) else null }

    fun save(attempt: StudyAttempt, day: String): StudyAttempt = transaction { db ->
        val next = attempt.copy(revision = attempt.revision + 1)
        val values = ContentValues().apply {
            put("revision", next.revision)
            put("state", encodeState(next))
            next.finishedAt?.let { ended ->
                val score = next.score()
                put("ended", ended)
                put("day", day)
                put("attempted", score.attempted)
                put("graded", score.graded)
                put("correct", score.correct)
            }
        }
        val changed = db.update("attempts", values, "id=? AND revision=? AND ended IS NULL",
            arrayOf(attempt.id.toString(), attempt.revision.toString()))
        check(changed == 1) { "Study session has changed" }
        if (next.complete && !next.interrupted) {
            for (group in next.groups) for (item in group.items) {
                val given = next.selections[item.id] ?: continue
                val key = item.key ?: continue
                updateReview(db, group, item.id, wrong = given != key.choice)
            }
        }
        next
    }

    fun toggleBookmark(group: StudyGroup, itemId: String) = transaction { db ->
        require(group.items.any { it.id == itemId })
        val marked = reviewFlags(db, itemId).first
        updateReview(db, group, itemId, marked = !marked)
    }

    fun setGoal(value: Int) {
        require(value in 1..200)
        writableDatabase.insertWithOnConflict("settings", null, ContentValues().apply {
            put("name", "daily_goal")
            put("value", value)
        }, SQLiteDatabase.CONFLICT_REPLACE).also { check(it != -1L) }
    }

    fun dashboard(day: String): StudyDashboard {
        val db = readableDatabase
        val history = db.rawQuery(
            "SELECT id,part,ended,total,attempted,graded,correct FROM attempts WHERE ended IS NOT NULL ORDER BY ended DESC,id DESC LIMIT 100",
            null,
        ).use { cursor ->
            buildList { while (cursor.moveToNext()) add(StudyHistory(
                cursor.getLong(0), cursor.getInt(1), cursor.getLong(2),
                StudyScore(cursor.getInt(3), cursor.getInt(4), cursor.getInt(5), cursor.getInt(6)),
            )) }
        }
        val stats = db.rawQuery(
            "SELECT part,SUM(graded),SUM(correct) FROM attempts WHERE ended IS NOT NULL AND part BETWEEN 1 AND 7 GROUP BY part", null,
        ).use { c -> buildList { while (c.moveToNext()) add(PartStats(c.getInt(0), c.getInt(1), c.getInt(2))) } }
        val today = db.rawQuery("SELECT COALESCE(SUM(attempted),0) FROM attempts WHERE day=?", arrayOf(day))
            .use { it.moveToFirst(); it.getInt(0) }
        val goal = db.rawQuery("SELECT value FROM settings WHERE name='daily_goal'", null)
            .use { if (it.moveToFirst()) it.getInt(0) else 10 }
        return StudyDashboard(active(), history, reviews(db), stats, today, goal)
    }

    fun clear() = transaction { db ->
        db.delete("review", null, null)
        db.delete("attempts", null, null)
        db.delete("settings", null, null)
    }

    private fun reviews(db: SQLiteDatabase): List<StudyReview> =
        db.rawQuery("SELECT item_id,snapshot,marked,wrong FROM review ORDER BY rowid DESC", null).use { c ->
            buildList { while (c.moveToNext()) {
                val group = readStudyGroup(JSONObject(c.getString(1)))
                add(StudyReview(group, group.items.first { it.id == c.getString(0) }, c.getInt(2) == 1, c.getInt(3) == 1))
            } }
        }

    private fun reviewFlags(db: SQLiteDatabase, itemId: String): Pair<Boolean, Boolean> =
        db.rawQuery("SELECT marked,wrong FROM review WHERE item_id=?", arrayOf(itemId)).use {
            if (it.moveToFirst()) (it.getInt(0) == 1) to (it.getInt(1) == 1) else false to false
        }

    private fun updateReview(db: SQLiteDatabase, group: StudyGroup, itemId: String, marked: Boolean? = null, wrong: Boolean? = null) {
        val (wasMarked, wasWrong) = reviewFlags(db, itemId)
        val keepMarked = marked ?: wasMarked
        val keepWrong = wrong ?: wasWrong
        if (!keepMarked && !keepWrong) {
            db.delete("review", "item_id=?", arrayOf(itemId))
        } else {
            val values = ContentValues().apply {
                put("item_id", itemId)
                put("snapshot", writeStudyGroup(group).toString())
                put("marked", if (keepMarked) 1 else 0)
                put("wrong", if (keepWrong) 1 else 0)
            }
            check(db.insertWithOnConflict("review", null, values, SQLiteDatabase.CONFLICT_REPLACE) != -1L)
        }
    }

    private fun <T> transaction(block: (SQLiteDatabase) -> T): T {
        val db = writableDatabase
        db.beginTransaction()
        try {
            val value = block(db)
            db.setTransactionSuccessful()
            return value
        } finally {
            db.endTransaction()
        }
    }

    private fun decodeAttempt(c: Cursor): StudyAttempt {
        val state = JSONObject(c.getString(c.getColumnIndexOrThrow("state")))
        val ended = c.getColumnIndexOrThrow("ended")
        return StudyAttempt(
            groups = JSONArray(c.getString(c.getColumnIndexOrThrow("snapshot"))).objects().map(::readStudyGroup),
            id = c.getLong(c.getColumnIndexOrThrow("id")),
            revision = c.getInt(c.getColumnIndexOrThrow("revision")),
            position = state.getInt("position"),
            selections = decodeMap(state.getJSONObject("selections")),
            readingOffsets = decodeMap(state.getJSONObject("readingOffsets")),
            finishedAt = if (c.isNull(ended)) null else c.getLong(ended),
            interrupted = state.getBoolean("interrupted"),
        )
    }

    private fun encodeState(attempt: StudyAttempt): String = JSONObject().put("position", attempt.position)
        .put("selections", JSONObject(attempt.selections)).put("readingOffsets", JSONObject(attempt.readingOffsets))
        .put("interrupted", attempt.interrupted).toString()

    private fun decodeMap(value: JSONObject): Map<String, Int> = value.keys().asSequence().associateWith(value::getInt)
}
