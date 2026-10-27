# Dipole Antenna - 3D Radiation Pattern  of dipole antenna 

import numpy as np
import matplotlib.pyplot as plt

# Angle values
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)

theta, phi = np.meshgrid(theta, phi)

# Radiation pattern
R = np.abs(np.sin(theta))

# Coordinate conversion
X = R * np.sin(theta) * np.cos(phi)
Y = R * np.sin(theta) * np.sin(phi)
Z = R * np.cos(theta)

# Plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(X, Y, Z)

ax.set_title("3D Radiation Pattern of Dipole Antenna")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()