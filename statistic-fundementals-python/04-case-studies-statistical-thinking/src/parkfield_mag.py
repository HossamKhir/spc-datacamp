#! /usr/bin/python3
"""
:file: parkfield_mag.py
:author: Hossam Khair
"""
import os
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
import json

DATA_PATH = "../data/raw"

with open(os.path.join(DATA_PATH, "mags.json")) as mags:
    mags = mags.read()
    mags = json.loads(mags)

if __name__ == "__main__":
    pass
    # Make the plot
    _ = plt.plot(*dcst.ecdf(mags), marker=".", linestyle="none")

    # Label axes and show plot
    plt.xlabel("magnitude")
    plt.ylabel("ECDF")
    plt.show()
