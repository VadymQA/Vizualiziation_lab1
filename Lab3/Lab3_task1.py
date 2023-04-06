import numpy as np
import matplotlib.pyplot as plt

def u(x, y):
    return -2*np.log(x**2 + 5) - 4*x*y

def v(x, y):
    return -4*x**2

xx, yy = np.meshgrid(np.linspace(-3, 6, 15), np.linspace(-3, 6, 15))
u_val = u(xx, yy)
v_val = v(xx, yy)

# Векторне поле
plt.quiver(xx, yy, u_val, v_val)
plt.title('Векторне поле')
plt.show()

# Градієнт
fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')
ax.streamplot(xx, yy, u_val, v_val, color=u_val, cmap='viridis')
plt.title('Градієнт')
plt.show()