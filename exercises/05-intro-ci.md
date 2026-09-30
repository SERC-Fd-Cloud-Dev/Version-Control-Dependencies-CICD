# Exercise 5 — Introductory CI with GitHub Actions

**Purpose:** add and explain automated checks for each pushed commit and pull
request. **Time:** about 55 minutes. **Guidance:** supported.

## Starting state

Start from your own `main` after the dependency PR is merged. Confirm the local
game, Ruff and pytest work. Create a new branch, for example `ci/python-checks`.
The starter intentionally has no active workflow.

## Complete and activate the scaffold

1. Read `exercises/templates/python-ci.yml`. It is a template, not an active
   workflow. Review each TODO and confirm the documented Python version is
   3.12. The file is valid YAML and already contains the required checks.
2. Create `.github/workflows/` and copy the template there as
   `.github/workflows/python-ci.yml`. On macOS/Linux:

   ```sh
   mkdir -p .github/workflows
   cp exercises/templates/python-ci.yml .github/workflows/python-ci.yml
   ```

   In Windows PowerShell:

   ```powershell
   New-Item -ItemType Directory -Force .github/workflows
   Copy-Item exercises/templates/python-ci.yml .github/workflows/python-ci.yml
   ```

3. Inspect the new workflow. It must run on both `push` and `pull_request`, check
   out the triggering commit, set up Python 3.12, install
   `requirements-dev.txt`, and run `ruff check .` and `pytest`. Keep permissions
   read-only; no secrets or deployment steps are needed.
4. Commit and push the branch to your own repository. Open a PR to your own
   `main`. On GitHub, inspect the run attached to the current commit, open its
   steps and identify what each one does. Do not claim a run passed unless the
   PR shows a successful run for its head commit.

The template follows the official [workflow syntax documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
and the official [`actions/checkout`](https://github.com/actions/checkout) and
[`actions/setup-python`](https://github.com/actions/setup-python) repositories.
It uses their current major action references and grants only `contents: read`.

## Classify the delivery practice

For each statement, label it **continuous integration**, **continuous
delivery**, or **continuous deployment**, and explain the boundary:

1. Every PR automatically runs lint and tests.
2. A passing commit is automatically packaged and made ready for a person to
   approve a release.
3. Every passing change is automatically released to users without a manual
   approval.

This repository implements only the checks in statement 1. It does not package
or deploy the game.

## Evidence and self-check

Show your PR, the workflow file and a successful Actions run for its current
head commit. Explain the triggers, permissions, checkout, Python setup,
dependency installation and both checks. Locally compare its commands with
`ruff check .`, `pytest` and `requirements-dev.txt`.

## Troubleshooting

- GitHub Actions only discovers workflow files under `.github/workflows/`;
  leaving the file under `exercises/templates/` does not activate it.
- Check indentation and the run's exact commit SHA if a workflow is missing or
  appears stale.
- A dependency installation failure often means the runtime package was added
  to the wrong file or is missing from `requirements.txt`.
- Check whether the branch was pushed to your personal repository and the PR
  targets its `main`.

## Completion checklist

- [ ] Copied and reviewed the template and its TODOs.
- [ ] Confirmed push/PR triggers, Python 3.12, requirements and both checks.
- [ ] Used minimal read-only permissions and no secrets or deployment.
- [ ] Inspected the successful run for the PR's current commit.
- [ ] Classified CI, continuous delivery and continuous deployment.
