"""Movie records used by the game."""

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Movie:
    title: str
    year: int
    genre: str
    director: str


MOVIE_DATA_FILE = Path(__file__).with_name("movies.json")

with MOVIE_DATA_FILE.open(encoding="utf-8") as movie_file:
    MOVIES = tuple(Movie(**record) for record in json.load(movie_file))
