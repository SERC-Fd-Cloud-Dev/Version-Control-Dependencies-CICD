# Homework — Genre selection

**Purpose:** independently extend the completed game while preserving existing
difficulty behaviour and practising the full PR/CI workflow. **Time:** about
one hour.

## Starting state

Use your completed class repository after the CI workflow is merged. Update
your own `main` and create a new feature branch, for example
`feature/genre-selection`.

## Task

Before the movie is selected, let the player choose one of the genres present
in the movie data or **Any**. The selected record must belong to the chosen
genre, or may come from the full catalogue for Any. Invalid input must recover
clearly without crashing. Keep the existing Easy/Normal/Hard attempt behaviour.

Make logical commits, inspect each diff and manually try at least two genres,
Any and invalid input. Run `ruff check .` and the supplied `pytest` checks. Push
your branch and open a PR to your own `main`; confirm a successful Actions run
for its current commit and **leave the PR open for review**. Do not write new
tests for this task.

## Reflection

1. Why did you use a feature branch?
2. Which commit message in your work is most useful to a reviewer, and why?
3. What did CI check, and what might it miss?

**Optional extension:** derive the genre menu dynamically from the movie data
instead of hard-coding its current genres.

**Catch-up route:** implement one named genre mode, make one useful commit, and
get a green CI run. Complete the full genre feature afterwards.

## Evidence and self-check

Your PR should show the branch's focused changes, manual checks for two genres,
Any and invalid input, a passing Ruff/test run, and a successful Actions run
for the PR head. The PR must remain open.

## Troubleshooting

- Check that filtering happens before random movie selection and that Any uses
  the full movie collection.
- If invalid input terminates the game, continue prompting until it is valid.
- If difficulty limits change, trace the difficulty choice through the genre
  choice into the same round.
- Make sure the workflow run belongs to the current PR commit, not an earlier
  push.

## Completion checklist

- [ ] Created a feature branch from the latest personal `main`.
- [ ] Implemented named-genre and Any selection before random selection.
- [ ] Preserved difficulty and handled invalid input.
- [ ] Manually tried two genres, Any and invalid input.
- [ ] Ran Ruff and supplied tests; pushed a logical commit history.
- [ ] Opened a PR with passing CI and left it open for review.
- [ ] Answered the three reflection questions.
