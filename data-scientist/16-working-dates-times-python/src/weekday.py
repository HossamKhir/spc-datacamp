#! /usr/bin/python3
"""
"""
import pandas as pd
from load_csv import rides

if __name__ == "__main__":
    # Add a column for the weekday of the start of the ride
    rides["Ride start weekday"] = rides["Start date"].dt.weekday_name

    # Print the median trip time per weekday
    print(rides.groupby("Ride start weekday")["Duration"].median())
