import numpy as np
import matplotlib.pyplot as plt

def simulate_robots(N, M=20, time_steps=1000, wait_time=7):
    stick_sites = np.zeros(M)
    robots = np.random.randint(0, M, size=N)
    stick_pulls = 0

    for _ in range(time_steps):
        # Robots act
        for i in range(N):
            site = robots[i]
            stick_sites[site] += 1
            # Check if stick can be pulled
            if stick_sites[site] == 2:
                stick_pulls += 1
                stick_sites[site] = 0  # Stick is immediately replaced

        # Move robots after waiting time
        if _ % wait_time == 0:
            for i in range(N):
                commute_time = N + np.random.choice([0, 1, 2])
                # Wait for commute time or move immediately if time elapsed
                if commute_time <= wait_time:
                    robots[i] = np.random.randint(0, M)

    return stick_pulls

# Parameters
system_sizes = range(2, 21)
trials = 5000
results = np.zeros(len(system_sizes))

for index, N in enumerate(system_sizes):
    pulls = [simulate_robots(N) for _ in range(trials)]
    results[index] = np.mean(pulls)

# Normalize by the result for N=2
relative_capacity = results / results[0]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(system_sizes, relative_capacity, marker='o')
plt.title('System Size vs Relative Capacity (Linear Commute Time)')
plt.xlabel('Number of Robots (N)')
plt.ylabel('Relative Capacity')
plt.grid(True)
plt.show()
