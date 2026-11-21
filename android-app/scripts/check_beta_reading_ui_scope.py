#!/usr/bin/env python3
"""Static BUI-01..03 boundary guard; not a compiler, device check, ECP or QA pass."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
app = root / "app/src/main/java/vn/toeiclearning/alpha"
models = (app / "domain/AlphaModels.kt").read_text(encoding="utf-8")
fixtures = (app / "domain/SyntheticCatalogue.kt").read_text(encoding="utf-8")
ui = (app / "ui/AlphaApp.kt").read_text(encoding="utf-8")

reading_ui = ui.partition("private fun ReadingScreen(")[2].partition("private fun MockBlockedScreen(")[0]
reading_column = re.search(r"\bColumn\(\s*modifier\s*=\s*([^,]+),", reading_ui)
reading_modifier = re.sub(r"\s+", "", reading_column[1]) if reading_column else ""

checks = {
    "Reading session remains in-memory": "data class ReadingSession" in models and "returnToPassage" in models,
    "passage anchor is captured before questions": "openQuestions(itemIndex: Int, itemOffset: Int)" in models,
    "synthetic Part 6/7 fixtures stay bounded": "DEMO-P6-TEXT" in fixtures and "DEMO-P7-TEXT" in fixtures,
    "responsive reading gutter is source-defined": "val readingGutter = if (maxWidth < 400.dp)" in ui,
    "Reading column caps width at 720dp before filling and stays centered":
        reading_modifier == "Modifier.widthIn(max=720.dp).fillMaxSize().align(Alignment.TopCenter)",
    "passage list has stable keys": "key = { index, _ -> \"${passage.id}-$index\" }" in ui,
    "question navigation remains horizontally scrollable": "LazyRow(" in ui,
    "radio choices expose native selection semantics": "Role.RadioButton" in ui and ".selectable(" in ui,
    "tap targets are source-targeted at 48dp": "heightIn(min = 48.dp)" in ui,
    "no remote data package": not (app / "data/remote").exists(),
    "no media assets introduced": not any((root / "app/src/main").rglob("*.mp3")),
}

for name, ok in checks.items():
    print(("PASS" if ok else "FAIL") + " static: " + name)
if not all(checks.values()):
    raise SystemExit("Beta Reading UI scope guard failure")
print(f"BETA READING UI SCOPE GUARD: PASS ({len(checks)} documentary checks); device/QA NOT RUN")
