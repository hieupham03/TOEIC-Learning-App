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
        runCatching { readStudyGroup(row).also { group ->
            require(group.source.startsWith("https://"))
            for (asset in listOfNotNull(group.audio, group.image)) {
                require(verified.getOrPut(asset) { verifyMedia(assets, asset) })
            }
        } }.getOrNull()
    val groups = rows.mapNotNull(::verifiedGroup)
    require(groups.map { it.id }.distinct().size == groups.size)
    val ids = groups.flatMap { it.items }.map { it.id }
    require(ids.distinct().size == ids.size)
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

internal fun readStudyGroup(row: JSONObject): StudyGroup {
    val part = row.getInt("part")
    val items = row.getJSONArray("items").objects().map {
        val key = it.optJSONObject("key")?.let { key ->
            require(key.getString("status") == "VERIFIED")
            StudyKey(key.getInt("choice"), key.getString("evidence"), key.optString("explanation").ifBlank { null })
        }
        StudyItem(it.getString("id"), it.getInt("number"), it.optString("prompt"), it.getJSONArray("choices").strings(), key)
    }
    val audio = readAsset(row, "audio", "mp3")
    val image = readAsset(row, "image", "png|jpg")
    val passage = row.optString("passage").ifBlank { null }
    require(items.all { it.choices.size == if (part == 2) 3 else 4 })
    require((part in 1..4) == (audio != null))
    require(part != 1 || image != null)
    require(part !in 6..7 || image != null || passage != null)
    if (audio != null) require(row.getJSONArray("audioItems").strings() == items.map { it.id })
    return StudyGroup(row.getString("id"), part, row.getString("version"), items, row.getString("source"), passage, audio, image)
}

private fun readAsset(row: JSONObject, name: String, extensions: String): ListeningAsset? =
    row.optJSONObject(name)?.let { media ->
        val sha = media.getString("sha256")
        val path = media.getString("path")
        val size = media.getLong("size")
        require(sha.matches(Regex("[a-f0-9]{64}")) && size in 1..8_388_608)
        require(path.matches(Regex("study_pack/media/$sha\\.($extensions)")))
        ListeningAsset(path, size, sha)
    }

internal fun writeStudyGroup(group: StudyGroup): JSONObject {
    val items = group.items.map { item ->
        JSONObject().put("id", item.id).put("number", item.number)
            .put("prompt", item.prompt).put("choices", JSONArray(item.choices)).apply {
                item.key?.let {
                    put("key", JSONObject().put("status", "VERIFIED").put("choice", it.choice)
                        .put("evidence", it.evidence).put("explanation", it.explanation))
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
        }
}

private fun writeAsset(asset: ListeningAsset) =
    JSONObject().put("path", asset.path).put("sha256", asset.sha256).put("size", asset.size)
