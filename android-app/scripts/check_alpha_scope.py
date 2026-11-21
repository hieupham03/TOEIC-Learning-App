#!/usr/bin/env python3
"""Static safety lint for bounded CX-00..03. Not a compiler, ECP or QA pass."""
from pathlib import Path
import xml.etree.ElementTree as ET
root = Path(__file__).resolve().parents[1]
manifest = (root / 'app/src/main/AndroidManifest.xml').read_text(encoding='utf-8')
app = root / 'app/src/main/java/vn/toeiclearning/alpha'
models = (app / 'domain/AlphaModels.kt').read_text(encoding='utf-8')
fixtures = (app / 'domain/SyntheticCatalogue.kt').read_text(encoding='utf-8')
ui = (app / 'ui/AlphaApp.kt').read_text(encoding='utf-8')
ET.fromstring(manifest)
checks = {
    'no INTERNET permission': '<uses-permission' not in manifest,
    'only synthetic fixture types': 'syntheticOnly: Boolean = true' in models,
    'B1 A/B blocked in domain': 'realMockApprovedForLaunch: Boolean = false' in fixtures,
    'Part 1..4 blocked in fixture': fixtures.count('ContentReadiness.NOT_QA_READY') >= 6,
    'clear practice answer NOT SAVED wording': 'chưa lưu bền vững' in ui,
    'mock screen visibly blocks launch': 'CHƯA THỂ BẮT ĐẦU' in ui,
    'reading has passage return': 'Về đoạn văn' in ui and 'Đọc lại đoạn văn' in ui,
    'three approved tab labels': all(s in ui for s in ('Bắt đầu', 'Tiến độ', 'Cá nhân')),
    'no backend dependencies': not (root/'app/src/main/java/vn/toeiclearning/alpha/data/remote').exists(),
    'no MP3 fixtures': not any((root/'app/src/main').rglob('*.mp3')),
}
for name, ok in checks.items():
    print(('PASS' if ok else 'FAIL') + ' static: ' + name)
if not all(checks.values()):
    raise SystemExit('Scope guard failure')
print(f'ALPHA STATIC SCOPE GUARD: PASS ({len(checks)} documentary checks); Android build NOT RUN')
