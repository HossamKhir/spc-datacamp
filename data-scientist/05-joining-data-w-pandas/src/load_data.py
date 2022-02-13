#! /usr/bin/python3
"""
"""
import pandas as pd
import os

data_path = "./data/"


def load_gdp() -> pd.DataFrame:
    """"""
    return pd.read_csv(os.path.join(data_path, "gdp.csv"))


def load_sp500() -> pd.DataFrame:
    """"""
    return pd.read_csv(os.path.join(data_path, "sp500.csv"))


def load_unemployment() -> pd.DataFrame:
    """"""
    return pd.read_csv(os.path.join(data_path, "unemployment.csv"))


def load_inflation() -> pd.DataFrame:
    """"""
    return pd.read_csv(os.path.join(data_path, "inflation.csv"))


def load_pop() -> pd.DataFrame:
    """"""
    return pd.read_csv(os.path.join(data_path, "pop.csv"))


def load_wells() -> pd.DataFrame:
    """"""
    return pd.read_csv(os.path.join(data_path, "wells.csv"))


def load_jpm() -> pd.DataFrame:
    """"""
    return pd.read_csv(os.path.join(data_path, "jpm.csv"))


def load_bac() -> pd.DataFrame:
    """"""
    return pd.read_csv(os.path.join(data_path, "bac.csv"))


def load_recession() -> pd.DataFrame:
    """"""
    return pd.read_csv(os.path.join(data_path, "recession.csv"))


def load_ur_wide() -> pd.DataFrame:
    """"""
    return pd.read_csv(os.path.join(data_path, "ur_wide.csv"))


def load_ten_yr() -> pd.DataFrame:
    """"""
    return pd.read_csv(os.path.join(data_path, "ten_yr.csv"))


def load_dji() -> pd.DataFrame:
    """"""
    return pd.read_csv(os.path.join(data_path, "dji.csv"))


if __name__ == "__main__":
    pass
