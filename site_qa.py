#!/usr/bin/env python3
"""
Production QA crawler for idanstei.com
Standard-library only; no pip installs required.

Usage:
    python site_qa.py
    python site_qa.py > qa-report.txt

It checks:
- HTTPS / www redirect behavior
- robots.txt + sitemap.xml
- recursive same-origin crawl
- status codes / redirects
- titles, descriptions, canonicals, viewport, lang
- Open Graph / Twitter metadata
- JSON-LD presence/validity
- h1 counts
- image alt text
- internal links and assets
- PDF links
- mixed-content URLs
- old al-folio routes expected to be gone
- duplicate titles / descriptions
"""

from __future__ import annotations

import json
import re
import ssl
import sys
import time
from collections import defaultdict, deque
from dataclasses import dataclass, field
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse, urldefrag
from urllib.request import Request, build_opener, HTTPRedirectHandler
import xml.etree.ElementTree as ET

BASE = "https://idanstei.com/"
ORIGIN = "https://idanstei.com"
MAX_PAGES = 100
TIMEOUT = 15
UA = "IdanSteinbergProductionQA/1.0 (+site owner QA)"

EXPECTED_PUBLIC = {
    "https://idanstei.com/",
    "https://idanstei.com/cv/",
    "https://idanstei.com/publications/",
    "https://idanstei.com/thermoacoustic-imaging/",
}

OLD_ROUTES = [
    "/news/",
    "/plugins/",
    "/people/",
    "/blog/",
    "/projects/",
    "/repositories/",
    "/teaching/",
    "/books/",
]

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

no_redirect = build_opener(NoRedirect)

@dataclass
class Fetch:
    requested: str
    final: str = ""
    status: int = 0
    content_type: str = ""
    body: bytes = b""
    headers: dict = field(default_factory=dict)
    error: str = ""
    redirect_to: str = ""

def fetch(url: str, follow=True) -> Fetch:
    req = Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    opener = None if follow else no_redirect
    try:
        if opener:
            r = opener.open(req, timeout=TIMEOUT)
        else:
            from urllib.request import urlopen
            r = urlopen(req, timeout=TIMEOUT)
        body = r.read()
        return Fetch(
            requested=url,
            final=r.geturl(),
            status=getattr(r, "status", r.getcode()),
            content_type=r.headers.get_content_type() or "",
            body=body,
            headers=dict(r.headers.items()),
        )
    except HTTPError as e:
        body = b""
        try:
            body = e.read()
        except Exception:
            pass
        return Fetch(
            requested=url,
            final=getattr(e, "url", url),
            status=e.code,
            content_type=e.headers.get_content_type() if e.headers else "",
            body=body,
            headers=dict(e.headers.items()) if e.headers else {},
            error=str(e),
            redirect_to=e.headers.get("Location", "") if e.headers else "",
        )
    except (URLError, TimeoutError, OSError) as e:
        return Fetch(requested=url, final=url, error=str(e))

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self._in_title = False
        self.meta = []
        self.links = []
        self.images = []
        self.scripts = []
        self.stylesheets = []
        self.h1 = []
        self._in_h1 = False
        self._h1_parts = []
        self.html_lang = ""
        self.jsonld_raw = []

    @staticmethod
    def attrs_dict(attrs):
        return {str(k).lower(): (v or "") for k, v in attrs}

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        a = self.attrs_dict(attrs)
        if tag == "html":
            self.html_lang = a.get("lang", "")
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            self.meta.append(a)
        elif tag == "a":
            self.links.append(a)
        elif tag == "img":
            self.images.append(a)
        elif tag == "link":
            rel = a.get("rel", "").lower()
            if "stylesheet" in rel:
                self.stylesheets.append(a)
        elif tag == "script":
            self.scripts.append(a)
        elif tag == "h1":
            self._in_h1 = True
            self._h1_parts = []

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "title":
            self._in_title = False
        elif tag == "h1":
            self._in_h1 = False
            text = " ".join("".join(self._h1_parts).split())
            if text:
                self.h1.append(text)
            self._h1_parts = []

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_h1:
            self._h1_parts.append(data)

def meta_value(p: PageParser, *, name=None, prop=None):
    for m in p.meta:
        if name and m.get("name", "").lower() == name.lower():
            return m.get("content", "").strip()
        if prop and m.get("property", "").lower() == prop.lower():
            return m.get("content", "").strip()
    return ""

def canonical_value(p: PageParser):
    # HTMLParser stores <link> only if stylesheet in our main list, so parse canonicals separately
    # via regex is intentionally avoided; use a second tiny parser:
    return ""

class LinkMetaParser(PageParser):
    def __init__(self):
        super().__init__()
        self.link_tags = []
        self.script_stack = []
        self._in_jsonld = False
        self._jsonld_parts = []

    def handle_starttag(self, tag, attrs):
        super().handle_starttag(tag, attrs)
        a = self.attrs_dict(attrs)
        if tag.lower() == "link":
            self.link_tags.append(a)
        elif tag.lower() == "script":
            typ = a.get("type", "").lower()
            if typ == "application/ld+json":
                self._in_jsonld = True
                self._jsonld_parts = []

    def handle_endtag(self, tag):
        if tag.lower() == "script" and self._in_jsonld:
            raw = "".join(self._jsonld_parts).strip()
            if raw:
                self.jsonld_raw.append(raw)
            self._in_jsonld = False
            self._jsonld_parts = []
        super().handle_endtag(tag)

    def handle_data(self, data):
        if self._in_jsonld:
            self._jsonld_parts.append(data)
        super().handle_data(data)

def first_link_rel(p: LinkMetaParser, rel_name: str):
    rel_name = rel_name.lower()
    for a in p.link_tags:
        rels = a.get("rel", "").lower().split()
        if rel_name in rels:
            return a.get("href", "").strip()
    return ""

def normalize(url, base=BASE):
    if not url:
        return ""
    url = url.strip()
    if url.startswith(("mailto:", "tel:", "javascript:", "data:", "#")):
        return url
    absolute = urljoin(base, url)
    absolute, _ = urldefrag(absolute)
    return absolute

def same_origin(url):
    p = urlparse(url)
    return p.scheme in ("http", "https") and p.netloc.lower() == "idanstei.com"

def is_html(fetch_obj):
    return fetch_obj.content_type in ("text/html", "application/xhtml+xml") or (
        fetch_obj.body.lstrip().lower().startswith((b"<!doctype html", b"<html"))
    )

def status_label(code):
    if not code:
        return "ERROR"
    if 200 <= code < 300:
        return "OK"
    if 300 <= code < 400:
        return "REDIRECT"
    if 400 <= code < 500:
        return "CLIENT ERROR"
    return "SERVER ERROR"

def print_kv(k, v):
    print(f"  {k:<23} {v}")

print("=" * 78)
print("IDANSTEI.COM — PRODUCTION QA")
print("=" * 78)
print(f"Timestamp (local runtime): {time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
print()

# ---------------------------------------------------------------------
# 1. DOMAIN / REDIRECT CHECKS
# ---------------------------------------------------------------------
print("1. DOMAIN / REDIRECTS")
tests = [
    "http://idanstei.com/",
    "https://idanstei.com/",
    "http://www.idanstei.com/",
    "https://www.idanstei.com/",
]
for u in tests:
    r = fetch(u, follow=True)
    if r.error and not r.status:
        print(f"  FAIL {u} -> {r.error}")
    else:
        print(f"  {r.status}  {u} -> {r.final}")
print()

# ---------------------------------------------------------------------
# 2. ROBOTS + SITEMAP
# ---------------------------------------------------------------------
print("2. ROBOTS.TXT")
robots = fetch(urljoin(BASE, "robots.txt"))
print_kv("status", f"{robots.status} {status_label(robots.status)}")
robots_text = robots.body.decode("utf-8", "replace") if robots.body else ""
if robots_text:
    for line in robots_text.splitlines()[:30]:
        print("   ", line)
print()

print("3. SITEMAP.XML")
sitemap = fetch(urljoin(BASE, "sitemap.xml"))
print_kv("status", f"{sitemap.status} {status_label(sitemap.status)}")
sitemap_urls = []
if sitemap.status == 200 and sitemap.body:
    try:
        root = ET.fromstring(sitemap.body)
        for elem in root.iter():
            if elem.tag.endswith("loc") and elem.text:
                sitemap_urls.append(elem.text.strip())
    except ET.ParseError as e:
        print_kv("XML parse", f"FAIL: {e}")
print_kv("URL count", len(sitemap_urls))
for u in sitemap_urls:
    flag = "" if u in EXPECTED_PUBLIC else "  <-- UNEXPECTED"
    print(f"  {u}{flag}")
missing_expected = sorted(EXPECTED_PUBLIC - set(sitemap_urls))
if missing_expected:
    print("  MISSING EXPECTED:")
    for u in missing_expected:
        print("   ", u)
print()

# ---------------------------------------------------------------------
# 4. OLD ROUTES
# ---------------------------------------------------------------------
print("4. REMOVED AL-FOLIO ROUTES")
old_route_results = {}
for path in OLD_ROUTES:
    u = urljoin(BASE, path.lstrip("/"))
    r = fetch(u)
    old_route_results[u] = r
    good = r.status in (404, 410)
    print(f"  {'PASS' if good else 'CHECK'} {r.status or 'ERR':>3} {u} -> {r.final}")
print()

# ---------------------------------------------------------------------
# 5. CRAWL
# ---------------------------------------------------------------------
print("5. SAME-ORIGIN CRAWL")
seed = list(dict.fromkeys([BASE] + sitemap_urls))
q = deque(seed)
seen = set()
pages = {}
resources = set()
incoming = defaultdict(set)
external = set()

while q and len(seen) < MAX_PAGES:
    u = q.popleft()
    if not same_origin(u) or u in seen:
        continue
    seen.add(u)
    r = fetch(u)
    pages[u] = (r, None)
    print(f"  {r.status or 'ERR':>3} {u}" + (f" -> {r.final}" if r.final != u else ""))
    if r.status != 200 or not is_html(r):
        continue
    text = r.body.decode("utf-8", "replace")
    p = LinkMetaParser()
    try:
        p.feed(text)
    except Exception as e:
        print(f"      HTML parse warning: {e}")
    pages[u] = (r, p)

    for a in p.links:
        href = normalize(a.get("href", ""), r.final or u)
        if not href or href.startswith(("mailto:", "tel:", "javascript:", "data:", "#")):
            continue
        if same_origin(href):
            incoming[href].add(u)
            if href not in seen:
                q.append(href)
        elif urlparse(href).scheme in ("http", "https"):
            external.add(href)

    for img in p.images:
        src = normalize(img.get("src", ""), r.final or u)
        if same_origin(src):
            resources.add(src)
    for s in p.scripts:
        src = normalize(s.get("src", ""), r.final or u)
        if same_origin(src):
            resources.add(src)
    for l in p.link_tags:
        href = normalize(l.get("href", ""), r.final or u)
        if same_origin(href) and href:
            resources.add(href)

print(f"  Crawled HTML/internal URLs: {len(pages)}")
print()

# ---------------------------------------------------------------------
# 6. PAGE QA
# ---------------------------------------------------------------------
print("6. PAGE-BY-PAGE SEO / ACCESSIBILITY")
titles = defaultdict(list)
descriptions = defaultdict(list)
issues = []

for u in sorted(pages):
    r, p = pages[u]
    if r.status != 200 or not p or not is_html(r):
        continue

    title = " ".join(p.title.split())
    desc = meta_value(p, name="description")
    canonical = first_link_rel(p, "canonical")
    viewport = meta_value(p, name="viewport")
    robots_meta = meta_value(p, name="robots")
    og_title = meta_value(p, prop="og:title")
    og_desc = meta_value(p, prop="og:description")
    og_image = meta_value(p, prop="og:image")
    og_url = meta_value(p, prop="og:url")
    twitter_card = meta_value(p, name="twitter:card")
    apple = first_link_rel(p, "apple-touch-icon")
    icon = first_link_rel(p, "icon")
    missing_alt = [x.get("src", "") for x in p.images if "alt" not in x or not x.get("alt", "").strip()]
    mixed = []

    # mixed content in anchors/images/scripts/links
    candidates = []
    candidates += [a.get("href","") for a in p.links]
    candidates += [i.get("src","") for i in p.images]
    candidates += [s.get("src","") for s in p.scripts]
    candidates += [l.get("href","") for l in p.link_tags]
    mixed = [x for x in candidates if x.strip().lower().startswith("http://")]

    jsonld_valid = True
    if p.jsonld_raw:
        for raw in p.jsonld_raw:
            try:
                json.loads(raw)
            except Exception:
                jsonld_valid = False

    if title:
        titles[title].append(u)
    if desc:
        descriptions[desc].append(u)

    local_issues = []
    if not title:
        local_issues.append("missing <title>")
    elif len(title) > 65:
        local_issues.append(f"title long ({len(title)} chars)")
    if not desc:
        local_issues.append("missing meta description")
    elif len(desc) > 165:
        local_issues.append(f"description long ({len(desc)} chars)")
    if not canonical:
        local_issues.append("missing canonical")
    elif normalize(canonical, r.final or u) != r.final:
        local_issues.append(f"canonical differs: {canonical}")
    if not viewport:
        local_issues.append("missing viewport")
    if not p.html_lang:
        local_issues.append("missing html lang")
    if len(p.h1) != 1:
        local_issues.append(f"h1 count={len(p.h1)}")
    if missing_alt:
        local_issues.append(f"{len(missing_alt)} image(s) missing alt")
    if mixed:
        local_issues.append(f"{len(mixed)} mixed-content URL(s)")
    if not og_title:
        local_issues.append("missing og:title")
    if not og_desc:
        local_issues.append("missing og:description")
    if not og_image:
        local_issues.append("missing og:image")
    if p.jsonld_raw and not jsonld_valid:
        local_issues.append("invalid JSON-LD")
    if not p.jsonld_raw:
        local_issues.append("no JSON-LD detected")
    if not apple:
        local_issues.append("no apple-touch-icon")

    print()
    print(f"  PAGE {u}")
    print_kv("title", title or "MISSING")
    print_kv("description", desc or "MISSING")
    print_kv("canonical", canonical or "MISSING")
    print_kv("h1", " | ".join(p.h1) if p.h1 else "MISSING")
    print_kv("lang", p.html_lang or "MISSING")
    print_kv("viewport", viewport or "MISSING")
    print_kv("robots meta", robots_meta or "(none; index/follow default)")
    print_kv("og:title", og_title or "MISSING")
    print_kv("og:description", og_desc or "MISSING")
    print_kv("og:image", og_image or "MISSING")
    print_kv("og:url", og_url or "MISSING")
    print_kv("twitter:card", twitter_card or "(not set)")
    print_kv("favicon", icon or "(not detected)")
    print_kv("apple touch icon", apple or "(not detected)")
    print_kv("JSON-LD blocks", len(p.jsonld_raw))
    print_kv("images missing alt", len(missing_alt))
    print_kv("same-origin incoming", len(incoming.get(u, set())))
    if local_issues:
        print("    ISSUES:")
        for x in local_issues:
            print("      -", x)
            issues.append((u, x))
    else:
        print("    PASS: no basic page-level issues found")

print()

# ---------------------------------------------------------------------
# 7. INTERNAL LINKS
# ---------------------------------------------------------------------
print("7. INTERNAL LINK STATUS")
internal_targets = sorted(set(incoming) | set(sitemap_urls) | {BASE})
broken_internal = []
for u in internal_targets:
    r = fetch(u)
    ok = 200 <= r.status < 400
    if not ok:
        broken_internal.append((u, r.status, r.error))
        print(f"  BROKEN {r.status or 'ERR':>3} {u} {r.error}")
print_kv("internal targets", len(internal_targets))
print_kv("broken", len(broken_internal))
if not broken_internal:
    print("  PASS: no broken internal targets found")
print()

# ---------------------------------------------------------------------
# 8. INTERNAL ASSETS
# ---------------------------------------------------------------------
print("8. INTERNAL ASSETS")
asset_fail = []
asset_sizes = []
for u in sorted(resources):
    r = fetch(u)
    if not (200 <= r.status < 400):
        asset_fail.append((u, r.status))
    else:
        asset_sizes.append((len(r.body), u, r.content_type))
print_kv("assets checked", len(resources))
print_kv("failed assets", len(asset_fail))
for u, code in asset_fail:
    print(f"  BROKEN {code} {u}")
if asset_sizes:
    print("  Largest fetched assets:")
    for size, u, ctype in sorted(asset_sizes, reverse=True)[:10]:
        print(f"    {size/1024:8.1f} KiB  {ctype:<20} {u}")
print()

# ---------------------------------------------------------------------
# 9. PDF LINKS
# ---------------------------------------------------------------------
print("9. PDF LINKS")
pdf_links = set()
for u, (r,p) in pages.items():
    if p:
        for a in p.links:
            href = normalize(a.get("href",""), r.final or u)
            if href.lower().split("?")[0].endswith(".pdf"):
                pdf_links.add(href)
if not pdf_links:
    print("  No PDF links detected")
else:
    for u in sorted(pdf_links):
        r = fetch(u)
        magic = r.body[:5] == b"%PDF-"
        print(f"  {r.status or 'ERR':>3} {'PDF' if magic else 'NOT-PDF':>7} {u} [{r.content_type}]")
print()

# ---------------------------------------------------------------------
# 10. DUPLICATES
# ---------------------------------------------------------------------
print("10. DUPLICATE METADATA")
dup_found = False
for title, urls in titles.items():
    if len(urls) > 1:
        dup_found = True
        print("  DUPLICATE TITLE:", repr(title))
        for u in urls: print("    ", u)
for desc, urls in descriptions.items():
    if len(urls) > 1:
        dup_found = True
        print("  DUPLICATE DESCRIPTION:", repr(desc))
        for u in urls: print("    ", u)
if not dup_found:
    print("  PASS: no duplicate titles/descriptions among crawled HTML pages")
print()

# ---------------------------------------------------------------------
# 11. SECURITY / DELIVERY HEADERS
# ---------------------------------------------------------------------
print("11. DELIVERY / SECURITY HEADERS (homepage)")
home = fetch(BASE)
for key in [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
    "Cache-Control",
    "Content-Encoding",
]:
    print_kv(key, home.headers.get(key, "(not set)"))
print("  Note: missing optional security headers are not automatically a launch blocker on GitHub Pages.")
print()

# ---------------------------------------------------------------------
# 12. EXTERNAL LINKS (status only; may include false positives/rate limits)
# ---------------------------------------------------------------------
print("12. EXTERNAL LINKS")
print_kv("unique external URLs", len(external))
external_fail = []
for i, u in enumerate(sorted(external), start=1):
    # Keep this courteous and bounded.
    r = fetch(u)
    ok = 200 <= r.status < 400
    marker = "OK" if ok else "CHECK"
    print(f"  {marker:<5} {r.status or 'ERR':>3} {u}")
    if not ok:
        external_fail.append((u, r.status, r.error))
    if i % 10 == 0:
        time.sleep(0.3)
print()

# ---------------------------------------------------------------------
# 13. SUMMARY
# ---------------------------------------------------------------------
print("=" * 78)
print("SUMMARY")
print("=" * 78)
print_kv("sitemap URLs", len(sitemap_urls))
print_kv("HTML/internal crawled", len(pages))
print_kv("page-level findings", len(issues))
print_kv("broken internal", len(broken_internal))
print_kv("failed internal assets", len(asset_fail))
print_kv("external URLs checked", len(external))
print_kv("external URLs to review", len(external_fail))

unexpected = sorted(set(sitemap_urls) - EXPECTED_PUBLIC)
if unexpected:
    print("\nUnexpected sitemap URLs:")
    for u in unexpected:
        print("  -", u)

if missing_expected:
    print("\nMissing expected sitemap URLs:")
    for u in missing_expected:
        print("  -", u)

if issues:
    print("\nPage-level findings:")
    for u, x in issues:
        print(f"  - {u}: {x}")

if broken_internal:
    print("\nBroken internal links:")
    for u, code, err in broken_internal:
        print(f"  - {code or 'ERR'} {u} {err}")

if asset_fail:
    print("\nBroken internal assets:")
    for u, code in asset_fail:
        print(f"  - {code or 'ERR'} {u}")

if external_fail:
    print("\nExternal links needing manual review (some sites block automated checks):")
    for u, code, err in external_fail:
        print(f"  - {code or 'ERR'} {u} {err}")

print("\nDone.")