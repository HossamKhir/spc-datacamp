#! /usr/bin/python3
"""
"""
import os
import pandas as pd

data_path = "../data/raw"


def load_df() -> pd.DataFrame:
    """"""
    return pd.read_csv(os.path.join(data_path, "df.csv"))


def load_gapminder() -> pd.DataFrame:
    """"""
    return pd.read_csv(os.path.join(data_path, "gapminder.csv"))


def load_pima_indians() -> pd.DataFrame:
    """"""
    return pd.read_csv(os.path.join(data_path, "pima-indians.csv"))


def load_voting() -> pd.DataFrame:
    """"""
    return pd.read_csv(os.path.join(data_path, "voting.csv"))


if __name__ == "__main__":
    pass
