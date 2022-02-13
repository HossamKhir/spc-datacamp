#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

data_path = "../data/raw"


def load_school() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(data_path, "school.csv"))


def load_college() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(data_path, "college.csv"))


def load_show() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(data_path, "show.csv"))


def load_accidents() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(data_path, "accidents.csv"))


def load_rent() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(data_path, "rent.csv"))


def load_grants() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(data_path, "grants.csv"))


def load_bike() -> pd.DataFrame:
    """"""
    return pd.read_csv(os.path.join(data_path, "bike.csv"))


if __name__ == "__main__":
    pass
