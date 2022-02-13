#! /usr/bin/python3
"""
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import necessary module
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Create engine: engine
    engine = create_engine("postgresql:///chinook.db")
