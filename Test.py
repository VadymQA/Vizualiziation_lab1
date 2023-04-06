import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(2, 2*np.pi, 1000)
alfa = 1

r1 = alfa * (1 + np.sin(theta)) / np.cos(theta)
r2 = alfa * (1 - np.sin(theta)) / np.cos(theta)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r1, label='r1')
ax.plot(theta, r2, label='r2')
ax.legend()
plt.show()