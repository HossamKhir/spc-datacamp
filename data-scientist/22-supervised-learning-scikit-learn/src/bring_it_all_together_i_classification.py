#! /usr/bin/python3
"""
"""
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report

from centering_scaling_pipeline import X, y

if __name__ == "__main__":
    # Setup the pipeline
    steps = [("scaler", StandardScaler()), ("SVM", SVC())]

    pipeline = Pipeline(steps)

    # Specify the hyperparameter space
    parameters = {"SVM__C": [1, 10, 100], "SVM__gamma": [0.1, 0.01]}

    # Create train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=21
    )

    # Instantiate the GridSearchCV object: cv
    cv = GridSearchCV(pipeline, parameters, cv=3)

    # Fit to the training set
    _ = cv.fit(X_train, y_train)

    # Predict the labels of the test set: y_pred
    y_pred = cv.predict(X_test)

    # Compute and print metrics
    print("Accuracy: {}".format(cv.score(X_test, y_test)))
    print(classification_report(y_test, y_pred))
    print("Tuned Model Parameters: {}".format(cv.best_params_))
