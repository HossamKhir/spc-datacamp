#! /usr/bin/python3
"""
:file: power_analysis_i.py
:author: Hossam Khair
"""
import numpy as np
import scipy.stats as st
# Initialize effect_size, control_mean, control_sd
effect_size, sample_size, control_mean, control_sd = .05, 50, 1, .5

if __name__ == "__main__":

    # Simulate control_time_spent and treatment_time_spent, assuming equal variance
    control_time_spent = np.random.normal(
        loc=control_mean, scale=control_sd, size=sample_size)
    treatment_time_spent = np.random.normal(
        loc=control_mean*(1+effect_size), scale=control_sd, size=sample_size)

    # Run the t-test and get the p_value
    t_stat, p_value = st.ttest_ind(treatment_time_spent, control_time_spent)
    stat_sig = p_value < effect_size
    print("P-value: {}, Statistically Significant? {}".format(p_value, stat_sig))
