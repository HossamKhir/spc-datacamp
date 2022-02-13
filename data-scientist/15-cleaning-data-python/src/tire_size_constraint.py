#! /usr/bin/python3
"""
"""

from load_data import load_ride_share

ride_sharing = load_ride_share()

if __name__ == "__main__":
    # Convert tire_sizes to integer
    ride_sharing["tire_sizes"] = ride_sharing["tire_sizes"].astype("int")

    # Set all values above 27 to 27
    ride_sharing.loc[ride_sharing["tire_sizes"] > 27, "tire_sizes"] = 27

    # Reconvert tire_sizes back to categorical
    ride_sharing["tire_sizes"] = ride_sharing["tire_sizes"].astype("category")

    # Print tire size description
    print(ride_sharing["tire_sizes"].describe())
