import numpy as np
from scipy.stats import poisson

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
    # Initialize variables
    waiting_list = []
    current_job_time = 0  # Time steps remaining to finish the current job
    
    # Track waiting list length over time for calculating the average later
    waiting_list_lengths = []

    # Simulation loop
    for step in range(total_time_steps):
        # Add new jobs according to the Poisson distribution
        new_jobs = poisson.rvs(mu=alpha)
        waiting_list.extend([processing_time] * new_jobs)

        # Check if the system is currently processing a job
        if current_job_time > 0:
            current_job_time -= 1  # Continue processing the current job
            #print(f"WORKING ON CURRENT JOB")
        elif waiting_list:
            current_job_time = waiting_list.pop(0) - 1  # Start a new job if available
            #print(f"WORKING ON WAITING LIST")

        # Record the length of the waiting list
        waiting_list_lengths.append(len(waiting_list))
        #print(f"length of waiting list: {len(waiting_list)}")
        
    # Calculate the average waiting list length
    average_waiting_list_length = np.mean(waiting_list_lengths)
    return average_waiting_list_length

# Parameters
alpha = 0.1
processing_time = 4
total_time_steps = 2000

# Run the simulation
average_waiting_list_length = simulate_queue(alpha, processing_time, total_time_steps)
print(f"Average length of the waiting list: {average_waiting_list_length}")
