#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_accidents

df = load_accidents()

if __name__ == "__main__":
    # Create a pairwise plot of the variables using a scatter plot
    sns.pairplot(data=df, vars=["fatal_collisions", "premiums"], kind="scatter")

    plt.show()
    plt.clf()

    # Plot the same data but use a different color palette and color code by Region
    sns.pairplot(
        data=df,
        vars=["fatal_collisions", "premiums"],
        kind="scatter",
        hue="Region",
        palette="RdBu",
        diag_kws={"alpha": 0.5},
    )

    plt.show()
    plt.clf()
