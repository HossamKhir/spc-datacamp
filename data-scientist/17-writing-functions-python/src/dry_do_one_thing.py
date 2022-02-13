#! /usr/bin/python3
"""
:file: dry_do_one_thing.py

implementing DRY (Don't Repeat Yourself) and Do One Thing principles
"""

import pandas as pd


def standardize(column):
    """Standardize the values in a column.

    Args:
      column (pandas Series): The data to standardize.

    Returns:
      pandas Series: the values as z-scores
    """
    # Finish the function so that it returns the z-scores
    z_score = (column - column.mean()) / column.std()
    return z_score


def mean(values):
    """Get the mean of a list of values

    Args:
      values (iterable of float): A list of numbers

    Returns:
      float
    """
    # Write the mean() function
    mean = sum(values) / len(values)
    return mean


def median(values):
    """Get the median of a list of values

    Args:
      values (iterable of float): A list of numbers

    Returns:
      float
    """
    # Write the median() function
    midpoint = len(values)//2
    if not len(values) % 2:
        median = (values[midpoint - 1] + values[midpoint]) / 2
    else:
        median = values[midpoint]
    return median


if __name__ == "__main__":
    df = pd.DataFrame({
        "y1_gpa": [2.785877, 1.144557, 0.907406, 2.205259, 2.877876, ],
        "y2_gpa": [2.052513, 2.666498, 0.423634, 0.523580, 1.287922, ],
        "y3_gpa": [2.170544, 0.267098, 2.613459, 3.984345, 3.077589, ],
        "y4_gpa": [0.065570, 2.884737, 0.030950, 0.339289, 0.901994, ]
    })
    # Use the standardize() function to calculate the z-scores
    df['y1_z'] = standardize(df.y1_gpa)
    df['y2_z'] = standardize(df.y2_gpa)
    df['y3_z'] = standardize(df.y3_gpa)
    df['y4_z'] = standardize(df.y4_gpa)
