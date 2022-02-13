#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
from custom_barplots import student_data

if __name__ == "__main__":
    # Set the whiskers to 0.5 * IQR
    sns.catplot(x="romantic", y="G3", data=student_data, kind="box", whis=0.5)

    # Show plot
    plt.show()

    # Extend the whiskers to the 5th and 95th percentile
    sns.catplot(x="romantic", y="G3", data=student_data, kind="box", whis=[5, 95])

    # Show plot
    plt.show()

    # Set the whiskers at the min and max values
    sns.catplot(x="romantic", y="G3", data=student_data, kind="box", whis=[0, 100])

    # Show plot
    plt.show()
