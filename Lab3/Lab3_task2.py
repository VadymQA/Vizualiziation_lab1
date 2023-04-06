import numpy as np

import matplotlib.pyplot as plt


def u(x, y):
    return x + 2 * y**2


def v(x, y):
    return y + 2 * x**2


xx, yy = np.meshgrid(np.linspace(-3, 6, 10),
                     np.linspace(-3, 6, 10))

u_val = u(xx, yy)
v_val = v(xx, yy)
plt.quiver(xx, yy, u_val, v_val)
plt.show()
plt.streamplot(xx, yy, u_val, v_val)
plt.show()












