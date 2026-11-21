"""Offline integrity and format checks for bounded Listening media."""
from hashlib import sha256
from io import BytesIO
from pathlib import Path
import json
import math
import shutil
import struct
import subprocess
import wave
import zlib


def mp3_info(data):
    offset = 0
    if data.startswith(b"ID3"):
        if len(data) < 10 or any(byte >= 128 for byte in data[6:10]):
            raise ValueError("Malformed MP3 ID3 header")
        tag_size = sum(byte << (7 * (3 - i)) for i, byte in enumerate(data[6:10]))
        offset = 10 + tag_size + (10 if data[3] == 4 and data[5] & 0x10 else 0)
    end = len(data)
    if end - offset >= 128 and data[-128:-125] == b"TAG":
        end -= 128
    rates = (44100, 48000, 32000)
    v1 = (0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 0)
    v2 = (0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, 0)
    frames, samples = 0, 0
    format_key = None
    while offset < end:
        if end - offset < 4:
            raise ValueError("Truncated MP3 frame header")
        header = int.from_bytes(data[offset:offset+4], "big")
        version, layer = (header >> 19) & 3, (header >> 17) & 3
        bit_index, rate_index = (header >> 12) & 15, (header >> 10) & 3
        if header >> 21 != 2047 or version == 1 or layer != 1 or rate_index == 3:
            raise ValueError("Invalid MPEG Layer III frame")
        rate = rates[rate_index] // {0: 4, 2: 2, 3: 1}[version]
        bitrate = (v1 if version == 3 else v2)[bit_index]
        channels = 1 if (header >> 6) & 3 == 3 else 2
        if not bitrate or (format_key is not None and format_key != (rate, channels)):
            raise ValueError("Unsupported MP3 framing or format change")
        size = (144000 if version == 3 else 72000) * bitrate // rate + ((header >> 9) & 1)
        if offset + size > end:
            raise ValueError("Truncated MP3 frame payload")
        format_key = (rate, channels)
        frames += 1
        samples += 1152 if version == 3 else 576
        offset += size
    if frames < 2:
        raise ValueError("MP3 needs at least two complete frames")
    return {"mime": "audio/mpeg", "format": "mp3", "sample_rate_hz": rate, "channels": channels,
            "duration_seconds": round(samples / rate, 6), "duration_method": "mpeg_frame_estimate"}


def wav_info(data):
    if len(data) < 44 or int.from_bytes(data[4:8], "little") != len(data) - 8:
        raise ValueError("Truncated or inconsistent WAV container length")
    try:
        with wave.open(BytesIO(data), "rb") as stream:
            frames = stream.getnframes()
            size = frames * stream.getsampwidth() * stream.getnchannels()
            if not frames or len(stream.readframes(frames)) != size:
                raise ValueError("WAV has empty or truncated PCM")
            return {"mime": "audio/wav", "format": "wav", "sample_rate_hz": stream.getframerate(),
                    "channels": stream.getnchannels(), "duration_seconds": round(frames / stream.getframerate(), 6),
                    "duration_method": "pcm_frame_count"}
    except (wave.Error, EOFError) as error:
        raise ValueError("Invalid or unsupported PCM WAV") from error


def png_info(data):
    offset, seen = 8, []
    while offset + 12 <= len(data):
        length, kind = struct.unpack_from(">I4s", data, offset)
        end = offset + 8 + length
        if end + 4 > len(data) or zlib.crc32(data[offset+4:end]) != int.from_bytes(data[end:end+4], "big"):
            raise ValueError("Invalid PNG chunk length or CRC")
        seen.append(kind)
        if len(seen) == 1 and (kind != b"IHDR" or length != 13 or 0 in struct.unpack_from(">II", data, offset+8)):
            raise ValueError("Invalid PNG header")
        offset = end + 4
        if kind == b"IEND":
            if not length and offset == len(data) and b"IDAT" in seen:
                return {"mime": "image/png", "format": "png"}
            break
    raise ValueError("Missing PNG data or terminal chunk")


def jpeg_info(data):
    offset, frame, scan = 2, False, False
    frame_markers = {0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7,
                     0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf}
    while offset < len(data) and data[offset] == 0xff:
        while offset < len(data) and data[offset] == 0xff:
            offset += 1
        if offset == len(data):
            break
        marker = data[offset]
        offset += 1
        if marker == 0xd9:
            if frame and scan and offset == len(data):
                return {"mime": "image/jpeg", "format": "jpeg"}
            break
        if marker in {0, 0xd8} or 0xd0 <= marker <= 0xd7 or offset + 2 > len(data):
            break
        length = int.from_bytes(data[offset:offset+2], "big")
        end = offset + length
        if length < 2 or end > len(data):
            break
        if marker in frame_markers:
            if length < 11:
                break
            height, width = struct.unpack_from(">HH", data, offset + 3)
            if not height or not width or length != 8 + 3 * data[offset + 7]:
                break
            frame = True
        if marker == 0xda:
            if not frame or length < 8 or length != 6 + 2 * data[offset + 2]:
                break
            # Entropy bytes escape 0xFF as FF00. Restart markers are also
            # part of the scan. All other markers end the current scan.
            cursor = end
            while True:
                marker_start = data.find(b"\xff", cursor)
                if marker_start < 0 or marker_start + 1 == len(data):
                    raise ValueError("JPEG scan has no terminal marker")
                code = marker_start + 1
                while code < len(data) and data[code] == 0xff:
                    code += 1
                if code == len(data):
                    raise ValueError("JPEG scan has a truncated marker")
                if data[code] == 0 or 0xd0 <= data[code] <= 0xd7:
                    cursor = code + 1
                else:
                    if marker_start == end:
                        raise ValueError("JPEG contains an empty scan")
                    scan = True
                    end = marker_start
                    break
        offset = end
    raise ValueError("Malformed or truncated JPEG marker structure")


def inspect_media(data):
    if data.startswith(b"RIFF") and data[8:12] == b"WAVE":
        info = wav_info(data)
    elif data.startswith(b"ID3") or (len(data) >= 2 and data[0] == 0xff and data[1] & 0xe0 == 0xe0
                                      and not data.startswith(b"\xff\xd8\xff")):
        info = mp3_info(data)
    elif data.startswith(b"\x89PNG\r\n\x1a\n"):
        info = png_info(data)
    elif data.startswith(b"\xff\xd8\xff"):
        info = jpeg_info(data)
    else:
        raise ValueError("Unsupported or malformed media signature")
    return {"bytes": len(data), "sha256": sha256(data).hexdigest(), **info}


def probe_audio(path: Path):
    """Metadata probe and optional full decode using already installed tools."""
    probe = shutil.which("ffprobe")
    decoder = shutil.which("ffmpeg")
    found = {"probe_status": "NOT_RUN", "decode_status": "NOT_RUN"}
    for kind, tool, args in (
        ("probe", probe, ["-v", "error", "-protocol_whitelist", "file", "-show_entries",
                         "stream=codec_name,channels,sample_rate:format=duration,format_name", "-of", "json", str(path)]),
        ("decode", decoder, ["-nostdin", "-v", "error", "-xerror", "-protocol_whitelist", "file",
                             "-i", str(path), "-map", "0:a:0", "-f", "null", "-"]),
    ):
        if not tool:
            continue
        try:
            process = subprocess.run([tool, *args], capture_output=True, timeout=20, check=False)
            found[f"{kind}_exit_code"] = process.returncode
            found[f"{kind}_status"] = "PASS" if process.returncode == 0 else "FAIL"
            if kind == "probe" and process.returncode == 0:
                parsed = json.loads(process.stdout)
                audio = parsed["streams"][0]
                duration = float(parsed["format"]["duration"])
                if not math.isfinite(duration) or duration <= 0:
                    raise ValueError("Invalid probed duration")
                found["probed"] = {"duration_seconds": duration, "format": parsed["format"]["format_name"],
                                   "codec": audio["codec_name"], "channels": audio["channels"],
                                   "sample_rate_hz": int(audio["sample_rate"])}
        except (OSError, TypeError, ValueError, KeyError, IndexError, subprocess.TimeoutExpired):
            found[f"{kind}_status"] = "FAIL"
    return found
