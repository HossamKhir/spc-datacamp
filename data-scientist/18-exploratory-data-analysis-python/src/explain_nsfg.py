#! /usr/bin/python3
"""
"""
from load_data import load_nsfg

nsfg = load_nsfg()

if __name__ == "__main__":
    # Display the number of rows and columns
    print(nsfg.shape)

    # Display the names of the columns
    print(nsfg.columns)

    # Select column birthwgt_oz1: ounces
    ounces = nsfg["birthwgt_oz1"]

    # Print the first 5 elements of ounces
    print(ounces.iloc[:5])
