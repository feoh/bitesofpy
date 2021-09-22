import csv
import statistics
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

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


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies_by_director = {}

    mcsv = open(local,'r',encoding='UTF-8')
    movie_csv_dict_reader = csv.DictReader(mcsv)

    for movie_dict in movie_csv_dict_reader:
        this_director = movie_dict['director_name']
        this_movie: Movie = Movie(title=movie_dict['movie_title'], year=movie_dict['title_year'], score=movie_dict[
            "imdb_score"])
        movies_by_director.setdefault(this_director, [])
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
    tl = [tuple(director,calc_mean_score(directors[director])) for director in directors]
    return tl

