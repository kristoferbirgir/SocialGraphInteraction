#!/usr/bin/env python
"""Download the frozen week-1 Marvel snapshot from the course data page.

Usage:
    uv run scripts/download_marvel_week1.py

Re-running is safe: it re-downloads, re-checks file sizes are non-empty, and
overwrites the manifest with a fresh retrieval timestamp and checksums.
"""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import UTC, datetime

import httpx

from sgi.paths import MARVEL_RAW_DIR

BASE_URL = "https://sunelehmann.com/socialgraphs2026-web/data/"
FILENAMES = ["week1_nodes.tsv", "week1_edges.tsv"]
USER_AGENT = (
    "SocialGraphInteraction-coursework/0.1 (DTU 02805 student group; contact via GitHub repo)"
)


def sha256_of(path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    MARVEL_RAW_DIR.mkdir(parents=True, exist_ok=True)
    manifest = {
        "source_page": "https://sunelehmann.com/socialgraphs2026-web/data/",
        "week1_instructions": "https://sunelehmann.com/socialgraphs2026-web/weeks/week1.html",
        "snapshot_identity": "week 1 release, frozen 2026-08-26 (per file header comments)",
        "retrieved_at": datetime.now(UTC).isoformat(),
        "files": {},
    }

    client_kwargs = {"headers": {"User-Agent": USER_AGENT}, "follow_redirects": True, "timeout": 30}
    with httpx.Client(**client_kwargs) as client:
        for filename in FILENAMES:
            url = BASE_URL + filename
            dest = MARVEL_RAW_DIR / filename
            print(f"Downloading {url} -> {dest}")
            response = client.get(url)
            response.raise_for_status()
            if not response.content:
                raise RuntimeError(f"Downloaded empty file: {url}")
            dest.write_bytes(response.content)
            manifest["files"][filename] = {
                "source_url": url,
                "sha256": sha256_of(dest),
                "size_bytes": dest.stat().st_size,
            }

    manifest_path = MARVEL_RAW_DIR / "MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Wrote {manifest_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
