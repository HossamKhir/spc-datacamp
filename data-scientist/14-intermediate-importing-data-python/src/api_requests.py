#! /usr/bin/python3
"""
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import requests package
import requests

# Assign URL to variable: url
url = "http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network"

if __name__ == "__main__":
    # Package the request, send the request and catch the response: r
    r = requests.get(url)

    # Print the text of the response
    print(r.text)
