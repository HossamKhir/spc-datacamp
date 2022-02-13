#! /usr/bin/python3
"""
"""
import pandas as pd
import datetime as dt
from load_data import load_ride_share

ride_sharing = load_ride_share()

if __name__ == "__main__":
    # Convert ride_date to datetime
    ride_sharing["ride_dt"] = pd.to_datetime(ride_sharing["ride_date"])

    # Save today's date
    today = dt.date.today()

    # Set all in the future to today's date
    # ride_sharing.loc[ride_sharing["ride_dt"].dt.date > today, "ride_dt"] = today
    ride_sharing.loc[
        ride_sharing["ride_dt"].dt.date > pd.Timestamp(today), "ride_dt"
    ] = pd.Timestamp(today)

    # Print maximum of ride_dt column
    print(ride_sharing["ride_dt"].max())
