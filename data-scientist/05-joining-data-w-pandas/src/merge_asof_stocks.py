#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
from load_data import load_jpm, load_wells, load_bac

jpm = load_jpm()
wells = load_wells()
bac = load_bac()

if __name__ == "__main__":
    # Use merge_asof() to merge jpm and wells
    jpm_wells = pd.merge_asof(
        jpm, wells, on="date_time", suffixes=("", "_wells"), direction="nearest"
    )

    # Use merge_asof() to merge jpm_wells and bac
    jpm_wells_bac = pd.merge_asof(
        jpm_wells, bac, on="date_time", suffixes=("_jpm", "_bac"), direction="nearest"
    )

    # Compute price diff
    price_diffs = jpm_wells_bac.diff()

    # Plot the price diff of the close of jpm, wells and bac only
    price_diffs.plot(y=["close_jpm", "close_wells", "close_bac"])
    plt.show()
