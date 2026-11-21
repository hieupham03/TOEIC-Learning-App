#!/usr/bin/env python3
"""Check original tone provenance and the separate synthetic Listening entry."""
import hashlib
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

sys.dont_write_bytecode = True
from generate_listening_tones import ASSETS, FREQUENCIES, make_tone

main = Path(__file__).resolve().parents[1] / "app/src/main"
source = main / "java/vn/toeiclearning/alpha"
ui = (source / "ui/AlphaApp.kt").read_text(encoding="utf-8")
screen = (source / "ui/ListeningDemoScreen.kt").read_text(encoding="utf-8")
domain = (source / "domain/ListeningDemo.kt").read_text(encoding="utf-8")
manifest = ET.parse(main / "AndroidManifest.xml")
expected = {ASSETS / f"cx04_tone_p{part}_v1.wav" for part in range(1, 5)}
inventory = dict(re.findall(r'fixture\(([1-4]), "([0-9a-f]{64})"\)', domain))
audio_extensions = {".wav", ".mp3", ".mp4", ".m4a", ".aac", ".ogg", ".opus", ".flac", ".amr", ".mid"}
audio_files = {p for p in main.rglob("*") if p.is_file() and p.suffix.lower() in audio_extensions}

checks = {
    "no declared Android permissions": not any(
        child.tag.startswith("uses-permission") for child in manifest.getroot()
    ),
    "only four authorized demo audio paths": audio_files == expected
    and {p for p in ASSETS.rglob("*") if p.is_file()} == expected,
    "distinct versioned hashes for Parts 1 through 4": len(set(inventory.values())) == 4,
    "separate Task Hub entry and blocked main Part picker": "AlphaRoute.LISTENING_DEMO" in ui
    and "enabled = part.canEnterSyntheticAlpha" in ui and "CHƯA THỂ BẮT ĐẦU" in ui,
    "visible synthetic and not-QA labels": "Không phải bài nghe TOEIC · Chưa QA" in screen,
}
for part, frequency in enumerate(FREQUENCIES, 1):
    asset = ASSETS / f"cx04_tone_p{part}_v1.wav"
    data = asset.read_bytes() if asset.is_file() else b""
    checks[f"Part {part} matches generator and declared SHA-256"] = (
        data == make_tone(frequency) and hashlib.sha256(data).hexdigest() == inventory.get(str(part))
    )

for label, passed in checks.items():
    print(f"{'PASS' if passed else 'FAIL'}: {label}")
if not all(checks.values()):
    raise SystemExit(1)
print(f"CX-04 LISTENING SOURCE GUARD: PASS ({len(checks)} checks)")
