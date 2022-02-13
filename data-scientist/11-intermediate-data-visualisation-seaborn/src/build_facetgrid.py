#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_college

df = load_college()

if __name__ == "__main__":
    # Create FacetGrid with Degree_Type and specify the order of the rows using row_order
    g2 = sns.FacetGrid(
        df,
        row="Degree_Type",
        row_order=["Graduate", "Bachelors", "Associates", "Certificate"],
    )

    # Map a pointplot of SAT_AVG_ALL onto the grid
    g2.map(sns.pointplot, "SAT_AVG_ALL")

    # Show the plot
    plt.show()
    plt.clf()
