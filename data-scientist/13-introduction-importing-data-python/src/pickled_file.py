#! /usr/bin/python3
"""
"""
import os

# Import pickle package
import pickle

DATA_PATH = "../data/raw"

if __name__ == "__main__":
    # Open pickle file and load data: d
    with open(os.path.join(DATA_PATH, "data.pkl"), "rb") as file:
        d = pickle.load(file)

    # Print d
    print(d)

    # Print datatype of d
    print(type(d))
