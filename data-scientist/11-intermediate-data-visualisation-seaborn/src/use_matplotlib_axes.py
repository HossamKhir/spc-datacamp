#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_rent

df = load_rent()

if __name__ == "__main__":
    pass
    # Create a figure and axes
    fig, ax = plt.subplots()

    # Plot the distribution of data
    sns.displot(df["fmr_3"], ax=ax)

    # Create a more descriptive x axis label
    ax.set(xlabel="3 Bedroom Fair Market Rent")

    # Show the plot
    plt.show()
