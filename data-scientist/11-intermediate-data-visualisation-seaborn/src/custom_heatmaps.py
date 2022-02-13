#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_show

df = load_show()

if __name__ == "__main__":
    # Create the crosstab DataFrame
    pd_crosstab = pd.crosstab(df["Group"], df["YEAR"])

    # Plot a heatmap of the table with no color bar and using the BuGn palette
    sns.heatmap(pd_crosstab, cbar=False, cmap="BuGn", linewidths=0.3)

    # Rotate tick marks for visibility
    plt.yticks(rotation=0)
    plt.xticks(rotation=90)

    # Show the plot
    plt.show()
    plt.clf()
