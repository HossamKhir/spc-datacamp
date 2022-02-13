#! /usr/bin/python3
"""
:file: hypothesis_test.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from ecdf_beak_depth import bd_1975, bd_2012
from bootstrap_mean_variance import draw_bs_reps

mean_diff = 0.22622047244094645

if __name__ == "__main__":
    # Compute mean of combined data set: combined_mean
    combined_mean = np.mean(np.concatenate((bd_1975, bd_2012)))

    # Shift the samples
    bd_1975_shifted = bd_1975 - np.mean(bd_1975) + combined_mean
    bd_2012_shifted = bd_2012 - np.mean(bd_2012) + combined_mean

    # Get bootstrap replicates of shifted data sets
    bs_replicates_1975 = draw_bs_reps(bd_1975_shifted, np.mean, 10**4)
    bs_replicates_2012 = draw_bs_reps(bd_2012_shifted, np.mean, 10**4)

    # Compute replicates of difference of means: bs_diff_replicates
    bs_diff_replicates = bs_replicates_2012 - bs_replicates_1975

    # Compute the p-value
    p = np.sum(bs_diff_replicates >= mean_diff) / len(bs_diff_replicates)

    # Print p-value
    print('p =', p)
