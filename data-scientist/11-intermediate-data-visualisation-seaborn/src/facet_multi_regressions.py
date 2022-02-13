#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from regression_plot import df

if __name__ == "__main__":
    # Create a regression plot with multiple rows
    sns.lmplot(data=df, x="insurance_losses", y="premiums", row="Region")

    # Show the plot
    plt.show()
