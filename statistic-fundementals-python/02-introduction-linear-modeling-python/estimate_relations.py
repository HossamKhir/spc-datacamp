#! /usr/bin/python3
"""
:file: estimate_relations.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt

# Complete the function to model the efficiency.


def efficiency_model(miles, gallons):
    return np.mean(miles / gallons)


car1 = {
    'gallons': np.array([
        0.03333333, 1.69666667, 3.36, 5.02333333, 6.68666667, 8.35,
        10.01333333, 11.67666667, 13.34, 15.00333333, 16.66666667
    ]),
    'miles': np.array([
        1., 50.9, 100.8, 150.7, 200.6, 250.5, 300.4, 350.3, 400.2, 450.1, 500.
    ])
}

car2 = {
    'gallons': np.array([
        0.02, 1.018, 2.016, 3.014, 4.012, 5.01, 6.008, 7.006, 8.004, 9.002, 10.
    ]),
    'miles': np.array([
        1., 50.9, 100.8, 150.7, 200.6, 250.5, 300.4, 350.3, 400.2, 450.1, 500.
    ])
}

if __name__ == "__main__":
    # Use the function to estimate the efficiency for each car.
    car1['mpg'] = efficiency_model(car1['miles'], car1['gallons'])
    car2['mpg'] = efficiency_model(car2['miles'], car2['gallons'])

    # Finish the logic statement to compare the car efficiencies.
    if car1['mpg'] > car2['mpg']:
        print('car1 is the best')
    elif car1['mpg'] < car2['mpg']:
        print('car2 is the best')
    else:
        print('the cars have the same efficiency')
