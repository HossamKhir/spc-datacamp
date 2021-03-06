#! /usr/bin/python3
"""
:file: pearson.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from covariance import pearson_r

illiteracy = fertility = np.array([])

if __name__ == "__main__":
    # Compute observed correlation: r_obs
    r_obs = pearson_r(illiteracy, fertility)

    # Initialize permutation replicates: perm_replicates
    perm_replicates = np.empty(10000)

    # Draw replicates
    for i in range(10**4):
        # Permute illiteracy measurments: illiteracy_permuted
        illiteracy_permuted = np.random.permutation(illiteracy)

        # Compute Pearson correlation
        perm_replicates[i] = pearson_r(illiteracy_permuted, fertility)

    # Compute p-value: p
    p = np.sum(perm_replicates >= r_obs) / len(perm_replicates)
    print('p-val =', p)
