#! /usr/bin/python3
"""
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from hello_sql import engine

if __name__ == "__main__":
    # Open engine in context manager
    # Perform query and save results to DataFrame: df
    with engine.connect() as con:
        rs = con.execute("SELECT last_name, title FROM Employee")
        df = pd.DataFrame(rs.fetchmany(size=3))
        df.columns = rs.keys()

    # Print the length of the DataFrame df
    print(len(df))

    # Print the head of the DataFrame df
    print(df.head())
