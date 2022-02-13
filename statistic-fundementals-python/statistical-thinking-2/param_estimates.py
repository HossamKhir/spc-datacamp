#! /usr/bin/python3
"""
:file: param_estimates.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from bootstrap_mean_variance import draw_bs_reps
from ecdf_beak_depth import bd_1975, bd_2012

if __name__ == "__main__":
    # Compute the difference of the sample means: mean_diff
    mean_diff = np.mean(bd_2012) - np.mean(bd_1975)

    # Get bootstrap replicates of means
    bs_replicates_1975 = draw_bs_reps(bd_1975, np.mean, 10**4)
    bs_replicates_2012 = draw_bs_reps(bd_2012, np.mean, 10**4)

    # Compute samples of difference of means: bs_diff_replicates
    bs_diff_replicates = bs_replicates_2012 - bs_replicates_1975

    # Compute 95% confidence interval: conf_int
    conf_int = np.percentile(bs_diff_replicates, [2.5, 97.5])

    # Print the results
    print('difference of means =', mean_diff, 'mm')
    print('95% confidence interval =', conf_int, 'mm')
