#! /usr/bin/python3
"""
"""
import pandas as pd
import os

data_path = "../data/raw"

movies = pd.read_csv(os.path.join(data_path, "movies.csv"))
financials = pd.read_csv(os.path.join(data_path, "financials.csv"))
toy_story = pd.read_csv(os.path.join(data_path, "toy_story.csv"))
taglines = pd.read_csv(os.path.join(data_path, "taglines.csv"))
action_movies = pd.read_csv(os.path.join(data_path, "action_movies.csv"))
scifi_movies = pd.read_csv(os.path.join(data_path, "scifi_movies.csv"))
pop_movies = pd.read_csv(os.path.join(data_path, "pop_movies.csv"))
movie_to_genres = pd.read_csv(os.path.join(data_path, "movie_to_genres.csv"))
iron_1_actors = pd.read_csv(os.path.join(data_path, "iron_1_actors.csv"))
iron_2_actors = pd.read_csv(os.path.join(data_path, "iron_2_actors.csv"))
crews = pd.read_csv(os.path.join(data_path, "crews.csv"))
sequels = pd.read_csv(os.path.join(data_path, "sequels.csv"))

if __name__ == "__main__":
    pass
