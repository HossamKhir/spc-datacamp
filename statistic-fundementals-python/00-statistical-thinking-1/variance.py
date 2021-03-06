#! /usr/bin/python3
"""
:file: variance.py
:author: Hossam Khair
"""
import numpy as np
from sklearn.datasets import load_iris

data = load_iris()
versicolor_petal_length = data.data[data.target == 1, 2]

if __name__ == "__main__":
    # Array of differences to mean: differences
    differences = versicolor_petal_length - np.mean(versicolor_petal_length)

    # Square the differences: diff_sq
    diff_sq = differences**2

    # Compute the mean square difference: variance_explicit
    variance_explicit = np.mean(diff_sq)

    # Compute the variance using NumPy: variance_np
    variance_np = np.var(versicolor_petal_length)

    # Print the results
    print(variance_explicit, variance_np)

    # Compute the variance: variance
    variance = np.var(versicolor_petal_length)

    # Print the square root of the variance
    print(np.sqrt(variance))

    # Print the standard deviation
    print(np.std(versicolor_petal_length))
