#! /usr/bin/python3
"""
:file: mens_200_confidence.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
from geda_men_200_heats import mens_200_free_heats

if __name__ == "__main__":
    # Compute mean and median swim times
    mean_time = np.mean(mens_200_free_heats)
    median_time = np.median(mens_200_free_heats)

    # Draw 10,000 bootstrap replicates of the mean and median
    bs_reps_mean = dcst.draw_bs_reps(mens_200_free_heats, np.mean, size=10**4)
    bs_reps_median = dcst.draw_bs_reps(
        mens_200_free_heats, np.median, size=10**4)

    # Compute the 95% confidence intervals
    conf_int_mean = np.percentile(bs_reps_mean, [2.5, 97.5])
    conf_int_median = np.percentile(bs_reps_median, [2.5, 97.5])

    # Print the result to the screen
    print("""
    mean time: {0:.2f} sec.
    95% conf int of mean: [{1:.2f}, {2:.2f}] sec.

    median time: {3:.2f} sec.
    95% conf int of median: [{4:.2f}, {5:.2f}] sec.
    """.format(mean_time, *conf_int_mean, median_time, *conf_int_median))
