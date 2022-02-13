#! /usr/bin/python3
"""
"""
import seaborn as sns
import matplotlib.pyplot as plt

from load_data import load_brfss

brfss = load_brfss()

if __name__ == "__main__":
    # Drop rows with missing data
    data = brfss.dropna(subset=["INCOME2", "HTM4"])

    # Make a violin plot
    sns.violinplot(x="INCOME2", y="HTM4", data=data, inner=None)

    # Remove unneeded lines and label axes
    sns.despine(left=True, bottom=True)
    plt.xlabel("Income level")
    plt.ylabel("Height in cm")
    plt.show()
