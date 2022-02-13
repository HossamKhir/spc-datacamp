#! /usr/bin/python3
"""
:file: minimise_residuals.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from rss import load_data, model

# Complete function to load data, build model, compute RSS, and plot


def plot_data(x, y):
    fig, axis = plt.subplots(figsize=(12, 4))
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
    axis.set_ylabel('Altitude [meters]')
    axis.set_xlabel('Step Distance [km]')
    axis.set_title("Hiking  Trip")
    return fig


def plot_data_with_model(xd, yd, ym, title=""):
    fig = plot_data(xd, yd)
    fig.axes[0].plot(xd, ym, color="red")
    fig.axes[0].set_title(title)
    plt.show()
    return fig


def compute_rss_and_plot_fit(a0, a1):
    xd, yd = load_data()
    ym = model(xd, a0, a1)
    residuals = ym - yd
    rss = np.sum(np.square(residuals))
    summary = "Parameters a0={}, a1={} yield RSS={:0.2f}".format(a0, a1, rss)
    fig = plot_data_with_model(xd, yd, ym, summary)
    return rss, summary


if __name__ == "__main__":
    # Chose model parameter values and pass them into RSS function
    rss, summary = compute_rss_and_plot_fit(a0=150, a1=25)
    print(summary)
