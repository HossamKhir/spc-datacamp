#! /usr/bin/python3
"""
"""
# Import the Imputer module
from sklearn.impute import SimpleImputer
from sklearn.svm import SVC

if __name__ == "__main__":
    # Setup the Imputation transformer: imp
    imp = SimpleImputer(missing_values="NaN", strategy="most_frequent")

    # Instantiate the SVC classifier: clf
    clf = SVC()

    # Setup the pipeline with the required steps: steps
    steps = [("imputation", imp), ("SVM", clf)]
