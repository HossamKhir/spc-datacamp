#! /usr/bin/python3
"""
:file: p_value.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from permutation import permutation_sample
from bootstrap_mean_variance import draw_bs_reps


def draw_perm_reps(data_1, data_2, func, size=1):
    """Generate multiple permutation replicates."""

    # Initialize array of replicates: perm_replicates
    perm_replicates = np.empty(size)

    for i in range(size):
        # Generate permutation sample
        perm_sample_1, perm_sample_2 = permutation_sample(data_1, data_2)

        # Compute the test statistic
        perm_replicates[i] = func(perm_sample_1, perm_sample_2)

    return perm_replicates


def diff_of_means(data_1, data_2):
    """Difference in means of two arrays."""

    # The difference of means of data_1, data_2: diff
    diff = np.mean(data_1) - np.mean(data_2)

    return diff


df = pd.DataFrame()
force_a = force_b = np.array([])

if __name__ == "__main__":
    # Make bee swarm plot
    _ = sns.swarmplot(x="ID", y="impact_force", data=df)

    # Label axes
    _ = plt.xlabel('frog')
    _ = plt.ylabel('impact force (N)')

    # Show the plot
    plt.show()

    # Compute difference of mean impact force from experiment: empirical_diff_means
    empirical_diff_means = diff_of_means(force_a, force_b)

    # Draw 10,000 permutation replicates: perm_replicates
    perm_replicates = draw_perm_reps(force_a, force_b,
                                     diff_of_means, size=10000)

    # Compute p-value: p
    p = np.sum(perm_replicates >= empirical_diff_means) / len(perm_replicates)

    # Print the result
    print('p-value =', p)

    # Make an array of translated impact forces: translated_force_b
    translated_force_b = force_b + 0.55 - np.mean(force_b)

    # Take bootstrap replicates of Frog B's translated impact forces: bs_replicates
    bs_replicates = draw_bs_reps(translated_force_b, np.mean, 10000)

    # Compute fraction of replicates that are less than the observed Frog B force: p
    p = np.sum(bs_replicates <= np.mean(force_b)) / 10000

    # Print the p-value
    print('p = ', p)

    forces_concat = np.concatenate((force_a, force_b))

    # Compute mean of all forces: mean_force
    mean_force = np.mean(forces_concat)

    # Generate shifted arrays
    force_a_shifted = force_a - np.mean(force_a) + mean_force
    force_b_shifted = force_b - np.mean(force_b) + mean_force

    # Compute 10,000 bootstrap replicates from shifted arrays
    bs_replicates_a = draw_bs_reps(force_a_shifted, np.mean, 10**4)
    bs_replicates_b = draw_bs_reps(force_b_shifted, np.mean, 10**4)

    # Get replicates of difference of means: bs_replicates
    bs_replicates = bs_replicates_a - bs_replicates_b

    # Compute and print p-value: p
    p = np.sum(bs_replicates > empirical_diff_means) / len(bs_replicates)
    print('p-value =', p)
