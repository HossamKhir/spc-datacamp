#! /usr/bin/python3
"""
"""
import os

# Import pandas
import pandas as pd

DATA_PATH = "../data/raw"

# Load CSV into the rides variable
rides = pd.read_csv(
    os.path.join(DATA_PATH, "capital-onebike.csv"),
    parse_dates=["Start date", "End date"],
)

# Print the initial (0th) row
print(rides.iloc[0])
