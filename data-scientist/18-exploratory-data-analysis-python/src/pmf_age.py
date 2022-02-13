#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from empiricaldist import Pmf
from load_data import load_brfss

brfss = load_brfss()

if __name__ == "__main__":
    # Extract age
    age = brfss["AGE"]

    # Plot the PMF
    pmf_age = Pmf(age)
    pmf_age.bar()

    # Label the axes
    plt.xlabel("Age in years")
    plt.ylabel("PMF")
    plt.show()
