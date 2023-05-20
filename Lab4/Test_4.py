import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.patches import FancyArrowPatch

# Функція для обчислення координат вершин рівностороннього трикутника
def equilateral_triangle_vertices(side_length):
    height = side_length * np.sqrt(3) / 2
    A = (0, 0)
    B = (side_length / 2, height)
    C = (side_length, 0)
    return A, B, C

# Функція для повернення вектора на певний кут (градуси)
def rotate_vector(vector, angle_degrees):
    angle_radians = np.deg2rad(angle_degrees)
    rotation_matrix = np.array([[np.cos(angle_radians), -np.sin(angle_radians)],
                                [np.sin(angle_radians), np.cos(angle_radians)]])
    return np.matmul(rotation_matrix, vector)

# Розмір сторони трикутника
side_length = 10

# Обчислення вершин трикутника
A, B, C = equilateral_triangle_vertices(side_length)

# Ініціалізація фігури
fig, ax = plt.subplots()
ax.set_xlim(-5, side_length + 5)
ax.set_ylim(-5, side_length + 5)
ax.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], 'k-')
arrow = FancyArrowPatch(A, B, mutation_scale=15, lw=1, arrowstyle='->', color='r')
ax.add_patch(arrow)

# Анімація
def animate(i):
    t = i / 100
    if t <= 1:
        x, y = A[0] + t * (B[0] - A[0]), A[1] + t * (B[1] - A[1])
    elif t <= 2:
        t -= 1
        x, y = B[0] + t * (C[0] - B[0]), B[1] + t * (C[1] - B[1])
    else:
        t -= 2
        x, y = C[0] + t * (A[0] - C[0]), C[1] + t * (A[1] - C[1])

    direction = np.array([x - A[0], y - A[1]])
    angle = 60 * (i // 100)
    rotated_direction = rotate_vector(direction, angle)
    end_point = np.array([A[0], A[1]]) + rotated_direction
    arrow.set_positions((A[0], A[1]), end_point)
    return arrow,

ani = animation.FuncAnimation(fig, animate, frames=300, interval=20, blit=True)

# Збереження аніанімації у форматі .gif
ani.save('triangle_arrow_rotating_animation2.gif', writer='imagemagick', fps=30)

plt.show()