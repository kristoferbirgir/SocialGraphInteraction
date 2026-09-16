"""Repository-relative paths that work the same from notebooks, scripts, and tests."""

from __future__ import annotations

from pathlib import Path

# src/sgi/paths.py -> repo root is two parents up.
REPO_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = REPO_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MARVEL_RAW_DIR = RAW_DATA_DIR / "marvel" / "week1"
