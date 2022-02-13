#! /usr/bin/python3
"""
:file: linear_model_cosmology.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.formula.api import ols

df = pd.DataFrame()

if __name__ == "__main__":
    # Fit the model, based on the form of the formula
    model_fit = ols(formula="velocities ~ distances", data=df).fit()

    # Extract the model parameters and associated "errors" or uncertainties
    a0 = model_fit.params['Intercept']
    a1 = model_fit.params['distances']
    e0 = model_fit.bse['Intercept']
    e1 = model_fit.bse['distances']

    # Print the results
    print(
        'For slope a1={:.02f}, the uncertainty in a1 is {:.02f}'.format(a1, e1))
    print(
        'For intercept a0={:.02f}, the uncertainty in a0 is {:.02f}'.format(a0, e0))
