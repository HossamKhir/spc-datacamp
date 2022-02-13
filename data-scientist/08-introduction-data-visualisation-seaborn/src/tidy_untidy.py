#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns

# Import Pandas
import pandas as pd

csv_filepath = "../data/raw/untidy.csv"

if __name__ == "__main__":
    # Create a DataFrame from csv file
    df = pd.read_csv(csv_filepath)

    # Print the head of df
    print(df.head())
