#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from load_data import load_gapminder

# Import LinearRegression
from sklearn.linear_model import LinearRegression


df = load_gapminder()
y = df["life"].values
X_fertility = df["fertility"].values

if __name__ == "__main__":
    # Create the regressor: reg
    reg = LinearRegression()

    # Create the prediction space
    prediction_space = np.linspace(min(X_fertility), max(X_fertility)).reshape(-1, 1)

    # Fit the model to the data
    reg.fit(X_fertility, y)

    # Compute predictions over the prediction space: y_pred
    y_pred = reg.predict(prediction_space)

    # Print R^2
    print(reg.score(X_fertility, y))

    # Plot regression line
    plt.plot(prediction_space, y_pred, color="black", linewidth=3)
    plt.show()
