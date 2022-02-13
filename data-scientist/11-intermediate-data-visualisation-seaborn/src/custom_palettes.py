#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


if __name__ == "__main__":
    sns.palplot(sns.color_palette("Purples", 8))
    plt.show()
    plt.clf()

    sns.palplot(sns.color_palette("husl", 10))
    plt.show()
    plt.clf()

    sns.palplot(sns.color_palette("coolwarm", 6))
    plt.show()
    plt.clf()
