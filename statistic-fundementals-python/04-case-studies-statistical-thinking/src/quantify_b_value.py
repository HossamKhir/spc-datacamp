#! /usr/bin/python3
"""
:file: quantify_b_value.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
from eda_mags_pre_post_2010 import mags_pre, mags_post

mt = 3

if __name__ == "__main__":
    # Compute b-value and confidence interval for pre-2010
    b_pre, conf_int_pre = dcst.b_value(
        mags_pre, mt, perc=[2.5, 97.5], n_reps=10**4)

    # Compute b-value and confidence interval for post-2010
    b_post, conf_int_post = dcst.b_value(
        mags_post, mt, perc=[2.5, 97.5], n_reps=10**4)

    # Report the results
    print("""
    1980 through 2009
    b-value: {0:.2f}
    95% conf int: [{1:.2f}, {2:.2f}]

    2010 through mid-2017
    b-value: {3:.2f}
    95% conf int: [{4:.2f}, {5:.2f}]
    """.format(b_pre, *conf_int_pre, b_post, *conf_int_post))
