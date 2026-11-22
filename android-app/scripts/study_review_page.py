"""Render the self-contained offline content review page."""
import json

from activate_study_content import group_assets, item_binding


def render_review(target, groups, queue, decisions):
    pending = {row["itemId"]: row for row in queue}
    reviewed = {row["itemId"]: row for row in decisions}
    rows = [
        {**item_binding(group, item), **item, "part": group["part"], "passage": group.get("passage"),
         "assets": [{"kind": kind, "path": asset["path"], "sha256": asset["sha256"]} for kind, asset in group_assets(group)],
         "queue": pending.get(item["id"]), "review": reviewed.get(item["id"])}
        for group in groups for item in group["items"]
    ]
    data = json.dumps(rows, ensure_ascii=False).replace("<", "\\u003c")
    target.write_text(PAGE.replace("__REVIEW_ROWS__", data), encoding="utf-8")


PAGE = r"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; img-src 'self' file:; media-src 'self' file:; base-uri 'none'; form-action 'none'">
<title>Kiểm duyệt học liệu Study</title>
<style>
:root { color-scheme: light; font: 16px/1.55 system-ui, sans-serif; color: #14243d; background: #f4f7fb; }
* { box-sizing: border-box; }
body { max-width: 1120px; margin: 0 auto; padding: 22px; }
h1 { margin: 0; font-size: clamp(1.55rem, 4vw, 2.2rem); color: #1e3a5f; }
h2 { font-size: 1.25rem; margin-top: 0; }
fieldset, section { border: 1px solid #cbd5e1; border-radius: 12px; padding: 18px; margin: 0; background: white; min-width: 0; }
legend, label { font-weight: 600; }
label, button { display: block; }
input, textarea, select, button { font: inherit; min-height: 44px; max-width: 100%; }
input:not([type=checkbox]), textarea, select { width: 100%; padding: .45rem .55rem; border: 1px solid #64748b; border-radius: 6px; margin-bottom: .65rem; }
input[type=checkbox] { min-height: auto; }
button { border: 1px solid #1e3a5f; border-radius: 8px; color: #1e3a5f; background: white; padding: 0 .85rem; cursor: pointer; }
button.primary { background: #1e3a5f; color: white; }
button:disabled { cursor: default; opacity: .55; }
:focus-visible { outline: 3px solid #2563eb; outline-offset: 2px; }
.grid { display: grid; grid-template-columns: minmax(0, 1.18fr) minmax(0, 1fr); gap: 16px; margin: 14px 0; align-items: start; }
.line { display: flex; flex-wrap: wrap; gap: 8px; margin: 6px 0 12px; }
.line label { flex: 1 1 180px; }
p { margin: .4rem 0 .75rem; }
img, audio { display: block; max-width: 100%; margin: .5rem 0; }
img { height: auto; border: 1px solid #cbd5e1; }
.meta { color: #475569; overflow-wrap: anywhere; }
#message { min-height: 2em; color: #1e3a5f; font-weight: 600; }
pre { white-space: pre-wrap; overflow-wrap: anywhere; font: inherit; margin: .5rem 0; }
@media (max-width: 750px) { .grid { grid-template-columns: 1fr; } body { padding: 12px; } }
</style>
</head>
<body>
<h1>Kiểm duyệt học liệu Study</h1>
<p id="coverage" class="meta"></p>
<div class="line">
  <label>Tìm số câu hoặc mã câu<input id="search" type="search" autocomplete="off"></label>
  <label>Part<select id="part"><option value="">Tất cả</option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7</option></select></label>
  <label>Câu hỏi<select id="question"></select></label>
</div>
<label><input id="pendingKeys" type="checkbox"> Chỉ xem câu có khóa nguồn đang chờ duyệt</label>
<div class="line"><button id="prev">Câu trước</button><button id="next">Câu sau</button></div>
<main class="grid">
  <section aria-labelledby="questionTitle">
    <h2 id="questionTitle"></h2><p id="state"></p>
    <details><summary>Nguồn, phiên bản và mã câu</summary><pre id="meta" class="meta"></pre></details>
    <p id="passage"></p><div id="media"></div><p id="prompt"></p><ol id="choices" type="A"></ol>
  </section>
  <fieldset>
    <legend>Quyết định kiểm duyệt</legend>
    <label for="file">Tệp nguồn đáp án cục bộ</label><input id="file" type="file">
    <p id="digest" class="meta" aria-live="polite">Chọn tài liệu gốc đã đối chiếu.</p>
    <p id="expected" class="meta" aria-live="polite"></p>
    <label>URL nguồn tài liệu<input id="evidenceUrl" type="url"></label>
    <div class="line"><label>Người duyệt<input id="reviewer" maxlength="100"></label><label>Ngày đối chiếu<input id="reviewedAt" type="date"></label></div>
    <div class="line"><label>Đáp án nguồn<select id="label"></select></label><label>Trang / dòng / ô<input id="locator" maxlength="240"></label></div>
    <label>Trạng thái<select id="status"><option value="SOURCE_ONLY">Có nguồn, chờ duyệt</option><option value="APPROVED">Đã đối chiếu và duyệt</option><option value="REVOKED">Thu hồi phê duyệt</option></select></label>
    <label><input id="confirm" type="checkbox"> Tôi đã đối chiếu đúng câu, thứ tự lựa chọn và phiên bản.</label>
    <details><summary>Lời giải từ tài liệu nguồn</summary>
      <label>Nội dung<textarea id="explanation" rows="3" maxlength="5000"></textarea></label>
      <label>Vị trí lời giải<input id="explanationLocator" maxlength="240"></label>
    </details>
    <p id="message" role="status"></p>
    <div class="line"><button id="save" class="primary">Thêm vào danh sách</button><button id="download" disabled>Tải quyết định JSON</button></div>
  </fieldset>
</main>
<script type="application/json" id="rows">__REVIEW_ROWS__</script>
<script>
const byId = id => document.getElementById(id);
const rows = JSON.parse(byId('rows').textContent), drafts = new Map();
const states = {SOURCE_EVIDENCE_REQUIRED:'Thiếu bằng chứng', AWAITING_REVIEW:'Chờ duyệt',
  REVOKED:'Đã thu hồi', APPROVED:'Đã duyệt', REVIEW_REJECTED_OR_MISMATCH:'Lệch hoặc bị từ chối',
  SOURCE_EVIDENCE_REJECTED:'Bằng chứng không hợp lệ', SOURCE_ONLY:'Chờ duyệt'};
let shown = rows, position = 0, evidenceSha256 = '';
const value = id => byId(id).value.trim();
function options(node, entries) {
  node.replaceChildren(...entries.map(([label, value]) => new Option(label, value)));
}
function showEvidenceMatch() {
  const candidate = shown[position]?.queue?.candidate;
  const expected = byId('expected');
  expected.textContent = candidate ? 'SHA-256 dự kiến ' + candidate.evidenceSha256 : '';
  if (candidate && evidenceSha256) {
    expected.textContent = candidate.evidenceSha256 === evidenceSha256
      ? 'SHA-256 tệp đã chọn khớp với câu này.'
      : 'Tệp đã chọn khác bằng chứng của câu này. ' + expected.textContent;
  }
}
function show() {
  const row = shown[position], state = row && (drafts.get(row.id) || row.review || row.queue);
  const candidate = row?.queue?.candidate;
  byId('questionTitle').textContent = row ? 'Part ' + row.part + ' · Câu ' + row.number : 'Không tìm thấy câu';
  byId('state').textContent = states[state?.status] || '';
  byId('prompt').textContent = row?.prompt || '';
  byId('passage').textContent = row?.passage || '';
  const fields = row ? ['Câu ' + row.itemId, 'Nhóm ' + row.groupId, 'Nguồn đề ' + row.source,
    'SHA-256 phiên bản ' + row.version, 'SHA-256 câu ' + row.itemSha256] : [];
  if (candidate) fields.push('Nguồn khóa ' + candidate.evidenceUrl, 'SHA-256 khóa ' + candidate.evidenceSha256,
    'Vị trí khóa ' + candidate.locator);
  byId('meta').textContent = fields.join('\n');
  const media = byId('media');
  media.replaceChildren();
  row?.assets.forEach((asset, index) => {
    const element = document.createElement(asset.kind === 'audio' ? 'audio' : 'img');
    if (asset.kind === 'audio') {
      element.controls = true; element.preload = 'none'; element.setAttribute('aria-label', 'Audio nhóm');
    } else {
      element.alt = 'Ảnh nguồn ' + (index + 1); element.loading = 'lazy';
    }
    element.src = 'assets/' + asset.path; media.append(element);
    const hash = document.createElement('p'); hash.className = 'meta'; hash.textContent = 'SHA-256 ' + asset.sha256; media.append(hash);
  });
  byId('choices').replaceChildren(...(row?.choices || []).map(choice => {
    const li = document.createElement('li'); li.textContent = choice; return li;
  }));
  options(byId('label'), [['Chọn từ tài liệu', ''], ...Array.from('ABCD'.slice(0, row?.choices.length || 0), c => [c, c])]);
  byId('evidenceUrl').value = state?.evidenceUrl || candidate?.evidenceUrl || row?.source || '';
  byId('label').value = state?.label || candidate?.label || '';
  byId('locator').value = state?.locator || candidate?.locator || '';
  byId('explanation').value = state?.explanation || '';
  byId('explanationLocator').value = state?.explanationLocator || '';
  byId('status').value = 'SOURCE_ONLY';
  byId('confirm').checked = false;
  showEvidenceMatch();
  byId('save').disabled = !row;
  byId('prev').disabled = !row || position < 1; byId('next').disabled = position >= shown.length - 1;
}
function filter() {
  const query = value('search').toLowerCase(), part = value('part');
  shown = rows.filter(row => (!part || part === String(row.part)) &&
    (!byId('pendingKeys').checked || row.queue?.status === 'AWAITING_REVIEW') &&
    (!query || row.id.toLowerCase().includes(query) || String(row.number) === query));
  options(byId('question'), shown.map((row, index) => ['Part ' + row.part + ' · Câu ' + row.number + ' · ' + row.id, index]));
  position = 0; show();
}
function move(to) { position = to; byId('question').value = String(to); show(); }
byId('search').oninput = byId('part').onchange = byId('pendingKeys').onchange = filter;
byId('question').onchange = () => move(Number(value('question')));
byId('prev').onclick = () => move(position - 1);
byId('next').onclick = () => move(position + 1);
byId('file').onchange = async () => {
  const input = byId('file'), file = input.files[0], digest = byId('digest');
  evidenceSha256 = '';
  showEvidenceMatch();
  if (!file || file.size < 1 || file.size > 12 * 1024 * 1024) { digest.textContent = 'Tệp phải từ 1 byte đến 12 MiB.'; return; }
  try {
    const bytes = new Uint8Array(await crypto.subtle.digest('SHA-256', await file.arrayBuffer()));
    if (input.files[0] !== file) return;
    evidenceSha256 = Array.from(bytes, byte => byte.toString(16).padStart(2, '0')).join('');
    digest.textContent = file.name + ' · SHA-256 ' + evidenceSha256;
    showEvidenceMatch();
  } catch { digest.textContent = 'Không đọc được SHA-256 trong trình duyệt này. Mở tệp bằng Edge hoặc Chrome.'; }
};
byId('save').onclick = () => {
  const row = shown[position], status = value('status'), message = byId('message');
  let sourceMatches = false;
  try {
    const evidence = new URL(value('evidenceUrl'));
    sourceMatches = evidence.protocol === 'https:' && evidence.hostname === new URL(row.source).hostname;
  } catch {}
  if (!sourceMatches || !evidenceSha256 || !value('label') || !value('locator') || !value('reviewer') || !value('reviewedAt')) {
    message.textContent = 'Chọn tệp và điền URL cùng nguồn, đáp án, vị trí, người duyệt và ngày.'; return;
  }
  if (status !== 'SOURCE_ONLY' && !byId('confirm').checked) {
    message.textContent = 'Xác nhận đã đối chiếu trước khi duyệt hoặc thu hồi.'; return;
  }
  const candidate = row.queue?.candidate;
  if (status === 'APPROVED' && candidate && (candidate.evidenceSha256 !== evidenceSha256 ||
      candidate.evidenceUrl !== value('evidenceUrl') || candidate.label !== value('label') || candidate.locator !== value('locator'))) {
    message.textContent = 'Quyết định chưa khớp khóa nguồn đã lưu. Kiểm tra tệp, URL, đáp án và vị trí.'; return;
  }
  const explanation = value('explanation'), explanationLocator = value('explanationLocator');
  if ((explanation || explanationLocator) && (status !== 'APPROVED' || !explanation || !explanationLocator)) {
    message.textContent = 'Lời giải cần nội dung, vị trí nguồn và câu đã duyệt.'; return;
  }
  const {itemId, groupId, source, version, itemSha256} = row;
  drafts.set(itemId, {itemId, groupId, source, version, itemSha256, evidenceSha256, status,
    label: value('label'), evidenceUrl: value('evidenceUrl'), locator: value('locator'),
    reviewer: value('reviewer'), reviewedAt: value('reviewedAt'), explanation, explanationLocator});
  byId('download').disabled = false;
  message.textContent = 'Đã thêm ' + drafts.size + ' quyết định. Tải JSON để nhập vào công cụ kiểm tra.';
};
byId('download').onclick = () => {
  const url = URL.createObjectURL(new Blob([JSON.stringify([...drafts.values()], null, 2)], {type:'application/json'}));
  const link = document.createElement('a');
  link.href = url; link.download = 'study-review-decisions.json'; link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
};
byId('reviewedAt').value = new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().slice(0, 10);
byId('coverage').textContent = rows.length + ' câu · ' + rows.filter(row => row.sourceKey).length +
  ' có đáp án nguồn · ' + rows.filter(row => row.key).length + ' đã duyệt';
byId('pendingKeys').checked = rows.some(row => row.queue?.status === 'AWAITING_REVIEW');
filter();
</script>
</body>
</html>
"""
