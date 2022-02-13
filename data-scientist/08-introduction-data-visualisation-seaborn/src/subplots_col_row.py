#! /usr/bin/python3
"""
"""
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

DATA_PATH = "../data/raw"

student_data = pd.read_csv(os.path.join(DATA_PATH, "student_data.csv"))


if __name__ == "__main__":
    # Change to use relplot() instead of scatterplot()
    sns.relplot(x="absences", y="G3", data=student_data, kind="scatter")

    # Show plot
    plt.show()

    # Change to make subplots based on study time
    sns.relplot(
        x="absences", y="G3", data=student_data, kind="scatter", col="study_time"
    )

    # Show plot
    plt.show()

    # Change this scatter plot to arrange the plots in rows instead of columns
    sns.relplot(
        x="absences", y="G3", data=student_data, kind="scatter", row="study_time"
    )

    # Show plot
    plt.show()
