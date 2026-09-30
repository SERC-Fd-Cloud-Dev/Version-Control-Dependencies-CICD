# Exercise 1 — Git recap and commit quality

**Purpose:** refresh reading status, diffs and history, and practise describing
the actual scope of a commit. **Time:** about 25 minutes.

## Starting state

Use your own clone of the starter repository. Confirm `git remote -v` points to
your personal copy. Do not change application code during this activity.

## Tasks

1. Before editing, run `git status`, `git diff`, and `git log --oneline -5`.
   Record what each says about the current working tree and recent history.
2. Read the game source and tests. For each change below, identify which file
   would have changed and what a reviewer should be able to learn from the diff:

   | Weak history | Change represented |
   | --- | --- |
   | `update` | Added movie records and populated a new genre |
   | `stuff` | Added whitespace/case-insensitive guess comparison |
   | `fix` | Empty input now retries without using a guess |
   | `final` | Added the four-guess limit and remaining-attempt message |

3. Rewrite those four messages so each is short, specific, imperative and scoped
   to its change. Compare the proposed commit boundaries: would any two changes
   be easier to review separately?
4. Explain what you would inspect before committing and what evidence in a diff
   would tell you a commit contains unrelated work.

## Evidence and self-check

Keep your notes or discuss them with a partner. You should be able to explain
the difference between working-tree changes, staged changes and committed
history; each proposed message should identify its change without saying only
“update”, “stuff”, “fix” or “final”.

<details>
<summary>Feedback — open after attempting the task</summary>

Useful examples include `Add science-fiction movie records`, `Normalize title
guesses`, `Retry empty guesses without spending an attempt`, and `Report
remaining guesses after a miss`. Other wording is fine if it accurately
describes only the relevant change. A focused diff makes that claim verifiable.

</details>

## Troubleshooting

- An empty `git diff` is normal before you edit; use the source and test files
  to reason about the listed history.
- If your tree is not clean, inspect `git status` and decide whether the files
  are your own work before proceeding. Do not discard work to make it clean.

## Completion checklist

- [ ] Interpreted status, diff and log output.
- [ ] Mapped the four weak messages to concrete changes.
- [ ] Suggested better scoped commit messages and explained why.
