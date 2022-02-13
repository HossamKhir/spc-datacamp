#! /usr/bin/python3
"""
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = "https://www.python.org/~guido/"

if __name__ == "__main__":
    # Package the request, send the request and catch the response: r
    r = requests.get(url)

    # Extracts the response as html: html_doc
    html_doc = r.text

    # Create a BeautifulSoup object from the HTML: soup
    soup = BeautifulSoup(html_doc)

    # Prettify the BeautifulSoup object: pretty_soup
    pretty_soup = soup.prettify()

    # Print the response
    print(pretty_soup)
