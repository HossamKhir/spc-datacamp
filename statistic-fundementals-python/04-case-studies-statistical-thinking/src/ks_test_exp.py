#! /usr/bin/python3
"""
:file: ks_test_exp.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
from parkfield_interearthquake import time_gap, mean_time_gap

if __name__ == "__main__":
    pass
# Draw target distribution: x_f
x_f = np.random.exponential(mean_time_gap, size=10**4)

# Compute K-S stat: d
d = dcst.ks_stat(x_f, time_gap)

# Draw K-S replicates: reps
reps = dcst.draw_ks_reps(len(time_gap), np.random.exponential,
                         args=(mean_time_gap,), size=10**4, n_reps=10**4)

# Compute and print p-value
p_val = np.sum(reps >= d) / 10000
print('p =', p_val)
