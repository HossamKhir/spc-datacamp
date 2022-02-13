#! /usr/bin/python3
"""
:file: hypothesis_test_chance.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
from current_effect_lane_pos import lanes, f_13

if __name__ == "__main__":
    # Compute observed correlation: rho
    rho = dcst.pearson_r(lanes, f_13)

    # Initialize permutation reps: perm_reps_rho
    perm_reps_rho = np.empty(10**4)

    # Make permutation reps
    for i in range(10000):
        # Scramble the lanes array: scrambled_lanes
        scrambled_lanes = np.random.permutation(lanes)

        # Compute the Pearson correlation coefficient
        perm_reps_rho[i] = dcst.pearson_r(scrambled_lanes, f_13)

    # Compute and print p-value
    p_val = np.sum(perm_reps_rho >= rho) / 10000
    print('p =', p_val)
