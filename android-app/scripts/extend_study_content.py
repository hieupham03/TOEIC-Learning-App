"""Replay or extend CONTENT-02 from the immutable local CONTENT-01 APK and cached source."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
from zipfile import ZipFile

from acquire_study_content import (
    BATCH as PREVIOUS, PAGE, ROOT, SOURCE, fetch_asset, parse_study_record, snapshot_groups,
    project_items, read_json, write_json,
)
from activate_study_content import group_assets, verify_media
from listening_http import BoundedClient, FetchError

ROOT02 = ROOT / "content-02"
MAX_BATCH_BYTES = 100 * 1024**2
MAX_BATCH_REQUESTS = 80


def save_json(path, value):
    temp = path.with_suffix(".tmp")
    write_json(temp, value)
    temp.replace(path)


class ReceiptClient(BoundedClient):
    """Persist a conservative charge before sending a request."""

    def __init__(self, ledger):
        super().__init__(max_requests=MAX_BATCH_REQUESTS, max_bytes=MAX_BATCH_BYTES)
        self.ledger = ledger
        journal = read_json(ledger) if ledger.is_file() else {}
        self.audit = journal.get("http", [])
        self.requests = len(self.audit)
        self.downloaded = sum(row["bytes"] for row in self.audit)
        self.stop_reason = journal.get("stop_reason")
        refused = next((row["status"] for row in self.audit if row["status"] in (401, 403, 407, 429, 451)), None)
        if refused and not self.stop_reason:
            self.stop_reason = f"HTTP {refused} — source stopped"
        if self.audit:
            self.last_start["zenlishtoeic.vn"] = self.now()

    def persist(self, pending=None):
        save_json(self.ledger, {"http": self.audit + ([pending] if pending else []), "stop_reason": self.stop_reason})

    def _attempt(self, url, limit, accept, check_robots):
        remaining = min(limit, self.max_bytes - self.downloaded)
        if self.requests >= self.max_requests or remaining <= 0:
            raise FetchError("CONTENT-02 HTTP budget exhausted", blocked=True)
        # Persist the allowance as consumed if the process is killed before a result is recorded.
        self.persist({"url": url, "status": None, "bytes": remaining, "interrupted": True})
        try:
            return super()._attempt(url, limit, accept, check_robots)
        finally:
            self.persist()


def seed_previous(directory):
    target = directory / "base-media"
    target.mkdir(exist_ok=True)
    with ZipFile(PREVIOUS / "TOEIC-Study-0.3.1-debug.apk") as apk:
        raw = apk.read("assets/study_pack/pack.json")
        if sha256(raw).hexdigest() != read_json(PREVIOUS / "activation.json")["pack_sha256"]:
            raise ValueError("CONTENT-01 APK and activation receipt differ")
        base = json.loads(raw)
        if base.get("schema") != 1 or sum(len(g["items"]) for g in base["practice"]) != 101:
            raise ValueError("Expected the original 101-question CONTENT-01 pack")
        for group in base["practice"]:
            for _, asset in group_assets(group):
                body = apk.read("assets/" + asset["path"])
                if len(body) != asset["size"] or sha256(body).hexdigest() != asset["sha256"]:
                    raise ValueError("CONTENT-01 APK asset integrity mismatch")
                name = Path(asset["path"]).name
                file = target / name
                if not file.is_file() or file.read_bytes() != body:
                    file.write_bytes(body)
    return base


def snapshot_source():
    path = SOURCE / "zenlish-p3-q32-34/source_page.html"
    content = path.read_bytes()
    receipt = read_json(path.with_name("acquisition.json"))["page"]
    if sha256(content).hexdigest() != receipt["sha256"] or len(content) != receipt["bytes"] or receipt["url"] != PAGE:
        raise ValueError("Snapshot and request receipt differ")
    return content


def collect(directory=ROOT02, *, fetch=False):
    directory.mkdir(parents=True, exist_ok=True)
    media = directory / "media"
    media.mkdir(exist_ok=True)
    cache_file = directory / "media-receipts.json"
    cache = read_json(cache_file) if cache_file.exists() else {}
    client = ReceiptClient(directory / "http-journal.json")
    base = seed_previous(directory)
    snapshot = snapshot_source()
    version = sha256(snapshot).hexdigest()
    existing = {group["id"] for group in base["practice"]}
    hashes = {asset["sha256"] for group in base["practice"] for _, asset in group_assets(group)}

    def acquire(url, kind):
        if url in cache:
            row = cache[url]
            if "asset" in row:
                return row["asset"]
            raise ValueError(row["failure"])
        if not fetch or client.stop_reason:
            raise ValueError("Media not cached" if not client.stop_reason else "Network stopped for this batch")
        try:
            asset, receipt = fetch_asset(client, url, media, kind)
            cache[url] = {"asset": asset, "receipt": receipt}
            return asset
        except (FetchError, ValueError) as error:
            if isinstance(error, FetchError) and error.blocked:
                client.stop_reason = str(error)
                client.persist()
            cache[url] = {"failure": str(error)}
            raise
        finally:
            if url in cache:
                save_json(cache_file, cache)

    groups, omitted = [], []
    for source_id, record in snapshot_groups(snapshot.decode("utf-8-sig")).items():
        group_id = f"zenlish:{source_id}"
        if group_id in existing:
            continue
        try:
            part, questions, passage, audio_url, image_urls = parse_study_record(record)
            items = project_items(questions)
            audio = acquire(audio_url, "audio") if audio_url else None
            images = [acquire(url, "image") for url in image_urls]
            group = {"id": group_id, "part": part, "source": PAGE, "version": version,
                     "passage": passage, "audio": audio, "audioItems": [item["id"] for item in items] if audio else [],
                     "image": images[0] if images else None, "items": items}
            if len(images) > 1:
                group["extraImages"] = images[1:]
            current = [asset["sha256"] for _, asset in group_assets(group)]
            if len(current) != len(set(current)) or hashes.intersection(current):
                raise ValueError("Media duplicates another group")
            verify_media(group, media, media)
            hashes.update(current)
            groups.append(group)
        except (ValueError, OSError) as error:
            first = record["sub_questions"][0]
            omitted.append({"id": group_id, "count": len(record["sub_questions"]),
                            "first": first.get("index") or first.get("title", "").partition(".")[0], "reason": str(error)})
    save_json(directory / "new-groups.json", groups)
    report = {"snapshot": version, "new_groups": len(groups), "new_items": sum(len(g["items"]) for g in groups),
              "requests": client.requests, "bytes": client.downloaded, "omitted": omitted, "stop_reason": client.stop_reason}
    save_json(directory / "acquisition.json", report)
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true", help="Download uncached exact media within the persistent batch budget")
    print(json.dumps(collect(fetch=parser.parse_args().fetch), ensure_ascii=False))
