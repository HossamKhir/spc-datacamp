#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_rent

df = load_rent()

if __name__ == "__main__":
    # Plot the pandas histogram
    df["fmr_2"].plot.hist()
    plt.show()
    plt.clf()

    # Set the default seaborn style
    sns.set()

    # Plot the pandas histogram again
    df["fmr_2"].plot.hist()
    plt.show()
    plt.clf()
