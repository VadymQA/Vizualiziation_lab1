import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
U = 10 * (X ** 3) * (np.sin(Y) * np.sin(Y)) - (2 * (X**2) * (Y**3))

surf = ax.plot_surface(X, Y, U, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('U')
ax.set_title(r'$10x^3\sin^2y - 2x^2y^3$')

ax.zaxis.set_major_locator(LinearLocator(10))
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

np.savetxt('data_1_2.txt', np.c_[X.ravel(), Y.ravel(), U.ravel()], header='X Y Z')
