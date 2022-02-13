#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
from facetgrids_v_axessubplots import mpg

if __name__ == "__main__":
    # Create scatter plot
    g = sns.relplot(x="weight", y="horsepower", data=mpg, kind="scatter")

    # Add a title "Car Weight vs. Horsepower"
    g.fig.suptitle("Car Weight vs. Horsepower")

    # Show plot
    plt.show()
