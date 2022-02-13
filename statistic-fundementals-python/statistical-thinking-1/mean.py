#! /usr/bin/python3
"""
:file: mean.py
:author: Hossam Khair
"""
import numpy as np
from sklearn.datasets import load_iris

data = load_iris()
versicolor_petal_length = data.data[data.target == 1, 2]


if __name__ == "__main__":
    # Compute the mean: mean_length_vers
    mean_length_vers = np.mean(versicolor_petal_length)

    # Print the result with some nice formatting
    print('I. versicolor:', mean_length_vers, 'cm')
