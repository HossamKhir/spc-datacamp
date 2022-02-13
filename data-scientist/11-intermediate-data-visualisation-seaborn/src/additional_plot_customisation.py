#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_rent

df = load_rent()

if __name__ == "__main__":
    # Create a figure and axes
    fig, ax = plt.subplots()

    # Plot the distribution of 1 bedroom rents
    sns.displot(df["fmr_1"], ax=ax)

    # Modify the properties of the plot
    ax.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100, 1500), title="US Rent")

    # Display the plot
    plt.show()
