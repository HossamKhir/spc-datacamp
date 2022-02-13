#! /usr/bin/python3
"""
"""
import os
import pandas as pd

DATA_PATH = "../data/raw"

summer_2016_medals = pd.read_csv(os.path.join(DATA_PATH, "summer_2016_medals.csv"))

# Extract the "Sport" column
sports_column = summer_2016_medals["Sport"]

# Find the unique values of the "Sport" column
sports = sports_column.unique()

# Print out the unique sports values
print(sports)

if __name__ == "__main__":
    pass
