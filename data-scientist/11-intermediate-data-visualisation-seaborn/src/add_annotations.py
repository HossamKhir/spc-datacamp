#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_rent

df = load_rent()

mean = df["fmr_1"].mean()
median = df["fmr_1"].median()


if __name__ == "__main__":
    # Create a figure and axes. Then plot the data
    fig, ax = plt.subplots()
    sns.histplot(df["fmr_1"], ax=ax)

    # Customize the labels and limits
    ax.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100, 1500), title="US Rent")

    # Add vertical lines for the median and mean
    ax.axvline(x=median, color="m", label="Median", linestyle="--", linewidth=2)
    ax.axvline(x=mean, color="b", label="Mean", linestyle="-", linewidth=2)

    # Show the legend and plot the data
    ax.legend()
    plt.show()
