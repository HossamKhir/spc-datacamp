#! /usr/bin/python3
"""
:file: assess_growth_rate.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

bac_area = np.array([
    5.574735, 5.71202325, 5.90339475, 6.19461225,
    6.456708, 6.85193175, 7.17643125, 7.56749475,
    8.087526, 8.586756, 8.74900575, 9.48120975,
    10.03868325, 10.550394, 11.13698925, 11.765187,
    12.38506425, 13.07566575, 13.7371455, 14.377824,
    14.89785525, 15.5177325, 16.341462, 17.31912075,
    18.4132665, 19.5947775, 20.96766, 22.07844675,
    23.41804725, 24.6702825, 26.25533775, 28.00264275,
    29.6293005, 31.41404775, 33.31944225, 35.59925925,
    37.974762, 40.787091, 43.749189, 46.8028125,
    50.28494175, 53.467533, 57.644424, 61.438572,
    64.72932975, 68.3861895, 71.539659, 75.85383825,
    81.61994475, 86.050611, 91.53798075, 98.231823,
    104.27666625, 110.862342, 118.31751
])

if __name__ == "__main__":
    # Compute logarithm of the bacterial area: log_bac_area
    log_bac_area = np.log(bac_area)

    # Compute the slope and intercept: growth_rate, log_a0
    growth_rate, log_a0 = np.polyfit(t, log_bac_area, 1)

    # Draw 10,000 pairs bootstrap replicates: growth_rate_bs_reps, log_a0_bs_reps
    growth_rate_bs_reps, log_a0_bs_reps = dcst.draw_bs_pairs_linreg(
        t, log_bac_area, size=10**4
    )

    # Compute confidence intervals: growth_rate_conf_int
    growth_rate_conf_int = np.percentile(growth_rate_bs_reps, [2.5, 97.5])

    # Print the result to the screen
    print("""
    Growth rate: {0:.4f} 1/hour
    95% conf int: [{1:.4f}, {2:.4f}] 1/hour
    """.format(growth_rate, *growth_rate_conf_int))
