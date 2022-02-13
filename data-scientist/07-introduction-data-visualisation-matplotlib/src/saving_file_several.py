#! /usr/bin/python3
"""
"""
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

DATA_PATH = "../data/raw"

medals = pd.read_csv(os.path.join(DATA_PATH, "medals.csv"), index_col=0)

medal_number = medals.apply((lambda r: np.sum(r)), axis=1)
# medal_number.hist()
fig, ax = plt.subplots()
ax.bar(medal_number.index, medal_number)
plt.xticks(rotation=90)
plt.show()

# Save as a PNG file
fig.savefig("my_figure.png")

# Save as a PNG file with 300 dpi
fig.savefig("my_figure_300dpi.png", dpi=300)

if __name__ == "__main__":
    pass
