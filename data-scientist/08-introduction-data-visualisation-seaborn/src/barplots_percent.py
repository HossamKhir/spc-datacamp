#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
from countplots import survey_data

if __name__ == "__main__":
    # Create a bar plot of interest in math, separated by gender
    sns.catplot(kind="bar", data=survey_data, x="Gender", y="Interested in Math")

    # Show plot
    plt.show()
