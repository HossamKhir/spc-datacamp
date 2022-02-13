#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
from subplots_col_row import student_data

if __name__ == "__main__":
    # Create a scatter plot of G1 vs. G3
    sns.relplot(x="G1", y="G3", data=student_data, kind="scatter")

    # Show plot
    plt.show()

    # Adjust to add subplots based on school support
    sns.relplot(
        x="G1",
        y="G3",
        data=student_data,
        kind="scatter",
        col="schoolsup",
        col_order=["yes", "no"],
    )

    # Show plot
    plt.show()

    # Adjust further to add subplots based on family support
    sns.relplot(
        x="G1",
        y="G3",
        data=student_data,
        kind="scatter",
        col="schoolsup",
        col_order=["yes", "no"],
        row="famsup",
        row_order=["yes", "no"],
    )

    # Show plot
    plt.show()
