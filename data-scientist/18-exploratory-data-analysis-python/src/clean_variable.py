#! /usr/bin/python3
"""
"""
import numpy as np
from load_data import load_nsfg

nsfg = load_nsfg()

if __name__ == "__main__":
    # Replace the value 8 with NaN
    nsfg["nbrnaliv"].replace(8, np.nan, inplace=True)

    # Print the values and their frequencies
    print(nsfg["nbrnaliv"].value_counts())
