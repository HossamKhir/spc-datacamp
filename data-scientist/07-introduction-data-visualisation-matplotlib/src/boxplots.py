#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from histograms import mens_gymnastics, mens_rowing

if __name__ == "__main__":
    pass
    _, ax = plt.subplots()

    # Add a boxplot for the "Height" column in the DataFrames
    ax.boxplot([mens_rowing["Height"], mens_gymnastics["Height"]])

    # Add x-axis tick labels:
    ax.set_xticklabels(["Rowing", "Gymnastics"])

    # Add a y-axis label
    ax.set_ylabel("Height (cm)")

    plt.show()
