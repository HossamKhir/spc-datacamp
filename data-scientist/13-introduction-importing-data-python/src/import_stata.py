#! /usr/bin/python3
"""
"""
# Import pandas
import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "../data/raw"

if __name__ == "__main__":
    # Load Stata file into a pandas DataFrame: df
    df = pd.read_stata(os.path.join(DATA_PATH, "disarea.dta"))

    # Print the head of the DataFrame df
    print(df.head())

    # Plot histogram of one column of the DataFrame
    pd.DataFrame.hist(df[["disa10"]])
    plt.xlabel("Extent of disease")
    plt.ylabel("Number of countries")
    plt.show()
