#! /usr/bin/python3
"""
"""
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

DATA_PATH = "../data/raw"

student_data = pd.read_csv(os.path.join(DATA_PATH, "student-data.csv"))

if __name__ == "__main__":
    # Create a scatter plot of absences vs. final grade
    sns.scatterplot(x="absences", y="G3", data=student_data, hue="location")

    # Show plot
    plt.show()

    # Change the legend order in the scatter plot
    sns.scatterplot(
        x="absences",
        y="G3",
        data=student_data,
        hue="location",
        hue_order=["Rural", "Urban"],
    )

    # Show plot
    plt.show()
