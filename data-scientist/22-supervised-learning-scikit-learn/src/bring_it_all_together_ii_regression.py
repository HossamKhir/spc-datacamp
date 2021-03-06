#! /usr/bin/python3
"""
"""
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import ElasticNet
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from centering_scaling_pipeline import X, y

if __name__ == "__main__":
    pass
    # Setup the pipeline steps: steps
    steps = [
        ("imputation", SimpleImputer(missing_values="NaN", strategy="mean")),
        ("scaler", StandardScaler()),
        ("elasticnet", ElasticNet()),
    ]

    # Create the pipeline: pipeline
    pipeline = Pipeline(steps=steps)

    # Specify the hyperparameter space
    parameters = {"elasticnet__l1_ratio": np.linspace(0, 1, 30)}

    # Create train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=42
    )

    # Create the GridSearchCV object: gm_cv
    gm_cv = GridSearchCV(pipeline, parameters, cv=3)

    # Fit to the training set
    gm_cv.fit(X_train, y_train)

    # Compute and print the metrics
    r2 = gm_cv.score(X_test, y_test)
    print("Tuned ElasticNet Alpha: {}".format(gm_cv.best_params_))
    print("Tuned ElasticNet R squared: {}".format(r2))
