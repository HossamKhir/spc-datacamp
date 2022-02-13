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
        rs = con.execute("SELECT * FROM Employee WHERE employee_id >= 6")
        df = pd.DataFrame(rs.fetchall())
        df.columns = rs.keys()

    # Print the head of the DataFrame df
    print(df.head())
