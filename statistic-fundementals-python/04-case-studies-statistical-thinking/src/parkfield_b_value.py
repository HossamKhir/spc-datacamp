#! /usr/bin/python3
"""
:file: parkfield_b_value.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
from parkfield_mag import mags
from b_value import b_value

mt = 3

if __name__ == "__main__":
    # Compute b-value and 95% confidence interval
    b, conf_int = b_value(mags, mt, perc=[2.5, 97.5], n_reps=10**4)

    # Generate samples to for theoretical ECDF
    m_theor = np.random.exponential(b/np.log(10), size=10**5) + mt

    # Plot the theoretical CDF
    _ = plt.plot(*dcst.ecdf(m_theor))

    # Plot the ECDF (slicing mags >= mt)
    _ = plt.plot(*dcst.ecdf(mags[mags >= mt]), marker='.', linestyle='none')

    # Pretty up and show the plot
    _ = plt.xlabel('magnitude')
    _ = plt.ylabel('ECDF')
    _ = plt.xlim(2.8, 6.2)
    plt.show()

    # Report the results
    print("""
    b-value: {0:.2f}
    95% conf int: [{1:.2f}, {2:.2f}]""".format(b, *conf_int))
