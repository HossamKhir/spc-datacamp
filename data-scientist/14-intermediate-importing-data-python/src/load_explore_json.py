#! /usr/bin/python3
"""
"""
import os
import json

DATA_PATH = "../data/raw"

if __name__ == "__main__":
    # Load JSON: json_data
    with open(os.path.join(DATA_PATH, "a_movie.json")) as json_file:
        json_data = json.load(json_file)

    # Print each key-value pair in json_data
    for k in json_data.keys():
        print(k + ": ", json_data[k])
