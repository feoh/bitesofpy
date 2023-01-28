import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movie_list = []
    for file in files:
        with open(file) as fl:
            movie_list.append(json.load(fl))

    return movie_list

        


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genre"""
    one_comedy = [ movie['Title'] for movie in movies if "Comedy" in movie['Genre']]
    return one_comedy[0]



# Format: "Awards":"3 wins & 11 nominations."
def get_nomination_count(movie):
    awards = movie['Awards']
    (_, nom_text) = awards.split('&')
    nom_text = nom_text.strip()
    (count, _) = nom_text.split()
    return int(count)

def get_runtime(movie):
    runtime_text = movie['Runtime']
    (mins, mins_text) = runtime_text.split()
    return int(mins)


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    movies_sorted_by_nominations = sorted(movies, key = get_nomination_count, reverse=True)
    return movies_sorted_by_nominations[0]['Title']
    


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    movies_sorted_by_runtime = sorted(movies, key=get_runtime, reverse=True)
    return movies_sorted_by_runtime[0]['Title']
