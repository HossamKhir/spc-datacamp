#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_bike

df = load_bike()

if __name__ == "__main__":
    pass
    # Build a JointGrid comparing humidity and total_rentals
    sns.set_style("whitegrid")
    g = sns.JointGrid(x="hum", y="total_rentals", data=df, xlim=(0.1, 1.0))

    g.plot(sns.regplot, sns.distplot)

    plt.show()
    plt.clf()

    # Create a jointplot similar to the JointGrid
    sns.jointplot(x="hum", y="total_rentals", kind="reg", data=df)

    plt.show()
    plt.clf()
