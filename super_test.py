import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.animation as animation
import matplotlib.patches as mpatches

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(-2, 12), ylim=(-2, 12))

triangle = np.array([[5, 0], [10, 10], [0, 10]])
# grid = np.mgrid[0.2:0.8:3j, 0.2:0.8:3j].reshape(2, -1).T

# Create a Line2D object to represent the arrow
line = mlines.Line2D([], [], linestyle='-', color='black', marker='^', markersize=2)



def init():
    ax.add_line(line)
    return line,


def animate(i):
    # визначаємо, на якому відрізку знаходиться точка кола
    segment_num = i // 120
    t = (i % 120) / 120

    # визначаємо координати точки, на яку буде переміщатись коло
    if segment_num == 0:
        x = triangle[0, 0] + t * (triangle[1, 0] - triangle[0, 0])
        y = triangle[0, 1] + t * (triangle[1, 1] - triangle[0, 1])
    elif segment_num == 1:
        x = triangle[1, 0] + t * (triangle[2, 0] - triangle[1, 0])
        y = triangle[1, 1] + t * (triangle[2, 1] - triangle[1, 1])
    else:
        x = triangle[2, 0] + t * (triangle[0, 0] - triangle[2, 0])
        y = triangle[2, 1] + t * (triangle[0, 1] - triangle[2, 1])

    # Update the position of the line
    line.set_xdata([x - 0.5, x])
    line.set_ydata([y - 0.5, y])

    return line,


anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=360,
                               interval=20,
                               blit=True)

triangle = np.array([[5, 1], [1, 9], [9, 9], [5, 1]])
plt.plot(triangle[:, 0], triangle[:, 1], color='black')

plt.show()
