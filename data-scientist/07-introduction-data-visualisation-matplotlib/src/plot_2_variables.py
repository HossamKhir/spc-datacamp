#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from data_time_index import climate_change

if __name__ == "__main__":
    pass
    # Initialise a Figure and Axes
    _, ax = plt.subplots()

    # Plot the CO2 variable in blue
    ax.plot(climate_change.index, climate_change["co2"], color="b")

    # Create a twin Axes that shares the x-axis
    ax2 = ax.twinx()

    # Plot the relative temperature in red
    ax2.plot(climate_change.index, climate_change["relative_temp"], color="r")

    plt.show()
