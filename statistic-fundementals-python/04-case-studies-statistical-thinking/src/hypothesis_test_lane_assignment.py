#! /usr/bin/python3
"""
:file: hypothesis_test_lane_assignment.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
from estimate_mean_improvement import f_mean, f

if __name__ == "__main__":
    # Shift f: f_shift
    f_shift = f - f_mean

    # Draw 100,000 bootstrap replicates of the mean: bs_reps
    bs_reps = dcst.draw_bs_reps(f_shift, np.mean, 10**5)

    # Compute and report the p-value
    p_val = np.sum(bs_reps >= f_mean) / 100000
    print('p =', p_val)
