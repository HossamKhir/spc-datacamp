#! /usr/bin/python3
"""
:file: measure_heritability.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from eda_heritability import bd_parent_fortis, bd_offspring_scandens, bd_offspring_fortis, bd_parent_scandens
from correlation_offspring_parent import draw_bs_pairs


def heritability(parents, offspring):
    """Compute the heritability from parent and offspring samples."""
    covariance_matrix = np.cov(parents, offspring)
    return covariance_matrix[0, 1] / covariance_matrix[0, 0]


# heritability_scandens

if __name__ == "__main__":
    # Compute the heritability
    heritability_scandens = heritability(
        bd_parent_scandens, bd_offspring_scandens)
    heritability_fortis = heritability(bd_parent_fortis, bd_offspring_fortis)

    # Acquire 1000 bootstrap replicates of heritability
    replicates_scandens = draw_bs_pairs(
        bd_parent_scandens, bd_offspring_scandens, heritability, size=1000)

    replicates_fortis = draw_bs_pairs(
        bd_parent_fortis, bd_offspring_fortis, heritability, size=1000)

    # Compute 95% confidence intervals
    conf_int_scandens = np.percentile(replicates_scandens, [2.5, 97.5])
    conf_int_fortis = np.percentile(replicates_fortis, [2.5, 97.5])

    # Print results
    print('G. scandens:', heritability_scandens, conf_int_scandens)
    print('G. fortis:', heritability_fortis, conf_int_fortis)

    # Initialize array of replicates: perm_replicates
    perm_replicates = np.empty(10**4)

    # Draw replicates
    for i in range(10000):
        # Permute parent beak depths
        bd_parent_permuted = np.random.permutation(bd_parent_scandens)
        perm_replicates[i] = heritability(
            bd_parent_permuted, bd_offspring_scandens)

    # Compute p-value: p
    p = np.sum(perm_replicates >= heritability_scandens) / len(perm_replicates)

    # Print the p-value
    print('p-val =', p)
