import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Define the values of alpha
alphas = [0.01, 0.1, 0.5, 1]

# Define a reasonable interval for X (number of arrivals)
x_values = np.arange(0, 10)  # since we have small alpha values, consider 0 to 10

# Plot the probability P(X = i) for each alpha
fig= plt.figure(figsize=(10, 6))
fig.suptitle('Task1.1(a)', fontsize=16)  # Set a title for the window


for alpha in alphas:
    # Calculate probabilities for the current alpha using the Poisson PMF
    probabilities = poisson.pmf(x_values, alpha)
    plt.plot(x_values, probabilities, marker='o', label=f'α = {alpha}')

plt.title('P(X = i) for α ∈ {0.01, 0.1, 0.5, 1} with Δt = 1')
plt.xlabel('Number of arrivals (X)')
plt.ylabel('Probability P(X = i)')
plt.xticks(x_values)  # Ensure all x-values are marked
plt.grid(True)
plt.legend()
plt.show()


