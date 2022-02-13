#! /usr/bin/python3
"""
"""
import pandas as pd
import os

data_path = "../data/raw"

ridership = pd.read_csv(os.path.join(data_path, "ridership.csv"))
cal = pd.read_csv(os.path.join(data_path, "cal.csv"))
stations = pd.read_csv(os.path.join(data_path, "stations.csv"))


if __name__ == "__main__":
    pass
