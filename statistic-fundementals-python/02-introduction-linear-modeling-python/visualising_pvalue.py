#! /usr/bin/python3
"""
:file: visualising_pvalue.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from test_statistic_effect_size import group_duration_long, group_duration_short
from visualising_test_statistic import shuffle_and_split


def compute_test_statistic(sample1, sample2):
    resample1 = np.random.choice(sample1, size=500, replace=True)
    resample2 = np.random.choice(sample2, size=500, replace=True)
    test_statistic = resample2 - resample1
    return test_statistic


def plot_test_stats_and_pvalue(test_statistic, shuffle_statistic):
    """
    Purpose: Plot the test statistic array as a histogram
    Args:
        test_statistic (np.array): an array of test statistic values, e.g. resample2 - resample1
        shuffle_statistic (np.array): an array of test statistic values, from shuffled resamples
    Returns:
        fig (plt.figure): matplotlib figure object
    """
    t_mean = np.mean(test_statistic)
    t_std = np.std(test_statistic)
    t_min = np.min(test_statistic)
    t_max = np.max(test_statistic)
    effect_size = np.mean(test_statistic)
    p_value = len(
        shuffle_statistic[shuffle_statistic >= effect_size])/len(shuffle_statistic)
    # bin_edges = np.linspace(t_min, t_max, 21)
    bin_edges = np.linspace(-25, 25, 51)
    shuffle_opts = dict(rwidth=0.8, color='blue', alpha=0.35, label='Shuffled')
    test_opts = dict(rwidth=0.8, color='red', alpha=0.35, label='Unshuffled')
    fig, axis = plt.subplots(figsize=(12, 4))
    plt.hist(test_statistic, bins=bin_edges, **test_opts)
    plt.hist(shuffle_statistic, bins=bin_edges, **shuffle_opts)
    axis.axvline(effect_size, color='black', label='Effect Size')
    axis.axvspan(effect_size, +25, alpha=0.10, color='black', label='p-value')
    axis.grid()
    # axis.set_ylim(-5, +55)
    axis.set_xlim(-25, +25)
    axis.set_ylabel("Bin Counts")
    axis.set_xlabel("Test Statistic Values")
    title_form = ("Test Statistic Distibution, \n"
                  "Effect Size = {:0.2f}, p-value = {:0.02f}")
    axis.set_title(title_form.format(effect_size, p_value))
    axis.legend(loc='upper left')
    plt.show()
    return fig


if __name__ == "__main__":
    # Compute the test stat distribution and effect size for two population groups
    test_statistic_unshuffled = compute_test_statistic(
        group_duration_short, group_duration_long)
    effect_size = np.mean(test_statistic_unshuffled)

    # Randomize the two populations, and recompute the test stat distribution
    shuffled_half1, shuffled_half2 = shuffle_and_split(
        group_duration_short, group_duration_long)
    test_statistic_shuffled = compute_test_statistic(
        shuffled_half1, shuffled_half2)

    # Compute the p-value as the proportion of shuffled test stat values >= the effect size
    condition = test_statistic_shuffled >= effect_size
    p_value = len(test_statistic_shuffled[condition]
                  ) / len(test_statistic_shuffled)

    # Print p-value and overplot the shuffled and unshuffled test statistic distributions
    print("The p-value is = {}".format(p_value))
    fig = plot_test_stats_and_pvalue(
        test_statistic_unshuffled, test_statistic_shuffled)
