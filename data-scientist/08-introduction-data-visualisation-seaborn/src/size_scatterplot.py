#! /usr/bin/python3
"""
"""
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

DATA_PATH = "../data/raw"

mpg = pd.read_csv(os.path.join(DATA_PATH, "mpg.csv"))

if __name__ == "__main__":
    # Create scatter plot of horsepower vs. mpg
    sns.relplot(x="horsepower", y="mpg", data=mpg, kind="scatter", size="cylinders")

    # Show plot
    plt.show()

    # Create scatter plot of horsepower vs. mpg
    sns.relplot(
        x="horsepower",
        y="mpg",
        data=mpg,
        kind="scatter",
        size="cylinders",
        hue="cylinders",
    )

    # Show plot
    plt.show()
