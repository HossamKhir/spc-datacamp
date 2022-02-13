#! /usr/bin/python3
"""
"""
import pandas as pd
import numpy as np

# Import necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

from train_test_split_regression import X, y

if __name__ == "__main__":
    # Create a linear regression object: reg
    reg = LinearRegression()

    # Perform 3-fold CV
    cvscores_3 = cross_val_score(reg, X, y, cv=3)
    print(np.mean(cvscores_3))

    # Perform 10-fold CV
    cvscores_10 = cross_val_score(reg, X, y, cv=10)
    print(np.mean(cvscores_10))
