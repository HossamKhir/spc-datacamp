#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_rent

df = load_rent()

if __name__ == "__main__":
    # Loop through differences between bright and colorblind palettes
    for p in ["bright", "colorblind"]:
        sns.set_palette(p)
        sns.displot(df["fmr_3"])
        plt.show()

        # Clear the plots
        plt.clf()
