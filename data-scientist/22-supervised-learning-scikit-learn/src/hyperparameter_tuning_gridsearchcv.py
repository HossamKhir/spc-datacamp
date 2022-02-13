#! /usr/bin/python3
"""
"""
import pandas as pd
import numpy as np

# Import necessary modules
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

from build_log_regress_model import X, y


if __name__ == "__main__":
    # Setup the hyperparameter grid
    c_space = np.logspace(-5, 8, 15)
    param_grid = {"C": c_space}

    # Instantiate a logistic regression classifier: logreg
    logreg = LogisticRegression()

    # Instantiate the GridSearchCV object: logreg_cv
    logreg_cv = GridSearchCV(logreg, param_grid, cv=5)

    # Fit it to the data
    _ = logreg_cv.fit(X, y)

    # Print the tuned parameters and score
    print("Tuned Logistic Regression Parameters: {}".format(logreg_cv.best_params_))
    print("Best score is {}".format(logreg_cv.best_score_))
