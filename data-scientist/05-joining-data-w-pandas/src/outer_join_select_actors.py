#! /usr/bin/python3
"""
"""
import pandas as pd
from load_movies import iron_1_actors, iron_2_actors

if __name__ == "__main__":
    pass
# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
iron_1_and_2 = iron_1_actors.merge(
    iron_2_actors, how="outer", on=["id"], suffixes=["_1", "_2"]
)

# Create an index that returns true if name_1 or name_2 are null
m = (iron_1_and_2["name_1"].isna()) | (iron_1_and_2["name_2"].isna())

# Print the first few rows of iron_1_and_2
print(iron_1_and_2[m].head())
