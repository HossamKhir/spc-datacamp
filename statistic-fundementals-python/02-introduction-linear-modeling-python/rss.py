#! /usr/bin/python3
"""
:file: rss.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt


def load_data():
    num_pts = 21
    a0 = 3.0*50
    a1 = 0.5*50
    mu = 0
    sigma = 1
    ae = 0.5*50
    seed = 1234
    np.random.seed(seed)
    xmin = 0
    xmax = 10
    x1 = np.linspace(xmin, xmax, num_pts)
    e1 = np.array([np.random.normal(mu, sigma) for n in range(num_pts)])
    y1 = a0 + (a1*x1) + ae*e1
    return x1, y1


def model(x, a0=150, a1=25):
    """
    Purpose: 
        For a given measured data x, compute the model prediction for y
        The form of the model is y = a0 + a1*x
    Args:
        x (float, np.ndarray): independent variable, e.g. time
        a0 (float): default=150, coefficient for the Zeroth order term in the model, i.e. a0
        a1 (float): default=25, coefficient for the 1st order term in the model, i.e. a1*x
    Returns:
        y (float, np.ndarray): model values predicted for corresponding input x.
    """
    y = a0 + (a1*x)
    return y


if __name__ == "__main__":
    # Load the data
    x_data, y_data = load_data()

    # Model the data with specified values for parameters a0, a1
    y_model = model(x_data, a0=150, a1=25)

    # Compute the RSS value for this parameterization of the model
    rss = np.sum(np.square(y_model - y_data))
    print("RSS = {}".format(rss))
