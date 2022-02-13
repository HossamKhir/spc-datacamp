#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from data_time_index import climate_change


if __name__ == "__main__":
    _, ax = plt.subplots()

    # Add the time-series for "relative_temp" to the plot
    ax.plot(climate_change.index, climate_change.relative_temp)

    # Set the x-axis label
    ax.set_xlabel("Time")

    # Set the y-axis label
    ax.set_ylabel("Relative temperature (Celsius)")

    # Show the figure
    plt.show()
