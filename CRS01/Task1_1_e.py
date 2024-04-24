from Task1_1_d import average_waiting_list_length
import numpy as np
import matplotlib.pyplot as plt

# Set up your parameters and ranges

num_samples = 200
total_time_steps = 2000
processing_times = [4, 2]  # Job processing durations to compare
alpha_range_1 = np.arange(0.005, 0.255, 0.005)
alpha_range_2 = np.arange(0.005, 0.505, 0.005)

# Run simulations
average_lengths_1 = average_waiting_list_length(alpha_range_1, num_samples, processing_times[0], total_time_steps)
average_lengths_2 = average_waiting_list_length(alpha_range_2, num_samples, processing_times[1], total_time_steps)

# Plotting
fig=plt.figure(figsize=(12, 8))
fig.suptitle('Task1.1(e)', fontsize=16)  # Set a title for the window
plt.plot(alpha_range_1, average_lengths_1, marker='o', linestyle='-', color='b', label='4 steps per job')
plt.plot(alpha_range_2, average_lengths_2, marker='x', linestyle='-', color='r', label='2 steps per job')
plt.title('Average Waiting List Length vs. Arrival Rate (α) for Different Processing Times')
plt.xlabel('Arrival Rate (α)')
plt.ylabel('Average Waiting List Length')
plt.legend()
plt.grid(True)
plt.show()