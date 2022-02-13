#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from load_data import load_brfss

brfss = load_brfss()

if __name__ == "__main__":
    # Select the first 1000 respondents
    brfss = brfss[:1000]

    # Extract age and weight
    age = brfss["AGE"]
    weight = brfss["WTKG3"]

    # Make a scatter plot
    plt.plot(age, weight, "o", alpha=0.1)

    plt.xlabel("Age in years")
    plt.ylabel("Weight in kg")

    plt.show()
