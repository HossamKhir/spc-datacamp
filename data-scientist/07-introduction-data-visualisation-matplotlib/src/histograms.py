#! /usr/bin/python3
"""
"""
import os
import matplotlib.pyplot as plt
import pandas as pd

DATA_PATH = "../data/raw"

mens_gymnastics = pd.read_csv(os.path.join(DATA_PATH, "mens_gymnastics.csv"))
mens_rowing = pd.read_csv(os.path.join(DATA_PATH, "mens_rowing.csv"))


if __name__ == "__main__":
    _, ax = plt.subplots()
    # Plot a histogram of "Weight" for mens_rowing
    ax.hist(mens_rowing["Weight"])

    # Compare to histogram of "Weight" for mens_gymnastics
    ax.hist(mens_gymnastics["Weight"])

    # Set the x-axis label to "Weight (kg)"
    ax.set_xlabel("Weight (kg)")

    # Set the y-axis label to "# of observations"
    ax.set_ylabel("# of observations")

    plt.show()
