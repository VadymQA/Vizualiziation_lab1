from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


x, y, z = np.meshgrid(np.arange(-3, 6, 0.6),
                      np.arange(-3, 6, 0.6),
                      np.arange(-3, 6, 2.4))

Fx = y - z / x**2
Fy = x + 1 / z
Fz = 1 / x - y / z**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(x, y, z, Fx, Fy, Fz, length=0.5, normalize=True, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(r'$F = (y - \frac{z}{x^2}; x + \frac{1}{z}; \frac{1}{x} - \frac{y}{z^2})$')

plt.show()