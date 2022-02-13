#! /usr/bin/python3
"""
"""
import numpy as np

# Import packages
import pandas as pd
import matplotlib.pyplot as plt

# Assign url of file: url
url = "https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv"

if __name__ == "__main__":

    # Read file into a DataFrame: df
    df = pd.read_csv(url, sep=";")

    # Print the head of the DataFrame
    print(df.head())

    # Plot first column of df
    pd.DataFrame.hist(df.ix[:, 0:1])
    plt.xlabel("fixed acidity (g(tartaric acid)/dm$^3$)")
    plt.ylabel("count")
    plt.show()
