#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

csv_filepath = "../data/raw/frame.csv"

if __name__ == "__main__":
    # Create a DataFrame from csv file
    df = pd.read_csv(csv_filepath)

    # Create a count plot with "Spiders" on the x-axis
    sns.countplot(x="Spiders", data=df)

    # Display the plot
    plt.show()
