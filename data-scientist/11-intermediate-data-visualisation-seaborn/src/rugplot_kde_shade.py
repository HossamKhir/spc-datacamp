#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from read_csv import df

if __name__ == "__main__":
    pass
# Create a distplot of the Award Amount
sns.distplot(df["Award_Amount"], hist=False, rug=True, kde_kws={"shade": True})

# Plot the results
plt.show()
