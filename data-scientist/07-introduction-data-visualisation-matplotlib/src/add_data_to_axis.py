#! /usr/bin/python3
"""
"""
import os
import matplotlib.pyplot as plt
import pandas as pd

DATA_PATH = "../data/raw"

seattle_weather = pd.read_csv(os.path.join(DATA_PATH, "seattle_weather.csv"))
austin_weather = pd.read_csv(os.path.join(DATA_PATH, "austin_weather.csv"))

if __name__ == "__main__":
    # Create a Figure and an Axes with plt.subplots
    fig, ax = plt.subplots()

    # Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
    ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

    # Plot MLY-PRCP-NORMAL from austin_weather against MONTH
    ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

    # Call the show function
    plt.show()
