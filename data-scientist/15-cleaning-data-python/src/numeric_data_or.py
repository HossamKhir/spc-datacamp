#! /usr/bin/python3
"""
"""
from load_data import load_ride_share

ride_sharing = load_ride_share()

if __name__ == "__main__":
    # Print the information of ride_sharing
    print(ride_sharing.info())

    # Print summary statistics of user_type column
    print(ride_sharing["user_type"].describe())

    # Convert user_type from integer to category
    ride_sharing["user_type_cat"] = ride_sharing["user_type"].astype("category")

    # Write an assert statement confirming the change
    assert ride_sharing["user_type_cat"].dtype == "category"

    # Print new summary statistics
    print(ride_sharing["user_type_cat"].describe())
