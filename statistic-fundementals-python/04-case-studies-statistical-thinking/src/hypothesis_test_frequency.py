#! /usr/bin/python3
"""
:file: hypothesis_test_frequency.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
from estimate_mean_time import mean_dt_post, mean_dt_pre, dt_pre, dt_post

if __name__ == "__main__":
    pass
# Compute the observed test statistic
mean_dt_diff = mean_dt_pre - mean_dt_post

# Shift the post-2010 data to have the same mean as the pre-2010 data
dt_post_shift = dt_post - mean_dt_post + mean_dt_pre

# Compute 10,000 bootstrap replicates from arrays
bs_reps_pre = dcst.draw_bs_reps(dt_pre, np.mean, 10**4)
bs_reps_post = dcst.draw_bs_reps(dt_post_shift, np.mean, 10**4)

# Get replicates of difference of means
bs_reps = bs_reps_pre - bs_reps_post

# Compute and print the p-value
p_val = np.sum(bs_reps >= mean_dt_diff) / 10000
print('p =', p_val)
