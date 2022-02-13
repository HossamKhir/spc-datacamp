#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_rent

df = load_rent()

if __name__ == "__main__":
    sns.set_style("dark")
    sns.displot(df["fmr_2"])
    plt.show()
    plt.clf()

    sns.set_style("whitegrid")
    sns.displot(df["fmr_2"])
    plt.show()
    plt.clf()
