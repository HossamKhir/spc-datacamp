#! /usr/bin/python3
"""
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import package
import requests

# Specify the url: url
url = "http://www.datacamp.com/teach/documentation"

if __name__ == "__main__":
    # Packages the request, send the request and catch the response: r
    r = requests.get(url)

    # Extract the response: text
    text = r.text

    # Print the html
    print(text)
