#! /usr/bin/python3
"""
:file: covariance_correlation.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from mean_deviation_std import x, y


def plot_normalized_deviations(*args, **kwargs):
    """
    """
    return None


if __name__ == "__main__":
    # Compute the covariance from the deviations.
    dx = x - np.mean(x)
    dy = y - np.mean(y)
    covariance = np.mean(dx * dy)
    print("Covariance: ", covariance)

    # Compute the correlation from the normalized deviations.
    zx = dx / np.std(x)
    zy = dy / np.std(y)
    correlation = np.mean(zx * zy)
    print("Correlation: ", correlation)

    # Plot the normalized deviations for visual inspection.
    fig = plot_normalized_deviations(zx, zy)
