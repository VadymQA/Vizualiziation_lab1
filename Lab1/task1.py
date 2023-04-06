import numpy as np
import matplotlib.pyplot as plt
import random as rd


def z_f(x):
    y = np.zeros_like(x)
    mask = x <= 0
    y[mask] = 5 * x[mask] ** 2 / (1 * x[mask] ** 2)
    y[~mask] = (1 + (2 * x[~mask] / (1 + x[~mask] ** 2))) ** (-1 / 2)
    return y

def y_f(x):
    return (2 + np.sin(x) * np.sin(x)) / ( 1 + x*x)


# x = np.arange(-7, -1, 4, 10)
x = np.arange(0, 2, 0.01)
y = y_f(x)
z = z_f(x)

fig1, ay = plt.subplots()
ay.plot(x, y)
ay.grid(True, linestyle='-.')
ay.set_xlabel('X')
ay.set_ylabel('Y')
ay.set_title(r'$\frac{2+\sin^2x}{1+x^2}$')
ay.tick_params(labelcolor='r', labelsize='medium', width=3)

fig2, az = plt.subplots()
az.plot(x, z)
az.grid(True, linestyle='-.')
az.set_xlabel('X')
az.set_ylabel('Y')
az.set_title(r'$\frac{5x^2}{x^2}, x \geq 0, \sqrt{1 + \frac{2x}{1 + x^2}}, x < 0$')

az.tick_params(labelcolor='r', labelsize='medium', width=3)
plt.show()


