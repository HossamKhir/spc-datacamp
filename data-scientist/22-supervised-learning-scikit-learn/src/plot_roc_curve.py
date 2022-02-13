#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt

from build_log_regress_model import logreg, y_test, X_test


if __name__ == "__main__":
    # Import necessary modules
    from sklearn.metrics import roc_curve

    # Compute predicted probabilities: y_pred_prob
    y_pred_prob = logreg.predict_proba(X_test)[:, 1]

    # Generate ROC curve values: fpr, tpr, thresholds
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

    # Plot ROC curve
    plt.plot([0, 1], [0, 1], "k--")
    plt.plot(fpr, tpr)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.show()
