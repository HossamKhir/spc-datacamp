#! /usr/bin/python3
"""
:file: hypothesis_test_different_b_val.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
from quantify_b_value import mt, mags_post, mags_pre

if __name__ == "__main__":
    # Only magnitudes above completeness threshold
    mags_pre = mags_pre[mags_pre >= mt]
    mags_post = mags_post[mags_post >= mt]

    # Observed difference in mean magnitudes: diff_obs
    diff_obs = np.mean(mags_post) - np.mean(mags_pre)

    # Generate permutation replicates: perm_reps
    perm_reps = dcst.draw_perm_reps(
        mags_post, mags_pre, dcst.diff_of_means,
        size=10**4
    )

    # Compute and print p-value
    p_val = np.sum(perm_reps < diff_obs) / 10000
    print('p =', p_val)
