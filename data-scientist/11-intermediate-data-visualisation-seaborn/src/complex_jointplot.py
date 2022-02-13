#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_bike

df = load_bike()

if __name__ == "__main__":
    # Create a jointplot of temp vs. casual riders
    # Include a kdeplot over the scatter plot
    g = sns.jointplot(
        x="temp",
        y="casual",
        kind="scatter",
        data=df,
        marginal_kws=dict(bins=10),
    ).plot_joint(sns.kdeplot)

    plt.show()
    plt.clf()

    # Replicate the above plot but only for registered riders
    g = sns.jointplot(
        x="temp",
        y="registered",
        kind="scatter",
        data=df,
        marginal_kws=dict(bins=10),
    ).plot_joint(sns.kdeplot)

    plt.show()
    plt.clf()
