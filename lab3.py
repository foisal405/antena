# Horn Antenna - 3D Radiation Pattern
import numpy as np
import matplotlib.pyplot as plt

# Angle values
theta = np.linspace(0, np.pi, 200)
phi = np.linspace(0, 2 * np.pi, 200)
theta, phi = np.meshgrid(theta, phi)

# Radiation pattern
u = 3 * np.sin(theta) * np.cos(phi)
v = 2 * np.sin(theta) * np.sin(phi)

R = np.sinc(u / np.pi) * np.sinc(v / np.pi)
R = np.where(np.cos(theta) >= 0, np.abs(R), 0)
R = R / np.max(R)

# Coordinate conversion
X = R * np.sin(theta) * np.cos(phi)
Y = R * np.sin(theta) * np.sin(phi)
Z = R * np.cos(theta)


# Plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(X, Y, Z, cmap='inferno')

ax.set_title("3D Radiation Pattern of Horn Antenna")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_box_aspect((1, 1, 1))

plt.show()

