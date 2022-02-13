#! /usr/bin/python3
"""
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from hello_sql import engine

if __name__ == "__main__":
    # Open engine in context manager
    with engine.connect() as con:
        rs = con.execute("SELECT * FROM Employee ORDER BY birth_date")
        df = pd.DataFrame(rs.fetchall())

        # Set the DataFrame's column names
        df.columns = rs.keys()

    # Print head of DataFrame
    print(df.head())
