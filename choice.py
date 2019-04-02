import pdb
import random

from titles import tvshows
from titles import movies


def get_movie():
    all_movies = movies()
    movies_amount = len(all_movies)
    selected_movie = all_movies[random.randint(0, movies_amount - 1)]
    return selected_movie

def get_tvshow():
    all_tvshows = tvshows()
    tvshows_amount = len(all_tvshows)
    selected_tvshow = all_tvshows[random.randint(0, tvshows_amount - 1)]
    return selected_tvshow

def choose():
    video_type = input("""
    [1] Movies
    [2] TVShows

    Only the number, please: """)

    print("""
    **************************************""")

    if video_type == '1':
        movie = get_movie()
        print(f"""
    Movie: {movie['title']}
    Genre: {movie['genre']}
    Where: {movie['broadcaster']}
    """)

    if video_type == '2':
        tvshow = get_tvshow()
        print(f"""
    TVShow: {tvshow['title']}
    Genre: {tvshow['genre']}
    Where: {tvshow['broadcaster']}
    """)

    else:
        print(">>> Which part is difficult to understand? Let's try again.")
        choose()

choose()
