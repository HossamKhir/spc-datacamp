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
    # Use the "ggplot" style and create new Figure/Axes
    plt.style.use("ggplot")
    fig, ax = plt.subplots()
    ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
    plt.show()

    # Use the "Solarize_Light2" style and create new Figure/Axes
    plt.style.use("Solarize_Light2")
    fig, ax = plt.subplots()
    ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
    plt.show()
