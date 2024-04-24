import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from tqdm import tqdm


def simulate_queue(alpha, processing_time, total_time_steps):
    """
    Simulate a queue system where jobs arrive according to a Poisson process and each job takes a fixed number of time steps to complete.

    Parameters:
    alpha (float): Rate of incoming jobs (Poisson parameter).
    processing_time (int): Number of time steps it takes to process one job.
    total_time_steps (int): Total number of time steps to simulate.

    Returns:
    float: The average length of the waiting list over the simulation.
    """
    waiting_list = []
    current_job_time = 0
    waiting_list_lengths = []

    for step in range(total_time_steps):
        new_jobs = poisson.rvs(mu=alpha)
        waiting_list.extend([processing_time] * new_jobs)

        if current_job_time > 0:
            current_job_time -= 1
        elif waiting_list:
            current_job_time = waiting_list.pop(0) - 1

        waiting_list_lengths.append(len(waiting_list))

    return np.mean(waiting_list_lengths)

def average_waiting_list_length(alpha_range, num_samples, processing_time, total_time_steps):
    """
    Compute the average waiting list length for different alpha rates.

    Parameters:
    alpha_range (np.ndarray): Array of alpha rates.
    num_samples (int): Number of independent runs for each alpha.
    processing_time (int): Processing time per job.
    total_time_steps (int): Total simulation steps per sample.

    Returns:
    list: Averages of waiting list lengths for each alpha.
    """
    averages = []
    for alpha in tqdm(alpha_range, desc='Processing alphas', leave=True):
        results = [simulate_queue(alpha, processing_time, total_time_steps) for _ in range(num_samples)]
        averages.append(np.mean(results))
    return averages

# Parameters
alpha_range = np.arange(0.005, 0.255, 0.005)
num_samples = 200
processing_time = 4
total_time_steps = 2000

# Calculate average waiting list lengths
average_lengths = average_waiting_list_length(alpha_range, num_samples, processing_time, total_time_steps)

# Plotting
fig=plt.figure(figsize=(10, 6))
fig.suptitle('Task1.1(d)', fontsize=16)  # Set a title for the window

plt.plot(alpha_range, average_lengths, marker='o', linestyle='-', color='b')
plt.title('Average Waiting List Length vs. Arrival Rate (α)')
plt.xlabel('Arrival Rate (α)')
plt.ylabel('Average Waiting List Length')
plt.grid(True)
plt.show()
