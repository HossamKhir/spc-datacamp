#! /usr/bin/python3
"""
"""
import pandas as pd
import os

data_path = "../data/raw"

taxi_owners = pd.read_csv(os.path.join(data_path, "taxi_owners.csv"))
taxi_veh = pd.read_csv(os.path.join(data_path, "taxi_veh.csv"))

if __name__ == "__main__":
    pass
