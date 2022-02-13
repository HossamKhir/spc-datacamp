#! /usr/bin/python3
"""
"""
import pandas as pd
from load_movies import action_movies, scifi_movies, movies

if __name__ == "__main__":
    # Merge action_movies to scifi_movies with right join
    action_scifi = action_movies.merge(scifi_movies, on=["movie_id"], how="right")

    # Merge action_movies to scifi_movies with right join
    action_scifi = action_movies.merge(
        scifi_movies, on="movie_id", how="right", suffixes=["_act", "_sci"]
    )

    # Print the first few rows of action_scifi to see the structure
    print(action_scifi.head())

    # Merge action_movies to the scifi_movies with right join
    action_scifi = action_movies.merge(
        scifi_movies, on="movie_id", how="right", suffixes=("_act", "_sci")
    )

    # From action_scifi, select only the rows where the genre_act column is null
    scifi_only = action_scifi[action_scifi.genre_act.isna()]

    # Merge action_movies to the scifi_movies with right join
    action_scifi = action_movies.merge(
        scifi_movies, on="movie_id", how="right", suffixes=("_act", "_sci")
    )

    # From action_scifi, select only the rows where the genre_act column is null
    scifi_only = action_scifi[action_scifi["genre_act"].isnull()]

    # Merge the movies and scifi_only tables with an inner join
    movies_and_scifi_only = movies.merge(
        scifi_only, left_on="id", right_on="movie_id", how="inner"
    )

    # Print the first few rows and shape of movies_and_scifi_only
    print(movies_and_scifi_only.head())
    print(movies_and_scifi_only.shape)
