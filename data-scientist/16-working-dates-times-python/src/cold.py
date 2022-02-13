#! /usr/bin/python3
"""
"""
import pandas as pd

# Import matplotlib
import matplotlib.pyplot as plt
from load_csv import rides

if __name__ == "__main__":
    # Resample rides to daily, take the size, plot the results
    rides.resample("D", on="Start date").size().plot(ylim=[0, 15])

    # Show the results
    plt.show()

    # Resample rides to monthly, take the size, plot the results
    rides.resample("M", on="Start date").size().plot(ylim=[0, 150])

    # Show the results
    plt.show()
