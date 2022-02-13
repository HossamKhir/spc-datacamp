#! /usr/bin/python3
"""
:file: least_squares_statsmodels.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.formula.api import ols
from rss import load_data
from minimise_residuals import compute_rss_and_plot_fit, plot_data_with_model

x_data, y_data = load_data()
df = pd.DataFrame(dict(x_column=x_data, y_column=y_data))

if __name__ == "__main__":
    # Pass data and `formula` into ols(), use and `.fit()` the model to the data
    model_fit = ols(formula="y_column ~ x_column", data=df).fit()

    # Use .predict(df) to get y_model values, then over-plot y_data with y_model
    y_model = model_fit.predict(df)
    fig = plot_data_with_model(x_data, y_data, y_model)

    # Extract the a0, a1 values from model_fit.params
    a0 = model_fit.params['Intercept']
    a1 = model_fit.params['x_column']

    # Visually verify that these parameters a0, a1 give the minimum RSS
    fig, rss = compute_rss_and_plot_fit(a0, a1)
