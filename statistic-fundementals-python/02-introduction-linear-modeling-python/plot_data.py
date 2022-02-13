#! /usr/bin/python3
"""
:file: plot_data.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from inter_extra_polation import times, distances

if __name__ == "__main__":
    # Create figure and axis objects using subplots()
    fig, axis = plt.subplots()

    # Plot line using the axis.plot() method
    line = axis.plot(times, distances, linestyle=" ", marker="o", color="red")

    # Use the plt.show() method to display the figure
    plt.show()
