#! /usr/bin/python3
"""
:file: eda_mags_pre_post_2010.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
from eda_earthquake_time import mags, time

# Get magnitudes before and after 2010
mags_pre = mags[time < 2010]
mags_post = mags[time >= 2010]

if __name__ == "__main__":
    # Generate ECDFs
    _ = plt.plot(*dcst.ecdf(mags_pre), marker='.', linestyle='none')
    _ = plt.plot(*dcst.ecdf(mags_post), marker='.', linestyle='none')

    # Label axes and show plot
    _ = plt.xlabel('magnitude')
    _ = plt.ylabel('ECDF')
    plt.legend(('1980 though 2009', '2010 through mid-2017'), loc='upper left')
    plt.show()
