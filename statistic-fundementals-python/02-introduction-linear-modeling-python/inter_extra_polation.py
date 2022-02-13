#! /usr/bin/python3
"""
:file: inter_extra_polation.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt


def model(time):
    """
    """
    return 50 * time


times = np.array([0.,  1.,  2.,  3.,  4.,  5.,  6.])
distances = np.array([0., 44.04512153, 107.16353484,
                      148.43674052, 196.39705633, 254.4358147, 300.])
if __name__ == "__main__":
    # interpolation
    # Compute the total change in distance and change in time
    total_distance = distances[-1] - distances[0]
    total_time = times[-1] - times[0]

    # Estimate the slope of the data from the ratio of the changes
    average_speed = total_distance / total_time

    # Predict the distance traveled for a time not measured
    elapse_time = 2.5
    distance_traveled = average_speed * elapse_time
    print("The distance traveled is {}".format(distance_traveled))

    # extrapolation
    # Select a time not measured.
    time = 8

    # Use the model to compute a predicted distance for that time.
    distance = model(time)

    # Inspect the value of the predicted distance traveled.
    print(distance)

    # Determine if you will make it without refuelling.
    answer = (distance <= 400)
    print(answer)
