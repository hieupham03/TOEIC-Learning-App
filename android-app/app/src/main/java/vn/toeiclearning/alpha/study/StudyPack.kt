package vn.toeiclearning.alpha.study

import android.content.res.AssetManager
import android.graphics.BitmapFactory
import org.json.JSONArray
import org.json.JSONObject
import vn.toeiclearning.alpha.domain.ListeningAsset

internal data class StudyPack(
    val groups: List<StudyGroup>,
    val skipped: Int = 0,
    val unavailable: Boolean = false,
    val forms: List<MockForm> = emptyList(),
) {
    val mocks = checkMockForms(forms, groups)
}

internal fun loadStudyPack(assets: AssetManager): StudyPack = runCatching {
    val root = assets.open("study_pack/pack.json").bufferedReader().use {
        val text = it.readText()
        require(text.length <= 1_000_000)
        JSONObject(text)
    }
    require(root.getInt("schema") == 1)
    val rows = root.getJSONArray("practice").objects()
    val verified = mutableMapOf<ListeningAsset, Boolean>()
    fun verifiedGroup(row: JSONObject): StudyGroup? =
        runCatching { readStudyGroup(row, requireAnswerProof = true).also { group ->
            require(group.source.startsWith("https://"))
            for (asset in listOfNotNull(group.audio) + group.images) {
                require(verified.getOrPut(asset) { verifyMedia(assets, asset) })
            }
        } }.getOrNull()
    val groups = rows.mapNotNull(::verifiedGroup)
    require(groups.map { it.id }.distinct().size == groups.size)
    val ids = groups.flatMap { it.items }.map { it.id }
    require(ids.distinct().size == ids.size)
    val media = groups.flatMap { group -> (listOfNotNull(group.audio) + group.images).map { it.sha256 } }
    require(media.distinct().size == media.size)
    val forms = runCatching {
        root.optJSONArray("forms")?.objects().orEmpty().map { form ->
            val review = form.optJSONObject("review")
            val evidence = if (review?.optString("status") == "APPROVED") review.optString("evidence") else ""
            MockForm(form.getString("id"), form.getString("version"), evidence,
                form.getJSONArray("groups").objects().mapNotNull(::verifiedGroup))
        }
    }.getOrDefault(emptyList())
    StudyPack(groups, rows.size - groups.size, forms = forms)
}.getOrElse { StudyPack(emptyList(), unavailable = true) }

private fun verifyMedia(assets: AssetManager, asset: ListeningAsset): Boolean = runCatching {
    val bytes = assets.open(asset.path).use { it.readBytes() }
    if (!asset.matches(bytes)) return false
    if (asset.path.endsWith(".mp3")) return true
    val bounds = BitmapFactory.Options().apply { inJustDecodeBounds = true }
    BitmapFactory.decodeByteArray(bytes, 0, bytes.size, bounds)
    bounds.outWidth > 0 && bounds.outHeight > 0 && bounds.outWidth.toLong() * bounds.outHeight <= 20_000_000
}.getOrDefault(false)

internal fun JSONArray.objects(): List<JSONObject> = (0 until length()).map { getJSONObject(it) }
private fun JSONArray.strings(): List<String> = (0 until length()).map { getString(it) }

internal fun readStudyGroup(row: JSONObject, requireAnswerProof: Boolean = false): StudyGroup {
    val part = row.getInt("part")
    val itemRows = row.getJSONArray("items").objects()
    val items = itemRows.map {
        val key = it.optJSONObject("key")?.takeUnless { requireAnswerProof }?.let { key ->
            require(key.getString("status") == "VERIFIED")
            StudyKey(key.getInt("choice"), key.getString("evidence"), key.optString("explanation").ifBlank { null },
                key.optBoolean("batchAccepted"))
        }
        StudyItem(it.getString("id"), it.getInt("number"), it.optString("prompt"), it.getJSONArray("choices").strings(),
            key, !requireAnswerProof && (it.optBoolean("hasSourceKey") || key != null))
    }
    val audio = readAsset(row, "audio", "mp3")
    val image = readAsset(row, "image", "png|jpg")
    val extraImages = row.optJSONArray("extraImages")?.objects().orEmpty().map { parseAsset(it, "png|jpg") }
    val passage = row.optString("passage").takeUnless { row.isNull("passage") || it.isBlank() }
    require(items.all { it.choices.size == if (part == 2) 3 else 4 })
    require((part in 1..4) == (audio != null))
    require(part != 1 || image != null)
    require(part !in 6..7 || image != null || passage != null)
    if (audio != null) require(row.getJSONArray("audioItems").strings() == items.map { it.id })
    val group = StudyGroup(row.getString("id"), part, row.getString("version"), items,
        row.getString("source"), passage, audio, image, extraImages)
    if (!requireAnswerProof) return group
    return group.copy(items = items.zip(itemRows).map { (item, itemRow) ->
        val sourceProof = itemRow.optJSONObject("sourceKey")?.answerProof()
        val review = itemRow.optJSONObject("key")?.takeIf { it.optString("status") == "VERIFIED" }?.let { approved ->
            approved.answerProof()?.let { proof -> StudyAnswerReview(proof, approved.opt("reviewer") as? String ?: "",
                approved.opt("evidence") as? String ?: "", (approved.opt("explanation") as? String)?.takeIf(String::isNotBlank),
                approved.optBoolean("batchAccepted")) }
        }
        applyStudyAnswer(group, item, sourceProof, review)
    })
}

private fun JSONObject.answerProof(): StudyAnswerProof? = runCatching {
    StudyAnswerProof(getString("groupId"), getString("itemId"), getString("source"), getString("version"),
        getString("itemSha256"), get("choice") as Int, getString("evidenceSha256"))
}.getOrNull()

private fun readAsset(row: JSONObject, name: String, extensions: String): ListeningAsset? =
    row.optJSONObject(name)?.let { parseAsset(it, extensions) }

private fun parseAsset(media: JSONObject, extensions: String): ListeningAsset {
    val sha = media.getString("sha256")
    val path = media.getString("path")
    val size = media.getLong("size")
    require(sha.matches(Regex("[a-f0-9]{64}")) && size in 1..12_582_912)
    require(path.matches(Regex("study_pack/media/$sha\\.($extensions)")))
    return ListeningAsset(path, size, sha)
}

internal fun writeStudyGroup(group: StudyGroup): JSONObject {
    val items = group.items.map { item ->
        JSONObject().put("id", item.id).put("number", item.number)
            .put("prompt", item.prompt).put("choices", JSONArray(item.choices)).apply {
                if (item.hasSourceKey) put("hasSourceKey", true)
                item.key?.let {
                    put("key", JSONObject().put("status", "VERIFIED").put("choice", it.choice)
                        .put("evidence", it.evidence).put("explanation", it.explanation)
                        .put("batchAccepted", it.batchAccepted))
                }
            }
    }
    return JSONObject().put("id", group.id).put("part", group.part).put("version", group.version)
        .put("source", group.source).put("passage", group.passage).put("items", JSONArray(items)).apply {
            group.audio?.let {
                put("audio", writeAsset(it))
                put("audioItems", JSONArray(group.items.map { item -> item.id }))
            }
            group.image?.let { put("image", writeAsset(it)) }
            if (group.extraImages.isNotEmpty()) put("extraImages", JSONArray(group.extraImages.map(::writeAsset)))
        }
}

private fun writeAsset(asset: ListeningAsset) =
    JSONObject().put("path", asset.path).put("sha256", asset.sha256).put("size", asset.size)
