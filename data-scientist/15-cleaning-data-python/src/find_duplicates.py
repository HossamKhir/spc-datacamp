#! /usr/bin/python3
"""
"""
import pandas as pd

ride_sharing = pd.read_csv("../data/raw/ride_share_minimal.csv")

if __name__ == "__main__":
    pass
    # Find duplicates
    duplicates = ride_sharing.duplicated("ride_id", keep=False)

    # Sort your duplicated rides
    duplicated_rides = ride_sharing[duplicates].sort_values("ride_id")

    # Print relevant columns of duplicated_rides
    print(duplicated_rides[["ride_id", "duration", "user_birth_year"]])
