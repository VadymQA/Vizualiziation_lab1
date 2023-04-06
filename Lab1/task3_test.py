import numpy as np
import matplotlib.pyplot as plt

alfa = 1

theta = np.linspace(0, 2 * np.pi, 1000)

r1 = alfa * (1 + np.sin(theta)) / np.cos(theta)
r2 = alfa * (1 - np.sin(theta)) / np.cos(theta)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r1, color='b', linewidth=2)
ax.plot(theta, r2, color='r', linewidth=1)
plt.title(r'$r = \frac{\alpha(1 \pm sin(\theta))}{cos(\theta)}$')

plt.show()

