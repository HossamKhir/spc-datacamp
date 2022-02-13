#! /usr/bin/python3
"""
"""
# Import necessary modules
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from drop_missing_values import df

X = df.drop(columns=["party"])
y = df["party"]

if __name__ == "__main__":
    pass

    # Setup the pipeline steps: steps
    steps = [
        (
            "imputation",
            SimpleImputer(missing_values="NaN", strategy="most_frequent"),
        ),
        ("SVM", SVC()),
    ]

    # Create the pipeline: pipeline
    pipeline = Pipeline(steps=steps)

    # Create training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Fit the pipeline to the train set
    _ = pipeline.fit(X_train, y_train)

    # Predict the labels of the test set
    y_pred = pipeline.predict(X_test)

    # Compute metrics
    print(classification_report(y_test, y_pred))
