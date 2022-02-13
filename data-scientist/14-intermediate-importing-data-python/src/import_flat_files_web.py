#! /usr/bin/python3
"""
"""
import numpy as np

# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd
import matplotlib.pyplot as plt

# Assign url of file: url
url = "https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv"

if __name__ == "__main__":
    # Save file locally
    urlretrieve(url, filename="winequality-red.csv")

    # Read file into a DataFrame and print its head
    df = pd.read_csv("winequality-red.csv", sep=";")
    print(df.head())
