import numpy as np
import matplotlib.pyplot as plt

alfa = 1.0
theta = np.linspace(0, 2*np.pi, 1000)
r1 = alfa * (1 + np.sin(theta)) / np.cos(theta)
r2 = alfa * (1 - np.sin(theta)) / np.cos(theta)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r1, linewidth=2, label=r'$r = \frac{\alpha(1 - sin(\theta))}{cos(\theta)}$')
ax.plot(theta, r2, linewidth=1, label=r'$r = \frac{\alpha(1 + sin(\theta))}{cos(\theta)}$')

ax.set_rlabel_position(-22.5)
ax.grid(True)
ax.legend(loc='right')
plt.title(r'$r = \frac{\alpha(1 \pm sin(\theta))}{cos(\theta)}$')
plt.show()






# ax.set_rticks(np.arange(-1, 1, 2))
# ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks












# import numpy as np
# import matplotlib.pyplot as plt
#
#
# # alfa = np.arange(0, 2, 0.01)
# r = np.arange(0, 2, 0.01)
# theta = 2 * np.pi * r
# # theta = alfa * (1 + np.sin(y)) / np.cos(y)
#
# ax = plt.subplot(111, projection='polar')
# ax.plot(theta, r)
# # ax.set_rmax(2)
# ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
# ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
# ax.grid(True)
#
# ax.set_title("A line plot on a polar axis", va='bottom')
# plt.show()
