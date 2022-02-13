#! /usr/bin/python3
"""
"""
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

DATA_PATH = "../data/raw"

survey_data = pd.read_csv(os.path.join(DATA_PATH, "survey_data.csv"))

if __name__ == "__main__":
    pass
# Set the style to "whitegrid"
sns.set_style("whitegrid")
sns.set_palette("Purples")
# sns.set_palette("RdBu")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", "Often", "Always"]

sns.catplot(x="Parents Advice", data=survey_data, kind="count", order=category_order)

# Show plot
plt.show()
