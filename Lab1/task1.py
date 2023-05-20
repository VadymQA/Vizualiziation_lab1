import numpy as np
import matplotlib.pyplot as plt

def z_f(x):
    y = np.zeros_like(x)
    for i, value in enumerate(x):
        if value <= 0:
            y[i] = 5 * value ** 2 / (1 * value ** 2)
        else:
            y[i] = (1 + (2 * value / (1 + value ** 2))) ** (-1 / 2)
    return y

def y_f(x):
    return (2 + np.sin(x) ** 3) / ( 1 + x**2)

x = np.arange(0, 2, 0.01)
y = y_f(x)
z = z_f(x)

fig1, ay = plt.subplots()
ay.plot(x, y)
ay.grid(True, linestyle='-.')
ay.set_xlabel('X')
ay.set_ylabel('Y')
ay.set_title(r'$\frac{2+\sin^3x}{1+x^2}$')
ay.tick_params(labelcolor='r', labelsize='medium', width=3)

fig2, az = plt.subplots()
az.plot(x, z)
az.grid(True, linestyle='-.')
az.set_xlabel('X')
az.set_ylabel('Y')
az.set_title(r'$\frac{5x^2}{1+x^2}, x \geq 0, \sqrt{1 + \frac{2x}{1 + x^2}}, x < 0$')

az.tick_params(labelcolor='r', labelsize='medium', width=3)
plt.show()

data = np.column_stack((x, y))
np.savetxt('data_1_1_1.txt', data, delimiter='\t', header='X\tY')

data = np.column_stack((x, z))
np.savetxt('data_1_1_2.txt', data, delimiter='\t', header='X\tZ')

