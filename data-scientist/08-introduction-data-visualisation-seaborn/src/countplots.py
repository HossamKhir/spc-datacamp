#! /usr/bin/python3
"""
"""
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

DATA_PATH = "../data/raw"

survey_data = pd.read_csv(os.path.join(DATA_PATH, "survey_data.csv"))

if __name__ == "__main__":
    # Create count plot of internet usage
    sns.catplot(kind="count", data=survey_data, x="Internet usage")

    # Show plot
    plt.show()

    # Change the orientation of the plot
    sns.catplot(y="Internet usage", data=survey_data, kind="count")

    # Show plot
    plt.show()

    # Create column subplots based on age category
    sns.catplot(y="Internet usage", data=survey_data, kind="count", col="Age Category")

    # Show plot
    plt.show()
