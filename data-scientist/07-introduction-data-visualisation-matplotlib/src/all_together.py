#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from plot_timeseries import plot_timeseries
from data_time_index import climate_change
import pandas as pd

if __name__ == "__main__":
    _, ax = plt.subplots()

    # Plot the CO2 levels time-series in blue
    plot_timeseries(
        ax,
        climate_change.index,
        climate_change.co2,
        "blue",
        "Time (years)",
        "CO2 levels",
    )

    # Create an Axes object that shares the x-axis
    ax2 = ax.twinx()

    # Plot the relative temperature data in red
    plot_timeseries(
        ax2,
        climate_change.index,
        climate_change.relative_temp,
        "red",
        "Time (years)",
        "Relative temp (Celsius)",
    )

    # Annotate point with relative temperature >1 degree
    ax2.annotate(
        ">1 degree",
        xytext=(pd.Timestamp("2008-10-06"), -0.2),
        xy=(pd.Timestamp("2015-10-06"), 1),
        arrowprops={"arrowstyle": "->", "color": "grey"},
    )

    plt.show()
