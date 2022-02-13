#! /usr/bin/python3
"""
"""
from load_data import load_brfss

brfss = load_brfss()

if __name__ == "__main__":
    # Select columns
    columns = ["AGE", "INCOME2", "_VEGESU1"]
    subset = brfss[columns]

    # Compute the correlation matrix
    print(subset.corr())
