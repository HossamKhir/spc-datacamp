#! /usr/bin/python3
"""
"""
import os
import pandas as pd

DATA_PATH = "../data/raw"


def load_nsfg() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(DATA_PATH, "nsfg.csv"))


def load_gss() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(DATA_PATH, "gss.csv"))


def load_brfss() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(DATA_PATH, "brfss.csv"))


if __name__ == "__main__":
    pass
