#! /usr/bin/python3
"""
"""
import os
import matplotlib.pyplot as plt
import pandas as pd

DATA_PATH = "../data/raw"

austin_weather = pd.read_csv(os.path.join(DATA_PATH, "austin_weather.csv"))
seattle_weather = pd.read_csv(os.path.join(DATA_PATH, "seattle_weather.csv"))


if __name__ == "__main__":
    _, ax = plt.subplots()

    # Add Seattle temperature data in each month with error bars
    ax.errorbar(
        seattle_weather["MONTH"],
        seattle_weather["MLY-TAVG-NORMAL"],
        yerr=seattle_weather["MLY-TAVG-STDDEV"],
    )

    # Add Austin temperature data in each month with error bars
    ax.errorbar(
        austin_weather["MONTH"],
        austin_weather["MLY-TAVG-NORMAL"],
        yerr=austin_weather["MLY-TAVG-STDDEV"],
    )

    # Set the y-axis label
    ax.set_ylabel("Temperature (Fahrenheit)")

    plt.show()
