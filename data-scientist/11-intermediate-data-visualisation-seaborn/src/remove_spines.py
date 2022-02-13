#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_rent

df = load_rent()

if __name__ == "__main__":
    # Set the style to white
    sns.set_style("white")

    # Create a regression plot
    sns.lmplot(data=df, x="pop2010", y="fmr_2")

    # Remove the spines
    sns.despine(left=False, right=True, top=True)

    # Show the plot and clear the figure
    plt.show()
    plt.clf()
