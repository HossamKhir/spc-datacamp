#! /usr/bin/python3
"""
"""
import os
import pandas as pd

data_path = "./data/"


def load_restaurants() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(data_path, "restaurants.csv"))


def load_restaurants_new() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(data_path, "restaurants_new.csv"))


def load_airlines() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(data_path, "airlines.csv"))


def load_airlines_full_name() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(data_path, "airlines_full_name.csv"))


def load_airlines_survey_response() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(data_path, "airlines_survey_response.csv"))


def load_airlines_full_name() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(data_path, "airlines_full_name.csv"))


def load_banking() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(data_path, "banking.csv"))


def load_categories() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(data_path, "categories.csv"))


def load_ride_share() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(data_path, "ride_share.csv"))


def load_ride_share_minimal() -> pd.DataFrame:
    """ """
    return pd.read_csv(os.path.join(data_path, "ride_share_minimal.csv"))


if __name__ == "__main__":
    pass
