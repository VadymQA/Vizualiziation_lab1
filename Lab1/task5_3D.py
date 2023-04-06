import matplotlib.pyplot as plt
import numpy as np


Z = np.array([[29, 51, 59, 478, 93, 244, 420, 510, 575, 625],
              [28, 46, 57, 52, 63, 93, 190, 275, 310, 355],
              [53, 73, 84, 105, 130, 180, 245, 265, 300, 335],
              [40, 70, 80, 105, 205, 480, 725, 935, 1000, 545]])

y_labels = np.array(['De', 'Fr', 'Uk', 'Ua'])
x_labels = np.array(['1900', '1913', '1929', '1938', '1950', '1960', '1970', '1980', '1990', '2000'])


# координати барів
xpos, ypos = np.meshgrid(np.arange(Z.shape[1]), np.arange(Z.shape[0]))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)


# розміри барів
dx = 0.75 * np.ones_like(zpos)
dy = dx.copy()
dz = Z.flatten()

#додано зміщення що б ось була по центру
ypos = np.add(ypos, -0.5 * dy)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')


# задаємо кожному бару свій колір
colors = ['red', 'gray', 'blue', 'yellow']
for i, country in enumerate(y_labels):
    start = i * len(x_labels)
    end = (i + 1) * len(x_labels)
    ax.bar3d(xpos[start:end], ypos[start:end], zpos[start:end], dx[start:end], dy[start:end], dz[start:end],
             color=colors[i])


ax.set_xticks(np.arange(len(x_labels)))
ax.set_yticks(np.arange(len(y_labels)))
ax.set_xticklabels(x_labels)
ax.set_yticklabels(y_labels)
ax.set_title('Промислове виробництво: додана вартість, в цінах нац. валют')
ax.set_ylabel('Country')
ax.set_xlabel('Years')
ax.set_zlabel('Billions $')

plt.show()