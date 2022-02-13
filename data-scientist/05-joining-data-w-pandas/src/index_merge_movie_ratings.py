#! /usr/bin/python3
"""
"""
import pandas as pd
from load_movies import movies, ratings

if __name__ == "__main__":
    pass
# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings, on="id", how="left")

# Print the first few rows of movies_ratings
print(movies_ratings.head())
