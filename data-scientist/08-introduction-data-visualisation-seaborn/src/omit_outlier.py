#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
from custom_barplots import student_data

if __name__ == "__main__":
    # Create a box plot with subgroups and omit the outliers
    sns.catplot(
        kind="box", data=student_data, x="internet", y="G3", hue="location", sym=""
    )

    # Show plot
    plt.show()
