#! /usr/bin/python3
"""
:file: linear_proportionality.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt

# Complete the function to convert C to F


def convert_scale(temps_C):
    (freeze_C, boil_C) = (0, 100)
    (freeze_F, boil_F) = (32, 212)
    change_in_C = boil_C - freeze_C
    change_in_F = boil_F - freeze_F
    slope = change_in_F / change_in_C
    intercept = freeze_F - freeze_C
    temps_F = intercept + (slope * temps_C)
    return temps_F


def plot_temperatures(temps_C, temps_F):
    """
    """
    font_options = {'family': 'Arial', 'size': 16}
    plt.rc('font', **font_options)
    fig, axis = plt.subplots(figsize=(16, 4))
    axis.plot(temps_C, temps_F)
    axis.set_xlabel("Temperature (Celsius)")
    axis.set_ylabel("Temperature (Fahrenheit)")
    axis.grid()
    plt.show()
    return fig


if __name__ == "__main__":
    # Use the convert function to compute values of F and plot them
    temps_C = np.linspace(0, 100, 101)
    temps_F = convert_scale(temps_C)
    fig = plot_temperatures(temps_C, temps_F)
