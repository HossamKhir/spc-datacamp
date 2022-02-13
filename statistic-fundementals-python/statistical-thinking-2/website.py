#! /usr/bin/python3
"""
:file: 
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from p_value import diff_of_means, draw_perm_reps

nht_dead = nht_live = np.array([])

if __name__ == "__main__":
    # Compute the observed difference in mean inter-no-hitter times: nht_diff_obs
    nht_diff_obs = diff_of_means(nht_dead, nht_live)

    # Acquire 10,000 permutation replicates of difference in mean no-hitter time: perm_replicates
    perm_replicates = draw_perm_reps(nht_dead, nht_live, diff_of_means, 10**4)

    # Compute and print the p-value: p
    p = np.sum(perm_replicates <= nht_diff_obs) / len(perm_replicates)
    print('p-val =', p)
