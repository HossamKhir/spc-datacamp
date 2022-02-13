#! /usr/bin/python3
"""
:file: visualising_rss_minima.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from rss import model, load_data

a1_array = np.linspace(15, 35, 101)
rss_list = []

x_data, y_data = load_data()


def compute_rss(yd, ym):
    rss = np.sum(np.square(yd-ym))
    return rss


def plot_rss_vs_a1(a1_array, rss_array):
    """
    Purpose:
        Plot RSS values (y-axis) versus a1 parameters values (x-axis)
         Also plot a point where the minimum RSS value occurs, and the 
         corresponding a1 value whose model resulted in that minimum RSS.
    Args:
        a1_array (np.array): an array of trial values for a1 (model slope)
        rss_array (np.array): an array of computed RSS values resulting from the a1_array
    Returns:
        fig (matplotlib.figure): figure object on which the data is plotted
    """
    font_options = {'family': 'Arial', 'size': 16}
    plt.rc('font', **font_options)
    fig, axis = plt.subplots(figsize=(12, 4))
    min_rss = np.min(rss_array)
    best_slope = a1_array[np.where(rss_array == min_rss)]
    axis.plot(a1_array, rss_array, marker="o", color='black')
    axis.plot(best_slope, min_rss, marker="o",
              markersize=12, linestyle=" ", color='red')
    # axis.xaxis.set_major_locator(MultipleLocator(5.0))
    # axis.xaxis.set_minor_locator(MultipleLocator(1.0))
    axis.grid(True, which="major")
    axis.set_ylabel("RSS")
    axis.set_xlabel("Slope $a_1$")
    axis.set_ylim([0, 100000])
    axis.set_title("Minimum RSS = {:.02f} \n came from $a_1$={}".format(
        min_rss, best_slope[0]))
    plt.show()
    return fig


if __name__ == "__main__":
    # Loop over all trial values in a1_array, computing rss for each
    for a1_trial in a1_array:
        y_model = model(x_data, a0=150, a1=a1_trial)
        rss_value = compute_rss(y_data, y_model)
        rss_list.append(rss_value)

    # Find the minimum RSS and the a1 value from whence it came
    rss_array = np.array(rss_list)
    best_rss = np.min(rss_array)
    best_a1 = a1_array[np.where(rss_array == best_rss)]
    print('The minimum RSS = {}, came from a1 = {}'.format(best_rss, best_a1))

    # Plot your rss and a1 values to confirm answer
    fig = plot_rss_vs_a1(a1_array, rss_array)
