from movie_game.data import Movie
from movie_game.game import (
    MAX_GUESSES,
    build_hint,
    is_correct_guess,
    normalize_guess,
    remaining_attempts,
    select_movie,
)


def test_guess_normalization_collapses_whitespace_and_case() -> None:
    assert normalize_guess("  the   MATRIX ") == "the matrix"


def test_title_comparison_ignores_case_and_whitespace() -> None:
    movie = Movie("The Matrix", 1999, "Science fiction", "The Wachowskis")
    assert is_correct_guess(" the   MATRIX ", movie)
    assert not is_correct_guess("The Matrices", movie)


def test_baseline_hint_uses_release_year() -> None:
    movie = Movie("Arrival", 2016, "Science fiction", "Denis Villeneuve")
    assert build_hint(movie) == "Hint: released in 2016."


def test_movie_selection_uses_the_supplied_collection() -> None:
    only_movie = Movie("Jaws", 1975, "Thriller", "Steven Spielberg")
    assert select_movie((only_movie,)) == only_movie


def test_remaining_attempts_starts_at_four_and_decreases() -> None:
    assert MAX_GUESSES == 4
    assert remaining_attempts(0) == 4
    assert remaining_attempts(1) == 3
    assert remaining_attempts(4) == 0
