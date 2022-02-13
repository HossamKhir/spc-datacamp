#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
from custom_barplots import student_data


if __name__ == "__main__":
    # Create a point plot of family relationship vs. absences
    sns.catplot(data=student_data, kind="point", x="famrel", y="absences")

    # Show plot
    plt.show()

    # Add caps to the confidence interval
    sns.catplot(x="famrel", y="absences", data=student_data, kind="point", capsize=0.2)

    # Show plot
    plt.show()

    # Remove the lines joining the points
    sns.catplot(
        x="famrel",
        y="absences",
        data=student_data,
        kind="point",
        capsize=0.2,
        join=False,
    )

    # Show plot
    plt.show()
