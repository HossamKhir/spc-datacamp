#! /usr/bin/python3
"""
:file: model_params.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from model_components import model

# Complete the plotting function definition


def plot_data(x, y):
    """
    Purpose:
        Create a plot of y versus x
    Args:
        x (np.array): array of values for the indepent variable, e.g. times
        y (np.array): array of values for the depedent variable, e.g. distances
    Returns:
        fig (matplotlib.figure): matplotlib figure object
    """
    font_options = {'family': 'Arial', 'size': 16}
    plt.rc('font', **font_options)
    fig, axis = plt.subplots(figsize=(8, 6))
    axis.plot(x, y, color="black", linestyle=" ", marker="o")
    axis.grid(True, which="both")
    axis.axhline(0, color="black")
    axis.axvline(0, color="black")
    axis.set_ylim([-5*50, 15*50])
    axis.set_xlim([-5, 15])
    # axis.xaxis.set_major_locator(MultipleLocator(5.0))
    # axis.xaxis.set_minor_locator(MultipleLocator(1.0))
    # axis.yaxis.set_major_locator(MultipleLocator(5.0*50))
    # axis.yaxis.set_minor_locator(MultipleLocator(1.0*50))
    axis.set_ylabel('Altitude (meters)')
    axis.set_xlabel('Step Distance (km)')
    axis.set_title("Hiking  Trip")
    return fig


def plot_data_with_model(xd, yd, ym):
    fig = plot_data(xd, yd)  # plot measured data
    fig.axes[0].plot(xd, ym, color='red')  # over-plot modeled data
    plt.show()
    return fig


xd = np.array([0., 0.5, 1., 1.5, 2., 2.5, 3., 3.5, 4., 4.5, 5.,
               5.5, 6., 6.5, 7., 7.5, 8., 8.5, 9., 9.5, 10.])
yd = np.array([161.78587909, 132.72560763, 210.81767421, 179.6837026, 181.98528167, 234.67907351, 246.48971034, 221.58691239,
               250.3924093, 206.43287615, 303.75089312, 312.29865056, 323.8331032, 261.9686295, 316.64806585, 337.55295912,
               360.13633529, 369.72729852, 408.0289548, 348.82736117, 394.93384188])

if __name__ == "__main__":
    # Select new model parameters a0, a1, and generate modeled `ym` from them.
    a0 = 150
    a1 = 25
    ym = model(xd, a0, a1)

    # Plot the resulting model to see whether it fits the data
    fig = plot_data_with_model(xd, yd, ym)
