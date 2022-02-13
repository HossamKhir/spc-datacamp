#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_school

df = load_school()

if __name__ == "__main__":
    # Create a boxplot
    sns.boxplot(data=df, x="Award_Amount", y="Model Selected")

    plt.show()
    plt.clf()

    # Create a violinplot with the husl palette
    sns.violinplot(data=df, x="Award_Amount", y="Model Selected", palette="husl")

    plt.show()
    plt.clf()

    # Create a lvplot with the Paired palette and the Region column as the hue
    sns.boxenplot(
        data=df, x="Award_Amount", y="Model Selected", palette="Paired", hue="Region"
    )

    plt.show()
    plt.clf()
