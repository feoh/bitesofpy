from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    steam_feed = feedparser.parse(FEED_URL)
    games_list = []
    entries = steam_feed['entries']
    for entry in entries:
        this_game = Game(title = entry['title'], link = entry['link'])
        games_list.append(this_game)

    return games_list