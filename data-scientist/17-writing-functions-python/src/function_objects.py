#! /usr/bin/python3
"""
:file: function_objects.py

playing around with functions as objects
"""
import pandas as pd


def has_docstring(func):
    """Check to see if the function 
    `func` has a docstring.

    Args:
      func (callable): A function.

    Returns:
      bool
    """
    return func.__doc__ is not None


def load_and_plot_data(filename):
    """Load a data frame and plot each column.

    Args:
        filename (str): Path to a CSV file of data.

    Returns:
        pandas.DataFrame
    """
    df = pd.load_csv(filename, index_col=0)
    df.hist()
    return df


def create_math_function(func_name):
    if func_name == "add":
        def add(a, b):
            return a + b
        return add
    elif func_name == "subtract":
        # Define the subtract() function
        def subtract(a, b):
            return a - b
        return subtract
    else:
        print("I don't know that one")


if __name__ == "__main__":
    ok = has_docstring(load_and_plot_data)

    if not ok:
        print("load_and_plot_data() doesn't have a docstring!")
    else:
        print("load_and_plot_data() looks ok")

    add = create_math_function("add")
    print("5 + 2 = {}".format(add(5, 2)))

    subtract = create_math_function("subtract")
    print("5 - 2 = {}".format(subtract(5, 2)))
