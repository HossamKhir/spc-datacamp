#! /usr/bin/python3
"""
:file: generate_perm_samples.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt


def swap_random(a, b):
    """Randomly swap entries in two arrays."""
    # Indices to swap
    swap_inds = np.random.random(size=len(a)) < .5

    # Make copies of arrays a and b for output
    a_out = np.copy(a)
    b_out = np.copy(b)

    # Swap values
    a_out[swap_inds] = b[swap_inds]
    b_out[swap_inds] = a[swap_inds]

    return a_out, b_out


if __name__ == "__main__":
    pass
