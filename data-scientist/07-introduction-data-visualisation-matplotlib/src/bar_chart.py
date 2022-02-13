#! /usr/bin/python3
"""
"""
import os
import matplotlib.pyplot as plt
import pandas as pd

DATA_PATH = "../data/raw"

medals = pd.read_csv(os.path.join(DATA_PATH, "medals.csv"), index_col=0)

if __name__ == "__main__":
    pass
    fig, ax = plt.subplots()

    # Plot a bar-chart of gold medals as a function of country
    ax.bar(medals.index, medals["Gold"])

    # Set the x-axis tick labels to the country names
    ax.set_xticklabels(medals.index, rotation=90)

    # Set the y-axis label
    ax.set_ylabel("Number of medals")

    plt.show()
