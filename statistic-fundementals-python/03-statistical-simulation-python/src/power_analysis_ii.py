#! /usr/bin/python3
"""
:file: power_analysis_ii.py
:author: Hossam Khair
"""
import numpy as np
import scipy.stats as st
from power_analysis_i import control_mean, control_sd, effect_size

sims = 1000

if __name__ == "__main__":
    sample_size = 50

    # Keep incrementing sample size by 10 till we reach required power
    while 1:
        control_time_spent = np.random.normal(
            loc=control_mean, scale=control_sd, size=(sample_size, sims))
        treatment_time_spent = np.random.normal(
            loc=control_mean*(1+effect_size), scale=control_sd, size=(sample_size, sims))
        t, p = st.ttest_ind(treatment_time_spent, control_time_spent)

        # Power is the fraction of times in the simulation when the p-value was less than 0.05
        power = (p < 0.05).sum()/sims
        if power >= .8:
            break
        else:
            sample_size += 10
    print("For 80% power, sample size required = {}".format(sample_size))
