#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_college

df = load_college()

if __name__ == "__main__":
    # Display a regression plot for Tuition
    sns.regplot(data=df, y="Tuition", x="SAT_AVG_ALL", marker="^", color="g")

    plt.show()
    plt.clf()

    # Display the residual plot
    sns.residplot(data=df, y="Tuition", x="SAT_AVG_ALL", color="g")

    plt.show()
    plt.clf()
