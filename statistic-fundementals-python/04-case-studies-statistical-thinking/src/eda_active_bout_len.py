#! /usr/bin/python3
"""
:file: 
:author: Hossam Khair
"""
import os
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
import json

DATA_PATH = "../data/raw"

with open(os.path.join(DATA_PATH, "bout_lengths_wt.json")) as file:
    bout_lengths_wt = file.read()
    bout_lengths_wt = np.array(json.loads(bout_lengths_wt))
    # bout_lengths_wt = np.array(list(bout_lengths_wt.values()))

with open(os.path.join(DATA_PATH, "bout_lengths_mut.json")) as file:
    bout_lengths_mut = file.read()
    bout_lengths_mut = np.array(json.loads(bout_lengths_mut))
    # bout_lengths_mut = np.array(list(bout_lengths_mut.values()))


if __name__ == "__main__":
    # Generate x and y values for plotting ECDFs
    x_wt, y_wt = dcst.ecdf(bout_lengths_wt)
    x_mut, y_mut = dcst.ecdf(bout_lengths_mut)

    # Plot the ECDFs
    _ = plt.plot(x_wt, y_wt, marker=".", linestyle="none")
    _ = plt.plot(x_mut, y_mut, marker=".", linestyle="none")

    # Make a legend, label axes, and show plot
    _ = plt.legend(("wt", "mut"))
    _ = plt.xlabel("active bout length (min)")
    _ = plt.ylabel("ECDF")
    plt.show()
