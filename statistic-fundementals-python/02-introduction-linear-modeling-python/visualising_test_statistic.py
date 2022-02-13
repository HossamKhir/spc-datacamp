#! /usr/bin/python3
"""
:file: visualising_test_statistic.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from test_statistic_effect_size import group_duration_short, group_duration_long


def plot_test_statistic(test_statistic, label=''):
    """
    Purpose: Plot the test statistic array as a histogram
    Args:
        test_statistic (np.array): an array of test statistic values, e.g. resample2 - resample1
    Returns:
        fig (plt.figure): matplotlib figure object
    """
    t_mean = np.mean(test_statistic)
    t_std = np.std(test_statistic)
    t_min = np.min(test_statistic)
    t_max = np.max(test_statistic)
    # bin_edges = np.linspace(t_min, t_max, 21)
    bin_edges = np.linspace(-25, 25, 51)
    data_opts = dict(rwidth=0.8, color='blue', alpha=0.5)
    fig, axis = plt.subplots(figsize=(12, 4))
    plt.hist(test_statistic, bins=bin_edges, **data_opts)
    axis.grid()
    axis.set_ylim(-5, +55)
    axis.set_xlim(-25, +25)
    axis.set_ylabel("Bin Counts")
    axis.set_xlabel("Test Statistic Values".format(label))
    title_form = "{} Groups: Test Statistic Distribution, \nMean = {:0.2f}, Std Error = {:0.2f}"
    axis.set_title(title_form.format(label, t_mean, t_std))
    plt.show()
    return fig


def shuffle_and_split(sample1, sample2):
    shuffled = np.concatenate((sample1, sample2))
    np.random.shuffle(shuffled)
    half_length = len(shuffled)//2
    sample1 = shuffled[0:half_length]
    sample2 = shuffled[half_length+1:]
    return sample1, sample2


if __name__ == "__main__":
    # From the unshuffled groups, compute the test statistic distribution
    resample_short = np.random.choice(
        group_duration_short, size=500, replace=True)
    resample_long = np.random.choice(
        group_duration_long, size=500, replace=True)
    test_statistic_unshuffled = resample_long - resample_short

    # Shuffle two populations, cut in half, and recompute the test statistic
    shuffled_half1, shuffled_half2 = shuffle_and_split(
        group_duration_short, group_duration_long)
    resample_half1 = np.random.choice(shuffled_half1, size=500, replace=True)
    resample_half2 = np.random.choice(shuffled_half2, size=500, replace=True)
    test_statistic_shuffled = resample_half2 - resample_half1

    # Plot both the unshuffled and shuffled results and compare
    fig = plot_test_statistic(test_statistic_unshuffled, label='Unshuffled')
    fig = plot_test_statistic(test_statistic_shuffled, label='Shuffled')
