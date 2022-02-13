#! /usr/bin/python3
"""
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from list_sheets_excel import xls

if __name__ == "__main__":
    # Load a sheet into a DataFrame by name: df1
    df1 = xls.parse("2004")

    # Print the head of the DataFrame df1
    print(df1.head())

    # Load a sheet into a DataFrame by index: df2
    df2 = xls.parse(0)

    # Print the head of the DataFrame df2
    print(df2.head())
