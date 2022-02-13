#! /usr/bin/python3
"""
:file: calculate_pi.py
:author: Hossam Khair
"""
import numpy as np

if __name__ == "__main__":
    pass
    # Initialize sims and circle_points
    sims, circle_points = 10**4, 0

    for i in range(sims):
        # Generate the two coordinates of a point
        point = np.random.uniform(-1, 1, size=2)
        # if the point lies within the unit circle, increment counter
        within_circle = point[0]**2 + point[1]**2 <= 1
        if within_circle == True:
            circle_points += 1

    # Estimate pi as 4 times the avg number of points in the circle.
    pi_sim = 4 * (circle_points) / sims
    print("Simulated value of pi = {}".format(pi_sim))
