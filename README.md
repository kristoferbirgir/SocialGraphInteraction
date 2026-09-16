# Social Graph Interaction

Group workspace for DTU course **02805 — Social Graphs and Interactions**. Three-person group;
eight weeks of network science and NLP on a shared Marvel Wikipedia dataset, plus a weekly
data-story post on our [GitHub Pages site](https://kristoferbirgir.github.io/SocialGraphInteraction/)
(once activated — see below).

## Repository layout

```
week1/ … week8/   Weekly folders. Each has a README with the week's date/topic, and
                   week1/ also holds this week's notebooks.
FinalProject/      Final project (not started yet).
src/sgi/           Reusable Python helpers (path constants, Marvel graph loader).
scripts/           One-off scripts, e.g. downloading the Marvel dataset snapshot.
tests/             Pytest tests for src/sgi, with small local fixtures (no network access).
data/raw/          Immutable, as-downloaded source data (git-tracked, small TSVs only).
data/processed/    Generated/derived data — safe to delete and regenerate.
website/           Astro static site (the group's GitHub Pages site).
```

## Prerequisites

- Python 3.12 (managed automatically by `uv` — see below)
- [`uv`](https://docs.astral.sh/uv/) for Python dependency management
- Node.js 20+ and npm, only needed for the `website/` site

## Python setup

```bash
uv sync --group dev
```

This creates `.venv/` (git-ignored) and installs everything pinned in `uv.lock` — JupyterLab,
ipykernel, NetworkX, NumPy, Matplotlib, pandas, httpx, plus dev tools (pytest, Ruff). Commit
`uv.lock` whenever dependencies change; never commit `.venv/`.

Register the Jupyter kernel once, so notebooks can use this environment:

```bash
uv run python -m ipykernel install --user --name=social-graph-interaction --display-name "Social Graph Interaction"
```

## Running things

```bash
uv run jupyter lab                 # open JupyterLab
uv run pytest                      # run the test suite
uv run ruff check .                # lint
uv run scripts/download_marvel_week1.py   # (re-)download the Marvel week-1 snapshot
```

To execute a notebook from a clean kernel from the command line (useful for checking it still
runs top to bottom):

```bash
uv run jupyter nbconvert --to notebook --execute --inplace week1/01_toolbox_karate_club.ipynb
```

## Notebook workflow

- Notebooks live inside their week's folder (e.g. `week1/01_toolbox_karate_club.ipynb`).
- Import shared helpers with `from sgi.marvel import ...` / `from sgi.paths import ...` —
  these work the same from a notebook, a script, or a test because `src/sgi/paths.py` resolves
  paths relative to the repository root, not the current working directory.
- Keep exercise answers and reflections your own. Don't let an AI tool write your reflections
  or "findings" sections — see `AI_METHODS.md` and `CLAUDE.md`.
- See `CONTRIBUTING.md` before editing a notebook someone else might also be editing.

## The Marvel dataset

The frozen week-1 snapshot (303 characters, 1,784 directed links, from Wikipedia's
`Category:Marvel Comics superheroes`) comes from the
[course data page](https://sunelehmann.com/socialgraphs2026-web/data/). Files live in
`data/raw/marvel/week1/` with a `MANIFEST.json` recording source URLs, retrieval time, and
checksums. If that folder is empty, run `uv run scripts/download_marvel_week1.py`, or ask a
groupmate for a copy — see `data/raw/README.md`.

`src/sgi/marvel.py` loads the graph with every node added before any edge, so the 17 isolated
characters survive, and provides `snapshot_report()` to compute the same summary statistics the
course page reports (node/edge counts, isolates, component sizes) — for comparison, not as
hard-coded answers.

## Website: local preview

```bash
cd website
npm install
npm run dev        # local preview at http://localhost:4321/SocialGraphInteraction/
npm run build      # static build to website/dist/
npm run preview    # serve the built site locally
```

To use a figure from a notebook in a post, export it from matplotlib
(`plt.savefig("../../website/src/assets/week1/my-figure.png", dpi=150, bbox_inches="tight")`)
and reference it from the Markdown post.

## GitHub Pages activation (manual, not done yet)

This repo has a prepared workflow (`.github/workflows/pages.yml`) but **nothing has been
pushed, and Pages has not been enabled.** To activate it:

1. Push this repository to GitHub (`git push`).
2. On GitHub: **Settings → Pages → Build and deployment → Source → GitHub Actions.**
3. Push to `main` (or run the workflow manually from the **Actions** tab) to trigger a deploy.
4. The site will be published at `https://kristoferbirgir.github.io/SocialGraphInteraction/`.

If the repository is ever renamed, update `base` in `website/astro.config.mjs` to match.
