#! /usr/bin/python3
"""
:file: prob_15.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

from hypothesis_test_lane_assignment import f, f_mean

swimtime_low_lanes_15 = np.array([
    27.66, 24.69, 23.29, 23.05, 26.87, 31.03, 22.04, 24.51, 21.86,
    25.64, 25.91, 24.77, 30.14, 27.23, 24.31, 30.2, 26.86
])
swimtime_high_lanes_15 = np.array([
    27.7, 24.64, 23.21, 23.09, 26.87, 30.74, 21.88, 24.5, 21.86,
    25.9, 26.2, 24.73, 30.13, 26.92, 24.31, 30.25, 26.76
])

if __name__ == "__main__":
    pass
    # Compute f and its mean
    f = (swimtime_low_lanes_15 - swimtime_high_lanes_15) / swimtime_low_lanes_15
    f_mean = np.mean(f)

    # Draw 10,000 bootstrap replicates
    bs_reps = dcst.draw_bs_reps(f, np.mean, size=10**4)

    # Compute 95% confidence interval
    conf_int = np.percentile(bs_reps, [2.5, 97.5])

    # Shift f
    f_shift = f - f_mean

    # Draw 100,000 bootstrap replicates of the mean
    bs_reps = dcst.draw_bs_reps(f_shift, np.mean, 10**5)

    # Compute the p-value
    p_val = np.sum(bs_reps >= f_mean) / 100000

    # Print the results
    print("""
    mean frac. diff.: {0:.5f}
    95% conf int of mean frac. diff.: [{1:.5f}, {2:.5f}]
    p-value: {3:.5f}""".format(f_mean, *conf_int, p_val))
