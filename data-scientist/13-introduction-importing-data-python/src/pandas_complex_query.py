#! /usr/bin/python3
"""
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from hello_sql import engine

if __name__ == "__main__":
    # Execute query and store records in DataFrame: df
    df = pd.read_sql_query(
        "SELECT * FROM Employee WHERE employee_id >= 6 ORDER BY birth_date", engine
    )

    # Print head of DataFrame
    print(df.head())
