#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import pandas as pd
from data_time_index import climate_change

if __name__ == "__main__":
    _, ax = plt.subplots()

    # Plot the relative temperature data
    ax.plot(climate_change.index, climate_change["relative_temp"])

    # Annotate the date at which temperatures exceeded 1 degree
    ax.annotate(">1 degree", (pd.Timestamp("2015-10-06"), 1))

    plt.show()
