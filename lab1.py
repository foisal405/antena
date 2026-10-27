import numpy as np
import matplotlib.pyplot as plt

# Angle values
theta = np.linspace(0.001, np.pi - 0.001, 200)
phi = np.linspace(0, 2*np.pi, 200)

theta, phi = np.meshgrid(theta, phi)

# Half-wave dipole radiation pattern
R = np.abs(np.cos((np.pi/2)*np.cos(theta)) / np.sin(theta))
R = R / np.max(R)

# Coordinate conversion
X = R * np.sin(theta) * np.cos(phi)
Y = R * np.sin(theta) * np.sin(phi)
Z = R * np.cos(theta)

# Plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, cmap='cool')

ax.set_title("3D Radiation Pattern of Half-Wave Dipole")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_box_aspect((1, 1, 1))

plt.show()

