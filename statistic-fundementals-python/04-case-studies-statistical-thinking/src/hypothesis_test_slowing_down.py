#! /usr/bin/python3
"""
:file: hypothesis_test_slowing_down.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

from linreg_av_split_time import split_number, mean_splits

if __name__ == "__main__":
    # Observed correlation
    rho = dcst.pearson_r(split_number, mean_splits)

    # Initialize permutation reps
    perm_reps_rho = np.empty(10000)

    # Make permutation reps
    for i in range(10000):
        # Scramble the split number array
        scrambled_split_number = np.random.permutation(split_number)

        # Compute the Pearson correlation coefficient
        perm_reps_rho[i] = dcst.pearson_r(scrambled_split_number, mean_splits)

    # Compute and print p-value
    p_val = np.sum(perm_reps_rho >= rho) / len(perm_reps_rho)
    print('p =', p_val)
