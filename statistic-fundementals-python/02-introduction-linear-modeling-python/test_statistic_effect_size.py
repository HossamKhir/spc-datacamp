#! /usr/bin/python3
"""
:file: test_statistic_effect_size.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from estimate_population_params import sample_distances


def plot_test_statistic(test_statistic):
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
    bin_edges = np.linspace(t_min, t_max, 21)
    data_opts = dict(rwidth=0.8, color='blue', alpha=0.5)
    fig, axis = plt.subplots(figsize=(12, 4))
    plt.hist(test_statistic, bins=bin_edges, **data_opts)
    axis.grid()
    axis.set_ylabel("Bin Counts")
    axis.set_xlabel("Distance Differences, late - early")
    title_form = "Test Statistic Distribution, \nMean = {:0.2f}, Std Error = {:0.2f}"
    axis.set_title(title_form.format(t_mean, t_std))
    plt.show()
    return fig


sample_times = np.linspace(0, 10, 1000)

group_duration_short = sample_distances[sample_times < 5]
group_duration_long = sample_distances[sample_times > 5]
if __name__ == "__main__":
    # Create two poulations, sample_distances for early and late sample_times.
    # Then resample with replacement, taking 500 random draws from each population.
    resample_short = np.random.choice(
        group_duration_short, size=500, replace=True)
    resample_long = np.random.choice(
        group_duration_long, size=500, replace=True)

    # Difference the resamples to compute a test statistic distribution, then compute its mean and stdev
    test_statistic = resample_long - resample_short
    effect_size = np.mean(test_statistic)
    standard_error = np.std(test_statistic)

    # Print and plot the results
    print('Test Statistic: mean={:0.2f}, stdev={:0.2f}'.format(
        effect_size, standard_error))
    fig = plot_test_statistic(test_statistic)
