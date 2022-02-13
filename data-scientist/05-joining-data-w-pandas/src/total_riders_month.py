#! /usr/bin/python3
"""
"""
import pandas as pd

from load_riders import ridership, cal, stations

if __name__ == "__main__":
    # Merge the ridership and cal tables
    ridership_cal = ridership.merge(cal, on=["year", "month", "day"])

    # Merge the ridership, cal, and stations tables
    ridership_cal_stations = ridership.merge(cal, on=["year", "month", "day"]).merge(
        stations, on="station_id"
    )

    # Create a filter to filter ridership_cal_stations
    filter_criteria = (
        (ridership_cal_stations["month"] == 7)
        & (ridership_cal_stations["day_type"] == "Weekday")
        & (ridership_cal_stations["station_name"] == "Wilson")
    )

    # Use .loc and the filter to select for rides
    print(ridership_cal_stations.loc[filter_criteria, "rides"].sum())
