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
        rs = con.execute(
            "SELECT title, name FROM Album JOIN Artist ON Album.artist_id = Artist.artist_id"
        )
        df = pd.DataFrame(rs.fetchall())
        df.columns = rs.keys()

    # Print head of DataFrame df
    print(df.head())
