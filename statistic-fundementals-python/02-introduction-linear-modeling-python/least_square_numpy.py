#! /usr/bin/python3
"""
:file: least_squares_numpy.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from rss import model
from minimise_residuals import compute_rss_and_plot_fit

x = np.array([0., 0.5, 1., 1.5, 2., 2.5, 3., 3.5, 4., 4.5, 5.,
              5.5, 6., 6.5, 7., 7.5, 8., 8.5, 9., 9.5, 10.])

y = np.array([161.78587909, 132.72560763, 210.81767421, 179.6837026, 181.98528167, 234.67907351, 246.48971034, 221.58691239,
              250.3924093, 206.43287615, 303.75089312, 312.29865056, 323.8331032, 261.9686295, 316.64806585, 337.55295912,
              360.13633529, 369.72729852, 408.0289548, 348.82736117, 394.93384188])

if __name__ == "__main__":
    # prepare the means and deviations of the two variables
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_dev = x - x_mean
    y_dev = y - y_mean

    # Complete least-squares formulae to find the optimal a0, a1
    a1 = np.sum(x_dev * y_dev) / np.sum(np.square(x_dev))
    a0 = y_mean - (a1 * x_mean)

    # Use the those optimal model parameters a0, a1 to build a model
    y_model = model(x, a0=a0, a1=a1)

    # plot to verify that the resulting y_model best fits the data y
    fig, rss = compute_rss_and_plot_fit(a0, a1)
