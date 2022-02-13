#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from histograms import mens_gymnastics, mens_rowing

if __name__ == "__main__":
    _, ax = plt.subplots()

    # Plot a histogram of "Weight" for mens_rowing
    ax.hist(mens_rowing["Weight"], label="Rowing", histtype="step", bins=5)

    # Compare to histogram of "Weight" for mens_gymnastics
    ax.hist(mens_gymnastics["Weight"], label="Gymnastics", histtype="step", bins=5)

    ax.set_xlabel("Weight (kg)")
    ax.set_ylabel("# of observations")

    # Add the legend and show the Figure
    ax.legend()
    plt.show()
