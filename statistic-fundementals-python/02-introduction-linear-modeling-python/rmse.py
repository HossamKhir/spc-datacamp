#! /usr/bin/python3
"""
:file: rmse.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt


def model_fit_and_predict(x, y):
    a0 = 150
    a1 = 25
    ym = a0 + (a1*x)
    return ym


x_data = np.array([0., 0.5, 1., 1.5, 2., 2.5, 3., 3.5, 4.,
                   4.5, 5., 5.5, 6., 6.5, 7., 7.5, 8., 8.5, 9., 9.5, 10.])
y_data = np.array([161.78587909, 132.72560763, 210.81767421, 179.6837026, 181.98528167, 234.67907351, 246.48971034, 221.58691239,
                   250.3924093, 206.43287615, 303.75089312, 312.29865056, 323.8331032, 261.9686295, 316.64806585, 337.55295912,
                   360.13633529, 369.72729852, 408.0289548, 348.82736117, 394.93384188])

y_model = model_fit_and_predict(x_data, y_data)
if __name__ == "__main__":
    # Build the model and compute the residuals "model - data"
    residuals = y_model - y_data

    # Compute the RSS, MSE, and RMSE and print the results
    RSS = np.sum(np.square(residuals))
    MSE = RSS/len(residuals)
    RMSE = np.sqrt(MSE)
    print('RMSE = {:0.2f}, MSE = {:0.2f}, RSS = {:0.2f}'.format(
        RMSE, MSE, RSS))
