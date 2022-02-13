#! /usr/bin/python3
"""
:file: max_likelihood.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from estimate_population_params import sample_distances, gaussian_model


def compute_loglikelihood(samples, mu, sigma=250):
    probs = np.zeros(len(samples))
    for n, sample in enumerate(samples):
        probs[n] = gaussian_model(sample, mu, sigma)
    loglikelihood = np.sum(np.log(probs))
    return loglikelihood


def plot_loglikelihoods(mu_guesses, loglikelihoods):
    max_loglikelihood = np.max(loglikelihoods)
    max_index = np.where(loglikelihoods == max_loglikelihood)
    max_guess = mu_guesses[max_index][0]
    font_options = {'family': 'Arial', 'size': 16}
    plt.rc('font', **font_options)
    fig, axis = plt.subplots(figsize=(10, 6))
    axis.plot(mu_guesses, loglikelihoods)
    axis.plot(max_guess, max_loglikelihood, marker="o", color="red")
    axis.grid()
    axis.set_ylabel('Log Likelihoods')
    axis.set_xlabel('Guesses for Mu')
    axis.set_title('Max Log Likelihood = {:0.1f} \n was found at Mu = {:0.1f}'.format(
        max_loglikelihood, max_guess))
    fig.tight_layout()
    plt.show()
    return fig


if __name__ == "__main__":
    # Compute sample mean and stdev, for use as model parameter value guesses
    mu_guess = np.mean(sample_distances)
    sigma_guess = np.std(sample_distances)

    # For each sample distance, compute the probability modeled by the parameter guesses
    probs = np.zeros(len(sample_distances))
    for n, distance in enumerate(sample_distances):
        probs[n] = gaussian_model(distance, mu=mu_guess, sigma=sigma_guess)

    # Compute and print the log-likelihood as the sum() of the log() of the probabilities
    loglikelihood = np.sum(np.log(probs))
    print('For guesses mu={:0.2f} and sigma={:0.2f}, the loglikelihood={:0.2f}'.format(
        mu_guess, sigma_guess, loglikelihood))

    sample_mean = np.mean(sample_distances)
    sample_stdev = np.std(sample_distances)

    # Create an array of mu guesses, centered on sample_mean, spread out +/- by sample_stdev
    low_guess = sample_mean - 2*sample_stdev
    high_guess = sample_mean + 2*sample_stdev
    mu_guesses = np.linspace(low_guess, high_guess, 101)

    # Compute the loglikelihood for each model created from each guess value
    loglikelihoods = np.zeros(len(mu_guesses))
    for n, mu_guess in enumerate(mu_guesses):
        loglikelihoods[n] = compute_loglikelihood(
            sample_distances, mu=mu_guess, sigma=sample_stdev)

    # Find the best guess by using logical indexing, the print and plot the result
    best_mu = mu_guesses[loglikelihoods == np.max(loglikelihoods)]
    print('Maximum loglikelihood found for best mu guess={}'.format(best_mu))
    fig = plot_loglikelihoods(mu_guesses, loglikelihoods)
