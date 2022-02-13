#! /usr/bin/python3
"""
:file: linear_model_anthropology.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

legs = np.array([35., 36.5, 38., 39.5, 41., 42.5, 44., 45.5, 47.,
                 48.5, 50., 51.5, 53., 54.5, 56., 57.5, 59., 60.5, 62., 63.5, 65.])

heights = np.array([145.75166215, 154.81989548, 147.45149903, 154.53270424, 166.17450311, 171.45325818, 149.44608871, 164.73275841,
                    168.82025028, 171.32607675, 182.07638078, 188.37513159, 188.08738789, 196.95181717, 192.85162151, 201.60765816,
                    210.66135402, 202.06143758, 215.72224422, 207.04958807, 215.8394592])

if __name__ == "__main__":
    model = LinearRegression(fit_intercept=False)

    # Prepare the measured data arrays and fit the model to them
    legs = legs.reshape(len(legs), 1)
    heights = heights.reshape(len(heights), 1)
    model.fit(legs, heights)

    # Use the fitted model to make a prediction for the found femur
    fossil_leg = 50.7
    fossil_height = model.predict(fossil_leg)
    print("Predicted fossil height = {:0.2f} cm".format(fossil_height[0, 0]))
