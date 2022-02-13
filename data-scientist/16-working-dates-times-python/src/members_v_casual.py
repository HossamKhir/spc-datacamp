#! /usr/bin/python3
"""
"""
import pandas as pd
from load_csv import rides

if __name__ == "__main__":
    # Resample rides to be monthly on the basis of Start date
    monthly_rides = rides.resample("M", on="Start date")["Member type"]

    # Take the ratio of the .value_counts() over the total number of rides
    print(monthly_rides.value_counts() / monthly_rides.size())
