#! /usr/bin/python3
"""
:file: civil_rights.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from p_value import draw_perm_reps


def frac_yea_dems(dems, reps):
    """Compute fraction of Democrat yea votes."""
    frac = np.sum(dems) / len(dems)
    return frac


# Construct arrays of data: dems, reps
dems = np.array([True] * 153 + [False] * 91)
reps = np.array([True] * 136 + [False] * 35)


if __name__ == "__main__":
    # Acquire permutation samples: perm_replicates
    perm_replicates = draw_perm_reps(dems, reps, frac_yea_dems, 10**4)

    # Compute and print p-value: p
    p = np.sum(perm_replicates <= 153/244) / len(perm_replicates)
    print('p-value =', p)
