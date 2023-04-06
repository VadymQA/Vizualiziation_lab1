from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# Задаємо область визначення
x, y, z = np.meshgrid(np.arange(-3, 6, 0.6),
                      np.arange(-3, 6, 0.6),
                      np.arange(-3, 6, 2.4))

# Обчислюємо векторне поле
Fx = y - z / x**2
Fy = x + 1 / z
Fz = 1 / x - y / z**2


# Створюємо тривимірний графік
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Будуємо векторне поле за допомогою функції quiver
ax.quiver(x, y, z, Fx, Fy, Fz, length=0.5, normalize=True, cmap='viridis')

# Встановлюємо підписи осей та заголовок
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(r'$F = (y - \frac{z}{x^2}; x + \frac{1}{z}; \frac{1}{x} - \frac{y}{z^2})$')

# Відображаємо графік
plt.show()