#! /usr/bin/python3
"""
"""
import numpy as np

# Import packages
from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

# Create engine: engine
engine = create_engine("postgresql:///chinook")

if __name__ == "__main__":
    # Open engine connection: con
    con = engine.connect()

    # Perform query: rs
    rs = con.execute("SELECT * FROM Album")

    # Save results of the query to DataFrame: df
    df = pd.DataFrame(rs.fetchall())

    # Close connection
    con.close()

    # Print head of DataFrame df
    print(df.head())
