#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
from size_scatterplot import mpg

if __name__ == "__main__":
    # Make the shaded area show the standard deviation
    sns.relplot(x="model_year", y="mpg", data=mpg, kind="line", ci="sd")

    # Show plot
    plt.show()
