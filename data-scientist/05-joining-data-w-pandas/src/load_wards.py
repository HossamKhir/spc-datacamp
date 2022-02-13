#! /usr/bin/python3
"""
"""
import pandas as pd
import os

data_path = "../data/raw"

wards = pd.read_csv(os.path.join(data_path, "wards.csv"))
census = pd.read_csv(os.path.join(data_path, "census.csv"))
wards_altered = pd.read_csv(os.path.join(data_path, "wards_altered.csv"))
census_altered = pd.read_csv(os.path.join(data_path, "census_altered.csv"))
zip_demo = pd.read_csv(os.path.join(data_path, "zip_demo.csv"))
land_use = pd.read_csv(os.path.join(data_path, "land_use.csv"))

if __name__ == "__main__":
    pass
