#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
from size_scatterplot import mpg

if __name__ == "__main__":
    # Create line plot of model year vs. horsepower
    sns.relplot(kind="line", data=mpg, x="model_year", y="horsepower", ci=None)

    # Show plot
    plt.show()

    # Change to create subgroups for country of origin
    sns.relplot(
        x="model_year", y="horsepower", data=mpg, kind="line", ci=None, style="origin"
    )

    # Show plot
    plt.show()

    # Add markers and make each line have the same style
    sns.relplot(
        x="model_year",
        y="horsepower",
        data=mpg,
        kind="line",
        ci=None,
        style="origin",
        hue="origin",
        markers=True,
        dashes=False,
    )

    # Show plot
    plt.show()
