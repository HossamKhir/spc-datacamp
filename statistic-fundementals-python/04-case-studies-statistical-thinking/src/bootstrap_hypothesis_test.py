#! /usr/bin/python3
"""
:file: bootstrap_hypothesis_test.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

from permutation_test import bout_lengths_wt, bout_lengths_het


if __name__ == "__main__":
    # Concatenate arrays: bout_lengths_concat
    bout_lengths_concat = np.concatenate((bout_lengths_wt, bout_lengths_het))

    # Compute mean of all bout_lengths: mean_bout_length
    mean_bout_length = np.mean(bout_lengths_concat)

    # Generate shifted arrays
    wt_shifted = bout_lengths_wt - np.mean(bout_lengths_wt) + mean_bout_length
    het_shifted = bout_lengths_het - \
        np.mean(bout_lengths_het) + mean_bout_length

    # Compute 10,000 bootstrap replicates from shifted arrays
    bs_reps_wt = dcst.draw_bs_reps(wt_shifted, np.mean, 10**4)
    bs_reps_het = dcst.draw_bs_reps(het_shifted, np.mean, 10**4)

    # Get replicates of difference of means: bs_replicates
    bs_reps = bs_reps_het - bs_reps_wt

    # Compute and print p-value: p
    p = np.sum(bs_reps >= diff_means_exp) / len(bs_reps)
    print('p-value =', p)
