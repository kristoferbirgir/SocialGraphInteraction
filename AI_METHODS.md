# AI methods log

A running log of AI-assisted work on this repo. The course explicitly wants you practicing
what to trust an AI tool with and what to verify yourself (see week 1, exercise 1.2) — this file
is where that practice becomes a habit. Add an entry whenever AI meaningfully helped with a
task. Only log assistance that actually happened; don't pre-fill entries for work not yet done.

## Entry template

```
### YYYY-MM-DD — short task title

- Tool: (e.g. GitHub Copilot / Claude / ChatGPT, model if known)
- Task: what you asked it to do
- What it produced: brief summary
- Verification: how you checked it (ran it? read it line by line? checked against a source?)
- Failures / corrections: anything it got wrong, and what you changed
- What you would NOT let it do unsupervised: (per exercise 1.2.3)
```

---

### 2026-09-16 — initial repository scaffold

- Tool: GitHub Copilot (Claude Sonnet 4.5 or similar in-editor agent)
- Task: set up the repository foundation — `uv`-managed Python environment, `src/sgi` graph
  loader, download script for the frozen Marvel week-1 snapshot, pytest fixtures/tests, a
  Karate Club toolbox notebook, a Marvel notebook scaffold, and an Astro static site skeleton
  for GitHub Pages.
- What it produced: `pyproject.toml`/`uv.lock`, `src/sgi/paths.py` and `src/sgi/marvel.py`,
  `scripts/download_marvel_week1.py`, `tests/` with local fixtures, two notebooks under
  `week1/`, and the `website/` Astro project with a homepage, about page, posts listing, and a
  week-1 draft post template.
- Verification: ran `uv run pytest` (6/6 passed), `uv run ruff check .` (clean), executed both
  notebooks from a clean kernel via `jupyter nbconvert --execute`, loaded the real downloaded
  Marvel snapshot and checked computed stats (303 nodes, 1,784 directed edges, 1,434 undirected
  edges, 17 isolates, component sizes 277/9/17×1) against the numbers published on the course
  data page — all matched. Built the Astro site (`npm run build`) and inspected the generated
  HTML to confirm internal links carry the `/SocialGraphInteraction` base path correctly.
- Failures / corrections: the first version of the Astro post layout read frontmatter fields
  as top-level props; Astro actually passes them as a single `frontmatter` object for
  Markdown-layout pages, so the title/date rendered blank until that was fixed and re-verified.
  `npx create-astro` crashed when its stdin was piped, so the site was scaffolded by hand
  instead of via the interactive CLI.
- What you would NOT let it do unsupervised: write the actual week-1 findings, reflections, or
  group member bios — those are left as explicit TODO placeholders for the group to fill in
  themselves. Exercise answers (1.1–1.8) still need to be done and understood by the group, not
  generated.
