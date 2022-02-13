#! /usr/bin/python3
"""
:file: visualising_variation_statistic.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from sample_statistic import population


def get_sample_statistics(population, num_samples=100, num_pts=1000):
    means = np.zeros(num_samples)
    deviations = np.zeros(num_samples)
    for ns in range(num_samples):
        sample = np.random.choice(population, num_pts)
        means[ns] = sample.mean()
        deviations[ns] = sample.std()
    return means, deviations


def plot_hist(data, bins, data_name, color='blue'):
    font_options = {'family': 'Arial', 'size': 16}
    plt.rc('font', **font_options)
    fig, axis = plt.subplots(figsize=(8, 4))
    axis.hist(data, bins=bins, rwidth=0.9, color=color)
    title = 'Distribution of the {}: \ncenter={:0.2f}, spead={:0.2f}'.format(
        data_name, data.mean(), data.std())
    x_label = 'Values of {}'.format(data_name)
    y_label = 'Bin counts of {}'.format(data_name)
    axis.set_ylabel(y_label)
    axis.set_xlabel(x_label)
    axis.set_title(title)
    plt.show()
    return fig


if __name__ == "__main__":
    # Generate sample distribution and associated statistics
    means, stdevs = get_sample_statistics(
        population, num_samples=100, num_pts=1000)

    # Define the binning for the histograms
    mean_bins = np.linspace(97.5, 102.5, 51)
    std_bins = np.linspace(7.5, 12.5, 51)

    # Plot the distribution of means, and the distribution of stdevs
    fig = plot_hist(data=means, bins=mean_bins,
                    data_name="Means", color='green')
    fig = plot_hist(data=stdevs, bins=std_bins,
                    data_name="Stdevs", color='red')
