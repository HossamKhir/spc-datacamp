#! /usr/bin/python3
"""
:file: swarm
:author: Hossam Khair
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame()

# Create bee swarm plot with Seaborn's default settings
sns.swarmplot(x="species", y="petal length (cm)", data=df)

# Label the axes
plt.xlabel("species")
plt.ylabel("petal length (cm)")

# Show the plot
plt.show()
