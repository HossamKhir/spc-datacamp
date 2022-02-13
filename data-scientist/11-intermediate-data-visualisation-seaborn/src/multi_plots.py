#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_rent

df = load_rent()

if __name__ == "__main__":
    # Create a plot with 1 row and 2 columns that share the y axis label
    fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True)

    # Plot the distribution of 1 bedroom apartments on ax0
    sns.histplot(df["fmr_1"], ax=ax0, kde=True)
    ax0.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100, 1500))

    # Plot the distribution of 2 bedroom apartments on ax1
    sns.histplot(df["fmr_2"], ax=ax1, kde=True)
    ax1.set(xlabel="2 Bedroom Fair Market Rent", xlim=(100, 1500))

    # Display the plot
    plt.show()
