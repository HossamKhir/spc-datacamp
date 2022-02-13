#! /usr/bin/python3
"""
"""
import pandas as pd

# Import necessary modules
from scipy.stats import randint
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import RandomizedSearchCV

from build_log_regress_model import X, y

if __name__ == "__main__":
    # Setup the parameters and distributions to sample from: param_dist
    param_dist = {
        "max_depth": [3, None],
        "max_features": randint(1, 9),
        "min_samples_leaf": randint(1, 9),
        "criterion": ["gini", "entropy"],
    }

    # Instantiate a Decision Tree classifier: tree
    tree = DecisionTreeClassifier()

    # Instantiate the RandomizedSearchCV object: tree_cv
    tree_cv = RandomizedSearchCV(tree, param_dist, cv=5)

    # Fit it to the data
    _ = tree_cv.fit(X, y)

    # Print the tuned parameters and score
    print("Tuned Decision Tree Parameters: {}".format(tree_cv.best_params_))
    print("Best score is {}".format(tree_cv.best_score_))
