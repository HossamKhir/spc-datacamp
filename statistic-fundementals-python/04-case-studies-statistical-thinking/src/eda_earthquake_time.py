#! /usr/bin/python3
"""
:file: eda_earthquake_time.py
:author: Hossam Khair
"""
import os
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
import json

DATA_PATH = "../data/raw"

with open(os.path.join(DATA_PATH, "time.json")) as time:
    time = time.read()
    time = json.loads(time)
with open(os.path.join(DATA_PATH, "mags.json")) as mags:
    mags = mags.read()
    mags = json.loads(mags)

if __name__ == "__main__":
    pass
    # Plot time vs. magnitude
    _ = plt.plot(time, mags, marker=".", linestyle="none", alpha=0.1)

    # Label axes and show the plot
    plt.xlabel("time (year)")
    plt.ylabel("magnitude")
    plt.show()
