import numpy as np
import matplotlib.pyplot as plt

def u(x, y):
    return -2*np.log(x**2 + 5) - 4*x*y


n = 256
x = np.linspace(-3., 6., n)  # діапазон по X
y = np.linspace(-3., 6., n)  # діапазон по Y
X, Y = np.meshgrid(x, y)

Z = -2*np.log(X**2 + 5) - 4*X*Y  # Формула скалярного поля

plt.pcolormesh(X, Y, Z)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Візуалізацію скалярного поля  $-2\\ln(X^2 + 5) - 4XY$')
plt.show()

#---------------------------------------------------------------------
xx, yy = np.meshgrid(np.linspace(-3, 6, 15), np.linspace(-3, 6, 15))
u_val = u(xx, yy)
u_dx, u_dy = np.gradient(u_val)

# Векторне поле
plt.quiver(xx, yy, u_dx, u_dy)
plt.title('Векторне поле ' + r'$u(x,y)=-2\ln(x^2+5) - 4xy$')

# Градієнт
fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')
ax.streamplot(xx, yy, u_dx, u_dy, color=u_val, cmap='viridis')
plt.title('Градієнт ' + r'$-2\ln(x^2+5) - 4xy$')

plt.show()