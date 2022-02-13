#! /usr/bin/python3
"""
:file: eda_heritability.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt

bd_parent_fortis = bd_offspring_fortis = bd_parent_scandens = bd_offspring_scandens = np.array([
])

if __name__ == "__main__":
    # Make scatter plots
    _ = plt.plot(bd_parent_fortis, bd_offspring_fortis,
                 marker='.', linestyle="none", color="blue", alpha=.5)
    _ = plt.plot(bd_parent_scandens, bd_offspring_scandens,
                 marker='.', linestyle="none", color="red", alpha=.5)

    # Label axes
    _ = plt.xlabel('parental beak depth (mm)')
    _ = plt.ylabel('offspring beak depth (mm)')

    # Add legend
    _ = plt.legend(('G. fortis', 'G. scandens'), loc='lower right')

    # Show plot
    plt.show()
