#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from load_data import load_nsfg

nsfg = load_nsfg()
agecon = nsfg.agecon

if __name__ == "__main__":
    # Plot the histogram
    plt.hist(agecon, bins=20)

    # Label the axes
    plt.xlabel("Age at conception")
    plt.ylabel("Number of pregnancies")

    # Show the figure
    plt.show()

    # Plot the histogram
    plt.hist(agecon, bins=20, histtype="step")

    # Label the axes
    plt.xlabel("Age at conception")
    plt.ylabel("Number of pregnancies")

    # Show the figure
    plt.show()
