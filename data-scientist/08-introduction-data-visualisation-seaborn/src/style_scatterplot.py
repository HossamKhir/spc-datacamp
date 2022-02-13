#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
from size_scatterplot import mpg

if __name__ == "__main__":
    # Create a scatter plot of acceleration vs. mpg
    sns.relplot(
        kind="scatter",
        data=mpg,
        x="acceleration",
        y="mpg",
        style="origin",
        hue="origin",
    )

    # Show plot
    plt.show()
