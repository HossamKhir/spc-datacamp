#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from simple_scatter import climate_change

if __name__ == "__main__":
    _, ax = plt.subplots()

    # Add data: "co2", "relative_temp" as x-y, index as colour
    ax.scatter(climate_change.co2, climate_change.relative_temp, c=climate_change.index)

    # Set the x-axis label to "CO2 (ppm)"
    ax.set_xlabel("CO2 (ppm)")

    # Set the y-axis label to "Relative temperature (C)"
    ax.set_ylabel("Relative temperature (C)")

    plt.show()
