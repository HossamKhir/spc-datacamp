#! /usr/bin/python3
"""
"""
import numpy as np

# Import scale
from sklearn.preprocessing import scale

from drop_missing_values import df

X = df.dropna().drop(columns=["party"]).astype(np.float64)

if __name__ == "__main__":
    # Scale the features: X_scaled
    X_scaled = scale(X)

    # print(X_scaled)

    # Print the mean and standard deviation of the unscaled features
    print("Mean of Unscaled Features: {}".format(np.mean(X)))
    print("Standard Deviation of Unscaled Features: {}".format(np.std(X)))

    # Print the mean and standard deviation of the scaled features
    print("Mean of Scaled Features: {}".format(np.mean(X_scaled)))
    print("Standard Deviation of Scaled Features: {}".format(np.std(X_scaled)))
