"""Game rules kept separate from terminal input and output."""

import random

from movie_game.data import MOVIES, Movie

MAX_GUESSES = 4


def select_movie(movies: tuple[Movie, ...] = MOVIES) -> Movie:
    """Choose a movie from the supplied collection."""
    return random.choice(movies)


def build_hint(movie: Movie) -> str:
    """Build the baseline year-based hint for a movie."""
    return f"Hint: released in {movie.year}."


def normalize_guess(guess: str) -> str:
    """Trim a guess and collapse repeated whitespace."""
    return " ".join(guess.split()).casefold()


def is_correct_guess(guess: str, movie: Movie) -> bool:
    """Return whether a guess matches the movie title."""
    return normalize_guess(guess) == normalize_guess(movie.title)


def remaining_attempts(guesses_used: int, limit: int = MAX_GUESSES) -> int:
    """Return the number of guesses left."""
    return limit - guesses_used


def play_round(guess_limit: int = MAX_GUESSES) -> None:
    """Run one complete round of the game in the terminal."""
    movie = select_movie()
    word_count = len(movie.title.split())
    print(
        f"The title starts with {movie.title[0]} and has {word_count} "
        f"{'word' if word_count == 1 else 'words'}. {build_hint(movie)}"
    )
    print(f"You have {guess_limit} guesses.")

    guesses_used = 0
    while guesses_used < guess_limit:
        guess = input("Your guess: ")
        if not normalize_guess(guess):
            print("Please enter a movie title; an empty guess does not count.")
            continue

        guesses_used += 1
        if is_correct_guess(guess, movie):
            print("Correct! Nice guessing.")
            return

        attempts_left = remaining_attempts(guesses_used, guess_limit)
        if attempts_left:
            guess_word = "guess" if attempts_left == 1 else "guesses"
            print(f"Not quite. You have {attempts_left} {guess_word} remaining.")
        else:
            print(f"No guesses left. The movie was {movie.title}.")


if __name__ == "__main__":
    play_round()
