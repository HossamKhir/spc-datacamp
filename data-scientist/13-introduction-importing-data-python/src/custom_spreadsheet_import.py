#! /usr/bin/python3
"""
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from list_sheets_excel import xls

if __name__ == "__main__":
    # Parse the first sheet and rename the columns: df1
    df1 = xls.parse(0, skiprows=[0], names=["Country", "AAM due to War (2002)"])

    # Print the head of the DataFrame df1
    print(df1.head())

    # Parse the first column of the second sheet and rename the column: df2
    df2 = xls.parse(1, usecols=[0], skiprows=[1], names=["Country"])

    # Print the head of the DataFrame df2
    print(df2.head())
