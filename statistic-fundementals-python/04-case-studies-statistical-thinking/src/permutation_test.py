#! /usr/bin/python3
"""
:file: permutation_test.py
:author: Hossam Khair
"""
import os
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
import json
from param_estimate import bout_lengths_wt

DATA_PATH = "../data/raw"

with open(os.path.join(DATA_PATH, "bout_lengths_het.json")) as file:
    bout_lengths_het = file.read()
    bout_lengths_het = np.array(json.loads(bout_lengths_het))


if __name__ == "__main__":
    # Compute the difference of means: diff_means_exp
    diff_means_exp = np.mean(bout_lengths_het) - np.mean(bout_lengths_wt)

    # Draw permutation replicates: perm_reps
    perm_reps = dcst.draw_perm_reps(
        bout_lengths_het, bout_lengths_wt, dcst.diff_of_means, size=10 ** 4
    )

    # Compute the p-value: p-val
    p_val = np.sum(perm_reps >= diff_means_exp) / len(perm_reps)

    # Print the result
    print("p =", p_val)
