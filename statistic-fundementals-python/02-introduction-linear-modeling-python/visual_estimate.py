#! /usr/bin/python3
"""
:file: visual_estimate.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt


def model(a0=0, a1=1):
    """
    """
    xm = np.linspace(-5, 15, 41)
    ym = a0 + (a1*xm)
    return xm, ym


def plot_data_and_model(xd, yd, xm, ym):
    """
    """
    fig, axis = plt.subplots()
    axis.plot(xd, yd, color="black", linestyle=" ",
              marker="o", label="Measured")
    axis.plot(xm, ym, color="red", linestyle="-", marker=None, label="Modeled")
    axis.axvline(0, color="black")
    axis.axhline(0, color="black")
    # axis.xaxis.set_major_locator(MultipleLocator(5.0))
    # axis.xaxis.set_minor_locator(MultipleLocator(1.0))
    # axis.yaxis.set_major_locator(MultipleLocator(5.0))
    # axis.yaxis.set_minor_locator(MultipleLocator(1.0))
    axis.set_xlim([-11, 11])
    axis.set_ylim([-11, 11])
    axis.grid(True, which="both")
    axis.legend(loc=2)
    return fig


xd = np.array([2., 2.5, 3., 3.5, 4., 4.5, 5., 5.5, 6., 6.5, 7.])
yd = np.array([4.24835708, 4.43086785, 5.32384427, 6.26151493, 5.88292331,
               6.38293152, 7.78960641, 7.88371736, 7.76526281, 8.77128002, 8.76829115])

if __name__ == "__main__":
    # Look at the plot data and guess initial trial values
    trial_slope = 1.125
    trial_intercept = 1.5

    # input thoses guesses into the model function to compute the model values.
    xm, ym = model(trial_intercept, trial_slope)

    # Compare your your model to the data with the plot function
    fig = plot_data_and_model(xd, yd, xm, ym)
    plt.show()

    # Repeat the steps above until your slope and intercept guess makes the model line up with the data.
    final_slope = trial_slope
    final_intercept = trial_intercept
