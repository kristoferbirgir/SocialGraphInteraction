# Contributing (group of 3)

Simple branch + PR workflow — nothing fancy, just enough to avoid stepping on each other.

## Workflow

1. Pull the latest `main` before starting: `git pull`.
2. Create a branch per piece of work: `git checkout -b week1-degree-distributions`.
3. Commit and push your branch: `git push -u origin week1-degree-distributions`.
4. Open a pull request into `main`. Have at least one other group member glance at it before
   merging — even a quick skim catches a lot.
5. Merge, then delete the branch. Pull `main` again before starting the next thing.

## Notebooks: don't edit the same one at the same time

Jupyter notebooks are JSON files. Two people editing the same notebook at the same time (even
on different branches) reliably produces unresolvable merge conflicts in cell output/metadata,
not just code. To avoid this:

- Before opening a notebook to edit, say so in your group chat.
- Prefer one person "owns" a given notebook for a given week; others create a new notebook
  (e.g. `01b_...ipynb`) for parallel exploration instead of editing the same file.
- If you must merge conflicting notebook changes, it's usually easier to reapply your changes
  by hand on top of the other version than to resolve the JSON diff.
- Clear cell outputs before committing if they're large/irrelevant (`Kernel → Restart Kernel and
  Clear Outputs`) to keep diffs small — but keep outputs for notebooks meant to show results.

## Commit messages

Short and specific: `week1: add degree distribution plots`, not `updates`.

## Reviewing each other's work

The course explicitly wants you to critique other groups' posts — get in the habit of reading
each other's notebooks and code with the same eye. A PR review doesn't need to be long: does the
code do what it says, do the numbers look plausible, is any reflection/finding actually yours?
