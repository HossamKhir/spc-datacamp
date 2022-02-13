#! /usr/bin/python3
"""
"""
import pandas as pd
from load_csv import rides

if __name__ == "__main__":
    # Group rides by member type, and resample to the month
    grouped = rides.groupby("Member type").resample("M", on="Start date")

    # Print the median duration for each group
    print(grouped["Duration"].median())
