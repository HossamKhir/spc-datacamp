#! /usr/bin/python3
"""
"""
import pandas as pd

from load_taxi import taxi_veh, taxi_owners

if __name__ == "__main__":
    # Merge the taxi_owners and taxi_veh tables
    taxi_own_veh = taxi_owners.merge(taxi_veh, on="vid")

    # Print the column names of the taxi_own_veh
    print(taxi_own_veh.columns)

    # Merge the taxi_owners and taxi_veh tables setting a suffix
    taxi_own_veh = taxi_owners.merge(taxi_veh, on="vid", suffixes=["_own", "_veh"])

    # Print the column names of taxi_own_veh
    print(taxi_own_veh.columns)

    # Print the value_counts to find the most popular fuel_type
    print(taxi_own_veh["fuel_type"].value_counts())
