"""Bounded, anonymous transport for the three approved public sites."""
from dataclasses import dataclass
from http.client import HTTPException, IncompleteRead
import re
import ssl
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

HOSTS = frozenset({"zenlishtoeic.vn", "test.thetoeiclab.vn", "study4.com"})
USER_AGENT = "TOEIC-Learning-App/1.0 (bounded public sample, Product Owner request)"
MAX_BYTES = 32 * 1024**2
MAX_MEDIA = 12 * 1024**2
MAX_REQUESTS = 24
REDIRECTS = {301, 302, 303, 307, 308}
TRANSIENT = {500, 502, 503, 504}


class FetchError(ValueError):
    def __init__(self, reason, *, blocked=False):
        super().__init__(reason)
        self.blocked = blocked


def approved_host(url):
    try:
        parsed = urlsplit(url)
        if (parsed.scheme == "https" and parsed.hostname in HOSTS and parsed.port in (None, 443)
                and parsed.username is None and parsed.password is None and not parsed.fragment
                and "%" not in (parsed.path + parsed.query) and url.isascii()
                and not any(ord(char) <= 32 or char == "\\" for char in url)):
            return parsed.hostname
    except ValueError:
        pass
    raise FetchError("URL outside approved HTTPS scope", blocked=True)


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def robot_rules(text):
    """Select product-token rules, or the wildcard group when absent."""
    groups, agents, directives = [], [], []
    for line in text.splitlines():
        key, sep, value = line.partition("#")[0].partition(":")
        if not sep:
            continue
        key, value = key.strip().lower(), value.strip()
        if key == "user-agent":
            if directives:
                groups.append((agents, directives))
                agents, directives = [], []
            agents.append(value.lower())
        elif agents and key in {"allow", "disallow", "crawl-delay", "request-rate"}:
            directives.append((key, value))
    groups.append((agents, directives))
    token = USER_AGENT.partition("/")[0].lower()
    specific = [rules for agents, rules in groups if token in agents]
    selected = specific or [rules for agents, rules in groups if "*" in agents]
    return [rule for rules in selected for rule in rules]


def robot_allows(rules, url):
    location = urlsplit(url)
    target = (location.path or "/") + ("?" + location.query if location.query else "")
    matches = []
    for key, rule in rules:
        if not rule or key not in {"allow", "disallow"}:
            continue
        anchor = rule.endswith("$")
        pattern = rule.removesuffix("$")
        # Collapse consecutive wildcards and use ordered literal searches,
        # avoiding backtracking on a remote robots.txt.
        first, *rest = pattern.split("*")
        if not target.startswith(first):
            continue
        if not rest:
            matched = not anchor or target == first
        else:
            position = len(first)
            if anchor and rest[-1]:
                suffix = rest.pop()
                limit = len(target) - len(suffix)
                matched = limit >= position and target.endswith(suffix)
            else:
                limit, matched = len(target), True
            for literal in rest:
                index = target.find(literal, position, limit)
                if index < 0:
                    matched = False
                    break
                position = index + len(literal)
        if matched:
            matches.append((len(pattern.replace("*", "").encode("utf-8")), key == "allow"))
    return max(matches, default=(0, True))[1]


@dataclass(frozen=True)
class Response:
    url: str
    status: int
    content_type: str
    body: bytes


class BoundedClient:
    def __init__(self, *, opener=None, now=time.monotonic, sleep=time.sleep,
                 max_requests=MAX_REQUESTS, max_bytes=MAX_BYTES):
        if not 1 <= max_requests <= 80 or not 1 <= max_bytes <= 100 * 1024**2:
            raise ValueError("Invalid bounded transport budget")
        self.opener = opener if opener is not None else build_opener(ProxyHandler({}), NoRedirect())
        self.max_requests, self.max_bytes = max_requests, max_bytes
        self.now, self.sleep = now, sleep
        self.requests = 0
        self.downloaded = 0
        self.last_start = {}
        self.robots = {}
        self.delay = {}
        self.blocked_hosts = set()
        self.audit = []

    def get(self, url, *, limit, accept):
        host = approved_host(url)
        if host in self.blocked_hosts:
            raise FetchError("Source already stopped", blocked=True)
        try:
            if host not in self.robots:
                self._load_robots(host)
            return self._follow(url, min(limit, MAX_MEDIA), accept, check_robots=True)
        except FetchError as error:
            if error.blocked:
                self.blocked_hosts.add(host)
            raise

    def _load_robots(self, host):
        url = f"https://{host}/robots.txt"
        response = self._follow(url, 256 * 1024, "text/plain", check_robots=False)
        if response.status in {404, 410}:
            self.robots[host] = None
            return
        text = response.body.decode("utf-8-sig", errors="replace")
        if (response.status != 200 or not response.content_type.startswith("text/plain")
                or "\ufffd" in text or "<html" in text.lower()):
            raise FetchError("Unable to establish robots policy", blocked=True)
        rules = robot_rules(text)
        for key, value in rules:
            if key == "request-rate":
                raise FetchError("Robots request-rate requires separate review", blocked=True)
            if key in {"allow", "disallow"} and ("%" in value or not value.isascii()):
                raise FetchError("Encoded robots rules require separate review", blocked=True)
            if key != "crawl-delay":
                continue
            try:
                seconds = float(value)
            except ValueError as error:
                raise FetchError("Unknown robots crawl delay", blocked=True) from error
            if not 0 <= seconds <= 20:
                raise FetchError("Robots delay outside bounded session", blocked=True)
            self.delay[host] = max(self.delay.get(host, 3), seconds)
        self.robots[host] = rules

    def _follow(self, url, limit, accept, *, check_robots):
        host = approved_host(url)
        redirected = {url}
        retries = 0
        while True:
            if check_robots:
                if re.search(r"(?i)/(?:login|signin|sign-in|wp-login\.php|dang-nhap)(?:[/?]|$)", urlsplit(url).path):
                    raise FetchError("Redirect or target requires sign-in", blocked=True)
                policy = self.robots.get(host)
                if policy is not None and not robot_allows(policy, url):
                    raise FetchError("robots.txt disallows the target", blocked=True)
            response, location, retry_after = self._attempt(url, limit, accept, check_robots)
            if response.status in (401, 403, 407, 429, 451):
                raise FetchError(f"HTTP {response.status} — source stopped", blocked=True)
            if response.status in REDIRECTS:
                if not location or len(redirected) >= 4:
                    raise FetchError("Redirect limit or invalid Location", blocked=True)
                destination = urljoin(url, location)
                if approved_host(destination) != host or destination in redirected:
                    raise FetchError("Cross-host or looping redirect refused", blocked=True)
                if not check_robots and urlsplit(destination).path != "/robots.txt":
                    raise FetchError("robots.txt redirected away from its policy path", blocked=True)
                redirected.add(destination)
                url = destination
                continue
            if response.status in TRANSIENT or response.status == 0:
                if retries >= 2 or retry_after:
                    raise FetchError(f"Transient failure after bounded attempts ({response.status or 'network error'})",
                                     blocked=True)
                retries += 1
                self.sleep(3 * retries)
                continue
            if response.status == 200 or (not check_robots and response.status in (404, 410)):
                return response
            raise FetchError(f"Unexpected HTTP {response.status}",
                             blocked=not check_robots or response.status >= 500)

    def _attempt(self, url, limit, accept, check_robots):
        host = approved_host(url)
        available = min(limit, self.max_bytes - self.downloaded)
        if self.requests >= self.max_requests or available <= 0:
            raise FetchError("Batch request or byte budget exhausted", blocked=True)
        delay = self.delay.get(host, 3)
        if host in self.last_start:
            self.sleep(max(0, delay - (self.now() - self.last_start[host])))
        started = self.now()
        self.last_start[host] = started
        self.requests += 1
        entry = {"url": url, "status": None, "bytes": 0}
        self.audit.append(entry)
        request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept, "Accept-Encoding": "identity"})
        try:
            with self.opener.open(request, timeout=20) as response:
                status = entry["status"] = response.status
                if response.geturl() != url:
                    raise FetchError("Unexpected automatic redirect", blocked=True)
                if status != 200:
                    return Response(url, status, "", b""), response.headers.get("Location"), response.headers.get("Retry-After")
                if response.headers.get("Content-Encoding", "identity").lower() != "identity":
                    raise FetchError("Unexpected encoded response")
                length = response.headers.get("Content-Length")
                if length is not None and (not length.isdigit() or int(length) > available):
                    raise FetchError("Response exceeds allowed size or has invalid length", blocked=True)
                body = bytearray()
                while len(body) < available:
                    chunk = response.read(min(65536, available - len(body)))
                    if not chunk:
                        break
                    body.extend(chunk)
                    entry["bytes"] += len(chunk)
                    self.downloaded += len(chunk)
                    if self.now() - started > 20:
                        raise TimeoutError("response exceeded the request deadline")
                if (length is None and len(body) == available) or (length is not None and len(body) != int(length)):
                    raise FetchError("Response incomplete or reached size limit without length", blocked=True)
                mime = response.headers.get("Content-Type", "").split(";", 1)[0].strip().lower()
                return Response(url, status, mime, bytes(body)), None, None
        except HTTPError as error:
            with error:
                entry["status"] = error.code
                return Response(url, error.code, "", b""), error.headers.get("Location"), error.headers.get("Retry-After")
        except IncompleteRead as error:
            entry["bytes"] += len(error.partial)
            self.downloaded += len(error.partial)
            entry["error_type"] = "IncompleteRead"
        except (OSError, URLError, HTTPException) as error:
            reason = getattr(error, "reason", error)
            entry["error_type"] = type(reason).__name__
            if isinstance(reason, OSError) and reason.errno is not None:
                entry["error_number"] = reason.errno
            if isinstance(reason, (ssl.SSLCertVerificationError, PermissionError)):
                raise FetchError("TLS trust or access error", blocked=True) from error
        return Response(url, 0, "", b""), None, None
