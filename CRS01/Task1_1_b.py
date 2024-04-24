import numpy as np
from scipy.stats import poisson

def sample_jobs(alpha, num_samples=100):
    """
    Sample the number of incoming jobs from a Poisson distribution.
    
    Parameters:
    alpha (float): The rate (mean number of events) of the Poisson distribution.
    num_samples (int): The number of samples to draw.
    
    Returns:
    np.ndarray: An array of samples representing the number of jobs.
    """
    # Generate random samples from a Poisson distribution
    samples = poisson.rvs(mu=alpha, size=num_samples)
    return samples

# Example usage:
alphas = [0.01, 0.1, 0.5, 1]  # Different rates of job arrivals
num_samples = 100  # Number of samples to draw for each alpha

# Sample and print the results for each alpha
for alpha in alphas:
    print(f"α = {alpha}:")
    samples = sample_jobs(alpha, num_samples)
    print(samples, "\n")  # Display the sampled number of jobs

