#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_college

df = load_college()

if __name__ == "__main__":
    # Create a factor plot that contains boxplots of Tuition values
    sns.factorplot(data=df, x="Tuition", kind="box", row="Degree_Type")

    plt.show()
    plt.clf()

    # Create a facetted pointplot of Average SAT_AVG_ALL scores facetted by Degree Type
    sns.factorplot(
        data=df,
        x="SAT_AVG_ALL",
        kind="point",
        row="Degree_Type",
        row_order=["Graduate", "Bachelors", "Associates", "Certificate"],
    )

    plt.show()
    plt.clf()
