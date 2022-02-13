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
    # Set style, enable color code, and create a magenta distplot
    sns.set(color_codes=True)
    sns.displot(df["fmr_3"], color="m")

    # Show the plot
    plt.show()
