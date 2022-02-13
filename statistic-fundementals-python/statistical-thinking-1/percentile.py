#! /usr/bin/python3
"""
:file: percentile.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from ecdf import ecdf

data = load_iris()
versicolor_petal_length = data.data[data.target == 1, 2]
x_vers, y_vers = ecdf(versicolor_petal_length)

if __name__ == "__main__":
    # Specify array of percentiles: percentiles
    percentiles = np.array([2.5, 25, 50, 75, 97.5])

    # Compute percentiles: ptiles_vers
    ptiles_vers = np.percentile(versicolor_petal_length, percentiles)

    # Print the result
    print(ptiles_vers)

    # Plot the ECDF
    _ = plt.plot(x_vers, y_vers, '.')
    _ = plt.xlabel('petal length (cm)')
    _ = plt.ylabel('ECDF')

    # Overlay percentiles as red diamonds.
    _ = plt.plot(ptiles_vers, percentiles/100, marker='D', color='red',
                 linestyle="none")

    # Show the plot
    plt.show()
