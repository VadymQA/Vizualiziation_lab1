import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
patch = plt.Polygon([[0,0], [1,1], [2,0]], closed=True, fc='y')

def init():
    patch.set_xy([[5,4], [5.5,5], [6,4], [5.75, 3.5], [5.25, 3.5]])
    ax.add_patch(patch)
    return patch,

def animate(i):
    x = 5 + 3 * np.sin(np.radians(i))
    y = 5 + 3 * np.cos(np.radians(i))
    patch.set_xy([[x+0.5,y+1], [x+1,y+0.5], [x+0.75,y], [x+0.25,y], [x,y+0.5]])
    return patch,

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=360,
                               interval=20,
                               blit=True)

writer = PillowWriter(fps=30)  # встановлюємо швидкість анімації
anim.save("animation-3v_2.gif", writer=writer)

plt.show()


