#! /usr/bin/python3
"""
:file: estimate_mean_time.py
:author: Hossam Khair
"""
import os
import json
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

DATA_PATH = "../data/raw"

dt_pre = np.array(
    [
        2.51473603e02,
        2.95650596e02,
        6.41211817e02,
        1.08631328e03,
        3.17616277e02,
        5.89587696e02,
        4.83564906e02,
        6.97670295e01,
        6.92609789e02,
        2.83876828e01,
        4.69754032e02,
        2.64696924e02,
        7.66216207e01,
        5.70100061e01,
        1.05893359e02,
        7.22457315e02,
        2.33767653e02,
        7.02367640e01,
        1.15034729e02,
        3.60481877e02,
        8.36271879e02,
        1.11819550e02,
        1.41778326e02,
        5.96888641e02,
        1.67632908e02,
        1.50228765e02,
        3.27358344e02,
        2.14424228e01,
        1.84269802e02,
        2.33111006e02,
        3.78900412e02,
        1.42433380e02,
        8.96787214e01,
        5.96520032e00,
        1.89851791e01,
        2.77352546e00,
        1.13775168e01,
        9.84176998e01,
        1.20027146e01,
        4.83078902e00,
        2.03967335e01,
        3.62722197e01,
        7.41380943e-01,
        5.61129875e01,
        2.23184198e01,
        2.00108958e00,
        7.00255109e-01,
        1.19086239e01,
        8.67777468e00,
        4.74607571e00,
        8.78615616e-01,
        6.85672396e00,
    ]
)

with open(os.path.join(DATA_PATH, "dt_post.json")) as dt_post:
    dt_post = dt_post.read()
    dt_post = json.loads(dt_post)


# Compute mean interearthquake time
mean_dt_pre = np.mean(dt_pre)
mean_dt_post = np.mean(dt_post)

# Draw 10,000 bootstrap replicates of the mean
bs_reps_pre = dcst.draw_bs_reps(dt_pre, np.mean, size=10 ** 4)
bs_reps_post = dcst.draw_bs_reps(dt_post, np.mean, size=10 ** 4)

# Compute the confidence interval
conf_int_pre = np.percentile(bs_reps_pre, [2.5, 97.5])
conf_int_post = np.percentile(bs_reps_post, [2.5, 97.5])

if __name__ == "__main__":
    # Print the results
    print(
        """1980 through 2009
        mean time gap: {0:.2f} days
        95% conf int: [{1:.2f}, {2:.2f}] days""".format(
            mean_dt_pre, *conf_int_pre
        )
    )

    print(
        """
        2010 through mid-2017
        mean time gap: {0:.2f} days
        95% conf int: [{1:.2f}, {2:.2f}] days""".format(
            mean_dt_post, *conf_int_post
        )
    )
