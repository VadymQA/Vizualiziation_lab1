import numpy as np
import matplotlib.pyplot as plt

alfa = 1

# theta та theta1 створюються в радіанах
theta_rad = np.linspace(0, 2* np.pi, 1000)
theta1_rad = np.linspace(0, 2* np.pi, 1000)

# перетворюємо радіани в градуси
theta = np.degrees(theta_rad)
theta1 = np.degrees(theta1_rad)

r1 = alfa * (1 + np.sin(theta_rad)) / np.cos(theta_rad)
r2 = alfa * (1 - np.sin(theta1_rad)) / np.cos(theta1_rad)

# Створимо маски для r1 та r2, щоб відфільтрувати значення, які виходять за межі [0, 5]
mask_r1 = (r1 >= 0) & (r1 <= 5)
mask_r2 = (r2 >= 0) & (r2 <= 5)

# Примінимо маски до наших масивів
theta_masked = theta[mask_r1 & mask_r2]
r1_masked = r1[mask_r1]
r2_masked = r2[mask_r2]

# Збереження відфільтрованих даних у текстовий файл
data = np.column_stack((theta_masked, r1_masked, r2_masked))
np.savetxt("output.txt", data)

ax = plt.subplot(111, projection='polar')
ax.plot(theta_rad, r1, color='b', linewidth=2)
ax.plot(theta1_rad, r2, color='r', linewidth=2)
plt.title(r'$r = \frac{\alpha(1 \pm sin(\theta))}{cos(\theta)}$')

ax.set_rmin(0)
ax.set_rmax(5)

plt.show()
