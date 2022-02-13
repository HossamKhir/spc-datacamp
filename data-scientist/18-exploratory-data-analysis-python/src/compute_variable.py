#! /usr/bin/python3
"""
"""
from load_data import load_nsfg

nsfg = load_nsfg()

if __name__ == "__main__":
    # Select the columns and divide by 100
    agecon = nsfg["agecon"] / 100
    agepreg = nsfg["agepreg"] / 100

    # Compute the difference
    preg_length = agepreg - agecon

    # Compute summary statistics
    print(preg_length.describe())
