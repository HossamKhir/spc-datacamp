#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
from custom_barplots import student_data

# Import median function from numpy
from numpy import median

if __name__ == "__main__":
    # Create a point plot with subgroups
    sns.catplot(
        data=student_data, kind="point", x="romantic", y="absences", hue="school"
    )

    # Show plot
    plt.show()

    # Turn off the confidence intervals for this plot
    sns.catplot(
        x="romantic",
        y="absences",
        data=student_data,
        kind="point",
        hue="school",
        ci=None,
    )

    # Show plot
    plt.show()

    # Plot the median number of absences instead of the mean
    sns.catplot(
        x="romantic",
        y="absences",
        data=student_data,
        kind="point",
        hue="school",
        ci=None,
        estimator=median,
    )

    # Show plot
    plt.show()
