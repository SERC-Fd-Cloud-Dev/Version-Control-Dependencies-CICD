# Exercise 4 — Python dependencies and Rich

**Purpose:** distinguish runtime and development dependencies, declare a small
runtime package, and reproduce an environment from committed files. **Time:**
about 50 minutes. **Guidance:** guided to supported.

## Starting state

Begin after your difficulty PR has been merged into your own `main`. Update
`main`, run the starter checks, and create another short-lived branch, such as
`feature/rich-display`.

## Add one small improvement

1. Choose one small terminal display improvement using [Rich](https://rich.readthedocs.io/),
   such as colouring the game title or the success/failure outcome. Keep the
   game a local command-line program; do not redesign its interaction.
2. Install Rich into your active `.venv`:

   ```sh
   python -m pip install "rich>=13.9,<15"
   ```

   Add the same constraint to `requirements.txt` so a fresh install can
   reproduce it. `requirements-dev.txt` already includes `requirements.txt`,
   Ruff and pytest.
3. Check `.gitignore`: `.venv`, Python caches and tool caches must not appear in
   your diff. Review `git status` and `git diff`.
4. Commit the display change and its runtime declaration together when they
   form one logical change. Push and open a PR to your own `main`; you may merge
   this PR before Exercise 5 adds CI.

## Recreate and verify the environment

From the repository root, create a separate clean environment and install only
the committed developer manifest:

```sh
python -m venv .venv-fresh
```

Activate it using the matching activation command in the root README, replacing
`.venv` with `.venv-fresh`, then run:

```sh
python -m pip install -r requirements-dev.txt
python -m movie_game
ruff check .
pytest
```

The game and checks should work without relying on packages installed only in
your original environment. Remove `.venv-fresh` when finished.

## Recognise package managers

| Language | Common package manager |
| --- | --- |
| Python | pip |
| JavaScript | npm |
| Java | Maven or Gradle |
| C# | NuGet |
| Ruby | Bundler |

This is a recognition comparison only; all practical commands in this lesson
are Python commands. A broad constraint (such as `>=13.9,<15`) permits compatible
updates and can install different patch versions at different times. An exact
lock records resolved versions for tighter repeatability. This exercise uses
the project's requirements files and does not require a packaging or lockfile
lecture.

## Evidence and self-check

Show the focused display diff, the Rich runtime declaration, and a clean
environment installed from committed manifests where the game, Ruff and pytest
all run successfully.

## Troubleshooting

- Check that `requirements.txt` contains the runtime package and
  `requirements-dev.txt` includes it via `-r requirements.txt`.
- If the fresh environment cannot import Rich, confirm you activated
  `.venv-fresh` and installed `requirements-dev.txt`, not only `requirements.txt`.
- If `.venv` or cache files appear in the diff, inspect `.gitignore`; do not
  commit the environment.
- Use the `.venv-fresh` activation path for your operating system, as described
  in the root README.

## Completion checklist

- [ ] Added one small Rich display improvement.
- [ ] Declared Rich as a runtime dependency.
- [ ] Kept Ruff and pytest as development dependencies and checked ignore rules.
- [ ] Recreated the environment from committed requirements files.
- [ ] Ran the game, Ruff and pytest; reviewed and merged my PR if ready.
