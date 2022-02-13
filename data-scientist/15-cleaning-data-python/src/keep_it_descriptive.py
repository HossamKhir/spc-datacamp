#! /usr/bin/python3
"""
"""
import pandas as pd

airlines = pd.read_csv("../data/raw/airlines_survey_response.csv")

if __name__ == "__main__":
    # Store length of each row in survey_response column
    resp_length = airlines["survey_response"].str.len()

    # Find rows in airlines where resp_length > 40
    airlines_survey = airlines[resp_length > 40]

    # Assert minimum survey_response length is > 40
    assert airlines_survey["survey_response"].str.len().min() > 40

    # Print new survey_response column
    print(airlines_survey["survey_response"])
