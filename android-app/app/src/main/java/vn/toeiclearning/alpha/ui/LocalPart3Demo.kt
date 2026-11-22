package vn.toeiclearning.alpha.ui

import android.content.res.AssetManager
import org.json.JSONObject
import vn.toeiclearning.alpha.domain.ListeningAsset

internal data class LocalPart3Item(val id: String, val number: Int, val prompt: String, val choices: List<String>)
internal data class LocalPart3Group(val audio: ListeningAsset, val items: List<LocalPart3Item>)

internal fun readLocalPart3(assets: AssetManager): LocalPart3Group? = runCatching {
    val json = assets.open("listening_preview/part3.json").bufferedReader().use { JSONObject(it.readText()) }
    val groupId = json.getString("groupId")
    require(groupId == "zenlish:41021")
    val rows = json.getJSONArray("items")
    require(rows.length() == 3)
    val items = (32..34).map { number ->
        val row = rows.getJSONObject(number - 32)
        val id = row.getString("id")
        val prompt = row.getString("prompt")
        val options = row.getJSONArray("choices")
        require(row.getInt("number") == number && id == "$groupId:$number")
        require(prompt.isNotBlank() && options.length() == 4)
        val choices = (0..3).map { options.getString(it).also { option -> require(option.isNotBlank()) } }
        LocalPart3Item(id, number, prompt, choices)
    }
    val audio = json.getJSONObject("audio")
    val itemIds = audio.getJSONArray("itemIds")
    require(audio.getString("groupId") == groupId && itemIds.length() == items.size)
    require(items.indices.all { itemIds.getString(it) == items[it].id })
    val size = audio.getLong("bytes")
    val sha256 = audio.getString("sha256")
    require(size in 1..2_097_152 && sha256.matches(Regex("[0-9a-f]{64}")))
    LocalPart3Group(ListeningAsset("listening_preview/part3.mp3", size, sha256), items)
}.getOrNull()
