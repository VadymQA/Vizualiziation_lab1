import numpy as np
import matplotlib.pyplot as plt

alfa = 1

theta =  np.linspace(0, 2* np.pi, 1000)
theta1 =  np.linspace(0, 2* np.pi, 1000)

r1 = alfa * (1 + np.sin(theta)) / np.cos(theta)
r2 = alfa * (1 - np.sin(theta1)) / np.cos(theta1)




ax = plt.subplot(111, projection='polar')
ax.plot(theta, r1, color='b', linewidth=2)
ax.plot(theta1, r2, color='r', linewidth=2)
plt.title(r'$r = \frac{\alpha(1 \pm sin(\theta))}{cos(\theta)}$')

ax.set_rmin(0)
ax.set_rmax(5)

plt.show()

theta2 = np.degrees(theta)
data = np.column_stack((theta2, r1, r2))
np.savetxt("output.txt", data)

