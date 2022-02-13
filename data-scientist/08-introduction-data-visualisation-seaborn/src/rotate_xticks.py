#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
from facetgrids_v_axessubplots import mpg

if __name__ == "__main__":
    # Create point plot
    sns.catplot(
        x="origin", y="acceleration", data=mpg, kind="point", join=False, capsize=0.1
    )

    # Rotate x-tick labels
    plt.xticks(rotation=90)

    # Show plot
    plt.show()
