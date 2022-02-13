#! /usr/bin/python3
"""
"""
# Import numpy
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Assign the filename: file
    file = "digits_header.txt"

    # Load the data: data
    data = np.loadtxt(file, delimiter="\t", skiprows=1, usecols=[0, 2])

    # Print data
    print(data)
