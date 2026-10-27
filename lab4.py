# Linear Antenna Array (2D)
import numpy as np
import matplotlib.pyplot as plt
# Parameters
N = 8
d = 0.5
# Number of elements
# Spacing (lambda/2)

k = 2 * np.pi
beta = 0
# Wave number
# Phase difference

theta = np.linspace(0, 2*np.pi, 1000)

# Array Factor
AF = np.zeros_like(theta, dtype=complex)

for n in range(N):
    AF += np.exp(1j * n * (k * d * np.cos(theta) + beta))

AF = np.abs(AF)
AF = AF / np.max(AF) # Normalize

# Plot
ax = plt.subplot(111, projection="polar")
ax.plot(theta, AF)
ax.set_title("Linear Antenna Array (2D)")
plt.show()