# Exercise 6 — Failure diagnosis

**Purpose:** read a CI failure, make the smallest targeted correction, and
interpret the limits of a green result. **Time:** about 20 minutes.
**Guidance:** independent mini-task.

## Starting state

Begin only after Exercise 5's workflow is passing on your own `main`. Update
`main` and create a separate branch, for example `practice/ruff-failure`.
Do not create this controlled failure on `main` or modify supplied tests.

## Diagnose, then repair

1. In `movie_game/game.py`, add an unused standard-library import such as
   `import statistics` alongside the other imports. Commit and push this
   deliberate failure on the practice branch.
2. Open the branch's Actions run. Identify the failed job and step, copy the
   decisive log line, and state the cause and smallest appropriate fix.
3. Remove only the unused import, commit the fix, and push again. Inspect the
   rerun and confirm it is for the updated commit and passes.
4. If Actions is delayed, use this prepared example to practise diagnosis:

   ```text
   Run ruff check .
   movie_game/game.py:5:8: F401 `statistics` imported but unused
   Found 1 error.
   Error: Process completed with exit code 1.
   ```

## Think about the result

What does a green workflow establish here? What might still need manual review,
such as whether the terminal experience is clear or whether a requested feature
is actually usable? Ruff and the supplied tests cover only their configured
checks; they do not prove every game behaviour or product decision.

## Evidence and self-check

Show the failing step and decisive diagnostic, explain the unused-import cause,
then show the passing rerun on the fixed commit. Keep both commits on this
separate practice branch; do not change or remove tests.

## Troubleshooting

- Confirm the deliberate import is unused and is not an import-order problem.
- The exact line number can differ; the decisive diagnostic is Ruff's `F401`
  unused-import report.
- If no run appears, confirm the workflow has been merged into `main`, then
  pushed the practice branch to your own repository.
- If Ruff reports a different problem, inspect the diff and diagnose that
  message; do not weaken configuration or edit tests to obtain a green result.

## Completion checklist

- [ ] Created a separate practice branch and one controlled failure commit.
- [ ] Identified the failing CI step, diagnostic and cause.
- [ ] Made a targeted fix and pushed it.
- [ ] Inspected a passing rerun for the fixed commit.
- [ ] Explained what green checks cover and what they can miss.
