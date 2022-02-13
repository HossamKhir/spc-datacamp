#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_school

df = load_school()

if __name__ == "__main__":
    # Create the stripplot
    sns.stripplot(data=df, x="Award_Amount", y="Model Selected", jitter=True)

    plt.show()

    # Create and display a swarmplot with hue set to the Region
    sns.swarmplot(data=df, x="Award_Amount", y="Model Selected", hue="Region")

    plt.show()
