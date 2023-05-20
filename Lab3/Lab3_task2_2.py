import numpy as np
import matplotlib.pyplot as plt

def u(x, y):
    return x + 2 * y**2

def v(x, y):
    return y + 2 * x**2

min = -3
max = 6

def create_stream_line(x0, y0, u, v, t0=-4, t1=4, dt=0.001):
    t = np.arange(t0, t1, dt)
    xx_new = np.zeros_like(t)
    yy_new = np.zeros_like(t)
    xx_new[0] = x0
    yy_new[0] = y0

    for i in range(1, t.size):
        xx_new[i] = x0 + u(x0, y0) * dt
        yy_new[i] = y0 + v(x0, y0) * dt

        x0, y0 = xx_new[i], yy_new[i]

    return xx_new, yy_new


n = 15
x = np.linspace(min, max, n)
y = np.linspace(min, max, n)
xx, yy = np.meshgrid(x, y)
u_val = u(xx, yy)
v_val = v(xx, yy)

plt.streamplot(xx, yy, u_val, v_val)

for i in range(min, max):
    x1, y1 = create_stream_line(i, i, u, v)
    plt.plot(x1, y1)

plt.xlim(min, max)
plt.ylim(min, max)
plt.title('Візуалізація ліній току')

plt.show()