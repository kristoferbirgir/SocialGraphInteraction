# data/raw/

Immutable, as-downloaded source data. Never hand-edit files here — if the
upstream data changes, re-run the relevant download script to refresh them.

- `marvel/week1/` — the frozen week-1 Marvel Wikipedia-links snapshot.
  Populate it with `uv run scripts/download_marvel_week1.py`. Each file is
  paired with `MANIFEST.json`, which records the source URLs, retrieval
  timestamp, and SHA-256 checksums for reproducibility.

If you can't reach the network, ask a groupmate for their copy of this
folder, or download the files by hand from
https://sunelehmann.com/socialgraphs2026-web/data/ and place them at
`data/raw/marvel/week1/week1_nodes.tsv` and `week1_edges.tsv`.
