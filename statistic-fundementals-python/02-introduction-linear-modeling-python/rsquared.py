#! /usr/bin/python3
"""
:file: rsquared.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from rmse import x_data, y_data, y_model


if __name__ == "__main__":
    # Compute the residuals and the deviations
    residuals = y_model - y_data
    deviations = np.mean(y_data) - y_data

    # Compute the variance of the residuals and deviations
    var_residuals = np.mean(np.square(residuals))
    var_deviations = np.mean(np.square(deviations))

    # Compute r_squared as 1 - the ratio of RSS/Variance
    r_squared = 1 - (var_residuals / var_deviations)
    print('R-squared is {:0.2f}'.format(r_squared))
