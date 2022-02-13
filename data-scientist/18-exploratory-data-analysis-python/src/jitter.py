#! /usr/bin/python3
"""
"""
import numpy as np
import matplotlib.pyplot as plt
from load_data import load_brfss

brfss = load_brfss()

if __name__ == "__main__":
    # Select the first 1000 respondents
    brfss = brfss[:1000]

    # Add jittering to age
    age = brfss["AGE"] + np.random.normal(0, 2.5, size=brfss.shape[0])
    # Extract weight
    weight = brfss["WTKG3"]

    # Make a scatter plot
    plt.plot(age, weight, "o", alpha=0.2, ms=5)

    plt.xlabel("Age in years")
    plt.ylabel("Weight in kg")
    plt.show()
