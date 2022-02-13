#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
from size_scatterplot import mpg

if __name__ == "__main__":
    # Create line plot
    sns.relplot(data=mpg, kind="line", x="model_year", y="mpg")

    # Show plot
    plt.show()
