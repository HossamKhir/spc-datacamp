#! /usr/bin/python3
"""
"""
import os
import matplotlib.pyplot as plt
import pandas as pd

DATA_PATH = "../data/raw"

climate_change = pd.read_csv(os.path.join(DATA_PATH, "climate_change.csv"))

if __name__ == "__main__":
    _, ax = plt.subplots()

    # Add data: "co2" on x-axis, "relative_temp" on y-axis
    ax.scatter(climate_change.co2, climate_change.relative_temp)

    # Set the x-axis label to "CO2 (ppm)"
    ax.set_xlabel("CO2 (ppm)")

    # Set the y-axis label to "Relative temperature (C)"
    ax.set_ylabel("Relative temperature (C)")

    plt.show()
