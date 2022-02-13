#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
from hue_scatter import student_data

if __name__ == "__main__":
    # Create a dictionary mapping subgroup values to colors
    palette_colors = {"Rural": "green", "Urban": "blue"}

    # Create a count plot of school with location subgroups
    sns.countplot(x="school", data=student_data, hue="location", palette=palette_colors)

    # Display plot
    plt.show()
