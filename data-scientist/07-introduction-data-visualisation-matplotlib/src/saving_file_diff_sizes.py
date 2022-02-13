#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from saving_file_several import medal_number, ax, fig

if __name__ == "__main__":
    # Set figure dimensions and save as a PNG
    fig.set_size_inches([3, 5])
    fig.savefig("figure_3_5.png")
    # Set figure dimensions and save as a PNG
    fig.set_size_inches([5, 3])
    fig.savefig("figure_5_3.png")
