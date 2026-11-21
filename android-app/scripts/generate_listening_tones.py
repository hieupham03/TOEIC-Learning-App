#!/usr/bin/env python3
"""Generate original CX-04 tone fixtures using integer PCM synthesis."""
from hashlib import sha256
from io import BytesIO
from pathlib import Path
import struct
import wave

ASSETS = Path(__file__).resolve().parents[1] / "app/src/main/assets/listening_demo"
RATE = 16000
SECONDS = 6
FREQUENCIES = (330, 440, 550, 660)


def make_tone(frequency):
    pcm = bytearray()
    for index in range(RATE * SECONDS):
        phase = (index * frequency) % RATE
        # A triangle wave with quiet gaps and short fades to avoid hard clicks.
        triangle = 4 * min(phase, RATE - phase) - RATE
        position = index % RATE
        envelope = max(0, min(320, position, 11200 - position))
        pcm.extend(struct.pack("<h", (triangle * 3600 * envelope) // (RATE * 320)))
    buffer = BytesIO()
    with wave.open(buffer, "wb") as stream:
        stream.setparams((1, 2, RATE, 0, "NONE", "not compressed"))
        stream.writeframes(pcm)
    return buffer.getvalue()


if __name__ == "__main__":
    ASSETS.mkdir(parents=True, exist_ok=True)
    for part, frequency in enumerate(FREQUENCIES, 1):
        asset = ASSETS / f"cx04_tone_p{part}_v1.wav"
        data = make_tone(frequency)
        asset.write_bytes(data)
        print(f"{asset.name} {frequency} Hz {sha256(data).hexdigest()}")
