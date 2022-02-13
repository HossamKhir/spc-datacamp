#! /usr/bin/python3
"""
"""
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

DATA_PATH = "../data/raw"

mpg = pd.read_csv(os.path.join(DATA_PATH, "mpg.csv"))

if __name__ == "__main__":
    # Create scatter plot
    g = sns.relplot(x="weight", y="horsepower", data=mpg, kind="scatter")

    # Identify plot type
    type_of_g = type(g)

    # Print type
    print(type_of_g)
