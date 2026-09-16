# Repository instructions (for AI coding agents)

This file is for any AI agent (Claude, Copilot, etc.) working in this repository. Read it
before making changes.

## Preserve existing work

- Don't overwrite or restructure files you weren't asked to touch. If something looks messy or
  inconsistent, ask before "cleaning it up."
- Weekly folders (`week1/` … `week8/`, `FinalProject/`) already have a convention: a `README.md`
  with the week's date and topic. Keep that convention; don't replace it.
- Notebooks may contain a group member's in-progress work and reflections. Never overwrite a
  notebook's existing analysis, reflection, or findings cells — only scaffold new, clearly
  empty/TODO sections.

## Reproducibility

- Python dependencies are managed with `uv` (`pyproject.toml` + `uv.lock`). Don't add
  dependencies by editing `.venv/` or running bare `pip install`; use `uv add` / `uv sync` and
  commit the updated lockfile.
- Paths must be repository-relative (see `src/sgi/paths.py`) so notebooks, scripts, and tests
  behave the same regardless of current working directory.
- Ordinary tests (`tests/`) must not require network access — use the fixtures in
  `tests/fixtures/`. Validating the real Marvel snapshot is a separate, explicit step.

## Source provenance

- Any dataset file under `data/raw/` must be paired with a manifest recording its source URL,
  retrieval time, and checksum (see `data/raw/marvel/week1/MANIFEST.json`). Never hand-edit raw
  data.
- Never guess a download URL or file format — verify it against the actual course page (or ask
  the user to confirm) before writing a download script.
- If a dataset can't be downloaded (blocked network, changed URL, etc.), say so explicitly and
  leave validation marked as pending. Do not substitute fabricated or synthetic data for a real
  dataset that was supposed to be downloaded.

## Never fabricate exercise answers or reflections

This is a learning exercise for a three-person student group, not a codebase to complete on
their behalf. Specifically:

- Do not write the group's reflections, "findings," "observations," or about-page bios. Leave
  clearly marked `TODO` / placeholder text instead, and say so when reporting back.
- Do not mark a study-progress item as "understanding: complete" just because code runs
  without errors. Understanding and implementation are different fields — leave understanding
  for the humans to assess honestly.
- It's fine (and expected) to scaffold structure, write loader/plumbing code, and set up
  toolchains — the boundary is generating the content that's supposed to prove the humans
  learned something.
