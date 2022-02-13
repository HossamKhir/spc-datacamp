#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from read_csv import df

if __name__ == "__main__":
    # Create a distplot
    sns.distplot(df["Award_Amount"], kde=False, bins=20)

    # Display the plot
    plt.show()
