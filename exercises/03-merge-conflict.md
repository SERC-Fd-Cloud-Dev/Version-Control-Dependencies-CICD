# Exercise 3 — Deliberate merge conflict

**Purpose:** resolve a real same-line conflict without risking classwork.
**Time:** about 20 minutes. **Guidance:** guided.

## Starting state and safety

This exercise uses a disposable repository at `practice/movie-hint-conflict/`,
which is ignored by `.gitignore`. It does not switch, reset or modify your game
repository's branches. Run the setup from the root of your class clone:

```sh
python exercises/scripts/create_conflict_practice.py
```

The script refuses to continue if that destination already exists. It creates
one fixed baseline, branches `hint-genre` and `hint-year-director` from that
same commit, and attempts a merge that must conflict on the `build_hint`
return statement. Re-create it only after you have finished with the disposable
directory: inspect it, then remove **only**
`practice/movie-hint-conflict/` yourself before running setup again. Never use
`git reset --hard` or force-push in your real class repository.

## Resolve the conflict

1. Enter the fixture and inspect `git status`, the conflicted file and
   `git log --oneline --graph --all`. Identify the shared baseline and each
   branch's requirement.
2. Combine both requirements into one useful hint: include the release year,
   director and genre. Remove every conflict marker while retaining a valid
   Python return statement.
3. From the class repository root, enter the fixture with
   `cd practice/movie-hint-conflict`. Run `python hint_demo.py` and make sure the
   output contains all three pieces of information.
4. Still in the fixture, stage and finish the merge:

   ```sh
   git add hint_demo.py
   git commit -m "Combine hint details"
   git status
   git log --oneline --graph --all
   ```

   Confirm the tree is clean and the merge history contains both branches.

## Evidence and self-check

Show the original conflict, your clean final hint, its check output, and the
resulting two-parent merge history. The real class repository should have the
same branch and working-tree state it had before this isolated activity.

## Troubleshooting

- The fixture can only be recreated if its exact destination is absent. Inspect
  existing work before manually removing that disposable directory.
- If the merge did not conflict, check that the two edits changed the same
  return line from the shared baseline; do not create a conflict in your real
  repository as a substitute.
- If Python reports a syntax error, look for leftover `<<<<<<<`, `=======` or
  `>>>>>>>` markers.
- If Git asks for an identity, the setup script sets a local identity only in
  the disposable fixture.

## Completion checklist

- [ ] Confirmed the exercise is inside the ignored disposable repository.
- [ ] Explained both branch requirements and resolved their conflict.
- [ ] Ran the hint check and finished the merge.
- [ ] Inspected the merge graph and left real work untouched.
