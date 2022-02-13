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
# Create a scatter plot by disabling the regression line
sns.regplot(data=df, y="Tuition", x="UG", fit_reg=False)

plt.show()
plt.clf()

# Create a regplot and bin the data into 8 bins
sns.regplot(data=df, y="Tuition", x="UG", x_bins=5)

plt.show()
plt.clf()

# Create a regplot and bin the data into 8 bins
sns.regplot(data=df, y="Tuition", x="UG", x_bins=8)

plt.show()
plt.clf()
