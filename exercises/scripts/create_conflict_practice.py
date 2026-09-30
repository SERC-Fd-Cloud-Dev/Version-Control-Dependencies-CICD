"""Create an isolated, disposable same-line merge-conflict exercise."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
DESTINATION = ROOT / "practice" / "movie-hint-conflict"
BASELINE = '''def build_hint(movie):
    return f"Hint: released in {movie['year']}."


movie = {
    "year": 1999,
    "genre": "Science fiction",
    "director": "Lana and Lilly Wachowski",
}
print(build_hint(movie))
'''


def run_git(*arguments: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *arguments],
        cwd=DESTINATION,
        check=check,
        capture_output=True,
        text=True,
    )


def write_hint(return_line: str) -> None:
    (DESTINATION / "hint_demo.py").write_text(
        BASELINE.replace(
            '    return f"Hint: released in {movie[\'year\']}."',
            return_line,
        ),
        encoding="utf-8",
    )


def main() -> int:
    if DESTINATION.exists():
        print(
            f"Refusing to overwrite existing path: {DESTINATION}\n"
            "Inspect or remove only this disposable fixture before retrying.",
            file=sys.stderr,
        )
        return 1

    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.mkdir()
    try:
        run_git("init", "-b", "main")
        run_git("config", "user.name", "Movie Game Exercise")
        run_git("config", "user.email", "exercise@example.invalid")
        (DESTINATION / "hint_demo.py").write_text(BASELINE, encoding="utf-8")
        (DESTINATION / "README.txt").write_text(
            "After resolving, check with: python hint_demo.py\n",
            encoding="utf-8",
        )
        run_git("add", "hint_demo.py", "README.txt")
        run_git("commit", "-m", "Create fixed hint baseline")

        run_git("switch", "-c", "hint-genre")
        write_hint('    return f"Hint: {movie[\'genre\']} movie."')
        run_git("commit", "-am", "Include genre in hint")

        run_git("switch", "main")
        run_git("switch", "-c", "hint-year-director")
        write_hint(
            '    return f"Hint: released in {movie[\'year\']}, '
            'directed by {movie[\'director\']}."'
        )
        run_git("commit", "-am", "Include year and director in hint")
        merge = run_git("merge", "hint-genre", check=False)
        if merge.returncode == 0:
            raise RuntimeError("The prepared branches unexpectedly merged cleanly.")
        status = run_git("status", "--short")
        if "UU hint_demo.py" not in status.stdout:
            raise RuntimeError("Expected hint_demo.py to have an unresolved conflict.")
    except (OSError, subprocess.CalledProcessError, RuntimeError) as error:
        print(f"Could not prepare the fixture: {error}", file=sys.stderr)
        print(
            f"Inspect the disposable path before removing it: {DESTINATION}",
            file=sys.stderr,
        )
        return 1

    print(f"Conflict ready in: {DESTINATION}")
    print("Resolve hint_demo.py, then stage and commit the merge in that directory.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
