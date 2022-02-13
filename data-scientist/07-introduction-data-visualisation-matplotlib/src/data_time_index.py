#! /usr/bin/python3
"""
"""
import os
import pandas as pd

DATA_PATH = "../data/raw"

# Read the data from file using read_csv
climate_change = pd.read_csv(
    os.path.join(DATA_PATH, "climate_change.csv"),
    parse_dates=["date"],
    index_col="date",
)
