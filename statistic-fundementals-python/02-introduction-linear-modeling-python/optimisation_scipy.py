#! /usr/bin/python3
"""
:file: optimisation_scipy.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as optimise
from rss import load_data
from minimise_residuals import compute_rss_and_plot_fit
# Define a model function needed as input to scipy


def model_func(x, a0, a1):
    return a0 + (a1*x)


# Load the measured data you want to model
x_data, y_data = load_data()

if __name__ == "__main__":
    # call curve_fit, passing in the model function and data; then unpack the results
    param_opt, param_cov = optimise.curve_fit(model_func, x_data, y_data)
    a0 = param_opt[0]  # a0 is the intercept in y = a0 + a1*x
    a1 = param_opt[1]  # a1 is the slope     in y = a0 + a1*x

    # test that these parameters result in a model that fits the data
    fig, rss = compute_rss_and_plot_fit(a0, a1)
