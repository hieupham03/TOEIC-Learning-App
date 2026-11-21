"""All transport responses and question/media records in this module are synthetic."""
from copy import deepcopy
from hashlib import sha256
from io import BytesIO
import html
import json
from pathlib import Path
import ssl
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from urllib.error import URLError

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import crawl_one_zenlish_part3_group as crawler
import crawl_zenlish_representative_groups as representative
import listening_http as http


PAGE, AUDIO = crawler.PAGE, crawler.AUDIO
ROBOTS = "https://zenlishtoeic.vn/robots.txt"


def fixture():
    return {"title": "Synthetic transport sample", "audio_url": AUDIO, "is_grouped": True,
            "sub_questions": [{
                "question_id": 700 + index, "index": str(index), "title": '<p>Invented &quot;prompt&quot;</p>',
                "choices": {label: f"Generated option {label}" for label in "ABCD"},
            } for index in crawler.INDICES], "question_id": "41021"}


def wrapped(group):
    return "<script>window.syntheticQuiz = " + json.dumps({"group": group}) + ";</script>"


def frames():
    return (bytes.fromhex("fffb90c0") + bytes(413)) * 3


class Reply(BytesIO):
    def __init__(self, url, spec):
        self.url, self.status, self.headers, data = url, *spec
        super().__init__(data)

    def geturl(self):
        return self.url


def response(status=200, body=b"", mime="text/html", **headers):
    return (status, {"Content-Type": mime, "Content-Length": str(len(body)), **headers}, body)


class FakeServer:
    def __init__(self, *specs):
        self.specs, self.urls, self.times = list(specs), [], []
        self.seconds = 0

    def open(self, request, timeout):
        assert timeout == 20
        assert "Cookie" not in request.headers and "Authorization" not in request.headers
        self.urls.append(request.full_url)
        self.times.append(self.seconds)
        spec = self.specs.pop(0)
        if isinstance(spec, Exception):
            raise spec
        return Reply(request.full_url, spec)

    def sleep(self, seconds):
        self.seconds += seconds

    def client(self):
        return http.BoundedClient(opener=self, now=lambda: self.seconds, sleep=self.sleep)


class ParserTests(unittest.TestCase):
    def test_changed_key_order_and_json_map_choices(self):
        rows = crawler.normalize_questions(crawler.extract_group(wrapped(fixture())))
        self.assertEqual([q["index"] for q in rows], [32, 33, 34])
        self.assertEqual(rows[0]["prompt"], 'Invented "prompt"')
        self.assertEqual(rows[0]["answer"]["status"], "ANSWER_KEY_UNVERIFIED")
        self.assertEqual(rows[0]["source_item_id"], 732)

    def test_nested_json_string_and_html_attribute(self):
        raw = json.dumps(fixture())
        for doc in (f"<script>JSON.parse({json.dumps(raw)})</script>",
                    f'<div data-quiz="{html.escape(raw, quote=True)}"></div>', raw):
            with self.subTest(kind=doc[:12]):
                self.assertEqual(len(crawler.normalize_questions(crawler.extract_group(doc))), 3)

    def test_wrong_audio_and_conflicting_identical_group_ids(self):
        wrong = fixture()
        wrong["audio_url"] = "/synthetic/wrong.mp3"
        for doc in (wrapped(wrong), wrapped(fixture()) + wrapped(wrong),
                    "<script>{malformed</script>", "<html><title>Ordinary page</title></html>"):
            with self.assertRaises(ValueError):
                crawler.extract_group(doc)

    def test_wrong_order_duplicate_ids_and_malformed_questions(self):
        original = fixture()
        for modify in (lambda q: q.reverse(), lambda q: q[0].update(question_id=q[1]["question_id"]),
                       lambda q: q[0].update(group_id=999), lambda q: q.pop(),
                       lambda q: q[0].update(choices={"A": "Only choice"}),
                       lambda q: q[0].update(choices=dict.fromkeys("ABCD", "")),
                       lambda q: q.__setitem__(0, None)):
            record = deepcopy(original)
            modify(record["sub_questions"])
            with self.assertRaises(ValueError):
                crawler.normalize_questions(record)

    def test_parent_echo_and_no_guessed_answer(self):
        record = fixture()
        record["sub_questions"][0].update(question_id=41021, answer="B")
        record["sub_questions"][1].update(answer="ambiguous option")
        items = crawler.normalize_questions(record)
        self.assertIsNone(items[0]["source_item_id"])
        self.assertEqual(items[0]["answer"]["label"], "B")
        self.assertIsNone(items[1]["answer"]["label"])

    def test_title_number_and_answer_array_variant(self):
        record = fixture()
        for index, question in zip(crawler.INDICES, record["sub_questions"]):
            question.clear()
            question.update(title=f"<p>{index}. Generated example</p>",
                            answer=[{"choice": letter, "choice_answer": f"Demo {letter}"} for letter in "ABCD"])
        items = crawler.normalize_questions(crawler.extract_group(wrapped(record)))
        self.assertEqual([item["index"] for item in items], list(crawler.INDICES))
        self.assertTrue(all(item["source_item_id"] is None and item["answer"]["label"] is None for item in items))
        record["sub_questions"][0]["index"] = 33
        with self.assertRaises(ValueError):
            crawler.normalize_questions(record)

    def test_interstitials_stop(self):
        for title in ("Just a moment...", "Sign in", "Access Denied"):
            with self.assertRaises(http.FetchError) as caught:
                crawler.extract_group(f"<title>{title}</title>")
            self.assertTrue(caught.exception.blocked)

    def test_mp3_mime_and_truncation(self):
        self.assertGreater(crawler.check_audio(http.Response(AUDIO, 200, "audio/mpeg", frames()))["duration_seconds"], 0)
        for mime, body in (("text/html", frames()), ("audio/mpeg", b"ID3" + b"x"*1024),
                           ("audio/mpeg", frames()[:-3])):
            with self.assertRaises(ValueError):
                crawler.check_audio(http.Response(AUDIO, 200, mime, body))
        with self.assertRaises(ValueError):
            crawler.check_audio(http.Response(PAGE + "wrong-clip.mp3", 200, "audio/mpeg", frames()), AUDIO)

    def test_part_one_labels_only_and_photo_are_bound_to_the_same_group(self):
        target = representative.TARGETS[0]
        row = {"question_id": target[1], "is_grouped": False, "audio_url": "/safe/" + target[3],
               "content": '<img src="/synthetic/example.png">',
               "sub_questions": [{"title": "1.", "answer": [
                   {"choice": letter, "choice_answer": ""} for letter in "ABCD"]}]}
        questions, audio_url, image = representative.load_group(wrapped(row), PAGE, target)
        self.assertTrue(audio_url.endswith(target[3]))
        self.assertTrue(image.endswith("synthetic/example.png"))
        self.assertEqual(questions[0]["presentation"], "SOURCE_LABELS_ONLY")
        self.assertEqual(questions[0]["image_source_url"], image)
        self.assertIsNone(questions[0]["answer"]["label"])
        row["content"] += '<img src="/synthetic/ambiguous.png">'
        with self.assertRaises(ValueError):
            representative.load_group(wrapped(row), PAGE, target)


class TransportTests(unittest.TestCase):
    def test_same_host_redirect_counted_and_throttled(self):
        server = FakeServer(response(404), response(302, Location="/approved-page/"), response(body=b"good"))
        client = server.client()
        got = client.get(PAGE, limit=8, accept="text/html")
        self.assertEqual(got.body, b"good")
        self.assertEqual(server.times, [0, 3, 6])
        self.assertEqual((client.requests, client.downloaded), (3, 4))

    def test_redirect_to_unapproved_host_insecure_or_sign_in_not_requested(self):
        for dest in ("https://other.invalid/media", "http://zenlishtoeic.vn/media",
                     "https://study4.com/same-budget-not-same-host", "/login/?continue=test"):
            server = FakeServer(response(404), response(302, Location=dest))
            client = server.client()
            with self.assertRaises(http.FetchError):
                client.get(AUDIO, limit=100, accept="audio/mpeg")
            self.assertEqual(server.urls, [ROBOTS, AUDIO])

    def test_403_429_and_robots_disallow_stop_host(self):
        for specs, count in (([response(403)], 1), ([response(404), response(429)], 2),
                             ([response(body=b"User-agent: *\nDisallow: /stm-*", mime="text/plain")], 1)):
            server = FakeServer(*specs)
            client = server.client()
            for _ in range(2):
                with self.assertRaises(http.FetchError) as caught:
                    client.get(PAGE, limit=100, accept="text/html")
                self.assertTrue(caught.exception.blocked)
            self.assertEqual(client.requests, count)

    def test_robots_allow_more_specific_path_and_respect_delay(self):
        data = b"User-agent: *\nDisallow: /stm-*\nAllow: /stm-quizzes/test-1-2022/$\nCrawl-delay: 5\n"
        server = FakeServer(response(body=data, mime="text/plain"), response(body=b"x"))
        server.client().get(PAGE, limit=10, accept="text/html")
        self.assertEqual(server.times, [0, 5])

    def test_network_timeout_and_503_retry_finitely(self):
        server = FakeServer(response(404), URLError(TimeoutError("synthetic")), response(503), response(502))
        client = server.client()
        with self.assertRaises(http.FetchError):
            client.get(PAGE, limit=10, accept="text/html")
        self.assertEqual(client.requests, 4)
        self.assertEqual(client.audit[1]["error_type"], "TimeoutError")

    def test_certificate_error_is_never_retried(self):
        server = FakeServer(URLError(ssl.SSLCertVerificationError("synthetic trust failure")))
        client = server.client()
        with self.assertRaises(http.FetchError) as caught:
            client.get(PAGE, limit=10, accept="text/html")
        self.assertTrue(caught.exception.blocked)
        self.assertEqual(client.requests, 1)

    def test_retry_after_and_size_budgets_hard_stop(self):
        for explicit in (response(503, **{"Retry-After": "1000"}), response(body=b"x"*20),
                         response(body=b"short", **{"Content-Length": "9"})):
            server = FakeServer(response(404), explicit)
            client = server.client()
            with self.assertRaises(http.FetchError):
                client.get(PAGE, limit=10, accept="text/html")
            self.assertEqual(client.requests, 2)
        client = FakeServer().client()
        client.robots["zenlishtoeic.vn"] = None
        client.requests = http.MAX_REQUESTS
        with self.assertRaises(http.FetchError):
            client.get(PAGE, limit=10, accept="text/html")
        self.assertEqual(client.requests, http.MAX_REQUESTS)

    def test_batch_byte_budget_limits_a_single_eligible_response(self):
        server = FakeServer(response(body=b"xx"))
        client = server.client()
        client.robots["zenlishtoeic.vn"] = None
        client.downloaded = http.MAX_BYTES - 1
        with self.assertRaises(http.FetchError):
            client.get(AUDIO, limit=http.MAX_MEDIA, accept="audio/mpeg")
        self.assertEqual(client.downloaded, http.MAX_BYTES - 1)
        self.assertEqual(client.audit[0]["bytes"], 0)

    def test_no_audio_request_until_group_is_valid(self):
        server = FakeServer(response(404), response(body=b"<html><p>Synthetic changed layout</p></html>"))
        with TemporaryDirectory() as temporary:
            receipt = crawler.run(Path(temporary), server.client())
        self.assertEqual(receipt["status"], "PARTIAL")
        self.assertEqual(receipt["questions"], 0)
        self.assertEqual(server.urls, [ROBOTS, PAGE])

    def test_receipt_continuation_carries_ledger_and_never_refetches_html(self):
        page = wrapped(fixture()).encode("utf-8")
        with TemporaryDirectory() as temporary:
            folder = Path(temporary)
            (folder / "source_page.html").write_bytes(page)
            previous = {"status": "PARTIAL", "page": {"url": PAGE, "response_status": 200, "bytes": len(page),
                                                     "sha256": sha256(page).hexdigest(), "mime": "text/html"},
                        "http_requests": 2, "downloaded_bytes": len(page),
                        "request_audit": [{"url": ROBOTS}, {"url": PAGE}], "retrieved_at_utc": "synthetic"}
            server = FakeServer(response(404), response(body=frames(), mime="audio/mpeg"))
            with patch.object(crawler, "BoundedClient", return_value=server.client()), patch.object(
                    crawler, "probe_audio", return_value={"decode_status": "NOT_RUN", "probe_status": "NOT_RUN"}):
                got = crawler.continue_from_receipt(folder, previous)
                self.assertEqual(got["status"], "FETCHED")
                self.assertEqual(got["http_requests"], 4)
                self.assertEqual(got["downloaded_bytes"], len(page) + len(frames()))
                self.assertEqual(server.urls, [ROBOTS, AUDIO])
                with self.assertRaises(FileExistsError):
                    crawler.continue_from_receipt(folder, previous)
                self.assertEqual(server.urls, [ROBOTS, AUDIO])


if __name__ == "__main__":
    unittest.main()
