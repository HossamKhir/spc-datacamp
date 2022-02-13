#! /usr/bin/python3
"""
:file: hypothesis_test_women_semi_finals.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
from generate_perm_samples import swap_random
from eda_finals_semi import semi_times, final_times
from param_estimate_finals_semi import f_mean

if __name__ == "__main__":
    # Set up array of permutation replicates
    perm_reps = np.empty(1000)

    for i in range(1000):
        # Generate a permutation sample
        semi_perm, final_perm = swap_random(semi_times, final_times)

        # Compute f from the permutation sample
        f = (semi_perm - final_perm) / semi_perm

        # Compute and store permutation replicate
        perm_reps[i] = np.mean(f)

    # Compute and print p-value
    print('p =', np.sum(perm_reps >= f_mean) / 1000)
