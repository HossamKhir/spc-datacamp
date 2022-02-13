#! /usr/bin/python3
"""
"""
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

DATA_PATH = "../data/raw"

student_data = pd.read_csv(os.path.join(DATA_PATH, "./student_data.csv"))

if __name__ == "__main__":
    # Create bar plot of average final grade in each study category
    sns.catplot(kind="bar", data=student_data, x="study_time", y="G3")

    # Show plot
    plt.show()

    # Rearrange the categories
    sns.catplot(
        x="study_time",
        y="G3",
        data=student_data,
        kind="bar",
        order=["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"],
    )

    # Show plot
    plt.show()

    # Turn off the confidence intervals
    sns.catplot(
        x="study_time",
        y="G3",
        data=student_data,
        kind="bar",
        order=["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"],
        ci=None,
    )

    # Show plot
    plt.show()
