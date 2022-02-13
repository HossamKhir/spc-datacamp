#! /usr/bin/python3
"""
:file: linear.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from covariance import pearson_r

illiteracy = fertility = np.array([])

if __name__ == "__main__":
    # Plot the illiteracy rate versus fertility
    _ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')

    # Set the margins and label axes
    plt.margins(.02)
    _ = plt.xlabel('percent illiterate')
    _ = plt.ylabel('fertility')

    # Show the plot
    plt.show()

    # Show the Pearson correlation coefficient
    print(pearson_r(illiteracy, fertility))

    # Perform a linear regression using np.polyfit(): a, b
    a, b = np.polyfit(illiteracy, fertility, 1)

    # Print the results to the screen
    print('slope =', a, 'children per woman / percent illiterate')
    print('intercept =', b, 'children per woman')

    # Make theoretical line to plot
    x = np.array([0, 100])
    y = a * x + b

    # Add regression line to your plot
    _ = plt.plot(x, y)

    # Draw the plot
    plt.show()

    # Specify slopes to consider: a_vals
    a_vals = np.linspace(0, .1, 200)

    # Initialize sum of square of residuals: rss
    rss = np.empty_like(a_vals)

    # Compute sum of square of residuals for each value of a_vals
    for i, a in enumerate(a_vals):
        rss[i] = np.sum((fertility - a*illiteracy - b)**2)

    # Plot the RSS
    plt.plot(rss, a_vals, '-')
    plt.xlabel('slope (children per woman / percent illiterate)')
    plt.ylabel('sum of square of residuals')

    plt.show()
