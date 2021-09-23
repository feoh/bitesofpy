import csv
import statistics
from collections import defaultdict, namedtuple
import os
from typing import List, Tuple, Any
from urllib.request import urlretrieve
import logging

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = os.getenv("TMP", "/tmp")

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def strip_unprintable(str):
    clean = [character for character in str if character.isprintable()]
    return "".join(clean)


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies_by_director = {}

    mcsv = open(local,'r',encoding='UTF-8')
    movie_csv_dict_reader = csv.DictReader(mcsv)

    for movie_dict in movie_csv_dict_reader:
        # This is gross but I can't find a more elegant way.
        if not(movie_dict['director_name'] and
               movie_dict['movie_title'] and
               movie_dict['title_year'] and
               movie_dict['imdb_score']):
            logging.info(f"Discarding: {movie_dict['title_year']} because it had a critical empty field.")
            continue

        this_director = strip_unprintable(movie_dict['director_name'])
        this_movie_title = strip_unprintable(movie_dict['movie_title'])
        this_movie_year = int(movie_dict['title_year'])

        this_movie_score = float(movie_dict["imdb_score"])

        this_movie: Movie = Movie(title=this_movie_title,
                                  year=this_movie_year,
                                  score=this_movie_score)
        movies_by_director.setdefault(this_director, [])
        if this_movie_year > 1960:
            movies_by_director[this_director].append(this_movie)

    return movies_by_director


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    scores = [movie.score for movie in movies]
    unrounded_mean = statistics.fmean(scores)
    return round(unrounded_mean, 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    director_scores: list[tuple[Any, float]] = []

    for director in directors:
        if len(directors[director]) < MIN_MOVIES:
            continue

        mean_score = calc_mean_score((directors[director]))
        director_scores.append((director, mean_score))

    director_scores.sort(key = lambda t: t[1], reverse=True)
    return director_scores
