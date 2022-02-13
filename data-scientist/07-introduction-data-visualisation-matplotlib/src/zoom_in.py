#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from data_time_index import climate_change

if __name__ == "__main__":
    # Use plt.subplots to create fig and ax
    _, ax = plt.subplots()

    # Create variable seventies with data from "1970-01-01" to "1979-12-31"
    seventies = climate_change["1970-01-01":"1979-12-31"]

    # Add the time-series for "co2" data from seventies to the plot
    ax.plot(seventies.index, seventies["co2"])

    # Show the figure
    plt.show()
