#! /usr/bin/python3
"""
"""
import pandas as pd
import os

data_path = "../data/raw"

biz_owners = pd.read_csv(os.path.join(data_path, "biz_owners.csv"))
licenses = pd.read_csv(os.path.join(data_path, "licenses.csv"))

if __name__ == "__main__":
    pass
