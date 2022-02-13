#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_school

df = load_school()

if __name__ == "__main__":
    pass
    # Show a countplot with the number of models used with each region a different color
    sns.countplot(data=df, y="Model Selected", hue="Region")

    plt.show()
    plt.clf()

    # Create a pointplot and include the capsize in order to show caps on the error bars
    sns.pointplot(data=df, y="Award_Amount", x="Model Selected", capsize=0.1)

    plt.show()
    plt.clf()

    # Create a barplot with each Region shown as a different color
    sns.barplot(data=df, y="Award_Amount", x="Model Selected", hue="Region")

    plt.show()
    plt.clf()
