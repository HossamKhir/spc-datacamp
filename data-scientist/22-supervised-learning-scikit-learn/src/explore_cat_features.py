#! /usr/bin/python3
"""
"""
# Import pandas
import pandas as pd
import matplotlib.pyplot as plt

# Read 'gapminder.csv' into a DataFrame: df
df = pd.read_csv("./data/gapminder.csv")

if __name__ == "__main__":
    # Create a boxplot of life expectancy per region
    df.boxplot("life", "Region", rot=60)

    # Show the plot
    plt.show()
