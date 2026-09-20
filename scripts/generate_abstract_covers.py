#!/usr/bin/env python3
"""Generate deterministic DiceBear Shapes covers for Hugo posts.

The generated SVGs are committed as Hugo assets so the published site does
not make a third-party request when a reader opens the homepage.
"""

from __future__ import annotations

import argparse
import re
import time
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONTENT_ROOT = PROJECT_ROOT / "yaoblog" / "content" / "posts"
OUTPUT_ROOT = PROJECT_ROOT / "yaoblog" / "assets" / "generated" / "abstract"
API_URL = "https://api.dicebear.com/10.x/shapes/svg"

GREYSCALE_OPTIONS = {
    "backgroundColor": "ececee",
    "shape1Color": "b6b6b9",
    "shape2Color": "7c7c80",
    "shape3Color": "343437",
}


def article_files() -> list[Path]:
    """Return canonical Markdown articles, excluding Hugo section indexes and iCloud copies."""

    return sorted(
        path
        for path in CONTENT_ROOT.rglob("*.md")
        if path.name != "_index.md" and not path.name.endswith(" 2.md")
    )


def asset_key(path: Path) -> str:
    relative = path.relative_to(CONTENT_ROOT).with_suffix("")
    raw_key = "-".join(relative.parts)
    return re.sub(r"[^a-zA-Z0-9_-]+", "-", raw_key).strip("-").lower()


def request_svg(path: Path) -> str:
    relative = path.relative_to(CONTENT_ROOT).with_suffix("").as_posix()
    query = {"seed": f"actuallyyao:{relative}", **GREYSCALE_OPTIONS}
    request = Request(
        f"{API_URL}?{urlencode(query)}",
        headers={"User-Agent": "actuallyyao-blog-abstract-generator/1.0"},
    )

    last_error: Exception | None = None
    for attempt in range(3):
        try:
            with urlopen(request, timeout=30) as response:
                svg = response.read().decode("utf-8")
            if not svg.lstrip().startswith("<svg"):
                raise ValueError("DiceBear returned a non-SVG response")
            return svg
        except Exception as error:  # pragma: no cover - network failures vary by environment
            last_error = error
            if attempt < 2:
                time.sleep(attempt + 1)

    raise RuntimeError(f"Could not generate {path}: {last_error}") from last_error


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate existing SVGs, useful after changing the preset.",
    )
    args = parser.parse_args()

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    generated = 0
    skipped = 0

    for article in article_files():
        target = OUTPUT_ROOT / f"{asset_key(article)}.svg"
        if target.exists() and not args.force:
            skipped += 1
            continue
        target.write_text(request_svg(article), encoding="utf-8")
        generated += 1
        print(f"generated {target.relative_to(PROJECT_ROOT)}")

    print(f"Done: {generated} generated, {skipped} already present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
