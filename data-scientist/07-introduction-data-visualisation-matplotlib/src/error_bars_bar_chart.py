#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from histograms import mens_gymnastics, mens_rowing

if __name__ == "__main__":
    _, ax = plt.subplots()

    row_height = mens_rowing["Height"]
    gym_height = mens_gymnastics["Height"]

    # Add a bar for the rowing "Height" column mean/std
    ax.bar("Rowing", row_height.mean(), yerr=row_height.std())

    # Add a bar for the gymnastics "Height" column mean/std
    ax.bar("Gymnastics", gym_height.mean(), yerr=gym_height.std())

    # Label the y-axis
    ax.set_ylabel("Height (cm)")

    plt.show()
