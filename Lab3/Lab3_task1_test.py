import numpy as np
import matplotlib.pyplot as plt

def u(x, y):
    return -2*np.log(x**2 + 5) - 4*x*y

n = 256
x = np.linspace(-3, 6, n)
y = np.linspace(-3, 6, n)
X, Y = np.meshgrid(x, y)

plt.pcolormesh(X, Y, u(X, Y))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Візуалізацію скалярного поля  $-2\\ln(X^2 + 5) - 4XY$')

xx, yy = np.meshgrid(np.linspace(-3, 6, 15), np.linspace(-3, 6, 15))
u_val = u(xx, yy)
u_dx, u_dy = np.gradient(u_val)

plt.quiver(xx, yy, u_dx, u_dy)
plt.title('Векторне поле ' + r'$u(x,y)=-2\ln(x^2+5) - 4xy$')

fig, ax = plt.subplots()
ax.streamplot(xx, yy, u_dx, u_dy, color=u_val, cmap='viridis')
plt.title('Градієнт ' + r'$-2\ln(x^2+5) - 4xy$')

plt.show()