#! /usr/bin/python3
"""
"""
import os
import pandas as pd

DATA_PATH = "../data/raw"

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Assign filename: file
    file = "titanic_corrupt.txt"

    # Import file: data
    data = pd.read_csv(
        os.path.join(DATA_PATH, file), sep="\t", comment="#", na_values="Nothing"
    )

    # Print the head of the DataFrame
    print(data.head())

    # Plot 'Age' variable in a histogram
    pd.DataFrame.hist(data[["Age"]])
    plt.xlabel("Age (years)")
    plt.ylabel("count")
    plt.show()
