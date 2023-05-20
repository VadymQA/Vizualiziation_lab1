import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib.patches as mpatches
from matplotlib.animation import PillowWriter

fig = plt.figure()
ax = plt.axes(xlim=(-2, 12), ylim=(-2, 12))
triangle = np.array([[5, 0], [10, 10], [0, 10]]) # Вершини трикутника
grid = np.mgrid[0.2:0.8:3j, 0.2:0.8:3j].reshape(2, -1).T
arrow = mpatches.FancyArrowPatch(posA=grid[4], posB=grid[4], # Створення стрілки
                                 arrowstyle='->', mutation_scale=20)

def init(): # Додаємо стрілку на графік
    ax.add_patch(arrow)
    return arrow,

def animate(i):
    segment_num = i // 120
    t = (i % 120) / 120
    # Обчислюємо координати стрілки залежно від сегмента трикутника
    if segment_num == 0:
        x = triangle[0, 0] + t * (triangle[1, 0] - triangle[0, 0])
        y = triangle[0, 1] + t * (triangle[1, 1] - triangle[0, 1])
    elif segment_num == 1:
        x = triangle[1, 0] + t * (triangle[2, 0] - triangle[1, 0])
        y = triangle[1, 1] + t * (triangle[2, 1] - triangle[1, 1])
    else:
        x = triangle[2, 0] + t * (triangle[0, 0] - triangle[2, 0])
        y = triangle[2, 1] + t * (triangle[0, 1] - triangle[2, 1])

    # Оновлюємо позицію стрілки
    arrow.set_positions((x-0.1,y-0.1),(x,y))
    return arrow,


anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=360,
                               interval=20,
                               blit=True)

writer = PillowWriter(fps=30)  # швидкість анімації
anim.save("animation-3v.gif", writer=writer)

plt.show()