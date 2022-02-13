#! /usr/bin/python3
"""
:file:
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt

x = y = np.array([])

if __name__ == "__main__":
    # Perform linear regression: a, b
    a, b = np.polyfit(x, y, 1)

    # Print the slope and intercept
    print(a, b)

    # Generate theoretical x and y data: x_theor, y_theor
    x_theor = np.array([3, 15])
    y_theor = a * x + b

    # Plot the Anscombe data and theoretical line
    _ = plt.plot(x, y, marker='.', linestyle="none")
    _ = plt.plot(x_theor, y_theor)

    # Label the axes
    plt.xlabel('x')
    plt.ylabel('y')

    # Show the plot
    plt.show()

    anscombe_x, anscombe_y = x, y

    # Iterate through x,y pairs
    for x, y in zip(anscombe_x, anscombe_y):
        # Compute the slope and intercept: a, b
        a, b = np.polyfit(x, y, 1)

        # Print the result
        print('slope:', a, 'intercept:', b)
