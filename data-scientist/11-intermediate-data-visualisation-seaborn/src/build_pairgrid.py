#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_accidents

df = load_accidents()

if __name__ == "__main__":
    # Create a PairGrid with a scatter plot for fatal_collisions and premiums
    g = sns.PairGrid(df, vars=["fatal_collisions", "premiums"])
    g2 = g.map(plt.scatter)

    plt.show()
    plt.clf()

    # Create the same PairGrid but map a histogram on the diag
    g = sns.PairGrid(df, vars=["fatal_collisions", "premiums"])
    g2 = g.map_diag(plt.hist)
    g3 = g2.map_offdiag(plt.scatter)

    plt.show()
    plt.clf()
