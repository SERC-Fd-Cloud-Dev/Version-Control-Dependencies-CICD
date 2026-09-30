# Version control, dependency management and introductory CI

This lesson focuses on Git collaboration, Python dependency management, and
simple automated CI with GitHub Actions. A small offline movie guessing game
provides the practical scenario; the focus is the development workflow, not
building a game. The example is new, not a copy of the program used in an earlier
Python lesson.

## Prerequisites

- Git and a GitHub account
- Python **3.12** (the same version used by the later CI exercise)
- A terminal: PowerShell on Windows, or Terminal on macOS/Linux

## Make and clone your own repository

Do not push classwork to the lecturer's repository.

1. On GitHub, use **Fork** to make a copy under your account. If forking is not
   available, use GitHub's **Import repository** page to import the class
   repository into your account.
2. Clone the URL shown for your own copy:

   ```sh
   git clone https://github.com/YOUR-ACCOUNT/Version-Control-Dependencies-CICD.git
   cd Version-Control-Dependencies-CICD
   git remote -v
   ```

   Check that `origin` is your personal repository before pushing.

## Create and activate an environment

Run these commands from the repository root.

**Windows PowerShell**

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, either use a permitted shell policy or run the
environment's Python directly as `.venv\Scripts\python.exe`.

**macOS/Linux**

```sh
python3.12 -m venv .venv
source .venv/bin/activate
```

Install the committed developer requirements (which also install runtime
requirements):

```sh
python -m pip install -r requirements-dev.txt
```

## Run and check the starter

```sh
python -m movie_game
ruff check .
pytest
```

The game chooses one record at random, gives a first-letter/word-count clue and
a release-year hint, and allows four valid guesses. Empty input does not use a
guess; correct guesses ignore case and repeated whitespace. There is one round,
no network access, and no replay or scoring.

Example interaction (the randomly selected title is intentionally not shown
here):

```text
The title starts with [first letter] and has [number] words.
Hint: released in [year].
You have 4 guesses.
Your guess: [a non-matching title]
Not quite. You have 3 guesses remaining.
```

## Exercises

Work through the numbered exercise briefs in order:

1. [Git recap and commit quality](exercises/01-git-recap.md)
2. [Difficulty and collaborative workflow](exercises/02-difficulty-and-prs.md)
3. [Deliberate merge conflict](exercises/03-merge-conflict.md)
4. [Python dependencies and Rich](exercises/04-python-dependencies.md)
5. [Introductory CI with GitHub Actions](exercises/05-intro-ci.md)
6. [Failure diagnosis](exercises/06-failure-diagnosis.md)

Independent homework: [Genre selection](exercises/homework-genre-selection.md).

## Project layout

```text
movie_game/                 game rules and CLI
movie_game/movies.json      editable movie catalogue
tests/                      five supplied starter checks
exercises/                  student briefs, workflow template and fixture setup
requirements.txt            runtime packages (empty until Exercise 4)
requirements-dev.txt         runtime requirements plus pinned Ruff and pytest
pyproject.toml               Ruff and pytest settings
```
