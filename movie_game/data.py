"""Movie records used by the game."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Movie:
    title: str
    year: int
    genre: str
    director: str


MOVIES = (
    Movie("The Matrix", 1999, "Science fiction", "Lana and Lilly Wachowski"),
    Movie("Arrival", 2016, "Science fiction", "Denis Villeneuve"),
    Movie("Back to the Future", 1985, "Science fiction", "Robert Zemeckis"),
    Movie("Jaws", 1975, "Thriller", "Steven Spielberg"),
    Movie("The Silence of the Lambs", 1991, "Thriller", "Jonathan Demme"),
    Movie("Groundhog Day", 1993, "Comedy", "Harold Ramis"),
    Movie("The Grand Budapest Hotel", 2014, "Comedy", "Wes Anderson"),
    Movie("Toy Story", 1995, "Adventure", "John Lasseter"),
    Movie("Raiders of the Lost Ark", 1981, "Adventure", "Steven Spielberg"),
    Movie("Spirited Away", 2001, "Adventure", "Hayao Miyazaki"),
    Movie("The Shawshank Redemption", 1994, "Drama", "Frank Darabont"),
    Movie("Forrest Gump", 1994, "Drama", "Robert Zemeckis"),
    Movie("The Lion King", 1994, "Animation", "Roger Allers and Rob Minkoff"),
    Movie("Finding Nemo", 2003, "Animation", "Andrew Stanton"),
)
