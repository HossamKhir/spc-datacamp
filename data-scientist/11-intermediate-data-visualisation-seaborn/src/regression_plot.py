#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_accidents

df = load_accidents()

if __name__ == "__main__":
    # Create a regression plot of premiums vs. insurance_losses
    sns.regplot(x="insurance_losses", y="premiums", data=df)

    # Display the plot
    plt.show()

    # Create an lmplot of premiums vs. insurance_losses
    sns.lmplot(x="insurance_losses", y="premiums", data=df)

    # Display the second plot
    plt.show()
