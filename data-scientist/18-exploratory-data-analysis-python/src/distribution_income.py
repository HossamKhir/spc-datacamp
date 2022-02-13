#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from empiricaldist import Pmf
from load_data import load_brfss


brfss = load_brfss()

if __name__ == "__main__":
    # Extract income
    income = brfss.INCOME2

    # Plot the PMF
    Pmf(income).bar()

    # Label the axes
    plt.xlabel("Income level")
    plt.ylabel("PMF")
    plt.show()
