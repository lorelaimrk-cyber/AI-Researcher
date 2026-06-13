#!/usr/bin/env python3
"""Gather the week's candidate stories for the newsletter.

Reads sources/sources.yaml, fetches each feed, keeps items from the last N days that match
the AI and domain keyword sets, classifies each into a content pillar, ranks by source
weight, keyword relevance, and recency, dedupes, and writes a dated brief into
sources/briefs/.

Dependency-light by design: feedparser, requests, PyYAML. No API keys.

Usage:
    python scripts/gather.py
    python scripts/gather.py --days 10 --max 40
    python scripts/gather.py --sources path/to/sources.yaml --out path/to/briefs
"""

from __future__ import annotations

import argparse
import math
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    import feedparser
    import requests
    import yaml
except ImportError as exc:  # pragma: no cover
    sys.stderr.write(
        "Missing a dependency: {}\n"
        "Install with: pip install -r scripts/requirements.txt\n".format(exc.name)
    )
    sys.exit(1)


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCES = REPO_ROOT / "sources" / "sources.yaml"
DEFAULT_OUT = REPO_ROOT / "sources" / "briefs"

PILLAR_TITLES = {
    "economics": "Pillar 1: Economics of billable expertise",
    "delivery": "Pillar 2: Delivery and tooling",
    "risk": "Pillar 3: Risk, liability, and governance",
    "talent": "Pillar 4: Talent and organization design",
    "market": "Pillar 5: Clients and the market",
    "unsorted": "Unsorted",
}
PILLAR_ORDER = ["economics", "delivery", "risk", "talent", "market", "unsorted"]

USER_AGENT = (
    "AI-Researcher-gather/1.0 (weekly newsletter brief; contact via repo owner)"
)


def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        config = yaml.safe_load(fh)
    if not config or "feeds" not in config:
        raise ValueError("sources.yaml must contain a 'feeds' list")
    config.setdefault("keywords", {})
    config.setdefault("settings", {})
    return config


def fetch_feed(url: str, timeout: int = 20):
    """Fetch a feed via requests (so we control timeout and UA), parse with feedparser.

    Returns a feedparser result, or None on a hard failure.
    """
    try:
        resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
        resp.raise_for_status()
        return feedparser.parse(resp.content)
    except Exception:
        # Fall back to letting feedparser fetch directly (handles some odd servers).
        try:
            return feedparser.parse(url)
        except Exception:
            return None


def entry_datetime(entry) -> datetime | None:
    for key in ("published_parsed", "updated_parsed"):
        value = entry.get(key)
        if value:
            try:
                return datetime.fromtimestamp(time.mktime(value), tz=timezone.utc)
            except (OverflowError, ValueError):
                continue
    return None


def clean_text(html: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html or "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (title or "").lower()).strip()


def count_hits(haystack: str, terms: list[str]) -> int:
    return sum(1 for term in terms if term and term.lower() in haystack)


def classify_pillar(haystack: str, pillar_terms: dict, feed_hint: str | None) -> str:
    best_pillar = None
    best_hits = 0
    for pillar in ["economics", "delivery", "risk", "talent", "market"]:
        terms = pillar_terms.get(pillar, [])
        hits = count_hits(haystack, terms)
        if hits > best_hits:
            best_hits = hits
            best_pillar = pillar
    if best_pillar:
        return best_pillar
    if feed_hint in PILLAR_TITLES and feed_hint != "unsorted":
        return feed_hint
    return "unsorted"


def recency_score(published: datetime | None, half_life_days: float) -> float:
    if published is None:
        return 0.5  # unknown date, treat as middling
    age_days = (datetime.now(timezone.utc) - published).total_seconds() / 86400.0
    age_days = max(age_days, 0.0)
    return math.pow(0.5, age_days / max(half_life_days, 0.1))


def build_items(config: dict, days_back: int) -> tuple[list[dict], list[str]]:
    kw = config["keywords"]
    ai_terms = kw.get("ai", [])
    domain_terms = kw.get("domain", [])
    pillar_terms = kw.get("pillars", {})
    half_life = float(config["settings"].get("recency_half_life_days", 3))

    now = datetime.now(timezone.utc)
    items: list[dict] = []
    dead_feeds: list[str] = []

    for feed in config["feeds"]:
        name = feed.get("name", feed.get("url", "unknown"))
        url = feed.get("url")
        weight = float(feed.get("weight", 1.0))
        hint = feed.get("pillar")
        if not url:
            continue

        parsed = fetch_feed(url)
        entries = getattr(parsed, "entries", None) if parsed else None
        if not entries:
            dead_feeds.append(name)
            continue

        kept_from_feed = 0
        for entry in entries:
            title = entry.get("title", "").strip()
            link = entry.get("link", "").strip()
            summary = clean_text(entry.get("summary", entry.get("description", "")))
            published = entry_datetime(entry)

            if published is not None:
                age_days = (now - published).total_seconds() / 86400.0
                if age_days > days_back:
                    continue

            haystack = " {} {} ".format(title, summary).lower()

            ai_hits = count_hits(haystack, ai_terms)
            domain_hits = count_hits(haystack, domain_terms)
            # Keep only items that touch both AI and the domain. If a feed has no dated
            # entries and is topical already (a Google News query), domain_hits may be 0,
            # so allow items that strongly hit AI from a domain-hinted feed.
            if ai_hits == 0:
                continue
            if domain_hits == 0 and hint is None:
                continue

            pillar = classify_pillar(haystack, pillar_terms, hint)
            rec = recency_score(published, half_life)
            relevance = ai_hits + domain_hits
            score = weight * (1.0 + 0.25 * relevance) * (0.5 + 0.5 * rec)

            items.append(
                {
                    "title": title,
                    "link": link,
                    "summary": summary[:280],
                    "source": name,
                    "published": published,
                    "pillar": pillar,
                    "score": round(score, 3),
                    "norm_title": normalize_title(title),
                }
            )
            kept_from_feed += 1

        if kept_from_feed == 0 and name not in dead_feeds:
            # Feed loaded but nothing matched. Not dead, just quiet this week.
            pass

    return items, dead_feeds


def dedupe(items: list[dict]) -> list[dict]:
    seen_titles: set[str] = set()
    seen_links: set[str] = set()
    out: list[dict] = []
    for item in sorted(items, key=lambda x: x["score"], reverse=True):
        nt = item["norm_title"]
        link = item["link"]
        if nt and nt in seen_titles:
            continue
        if link and link in seen_links:
            continue
        seen_titles.add(nt)
        if link:
            seen_links.add(link)
        out.append(item)
    return out


def render_brief(items: list[dict], dead_feeds: list[str], scanned: int, kept: int) -> str:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [
        "# Weekly brief: {}".format(today),
        "",
        "Window: last 7 days. Sources scanned: {}. Candidates kept: {}.".format(
            scanned, kept
        ),
        "",
        "Skim this, delete what bores you, then run prompts/01-research-brief.md with Claude.",
        "",
    ]

    by_pillar: dict[str, list[dict]] = {p: [] for p in PILLAR_ORDER}
    for item in items:
        by_pillar.setdefault(item["pillar"], []).append(item)

    for pillar in PILLAR_ORDER:
        bucket = by_pillar.get(pillar, [])
        if not bucket:
            continue
        lines.append("## {}".format(PILLAR_TITLES[pillar]))
        lines.append("")
        for i, item in enumerate(bucket, 1):
            date_str = (
                item["published"].strftime("%Y-%m-%d") if item["published"] else "undated"
            )
            lines.append("{}. **{}**".format(i, item["title"] or "(untitled)"))
            lines.append("   - Source: {} | {}".format(item["source"], date_str))
            lines.append("   - Link: {}".format(item["link"] or "(no link)"))
            lines.append("   - Score: {}".format(item["score"]))
            if item["summary"]:
                lines.append("   - Why it might matter: {}".format(item["summary"]))
            lines.append("")
        lines.append("")

    lines.append("## Source health")
    lines.append("")
    if dead_feeds:
        lines.append("Feeds that returned nothing this run (prune if this repeats):")
        for name in dead_feeds:
            lines.append("- {}".format(name))
    else:
        lines.append("All feeds returned at least one item.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Gather weekly newsletter candidates.")
    parser.add_argument("--sources", type=Path, default=DEFAULT_SOURCES)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--days", type=int, default=None, help="override days_back")
    parser.add_argument("--max", type=int, default=None, help="override max_items")
    args = parser.parse_args()

    if not args.sources.exists():
        sys.stderr.write("Sources file not found: {}\n".format(args.sources))
        return 1

    config = load_config(args.sources)
    days_back = args.days or int(config["settings"].get("days_back", 7))
    max_items = args.max or int(config["settings"].get("max_items", 30))

    print("Fetching {} feeds...".format(len(config["feeds"])))
    items, dead_feeds = build_items(config, days_back)
    scanned = len(items)
    items = dedupe(items)[:max_items]
    kept = len(items)

    brief = render_brief(items, dead_feeds, scanned, kept)

    args.out.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out_path = args.out / "{}-brief.md".format(today)
    out_path.write_text(brief, encoding="utf-8")

    print("Kept {} candidates after dedupe.".format(kept))
    if dead_feeds:
        print("Quiet or dead feeds this run: {}".format(", ".join(dead_feeds)))
    print("Wrote {}".format(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
