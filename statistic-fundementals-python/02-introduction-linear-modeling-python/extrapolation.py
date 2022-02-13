#! /usr/bin/python3
"""
:file: extrapolation.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt


def plot_data_model_tolerance(x_data, y_data, y_model, tolerance=100):
    """
    Purpose: 
        Plot data (x_data, y_data) and overplot model (x_data, y_model)
    Args:
        x_data (np.array): numpy array of values of independent variable
        y_data (np.array): numpy array of values of dependent variable
        y_model (np.array): numpy array of values of the modeled dependent variable
        tolerance (float): for plotting when np.abs(y_model - y_data) < tolerance
    Returns:
        fig (matplotlib.figure): matplotlib figure object
    """
    residuals = np.abs(y_model - y_data)
    x_good = x_data[residuals < tolerance]
    y_good = y_model[residuals < tolerance]
    x_min = np.min(x_good)
    x_max = np.max(x_good)
    font_options = {'family': 'Arial', 'size': 16}
    plt.rc('font', **font_options)
    fig, axis = plt.subplots(figsize=(8, 6))
    x = x_data
    y = y_data
    axis.plot(x[(x >= 0) & (x <= 10)], y[(x >= 0) & (x <= 10)],
              color="black", linestyle=" ", marker="o")
    axis.plot(x[x > 10], y[x > 10], color="blue", linestyle=" ", marker="o")
    axis.plot(x[x < 0], y[x < 0], color="blue", linestyle=" ", marker="o")
    axis.plot(x_data, y_model, color="red")
    axis.grid(True, which="both")
    axis.axhline(0, color="black")
    axis.axvline(0, color="black")
    axis.set_ylim([-5*50, 15*50])
    axis.set_xlim([-15, 25])
    # axis.xaxis.set_major_locator(MultipleLocator(5.0))
    # axis.xaxis.set_minor_locator(MultipleLocator(1.0))
    # axis.yaxis.set_major_locator(MultipleLocator(5.0*50))
    # axis.yaxis.set_minor_locator(MultipleLocator(1.0*50))
    axis.set_ylabel('Altitude (meters)')
    axis.set_xlabel('Step Distance (Kilometers)')
    axis.set_title("Hiking  Trip")
    style_options = dict(color="green", alpha=0.35, linewidth=8)
    line = axis.plot(x_good, y_good, **style_options)
    plt.show()
    return fig


x_data = np.array([-10., 9.5, 9., 8.5, 8., 7.5, 7., 6.5, 6., -5.5, 5., 4.5, 4., 3.5, 3., 2.5, 2., 1.5,
                   -1., 0.5, 0., 0.5, 1., 1.5, 2., 2.5, 3., 3.5, 4., 4.5, 5., 5.5, 6., 6.5, 7., 7.5,
                   8., 8.5, 9., 9.5, 10., 10.5, 11., 11.5, 12., 12.5, 13., 13.5, 14., 14.5, 15., 15.5, 16., 16.5,
                   17., 17.5, 18., 18.5, 19., 19.5, 20.])
y_data = np.array([73.33885174, 91.52854842, 41.87555998, 103.06980499, 77.57108039, 99.70512917, 106.70722978, 128.26034956,
                   117.88171452, 136.65021987, 82.60474807, 86.82566796, 122.477045, 114.41893877, 127.63451229, 143.2255083,
                   136.61217437, 154.76845765, 182.39147012, 122.51909166, 161.78587909, 132.72560763, 210.81767421, 179.6837026,
                   181.98528167, 234.67907351, 246.48971034, 221.58691239, 250.3924093, 206.43287615, 303.75089312, 312.29865056,
                   323.8331032, 261.9686295, 316.64806585, 337.55295912, 360.13633529, 369.72729852, 408.0289548, 348.82736117,
                   394.93384188, 366.03460828, 374.7693763, 371.26981466, 377.88763074, 320.70120977, 336.82269401, 262.00816122,
                   290.35612838, 308.90807157, 259.98783618, 265.86978322, 271.12330621, 258.58229827, 241.52677418, 204.38155251,
                   198.05166573, 174.36397174, 190.97570971, 217.20785477, 146.83883158])
y_model = np.array([-100., 87.5, 75., 62.5, 50., 37.5, 25., 12.5, 0., 12.5, 25., 37.5, 50., 62.5, 75., 87.5,
                    100., 112.5, 125., 137.5, 150., 162.5, 175., 187.5, 200., 212.5, 225., 237.5, 250., 262.5, 275., 287.5,
                    300., 312.5, 325., 337.5, 350., 362.5, 375., 387.5, 400., 412.5, 425., 437.5, 450., 462.5, 475., 487.5,
                    500., 512.5, 525., 537.5, 550., 562.5, 575., 587.5, 600., 612.5, 625., 637.5, 650.])

if __name__ == "__main__":
    # Compute the residuals, "data - model", and determine where [residuals < tolerance]
    residuals = np.abs(y_data - y_model)
    tolerance = 100
    x_good = x_data[residuals < 100]

    # Find the min and max of the "good" values, and plot y_data, y_model, and the tolerance range
    print('Maximum good x value = {}'.format(np.min(x_good)))
    print('Minimum good x value = {}'.format(np.max(x_good)))
    fig = plot_data_model_tolerance(x_data, y_data, y_model, tolerance)
