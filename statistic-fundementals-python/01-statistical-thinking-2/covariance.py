#! /usr/bin/python3
"""
:file: covariance.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

versicolor_petal_width, versicolor_petal_length = iris.data[iris.target == 1, 1:3]


def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x, y)

    # Return entry [0,1]
    return corr_mat[0, 1]


if __name__ == "__main__":
    # Make a scatter plot
    plt.plot(versicolor_petal_length, versicolor_petal_width,
             marker='.', linestyle="none")

    # Label the axes
    plt.xlabel("petal length (cm)")
    plt.ylabel("petal width (cm)")

    # Show the result
    plt.show()

    # Compute the covariance matrix: covariance_matrix
    covariance_matrix = np.cov(versicolor_petal_length, versicolor_petal_width)

    # Print covariance matrix
    print(covariance_matrix)

    # Extract covariance of length and width of petals: petal_cov
    petal_cov = covariance_matrix[0, 1]

    # Print the length/width covariance
    print(petal_cov)

    # Compute Pearson correlation coefficient for I. versicolor: r
    r = pearson_r(versicolor_petal_length, versicolor_petal_width)

    # Print the result
    print(r)
