#! /usr/bin/python3
"""
"""
from empiricaldist import Pmf
from load_data import load_gss
import matplotlib.pyplot as plt

gss = load_gss()

if __name__ == "__main__":
    # Select the age column
    age = gss["age"]

    # Make a PMF of age
    pmf_age = Pmf(age)

    # Plot the PMF
    pmf_age.bar()

    # Label the axes
    plt.xlabel("Age")
    plt.ylabel("PMF")
    plt.show()
