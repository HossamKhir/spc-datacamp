#! /usr/bin/python3
"""
"""
import numpy as np

# Import package
import pandas as pd
import matplotlib.pyplot as plt

# Assign url of file: url
url = "http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls"

if __name__ == "__main__":
    # Read in all sheets of Excel file: xls
    xls = pd.read_excel(url, sheet_name=None)

    # Print the sheetnames to the shell
    print(xls.keys())

    # Print the head of the first sheet (using its name, NOT its index)
    print(xls["1700"].head())
