#! /usr/bin/python3
"""
:file: model_components.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt

# Define the general model as a function


def model(x, a0=3, a1=2, a2=0):
    return a0 + (a1*x) + (a2*x*x)


def plot_prediction(x, y):
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
    fig, axis = plt.subplots()
    axis.plot(x, y, color="red", linestyle="-", marker="o")
    axis.grid(True, which="both")
    axis.axhline(0, color="black")
    axis.axvline(0, color="black")
    # axis.xaxis.set_major_locator(MultipleLocator(5.0))
    # axis.xaxis.set_minor_locator(MultipleLocator(1.0))
    # axis.yaxis.set_major_locator(MultipleLocator(5.0))
    # axis.yaxis.set_minor_locator(MultipleLocator(1.0))
    axis.set_ylabel('Y')
    axis.set_xlabel('X')
    axis.set_title("Plot of modeled Y for given X")
    plt.show()
    return fig


if __name__ == "__main__":
    # Generate array x, then predict y values for specific, non-default a0 and a1
    x = np.linspace(-10, 10, 21)
    y = model(x)

    # Plot the results, y versus x
    fig = plot_prediction(x, y)
