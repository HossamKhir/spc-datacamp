#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from empiricaldist import Cdf
from load_data import load_gss

gss = load_gss()

if __name__ == "__main__":
    # Select realinc
    income = gss.realinc

    # Make the CDF
    cdf_income = Cdf(income)

    # Plot it
    cdf_income.plot()

    # Label the axes
    plt.xlabel("Income (1986 USD)")
    plt.ylabel("CDF")
    plt.show()
