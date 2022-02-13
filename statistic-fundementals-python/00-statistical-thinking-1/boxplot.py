#! /usr/bin/python3
"""
:file: boxplot.py
:author: Hossam Khair
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame()

# Create box plot with Seaborn's default settings
sns.boxplot(x="species", y="petal length (cm)", data=df)

# Label the axes
plt.xlabel("species")
plt.ylabel("petal length (cm)")

# Show the plot
plt.show()
