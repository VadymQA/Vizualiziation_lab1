import numpy as np
import matplotlib.pyplot as plt

#((x^(2))/(a^(2)))+((y^(2))/(b^(2)))-((z^(2))/(c^(2)))=-1

a = 1
b = 2
c = 3

x = np.linspace(-a, a, 100)
y = np.linspace(-b, b, 100)
x, y = np.meshgrid(x, y)
u = c * np.sqrt((x**2/a**2) + (y**2/b**2) + 1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, u)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title(r'$\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{u^2}{c^2} = -1$')
plt.show()

# об'єднати x, y, u в один масив
combined = np.array([x.flatten(), y.flatten(), u.flatten()])

# зберегти combined в txt формат
np.savetxt('combined_values.txt', combined.T)