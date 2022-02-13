#! /usr/bin/python3
"""
:file: eda_peak_depth.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.DataFrame()

if __name__ == "__main__":
    # Create bee swarm plot
    _ = sns.swarmplot("year", "beak_depth", data=df)

    # Label the axes
    _ = plt.xlabel('year')
    _ = plt.ylabel('beak depth (mm)')

    # Show the plot
    plt.show()
