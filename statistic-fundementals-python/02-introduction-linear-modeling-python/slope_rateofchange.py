#! /usr/bin/python3
"""
:file: slope_rateofchange.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt


def plot_velocity_timeseries(times, velocities):
    fig, axis = plt.subplots()
    axis.plot(times, velocities, linestyle=" ", marker=".",
              color='black', label='Velocities')
    axis.axhline(np.mean(velocities), color='red',
                 alpha=0.5, lw=4, label='Mean Velocity')
    axis.grid(True, which="both")
    axis.set_ylabel("Instantaneous Velocity (Kilometers / Hours)")
    axis.set_xlabel("Time (Hours)")
    axis.set_ylim([0, 100])
    fig.tight_layout()
    fig.legend(loc='upper center')
    plt.show()
    return fig


times = np.array([0., 0.08333333, 0.16666667, 0.25, 0.33333333, 0.41666667, 0.5, 0.58333333, 0.66666667, 0.75,
                  0.83333333, 0.91666667, 1., 1.08333333, 1.16666667, 1.25, 1.33333333, 1.41666667, 1.5, 1.58333333,
                  1.66666667, 1.75, 1.83333333, 1.91666667, 2.])
distances = np.array([0.13536211, 4.11568697, 8.28931902, 12.41058595, 16.73878397, 20.64153844, 25.14540098, 29.10323276,
                      33.35991992, 37.47921914, 41.78850899, 45.66165494, 49.9731319, 54.13466214, 58.42781412, 62.40834239,
                      66.65229765, 70.76017847, 75.00351781, 79.2152346, 83.24161507, 87.59539364, 91.74179923, 95.87520786,
                      100.07507133])

if __name__ == "__main__":
    # Compute an array of velocities as the slope between each point
    diff_distances = np.diff(distances)
    diff_times = np.diff(times)
    velocities = diff_distances / diff_times

    # Characterise the centre and spread of the velocities
    v_avg = np.mean(velocities)
    v_max = np.max(velocities)
    v_min = np.min(velocities)
    v_range = v_max - v_min

    # Plot the distribution of velocities
    fig = plot_velocity_timeseries(times[1:], velocities)
