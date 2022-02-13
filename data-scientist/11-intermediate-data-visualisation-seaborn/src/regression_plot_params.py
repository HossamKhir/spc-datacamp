#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_college

df = load_college()

if __name__ == "__main__":
    pass

# Plot a regression plot of Tuition and the Percentage of Pell Grants
sns.regplot(data=df, y="Tuition", x="PCTPELL")

plt.show()
plt.clf()

# Create another plot that estimates the tuition by PCTPELL
sns.regplot(data=df, y="Tuition", x="PCTPELL", x_bins=5)

plt.show()
plt.clf()

# The final plot should include a line using a 2nd order polynomial
sns.regplot(data=df, y="Tuition", x="PCTPELL", x_bins=5, order=2)

plt.show()
plt.clf()
