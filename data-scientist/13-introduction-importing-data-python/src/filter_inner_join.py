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
        "SELECT * FROM Playlist_Track INNER JOIN Track ON Playlist_Track.track_id = Track.track_id WHERE milliseconds < 250000",
        engine,
    )

    # Print head of DataFrame
    print(df.head())
