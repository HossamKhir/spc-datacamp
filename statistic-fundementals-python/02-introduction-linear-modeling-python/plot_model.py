#! /usr/bin/python3
"""
:file: plot_model.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from inter_extra_polation import times, distances


def model(x, y, a0=0, a1=1):
    """
    """
    return a0 + a1 * x


measured_distances = distances / 50

if __name__ == "__main__":
    # Pass times and measured distances into model
    model_distances = model(times, measured_distances)

    # Create figure and axis objects and call axis.plot() twice to plot data and model distances versus times
    fig, axis = plt.subplots()
    axis.plot(times, measured_distances, linestyle=" ",
              marker="o", color="black", label="Measured")
    axis.plot(times, model_distances, linestyle="-",
              marker=None, color="red", label="Modeled")

    # Add grid lines and a legend to your plot, and then show to display
    axis.grid(True)
    axis.legend(loc="best")
    plt.show()
