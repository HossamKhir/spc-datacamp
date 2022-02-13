#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_show

df = load_show()

if __name__ == "__main__":
    # Create a crosstab table of the data
    pd_crosstab = pd.crosstab(df["Group"], df["YEAR"])
    print(pd_crosstab)

    # Plot a heatmap of the table
    sns.heatmap(pd_crosstab)

    # Rotate tick marks for visibility
    plt.yticks(rotation=0)
    plt.xticks(rotation=90)

    plt.show()
