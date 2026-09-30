# Exercise 2 — Difficulty and collaborative workflow

**Purpose:** add difficulty while practising short-lived branches and
peer-reviewed pull requests. **Time:** about 70 minutes. **Guidance:** supported.

## Starting state

Start from the passing game on your personal repository's `main`. Make sure your
starter checks pass before changing anything:

```sh
ruff check .
pytest
```

## Build and collaborate

1. Create and switch to a short-lived branch, for example
   `feature/difficulty`. Keep your own `main` as the PR base.
2. Add three choices: Easy allows **6 valid guesses**, Normal **4**, and Hard
   **3**. Make Normal the default if the player chooses not to select a mode.
   Ask for a mode before selecting a movie. Invalid input should explain the
   available choices and let the player try again without crashing or starting
   a round with an accidental value.
3. Separate genuinely distinct work into more than one logical commit—for
   example, the choice/validation and the attempt-limit behaviour, if your
   design separates them. Do not manufacture a commit solely to meet a count.
   Inspect `git diff` and `git diff --staged` before each commit.
4. Run the game several times and check each difficulty's guess limit. Check
   invalid mode input. Run `ruff check .` and `pytest`.
5. Push your feature branch to your own remote and open a PR **in your own
   repository**, with base `main`. Review the changed files, commit history and
   checks; ask a classmate to review if available. Merge only after review, then
   update your local `main`.

No CI workflow has been added yet. A missing CI check on this first PR is
expected; run the supplied Ruff and pytest checks locally.

## Strategy discussion

Four developers need to work on difficulty, scoring, hints and terminal display
at the same time. Compare the approaches and choose one for this small team:

| Approach | What to consider |
| --- | --- |
| Feature branching | Changes are isolated for review; long-lived branches can drift. |
| Trunk-based development | Small frequent integrations reduce divergence; the team needs frequent coordination and a safe trunk. |
| Gitflow | Separate release/hotfix conventions can help a release process; the extra branches and ceremony may be unnecessary here. |

State your choice and one trade-off. There is no single required answer; relate
it to team size, integration frequency and whether releases need a stabilization
branch.

## Evidence and self-check

Show your branch, more than one purposeful commit where the work supports it,
the PR diff and the merge. The game should visibly provide the selected limits,
reject invalid modes clearly, and preserve all starter behaviour. Your PR's
base and head repositories must both be your own.

## Troubleshooting

- If `origin` is the lecturer's repository, stop; fix your personal-copy setup
  before pushing. Never push the exercise branch to the lecturer's repository.
- If your branch is behind `main`, update safely before merging; inspect status
  and resolve conflicts deliberately rather than discarding edits.
- If GitHub says there are no checks, that is expected before Exercise 5.
- If a difficulty gives the wrong number of attempts, trace the selected limit
  from input through the round loop and re-run each mode.

## Completion checklist

- [ ] Added Easy/Normal/Hard and clear invalid-input handling.
- [ ] Made useful commits and inspected staged/unstaged diffs.
- [ ] Ran the game, Ruff and supplied tests.
- [ ] Opened, reviewed and merged a PR into my own `main`.
- [ ] Compared the three branching strategies and explained a trade-off.
