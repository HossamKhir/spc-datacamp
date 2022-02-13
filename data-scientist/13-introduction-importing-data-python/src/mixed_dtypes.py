#! /usr/bin/python3
"""
"""
import os
import numpy as np

DATA_PATH = "../data/raw"

if __name__ == "__main__":
    # Assign the filename: file
    file = "titanic.csv"

    # Import file using np.recfromcsv: d
    d = np.recfromcsv(os.path.join(DATA_PATH, file), encoding="utf-8")

    # Print out first three entries of d
    print(d[:3])
